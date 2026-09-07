"""
validate_planes.py - measure whether the inner copper pours stay CONNECTED.

WHY THIS EXISTS
---------------
EAGLE computes polygon fill when the board is loaded, so the *shape* of the
two inner pours is not known until then.  Every other document in this project
therefore records the pour as "NOT COMPUTED", and PCB_BUILD_GUIDE.md step 14
asks a human to eyeball the result in Fusion and look for a "thin neck".

That is a weak check for the single most important electrical property of this
board - an unbroken GND reference under the AD8232.  So this script computes
the thing that actually matters:

    after punching an antipad around every piece of foreign copper,
    is the pour still one region, and does every pad that needs it
    still reach that region?

It is NOT a reimplementation of EAGLE's pour, and it does not emit copper.  It
is a connectivity measurement on the same geometry EAGLE will fill.

WHAT MAKES IT WORTH RUNNING
---------------------------
The emitted polygons declare `isolate="0.4"`, so a foreign 0.6 mm via clears a
0.7 mm-radius hole - a 1.4 mm bite out of the plane.  There are 486 vias.  The
question of whether that fragments the plane is quantitative, not a matter of
opinion.

`orphans="off"` is also declared, which means EAGLE *deletes* islands that do
not touch the polygon's own signal.  A fragment is therefore not floating
copper you could ignore - it vanishes, and any pad that depended on it loses
its plane connection.  That is why this script reports per-pad region
membership and not just a region count.

TWO PASSES
----------
  strict      antipad = own radius + isolate.  Pure geometry.
  realistic   antipad = own radius + isolate + half the pour line width.
              EAGLE draws the pour with a 0.4 mm pen, so it cannot fill a
              corridor much narrower than that.  This pass approximates the
              corridors the pour will actually render.

Run:  python scripts/validate_planes.py
Exit: 0 if every plane-net contact reaches the main region in the strict pass
      1 otherwise
"""

from __future__ import annotations

import json
import pathlib
import sys
import xml.etree.ElementTree as ET

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import design as D          # noqa: E402
import geom                 # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
BRD = ROOT / "pcb" / f"{D.PROJECT}.brd" if hasattr(D, "PROJECT") else \
      ROOT / "pcb" / "SIH26113_Maternity_Assist_Belt.brd"

GRID = 0.05          # mm per cell
REPORT = ROOT / "pcb" / "plane_result.json"


# ---------------------------------------------------------------------------
# connected components, run-length + union-find (no scipy in this project)
# ---------------------------------------------------------------------------
def label(mask: np.ndarray):
    """Return (root_of_run, runs_by_row, area_by_root) for a boolean mask."""
    H, W = mask.shape
    parent: list[int] = []

    def find(a: int) -> int:
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[max(ra, rb)] = min(ra, rb)

    runs_by_row: list[list[tuple[int, int, int]]] = []
    prev: list[tuple[int, int, int]] = []
    for y in range(H):
        row = mask[y]
        d = np.diff(row.astype(np.int8))
        starts = (np.nonzero(d == 1)[0] + 1).tolist()
        ends = (np.nonzero(d == -1)[0] + 1).tolist()
        if row[0]:
            starts.insert(0, 0)
        if row[-1]:
            ends.append(W)
        cur = []
        for s, e in zip(starts, ends):
            rid = len(parent)
            parent.append(rid)
            cur.append((s, e, rid))
        i = j = 0
        while i < len(prev) and j < len(cur):
            ps, pe, pid = prev[i]
            cs, ce, cid = cur[j]
            if pe > cs and ce > ps:
                union(pid, cid)
            if pe < ce:
                i += 1
            else:
                j += 1
        runs_by_row.append(cur)
        prev = cur

    area: dict[int, int] = {}
    for cur in runs_by_row:
        for s, e, rid in cur:
            r = find(rid)
            area[r] = area.get(r, 0) + (e - s)
    return find, runs_by_row, area


def region_at(find, runs_by_row, gx: int, gy: int) -> int | None:
    if not (0 <= gy < len(runs_by_row)):
        return None
    for s, e, rid in runs_by_row[gy]:
        if s <= gx < e:
            return find(rid)
    return None


# ---------------------------------------------------------------------------
def main() -> int:
    brd = ET.parse(BRD).getroot()

    # ---- the pour polygons, as emitted ---------------------------------
    polys = {}
    for sig in brd.findall(".//signals/signal"):
        for poly in sig.findall("polygon"):
            polys[int(poly.get("layer"))] = {
                "net": sig.get("name"),
                "isolate": float(poly.get("isolate")),
                "width": float(poly.get("width")),
                "orphans": poly.get("orphans"),
                "pts": [(float(v.get("x")), float(v.get("y")))
                        for v in poly.findall("vertex")],
            }

    # ---- foreign / own copper that punches an INNER plane ---------------
    # SMD pads live only on layers 1 and 16, so they do not touch an inner
    # plane at all.  Only plated through-holes and vias do.
    obstacles = []      # (net, x, y, radius_of_copper, label)
    for p in D.PARTS:
        ds = geom.DS[p.deviceset]
        if ds.package is None:
            continue
        for pad_name, pd in geom.package_pads(ds.package).items():
            dx, dy, tht = geom.pad_extent(p.deviceset, pad_name, p.brot)
            if not tht:
                continue
            px, py = geom.rotate(pd.x, pd.y, p.brot)
            net = None
            for nm, conns in D.NETS.items():
                for ref, pin in conns:
                    if ref == p.ref and pad_name in geom.pad_of(
                            D.PART_BY_REF[ref].deviceset, pin):
                        net = nm
            obstacles.append((net, p.bx + px, p.by + py,
                              max(dx, dy) / 2.0, f"{p.ref}.{pad_name}"))

    for sig in brd.findall(".//signals/signal"):
        net = sig.get("name")
        for v in sig.findall("via"):
            dia = float(v.get("diameter", v.get("drill")))
            obstacles.append((net, float(v.get("x")), float(v.get("y")),
                              dia / 2.0, f"via@{v.get('x')},{v.get('y')}"))

    print("=" * 72)
    print("PLANE INTEGRITY - SIH26113 Maternity Assist Belt")
    print("=" * 72)
    print(f"grid            : {GRID} mm")
    print(f"through-holes   : {sum(1 for o in obstacles if 'via@' not in o[4])}")
    print(f"vias            : {sum(1 for o in obstacles if 'via@' in o[4])}")

    W = int(round(D.BOARD_W / GRID)) + 1
    H = int(round(D.BOARD_H / GRID)) + 1
    xs = np.arange(W) * GRID
    ys = np.arange(H) * GRID
    GX, GY = np.meshgrid(xs, ys)

    # ---- rasterise the pour outline (even-odd ray cast) -----------------
    def in_poly(pts) -> np.ndarray:
        inside = np.zeros((H, W), dtype=bool)
        n = len(pts)
        for i in range(n):
            x1, y1 = pts[i]
            x2, y2 = pts[(i + 1) % n]
            if y1 == y2:
                continue
            cond = ((GY >= np.minimum(y1, y2)) & (GY < np.maximum(y1, y2)))
            xint = x1 + (GY - y1) * (x2 - x1) / (y2 - y1)
            inside ^= cond & (GX < xint)
        return inside

    ax1, ay1, ax2, ay2 = D.ANTENNA_KEEPOUT
    keepout = (GX >= ax1) & (GX <= ax2) & (GY >= ay1) & (GY <= ay2)

    ez = [z for z in D.ZONES if "ECG" in z[0]][0]
    ecg = (GX >= ez[1]) & (GX <= ez[3]) & (GY >= ez[2]) & (GY <= ez[4])

    results = {}
    overall_ok = True

    for layer in sorted(polys):
        info = polys[layer]
        pnet = info["net"]
        base = in_poly(info["pts"]) & ~keepout
        base_area = base.sum() * GRID * GRID

        print()
        print("-" * 72)
        print(f"LAYER {layer}  pour net '{pnet}'   isolate={info['isolate']} mm "
              f"width={info['width']} mm orphans={info['orphans']}")
        print(f"  pour outline area (before antipads): {base_area:.1f} mm2")

        layer_res = {"net": pnet, "isolate": info["isolate"],
                     "width": info["width"], "outline_area_mm2": base_area,
                     "passes": {}}

        for pass_name, extra in (("strict", 0.0),
                                 ("realistic", info["width"] / 2.0)):
            mask = base.copy()
            punched = 0
            for net, x, y, r, _lbl in obstacles:
                if net == pnet:
                    continue                      # own net: connects, not cuts
                ar = r + info["isolate"] + extra
                x0 = max(0, int((x - ar) / GRID)); x1_ = min(W, int((x + ar) / GRID) + 2)
                y0 = max(0, int((y - ar) / GRID)); y1_ = min(H, int((y + ar) / GRID) + 2)
                if x0 >= x1_ or y0 >= y1_:
                    continue
                sub = ((GX[y0:y1_, x0:x1_] - x) ** 2
                       + (GY[y0:y1_, x0:x1_] - y) ** 2) <= ar * ar
                mask[y0:y1_, x0:x1_] &= ~sub
                punched += 1

            find, runs, area = label(mask)
            if not area:
                print(f"  [{pass_name}] POUR COMPLETELY REMOVED - impossible geometry")
                overall_ok = False
                continue
            roots = sorted(area, key=lambda r: -area[r])
            main_root = roots[0]
            tot = sum(area.values())
            a_mm = {r: area[r] * GRID * GRID for r in roots}

            # where does each own-net through-hole / via land?
            own = [(n, x, y, r, l) for (n, x, y, r, l) in obstacles if n == pnet]
            orphan = []
            for _n, x, y, _r, lbl in own:
                gx, gy = int(round(x / GRID)), int(round(y / GRID))
                reg = region_at(find, runs, gx, gy)
                if reg is None:
                    # a via sits in its own antipad-free spot; probe a ring
                    hit = None
                    for dx, dy in ((2, 0), (-2, 0), (0, 2), (0, -2),
                                   (4, 0), (-4, 0), (0, 4), (0, -4)):
                        hit = region_at(find, runs, gx + dx, gy + dy)
                        if hit is not None:
                            break
                    reg = hit
                if reg is None or reg != main_root:
                    orphan.append((lbl, "no copper" if reg is None else "side region"))

            ecg_cells = int((mask & ecg).sum())
            ecg_area = ecg_cells * GRID * GRID
            ecg_regions = set()
            ys_e, xs_e = np.nonzero(mask & ecg)
            for k in range(0, len(xs_e), max(1, len(xs_e) // 400 or 1)):
                reg = region_at(find, runs, int(xs_e[k]), int(ys_e[k]))
                if reg is not None:
                    ecg_regions.add(reg)

            print(f"  [{pass_name}] antipads punched: {punched}")
            print(f"  [{pass_name}] regions: {len(roots)}   "
                  f"largest {a_mm[main_root]:.1f} mm2 "
                  f"({100.0 * area[main_root] / tot:.2f}% of remaining copper)")
            if len(roots) > 1:
                small = ", ".join(f"{a_mm[r]:.2f}" for r in roots[1:6])
                print(f"  [{pass_name}] other regions (mm2): {small}"
                      f"{' ...' if len(roots) > 6 else ''}")
            print(f"  [{pass_name}] own-net contacts: {len(own)}   "
                  f"NOT on the main region: {len(orphan)}")
            for lbl, why in orphan[:10]:
                print(f"      ORPHAN {lbl}: {why}")
            print(f"  [{pass_name}] ECG zone Z3 pour area: {ecg_area:.1f} mm2, "
                  f"spanning {len(ecg_regions)} region(s) "
                  f"{'(main only - GOOD)' if ecg_regions == {main_root} else ''}")

            ok = (not orphan) and (ecg_regions == {main_root} or not ecg_regions)
            if pass_name == "strict" and not ok:
                overall_ok = False
            layer_res["passes"][pass_name] = {
                "antipads": punched,
                "regions": len(roots),
                "largest_mm2": a_mm[main_root],
                "largest_pct": 100.0 * area[main_root] / tot,
                "other_regions_mm2": [a_mm[r] for r in roots[1:]],
                "own_contacts": len(own),
                "orphans": [{"pad": l, "why": w} for l, w in orphan],
                "ecg_zone_area_mm2": ecg_area,
                "ecg_zone_regions": len(ecg_regions),
                "ecg_zone_on_main": ecg_regions == {main_root},
            }
        results[str(layer)] = layer_res

    REPORT.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print()
    print("=" * 72)
    print(f"wrote {REPORT.relative_to(ROOT)}")
    print("RESULT:", "PASS" if overall_ok else "FAIL")
    print()
    print("NOT a substitute for EAGLE's own pour computation. This measures")
    print("connectivity of the region EAGLE will fill; it does not emit copper.")
    print("Run RATSNEST in Fusion as well - PCB_BUILD_GUIDE.md step 14.")
    return 0 if overall_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
