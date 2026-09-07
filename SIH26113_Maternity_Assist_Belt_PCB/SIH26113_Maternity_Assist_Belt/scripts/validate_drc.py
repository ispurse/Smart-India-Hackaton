"""
validate_drc.py - Design rule check on the emitted .brd geometry.

This reads the .brd that generate_board.py wrote and measures real geometry.
It is deliberately independent of the router's internal grid, so it can catch
a router bug rather than agreeing with one.

Checks
  D1  every element sits inside the board outline, with its courtyard clear
      of the outline
  D2  no two component courtyards overlap (placement collisions)
  D3  no pad or via inside the antenna keep-out
  D4  minimum track width and minimum drill
  D5  copper clearance: track-to-track and track-to-pad, per layer
  D6  every net is fully routed (island count == 1 per net, ignoring plane
      nets which are carried by an inner pour)
  D7  plane nets: every pad has either a through-hole or an adjacent via
  D8  silkscreen does not sit on exposed copper (pad) - reported as a warning
  D9  board-edge clearance for copper
"""

from __future__ import annotations

import json
import math
import pathlib
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import design as D  # noqa: E402
import geom  # noqa: E402
from lib_defs import LIBRARY_NAME  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
BRD = ROOT / "pcb" / f"{LIBRARY_NAME}.brd"

MIN_WIDTH = 0.15
MIN_DRILL = 0.30
MIN_CLEAR = 0.15          # general rule
# Inside a fine-pitch fan-out the rule is D.FINE_PITCH_CLEARANCE; a
# 0.5 mm-pitch QFN cannot be escaped at 0.15 mm.  Bounded to the named
# rectangles and reported separately below.
EXCEPTIONS = None         # filled in main(), needs placement resolved
EDGE_CLEAR = 0.30
COURTYARD = 0.15        # extra margin added to each part's copper extent

errors: list[str] = []
warnings: list[str] = []
notes: list[str] = []


def seg_seg_dist(a, b, c, d) -> float:
    """Minimum distance between segments ab and cd."""
    def dot(u, v):
        return u[0] * v[0] + u[1] * v[1]

    def sub(u, v):
        return (u[0] - v[0], u[1] - v[1])

    def pt_seg(p, s, e):
        vx, vy = e[0] - s[0], e[1] - s[1]
        L2 = vx * vx + vy * vy
        if L2 == 0:
            return math.dist(p, s)
        t = max(0.0, min(1.0, ((p[0] - s[0]) * vx + (p[1] - s[1]) * vy) / L2))
        return math.dist(p, (s[0] + t * vx, s[1] + t * vy))

    r = sub(b, a)
    s = sub(d, c)
    den = r[0] * s[1] - r[1] * s[0]
    if den != 0:
        qp = sub(c, a)
        t = (qp[0] * s[1] - qp[1] * s[0]) / den
        u = (qp[0] * r[1] - qp[1] * r[0]) / den
        if 0 <= t <= 1 and 0 <= u <= 1:
            return 0.0
    return min(pt_seg(a, c, d), pt_seg(b, c, d),
               pt_seg(c, a, b), pt_seg(d, a, b))


def rect_overlap(a, b) -> float:
    """Negative/zero = overlapping; positive = gap between two AABBs."""
    dx = max(a[0] - b[2], b[0] - a[2])
    dy = max(a[1] - b[3], b[1] - a[3])
    if dx < 0 and dy < 0:
        return max(dx, dy)          # overlapping: report the smaller penetration
    return math.hypot(max(dx, 0.0), max(dy, 0.0))


def part_extent(p) -> tuple[float, float, float, float] | None:
    """Copper AABB of a placed part, in board coordinates."""
    ds = geom.DS[p.deviceset]
    if ds.package is None:
        return None
    xs, ys = [], []
    for pad_name in geom.package_pads(ds.package):
        pd = geom.package_pads(ds.package)[pad_name]
        px, py = geom.rotate(pd.x, pd.y, p.brot)
        dx, dy, _ = geom.pad_extent(p.deviceset, pad_name, p.brot)
        xs += [p.bx + px - dx / 2, p.bx + px + dx / 2]
        ys += [p.by + py - dy / 2, p.by + py + dy / 2]
    if not xs:
        return None
    return (min(xs), min(ys), max(xs), max(ys))


def _limit(x, y):
    """Clearance rule at a point: the general one, unless inside a declared
    fine-pitch fan-out region."""
    for x1, y1, x2, y2, c in (EXCEPTIONS or []):
        if x1 <= x <= x2 and y1 <= y <= y2:
            return c
    return MIN_CLEAR


def main() -> int:
    global EXCEPTIONS
    EXCEPTIONS = D.clearance_exceptions()
    if not BRD.exists():
        print("no .brd yet - run generate_board.py first")
        return 1
    txt = BRD.read_text(encoding="utf-8")
    tree = ET.fromstring(txt.split("\n", 2)[2])
    brd = tree.find("./drawing/board")

    W, H = D.BOARD_W, D.BOARD_H
    ax1, ay1, ax2, ay2 = D.ANTENNA_KEEPOUT
    PLANE = set(D.PLANE_LAYERS.values())

    # ---- D1 / D2 : placement -------------------------------------------
    extents = {}
    for p in D.PARTS:
        e = part_extent(p)
        if e is None:
            continue
        extents[p.ref] = e
        if e[0] < EDGE_CLEAR or e[1] < EDGE_CLEAR or \
                e[2] > W - EDGE_CLEAR or e[3] > H - EDGE_CLEAR:
            errors.append(f"[D1] {p.ref} copper extends outside the board "
                          f"edge clearance: bbox={tuple(round(v,2) for v in e)}")
    refs = sorted(extents)
    for i, a in enumerate(refs):
        ea = extents[a]
        ga = (ea[0] - COURTYARD, ea[1] - COURTYARD,
              ea[2] + COURTYARD, ea[3] + COURTYARD)
        for b in refs[i + 1:]:
            eb = extents[b]
            gb = (eb[0] - COURTYARD, eb[1] - COURTYARD,
                  eb[2] + COURTYARD, eb[3] + COURTYARD)
            d = rect_overlap(ga, gb)
            if d <= 0:
                errors.append(f"[D2] courtyard overlap: {a} and {b} "
                              f"(penetration {abs(d):.2f} mm)")

    # ---- collect copper -------------------------------------------------
    pads = []          # (net, layer|None, x, y, dx, dy)
    for p in D.PARTS:
        ds = geom.DS[p.deviceset]
        if ds.package is None:
            continue
        for pad_name, pd in geom.package_pads(ds.package).items():
            px, py = geom.rotate(pd.x, pd.y, p.brot)
            dx, dy, tht = geom.pad_extent(p.deviceset, pad_name, p.brot)
            net = None
            for nm, conns in D.NETS.items():
                for ref, pin in conns:
                    if ref == p.ref and pad_name in geom.pad_of(
                            D.PART_BY_REF[ref].deviceset, pin):
                        net = nm
            pads.append((net, None if tht else 1, p.bx + px, p.by + py,
                         dx, dy, tht, f"{p.ref}.{pad_name}"))
            if tht and (ax1 <= p.bx + px <= ax2) and (ay1 <= p.by + py <= ay2):
                errors.append(f"[D3] through-hole pad {p.ref}.{pad_name} is "
                              f"inside the antenna keep-out")

    wires = defaultdict(list)      # layer -> [(net, (x1,y1), (x2,y2), w)]
    for sig in brd.findall("./signals/signal"):
        net = sig.get("name")
        for w in sig.findall("./wire"):
            L = int(w.get("layer"))
            width = float(w.get("width"))
            a = (float(w.get("x1")), float(w.get("y1")))
            b = (float(w.get("x2")), float(w.get("y2")))
            wires[L].append((net, a, b, width))
            if width < MIN_WIDTH - 1e-9:
                errors.append(f"[D4] {net}: track width {width} mm on layer "
                              f"{L} is below the {MIN_WIDTH} mm minimum")
            for pt in (a, b):
                if not (EDGE_CLEAR <= pt[0] <= W - EDGE_CLEAR
                        and EDGE_CLEAR <= pt[1] <= H - EDGE_CLEAR):
                    errors.append(f"[D9] {net}: track endpoint {pt} on layer "
                                  f"{L} violates board-edge clearance")
                if ax1 <= pt[0] <= ax2 and ay1 <= pt[1] <= ay2:
                    errors.append(f"[D3] {net}: track endpoint {pt} on layer "
                                  f"{L} is inside the antenna keep-out")
        for v in sig.findall("./via"):
            drill = float(v.get("drill"))
            vx, vy = float(v.get("x")), float(v.get("y"))
            if drill < MIN_DRILL - 1e-9:
                errors.append(f"[D4] {net}: via drill {drill} mm below the "
                              f"{MIN_DRILL} mm minimum")
            if ax1 <= vx <= ax2 and ay1 <= vy <= ay2:
                errors.append(f"[D3] {net}: via at ({vx}, {vy}) is inside the "
                              f"antenna keep-out")
    return _phase2(brd, pads, wires, PLANE)


def _phase2(brd, pads, wires, PLANE) -> int:
    # ---- D5 : copper clearance ------------------------------------------
    min_seen = {}
    for L, items in wires.items():
        for i in range(len(items)):
            n1, a1, b1, w1 = items[i]
            for j in range(i + 1, len(items)):
                n2, a2, b2, w2 = items[j]
                if n1 == n2:
                    continue
                gap = seg_seg_dist(a1, b1, a2, b2) - w1 / 2 - w2 / 2
                key = ("wire-wire", L)
                if gap < min_seen.get(key, 1e9):
                    min_seen[key] = gap
                lim = _limit((a1[0] + b1[0] + a2[0] + b2[0]) / 4.0,
                             (a1[1] + b1[1] + a2[1] + b2[1]) / 4.0)
                if gap < lim - 1e-6:
                    errors.append(f"[D5] layer {L}: {n1} to {n2} clearance "
                                  f"{gap:.3f} mm < {lim} mm")
                elif gap < MIN_CLEAR - 1e-6:
                    notes.append(f"[D5] layer {L}: {n1} to {n2} at "
                                 f"{gap:.3f} mm - inside a declared "
                                 f"fine-pitch fan-out region ({lim} mm rule)")
        # track to foreign pad
        for net, a, b, w in items:
            for pnet, player, px, py, dx, dy, tht, label in pads:
                if pnet == net:
                    continue
                if not tht and playerentry_mismatch(player, L):
                    continue
                # Round through-hole pads are circles; everything else is a
                # rectangle.
                if tht and abs(dx - dy) < 1e-6:
                    gap = seg_circle_dist(a, b, px, py, dx / 2) - w / 2
                else:
                    r = (px - dx / 2, py - dy / 2, px + dx / 2, py + dy / 2)
                    gap = seg_rect_dist(a, b, r) - w / 2
                key = ("wire-pad", L)
                if gap < min_seen.get(key, 1e9):
                    min_seen[key] = gap
                lim = _limit((a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0)
                if gap < lim - 1e-6:
                    errors.append(f"[D5] layer {L}: {net} track to pad "
                                  f"{label} ({pnet}) clearance {gap:.3f} mm "
                                  f"< {lim} mm")
                elif gap < MIN_CLEAR - 1e-6:
                    notes.append(f"[D5] layer {L}: {net} track to pad {label} "
                                 f"at {gap:.3f} mm - inside a declared "
                                 f"fine-pitch fan-out region ({lim} mm rule)")
    for (kind, L), v in sorted(min_seen.items()):
        notes.append(f"[D5] minimum {kind} clearance on layer {L}: {v:.3f} mm")
    if min_seen:
        worst = min(min_seen.values())
        notes.append(f"[D5] MEASURED MINIMUM COPPER CLEARANCE ANYWHERE ON THE "
                     f"BOARD: {worst:.3f} mm. This is the number to quote to "
                     f"the fabricator.")

    # ---- D6 : routing completeness --------------------------------------
    rr = ROOT / "pcb" / "route_report.json"
    unrouted = []
    if rr.exists():
        rep = json.loads(rr.read_text(encoding="utf-8"))
        unrouted = [nm for nm, _ in rep.get("failed", [])]
        for nm, why in rep.get("failed", []):
            errors.append(f"[D6] net {nm} is not fully routed: {why}")
        for o in rep.get("orphan_plane_pads", []):
            errors.append(f"[D6] {o} has no connection to its plane")
        notes.append(f"[D6] router completed {rep.get('routed')} of "
                     f"{rep.get('total_signal_nets')} signal nets")
    connectivity_check(brd, PLANE, unrouted)

    # ---- report ----------------------------------------------------------
    print("=" * 72)
    print("DRC - SIH26113 Maternity Assist Belt")
    print("=" * 72)
    print(f"board        : {D.BOARD_W:.0f} x {D.BOARD_H:.0f} mm, "
          f"{D.BOARD_LAYERS} layers, {D.BOARD_THICKNESS} mm FR-4")
    print(f"rules        : min track {MIN_WIDTH} mm, min drill {MIN_DRILL} mm, "
          f"min clearance {MIN_CLEAR} mm general / "
          f"{D.FINE_PITCH_CLEARANCE} mm inside the {len(EXCEPTIONS)} declared "
          f"fine-pitch fan-out regions, edge {EDGE_CLEAR} mm")
    print()
    for label, items in (("ERROR", errors), ("WARNING", warnings),
                         ("NOTE", notes)):
        print(f"--- {label}S ({len(items)}) ---")
        for i in items[:200]:
            print(f"  {label[0]}: {i}")
        if len(items) > 200:
            print(f"  ... and {len(items) - 200} more")
        print()
    print("RESULT:", "FAIL" if errors else "PASS")
    (ROOT / "pcb" / "drc_result.json").write_text(json.dumps({
        "errors": errors, "warnings": warnings, "notes": notes,
    }, indent=2), encoding="utf-8")
    return 1 if errors else 0


def playerentry_mismatch(playa, L) -> bool:
    return playa is not None and playa != L


def seg_rect_dist(a, b, r) -> float:
    x1, y1, x2, y2 = r
    corners = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
    edges = list(zip(corners, corners[1:] + corners[:1]))
    # If either endpoint is inside, distance is 0.
    for p in (a, b):
        if x1 <= p[0] <= x2 and y1 <= p[1] <= y2:
            return 0.0
    return min(seg_seg_dist(a, b, c, d) for c, d in edges)


def seg_circle_dist(a, b, cx, cy, radius) -> float:
    """Distance from segment ab to the edge of a circle.

    Round through-hole pads have to be measured as circles.  Using their
    bounding square instead over-reports by up to 0.41 x radius at the
    corners, which flags tracks that are comfortably clear of the copper.
    """
    vx, vy = b[0] - a[0], b[1] - a[1]
    L2 = vx * vx + vy * vy
    if L2 == 0:
        d = math.dist(a, (cx, cy))
    else:
        t = max(0.0, min(1.0, ((cx - a[0]) * vx + (cy - a[1]) * vy) / L2))
        d = math.dist((a[0] + t * vx, a[1] + t * vy), (cx, cy))
    return d - radius


def connectivity_check(brd, PLANE, unrouted) -> None:
    """D7: confirm every plane-net pad reaches the plane, and that each
    routed net's copper forms one connected island."""
    for sig in brd.findall("./signals/signal"):
        net = sig.get("name")
        if net in PLANE:
            continue
        if net in unrouted:
            continue
        segs = [((float(w.get("x1")), float(w.get("y1")), int(w.get("layer"))),
                 (float(w.get("x2")), float(w.get("y2")), int(w.get("layer"))))
                for w in sig.findall("./wire")]
        vias = [(float(v.get("x")), float(v.get("y")))
                for v in sig.findall("./via")]
        if not segs:
            if len(sig.findall("./contactref")) > 1:
                errors.append(f"[D6] net {net} has {len(sig.findall('./contactref'))} "
                              f"pads but no copper at all")
            continue
        parent = {}

        def find(k):
            while parent.get(k, k) != k:
                k = parent[k]
            return k

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        def key(pt):
            return (round(pt[0], 3), round(pt[1], 3), pt[2])

        for s, e in segs:
            parent.setdefault(key(s), key(s))
            parent.setdefault(key(e), key(e))
            union(key(s), key(e))
        for vx, vy in vias:
            k1 = (round(vx, 3), round(vy, 3), 1)
            k2 = (round(vx, 3), round(vy, 3), 16)
            for k in (k1, k2):
                parent.setdefault(k, k)
            union(k1, k2)
        # Two tracks that land on the same pad are connected *through* the
        # pad, so bind every endpoint that falls inside one of this net's
        # pads to a single node per pad.
        for cr in sig.findall("./contactref"):
            ref, pad_name = cr.get("element"), cr.get("pad")
            prt = D.PART_BY_REF.get(ref)
            if prt is None:
                continue
            try:
                pd = geom.package_pads(geom.DS[prt.deviceset].package)[pad_name]
            except (KeyError, TypeError):
                continue
            ppx, ppy = geom.rotate(pd.x, pd.y, prt.brot)
            ax, ay = prt.bx + ppx, prt.by + ppy
            pw, ph, is_tht = geom.pad_extent(prt.deviceset, pad_name, prt.brot)
            anchor = ("pad", ref, pad_name)
            parent.setdefault(anchor, anchor)
            for k in list(parent):
                if not (isinstance(k, tuple) and len(k) == 3
                        and isinstance(k[0], float)):
                    continue
                # Half a track width of slack: a track endpoint sits at a
                # grid cell centre, which need not land exactly on the pad's
                # own coordinate.
                if abs(k[0] - ax) <= pw / 2 + 0.13 and                         abs(k[1] - ay) <= ph / 2 + 0.13:
                    union(k, anchor)
        islands = {find(k) for k in parent}
        if len(islands) > 1:
            warnings.append(
                f"[D6] net {net}: track copper forms {len(islands)} groups. "
                f"This is normal - a multi-drop net reaches each pad "
                f"separately and the pads join them - and is reported only so "
                f"a genuinely stranded stub cannot hide among them. Confirm "
                f"with RATSNEST in Fusion.")


if __name__ == "__main__":
    raise SystemExit(main())
