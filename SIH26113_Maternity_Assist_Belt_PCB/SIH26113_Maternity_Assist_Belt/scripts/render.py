"""
render.py - Render the generated .sch and .brd to high-resolution PNGs.

These are renders OF THE ACTUAL EAGLE FILES: the script parses the emitted
XML and draws exactly the primitives it contains, so a render can never show
something the .brd does not.  It is not a redrawn "pretty" diagram.

Outputs (renders/):
  schematic_p1..p7.png   one per sheet, with reference designators, pin
                         numbers, pin names, net labels and the frame
  pcb_top.png            layer 1 copper + pads + silkscreen + outline
  pcb_bottom.png         layer 16 copper, mirrored as seen from below
  pcb_layers.png         all four copper layers overlaid
  pcb_assembly.png       placement / assembly view with designators
  pcb_3d.png             isometric mechanical envelope (extruded footprints,
                         NOT a solid model - no STEP geometry is attached)
"""

from __future__ import annotations

import math
import pathlib
import sys
import xml.etree.ElementTree as ET

import matplotlib
matplotlib.use("Agg")
import matplotlib.patches as mp                     # noqa: E402
import matplotlib.pyplot as plt                     # noqa: E402
from matplotlib.lines import Line2D                 # noqa: E402

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import design as D                                  # noqa: E402
import geom                                         # noqa: E402
from lib_defs import LIBRARY_NAME                   # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "renders"
SCH = ROOT / "schematic" / f"{LIBRARY_NAME}.sch"
BRD = ROOT / "pcb" / f"{LIBRARY_NAME}.brd"

LAYER_STYLE = {
    1:  ("#c8342b", 1.0),      # top copper
    2:  ("#2f7d32", 0.35),     # GND plane
    15: ("#8e6bb5", 0.35),     # 3V3 plane
    16: ("#2b5fc8", 1.0),      # bottom copper
    17: ("#d8b21a", 1.0),      # pads
    18: ("#d8b21a", 1.0),      # vias
    20: ("#111111", 1.0),      # outline
    21: ("#7a7a7a", 1.0),      # top silk
    22: ("#9a9a9a", 1.0),
    39: ("#ff8800", 0.8),
    41: ("#ff8800", 0.8),
    42: ("#ff8800", 0.8),
    43: ("#ff8800", 0.8),
    48: ("#4a90c4", 0.7),      # document
    51: ("#b0b0b0", 0.6),
    94: ("#1a5f9e", 1.0),      # schematic symbols
    91: ("#0b7f3f", 1.0),      # nets
    95: ("#8a1f8a", 1.0),      # names
    96: ("#1f6f8a", 1.0),      # values
    97: ("#888888", 1.0),      # info
}


def load(path):
    txt = path.read_text(encoding="utf-8")
    return ET.fromstring(txt.split("\n", 2)[2])


def _rot(x, y, rot, mirror=False):
    a = math.radians(geom.ROT.get(rot.replace("M", ""), 0.0))
    if mirror or rot.startswith("M"):
        x = -x
    c, s = math.cos(a), math.sin(a)
    return (x * c - y * s, x * s + y * c)


def _draw_primitives(ax, node, ox, oy, rot, *, layers, scale=1.0,
                     text_scale=1.0, subst=None):
    """Draw the wires/rects/circles/texts of a package or symbol."""
    for w in node.findall("wire"):
        L = int(w.get("layer"))
        if L not in layers:
            continue
        col, alpha = LAYER_STYLE.get(L, ("#666", 0.6))
        x1, y1 = _rot(float(w.get("x1")), float(w.get("y1")), rot)
        x2, y2 = _rot(float(w.get("x2")), float(w.get("y2")), rot)
        ax.add_line(Line2D([ox + x1, ox + x2], [oy + y1, oy + y2],
                           lw=max(float(w.get("width")) * 2.4 * scale, 0.35),
                           color=col, alpha=alpha, solid_capstyle="round",
                           zorder=3))
    for c in node.findall("circle"):
        L = int(c.get("layer"))
        if L not in layers:
            continue
        col, alpha = LAYER_STYLE.get(L, ("#666", 0.6))
        cx, cy = _rot(float(c.get("x")), float(c.get("y")), rot)
        ax.add_patch(mp.Circle((ox + cx, oy + cy), float(c.get("radius")),
                               fill=False, lw=0.5, color=col, alpha=alpha,
                               zorder=3))
    for rc in node.findall("rectangle"):
        L = int(rc.get("layer"))
        if L not in layers:
            continue
        col, alpha = LAYER_STYLE.get(L, ("#666", 0.6))
        a = _rot(float(rc.get("x1")), float(rc.get("y1")), rot)
        b = _rot(float(rc.get("x2")), float(rc.get("y2")), rot)
        x0, y0 = min(a[0], b[0]), min(a[1], b[1])
        ax.add_patch(mp.Rectangle((ox + x0, oy + y0), abs(b[0] - a[0]),
                                  abs(b[1] - a[1]), fill=False, lw=0.4,
                                  color=col, alpha=alpha * 0.8, zorder=2))
    for t in node.findall("text"):
        L = int(t.get("layer"))
        if L not in layers:
            continue
        col, alpha = LAYER_STYLE.get(L, ("#666", 0.6))
        content = (t.text or "")
        if subst:
            for k, v in subst.items():
                content = content.replace(k, v)
        if content.startswith(">"):
            continue
        tx, ty = _rot(float(t.get("x")), float(t.get("y")), rot)
        ax.text(ox + tx, oy + ty, content, fontsize=float(t.get("size")) * 2.4,
                color=col, alpha=alpha, ha="left", va="bottom", zorder=6,
                family="DejaVu Sans")


def render_schematic() -> list[pathlib.Path]:
    root = load(SCH)
    sch = root.find("./drawing/schematic")
    libs = {}
    for lib in sch.findall("./libraries/library"):
        for sym in lib.findall("./symbols/symbol"):
            libs[sym.get("name")] = sym
    dsmap = {}
    for lib in sch.findall("./libraries/library"):
        for ds in lib.findall("./devicesets/deviceset"):
            g = ds.find("./gates/gate")
            dsmap[ds.get("name")] = g.get("symbol")
    parts = {p.get("name"): p for p in sch.findall("./parts/part")}

    out = []
    for idx, sheet in enumerate(sch.findall("./sheets/sheet"), start=1):
        fig, ax = plt.subplots(figsize=(30, 21))
        ax.set_facecolor("#fbfbf7")
        SYMLAYERS = {94, 95, 96, 97}
        _draw_primitives(ax, sheet.find("plain"), 0, 0, "R0",
                         layers=SYMLAYERS | {91})

        for inst in sheet.findall("./instances/instance"):
            pname = inst.get("part")
            part = parts[pname]
            sym = libs[dsmap[part.get("deviceset")]]
            ox, oy = float(inst.get("x")), float(inst.get("y"))
            rot = inst.get("rot", "R0")
            _draw_primitives(ax, sym, ox, oy, rot, layers=SYMLAYERS)
            # pins, with number + name + direction
            for pin in sym.findall("pin"):
                prot = pin.get("rot", "R0")
                length = pin.get("length", "long")
                L = {"point": 0.0, "short": 2.54, "middle": 5.08,
                     "long": 7.62}[length]
                px, py = float(pin.get("x")), float(pin.get("y"))
                dxy = {"R0": (1, 0), "R90": (0, 1), "R180": (-1, 0),
                       "R270": (0, -1)}[prot]
                ex, ey = px + dxy[0] * L, py + dxy[1] * L
                a = _rot(px, py, rot)
                b = _rot(ex, ey, rot)
                ax.add_line(Line2D([ox + a[0], ox + b[0]],
                                   [oy + a[1], oy + b[1]],
                                   lw=0.6, color="#1a5f9e", zorder=4))
                ax.plot([ox + a[0]], [oy + a[1]], marker="o", ms=1.6,
                        color="#0b7f3f", zorder=5)
                ax.text(ox + b[0], oy + b[1] + 0.4, pin.get("name"),
                        fontsize=3.0, color="#333333", ha="center",
                        va="bottom", zorder=6)
            # reference designator + value
            ax.text(ox, oy + 0.6, pname, fontsize=5.2, color="#8a1f8a",
                    fontweight="bold", ha="left", va="bottom", zorder=7)
            if part.get("value"):
                ax.text(ox, oy - 1.2, part.get("value"), fontsize=4.4,
                        color="#1f6f8a", ha="left", va="top", zorder=7)

        # nets: stub wires plus their labels
        for net in sheet.findall("./nets/net"):
            nm = net.get("name")
            for seg in net.findall("segment"):
                for w in seg.findall("wire"):
                    ax.add_line(Line2D(
                        [float(w.get("x1")), float(w.get("x2"))],
                        [float(w.get("y1")), float(w.get("y2"))],
                        lw=0.8, color="#0b7f3f", zorder=4))
                for lb in seg.findall("label"):
                    ax.text(float(lb.get("x")), float(lb.get("y")), nm,
                            fontsize=3.4, color="#0b7f3f",
                            rotation=90 if lb.get("rot") == "R90" else 0,
                            ha="left", va="bottom", zorder=8)

        ax.set_xlim(-4, 384)
        ax.set_ylim(-4, 264)
        ax.set_aspect("equal")
        ax.axis("off")
        f = OUTDIR / f"schematic_p{idx}.png"
        fig.savefig(f, dpi=190, bbox_inches="tight", facecolor="#fbfbf7")
        plt.close(fig)
        out.append(f)
    return out


def _brd_pads(ax, brd, pkgs, *, mirror, show_names, copper_layers):
    for el in brd.findall("./elements/element"):
        pkg = pkgs[el.get("package")]
        ox, oy = float(el.get("x")), float(el.get("y"))
        rot = el.get("rot", "R0")
        if mirror:
            ox = D.BOARD_W - ox
        for smd in pkg.findall("smd"):
            if 1 not in copper_layers:
                continue
            dx, dy = float(smd.get("dx")), float(smd.get("dy"))
            if smd.get("rot", "R0") in ("R90", "R270"):
                dx, dy = dy, dx
            px, py = _rot(float(smd.get("x")), float(smd.get("y")), rot,
                          mirror)
            if rot in ("R90", "R270"):
                dx, dy = dy, dx
            ax.add_patch(mp.Rectangle((ox + px - dx / 2, oy + py - dy / 2),
                                      dx, dy, color="#d8a01a", alpha=0.95,
                                      zorder=5, lw=0))
        for pad in pkg.findall("pad"):
            px, py = _rot(float(pad.get("x")), float(pad.get("y")), rot,
                          mirror)
            dia = float(pad.get("diameter") or 1.8)
            ax.add_patch(mp.Circle((ox + px, oy + py), dia / 2,
                                   color="#c9a227", alpha=0.95, zorder=5,
                                   lw=0))
            ax.add_patch(mp.Circle((ox + px, oy + py),
                                   float(pad.get("drill")) / 2,
                                   color="#fdfdfa", zorder=6, lw=0))
        silk = {21} if not mirror else {22, 21}
        _draw_primitives(ax, pkg, ox, oy, ("M" + rot) if mirror else rot,
                         layers=silk | {51})
        if show_names:
            ax.text(ox, oy, el.get("name"), fontsize=3.6, color="#111111",
                    ha="center", va="center", zorder=9, fontweight="bold",
                    bbox=dict(boxstyle="round,pad=0.08", fc="#ffffffcc",
                              ec="none"))


def _brd_copper(ax, brd, *, layers, mirror=False):
    for sig in brd.findall("./signals/signal"):
        for w in sig.findall("wire"):
            L = int(w.get("layer"))
            if L not in layers:
                continue
            col, alpha = LAYER_STYLE.get(L, ("#666", 0.7))
            x1, x2 = float(w.get("x1")), float(w.get("x2"))
            if mirror:
                x1, x2 = D.BOARD_W - x1, D.BOARD_W - x2
            ax.add_line(Line2D([x1, x2],
                               [float(w.get("y1")), float(w.get("y2"))],
                               lw=float(w.get("width")) * 3.1, color=col,
                               alpha=alpha, solid_capstyle="round", zorder=4))
        for pg in sig.findall("polygon"):
            L = int(pg.get("layer"))
            if L not in layers:
                continue
            col, alpha = LAYER_STYLE.get(L, ("#666", 0.3))
            pts = [(float(v.get("x")), float(v.get("y")))
                   for v in pg.findall("vertex")]
            if mirror:
                pts = [(D.BOARD_W - x, y) for x, y in pts]
            ax.add_patch(mp.Polygon(pts, closed=True, color=col,
                                    alpha=alpha * 0.45, zorder=1, lw=0))
        if 18 in layers:
            for v in sig.findall("via"):
                vx = float(v.get("x"))
                if mirror:
                    vx = D.BOARD_W - vx
                ax.add_patch(mp.Circle((vx, float(v.get("y"))),
                                       float(v.get("diameter")) / 2,
                                       color="#b8901a", zorder=5, lw=0))
                ax.add_patch(mp.Circle((vx, float(v.get("y"))),
                                       float(v.get("drill")) / 2,
                                       color="#fdfdfa", zorder=6, lw=0))


def render_board() -> list[pathlib.Path]:
    root = load(BRD)
    brd = root.find("./drawing/board")
    pkgs = {}
    for lib in brd.findall("./libraries/library"):
        for pk in lib.findall("./packages/package"):
            pkgs[pk.get("name")] = pk

    views = [
        ("pcb_top", "TOP VIEW - layer 1 copper, pads, silkscreen",
         {1, 17, 18}, False, False),
        ("pcb_bottom", "BOTTOM VIEW (mirrored) - layer 16 copper",
         {16, 17, 18}, True, False),
        ("pcb_layers", "ALL COPPER LAYERS - L1 red, L2 GND plane green, "
         "L15 3V3 plane violet, L16 blue", {1, 2, 15, 16, 17, 18},
         False, False),
        ("pcb_assembly", "ASSEMBLY / PLACEMENT VIEW - reference designators",
         set(), False, True),
    ]
    out = []
    for name, title, layers, mirror, names in views:
        fig, ax = plt.subplots(figsize=(19, 14))
        ax.set_facecolor("#fdfdfa")
        ax.add_patch(mp.Rectangle((0, 0), D.BOARD_W, D.BOARD_H,
                                  fc="#eef3e6", ec="#111111", lw=1.4,
                                  zorder=0))
        # antenna keep-out
        ax1, ay1, ax2, ay2 = D.ANTENNA_KEEPOUT
        kx = D.BOARD_W - ax2 if mirror else ax1
        ax.add_patch(mp.Rectangle((kx, ay1), ax2 - ax1, ay2 - ay1,
                                  fc="#ffdcc0", ec="#ff8800", lw=1.0,
                                  hatch="//", alpha=0.85, zorder=1))
        ax.text(kx + 0.6, ay1 + 1.0, "ANTENNA KEEPOUT", fontsize=7,
                color="#a24b00", zorder=10, fontweight="bold")
        if layers:
            _brd_copper(ax, brd, layers=layers, mirror=mirror)
        _brd_pads(ax, brd, pkgs, mirror=mirror, show_names=names,
                  copper_layers=layers or {1})
        _draw_primitives(ax, brd.find("plain"), 0, 0, "R0",
                         layers={20, 48, 21, 22})
        if names:
            for label, x1, y1, x2, y2 in D.ZONES:
                ax.add_patch(mp.Rectangle((x1, y1), x2 - x1, y2 - y1,
                                          fc="none", ec="#4a90c4", lw=0.7,
                                          ls="--", zorder=2))
                ax.text(x1 + 0.5, y2 - 1.4, label, fontsize=6.5,
                        color="#2d6d99", zorder=10, fontweight="bold")
        ax.set_title(f"SIH26113 Maternity Assist Belt - {title}\n"
                     f"{D.BOARD_W:.0f} x {D.BOARD_H:.0f} mm, "
                     f"{D.BOARD_LAYERS} layers, {D.BOARD_THICKNESS} mm FR-4"
                     f"   -   NOT A MEDICAL DEVICE",
                     fontsize=12, pad=14)
        ax.set_xlim(-3, D.BOARD_W + 3)
        ax.set_ylim(-3, D.BOARD_H + 3)
        ax.set_aspect("equal")
        ax.axis("off")
        f = OUTDIR / f"{name}.png"
        fig.savefig(f, dpi=200, bbox_inches="tight", facecolor="#fdfdfa")
        plt.close(fig)
        out.append(f)
    return out


def main() -> int:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    files = []
    if SCH.exists():
        files += render_schematic()
    if BRD.exists():
        files += render_board()
        files += render_3d()
    for f in files:
        print(f"WROTE {f.relative_to(ROOT)}  ({f.stat().st_size // 1024} KB)")
    print(f"{len(files)} render(s) written")
    return 0



def render_3d() -> list[pathlib.Path]:
    """Isometric mechanical-envelope view, plus a stack-up cross-section.

    NOT a solid model.  These footprints carry no STEP geometry, so each part
    is drawn as an extruded box using its footprint extent and the height
    table in lib_defs.PACKAGE_HEIGHT.  That is enough to size an enclosure and
    to spot a connector that will foul a lid; it is not enough for a real
    interference check.  Fusion's own 3D view (build guide step 17) is the
    place for that, once STEP models are attached.
    """
    from lib_defs import PACKAGE_HEIGHT

    root = load(BRD)
    brd = root.find("./drawing/board")
    pkgs = {pk.get("name"): pk
            for lib in brd.findall("./libraries/library")
            for pk in lib.findall("./packages/package")}

    # Isometric projection: x right-and-up, y left-and-up, z straight up.
    AX, AY = math.radians(30.0), math.radians(150.0)
    ZS = 2.2                                    # exaggerate height to see it

    def iso(x, y, z):
        return (x * math.cos(AX) + y * math.cos(AY),
                x * math.sin(AX) + y * math.sin(AY) + z * ZS)

    fig, ax = plt.subplots(figsize=(20, 13))
    ax.set_facecolor("#fdfdfa")

    W, H, T = D.BOARD_W, D.BOARD_H, D.BOARD_THICKNESS

    def quad(pts, **kw):
        ax.add_patch(mp.Polygon([iso(*p) for p in pts], closed=True, **kw))

    # Board substrate: top face plus the two visible sides.
    quad([(0, 0, 0), (W, 0, 0), (W, H, 0), (0, H, 0)],
         fc="#dfe8d2", ec="#5a6b48", lw=0.9, zorder=2)
    quad([(0, 0, -T), (W, 0, -T), (W, 0, 0), (0, 0, 0)],
         fc="#b9c79f", ec="#5a6b48", lw=0.7, zorder=1)
    quad([(W, 0, -T), (W, H, -T), (W, H, 0), (W, 0, 0)],
         fc="#a8b891", ec="#5a6b48", lw=0.7, zorder=1)

    # Antenna keep-out, marked on the board face.
    ax1, ay1, ax2, ay2 = D.ANTENNA_KEEPOUT
    quad([(ax1, ay1, 0), (min(ax2, W), ay1, 0),
          (min(ax2, W), min(ay2, H), 0), (ax1, min(ay2, H), 0)],
         fc="#ffdcc0", ec="#ff8800", lw=0.8, hatch="//", alpha=0.9, zorder=3)

    COLOUR = {"datasheet": "#c8342b", "typical": "#8a8f98"}
    boxes = []
    for el in brd.findall("./elements/element"):
        pkg_name = el.get("package")
        h, src = PACKAGE_HEIGHT.get(pkg_name, (1.0, "typical"))
        if h <= 0.0:
            continue
        ox, oy = float(el.get("x")), float(el.get("y"))
        rot = el.get("rot", "R0")
        pk = pkgs[pkg_name]
        xs, ys = [], []
        for prim in list(pk.findall("smd")) + list(pk.findall("pad")):
            px, py = _rot(float(prim.get("x")), float(prim.get("y")), rot)
            if prim.tag == "smd":
                dx, dy = float(prim.get("dx")), float(prim.get("dy"))
                if prim.get("rot", "R0") in ("R90", "R270"):
                    dx, dy = dy, dx
                if rot in ("R90", "R270"):
                    dx, dy = dy, dx
            else:
                dx = dy = float(prim.get("diameter") or 1.8)
            xs += [ox + px - dx / 2, ox + px + dx / 2]
            ys += [oy + py - dy / 2, oy + py + dy / 2]
        if not xs:
            continue
        boxes.append((min(xs), min(ys), max(xs), max(ys), h,
                      "datasheet" if src.startswith("datasheet") else "typical",
                      el.get("name"), pkg_name))

    # Painter's algorithm: draw far parts first so near ones overlap them.
    boxes.sort(key=lambda b: -(b[0] + b[1]))
    for x0, y0, x1, y1, h, kind, name, pkg_name in boxes:
        c = COLOUR[kind]
        quad([(x0, y0, h), (x1, y0, h), (x1, y1, h), (x0, y1, h)],
             fc=c, ec="#33383f", lw=0.35, alpha=0.95, zorder=6)
        quad([(x0, y0, 0), (x1, y0, 0), (x1, y0, h), (x0, y0, h)],
             fc=c, ec="#33383f", lw=0.3, alpha=0.72, zorder=5)
        quad([(x1, y0, 0), (x1, y1, 0), (x1, y1, h), (x1, y0, h)],
             fc=c, ec="#33383f", lw=0.3, alpha=0.55, zorder=5)
        if h >= 3.0:                            # label only the tall parts
            lx, ly = iso((x0 + x1) / 2, (y0 + y1) / 2, h + 0.6)
            ax.text(lx, ly, f"{name}\n{h:.1f}mm", fontsize=5.0, ha="center",
                    va="bottom", color="#1b1f24", zorder=12,
                    bbox=dict(boxstyle="round,pad=0.12", fc="#ffffffdd",
                              ec="none"))

    tallest = max(boxes, key=lambda b: b[4])
    ax.legend(handles=[
        mp.Patch(fc=COLOUR["datasheet"], ec="#33383f",
                 label="height from the manufacturer package drawing"),
        mp.Patch(fc=COLOUR["typical"], ec="#33383f",
                 label="height typical for the package family - CONFIRM the part bought"),
        mp.Patch(fc="#ffdcc0", ec="#ff8800", hatch="//",
                 label="antenna keep-out (no copper, no parts)"),
    ], loc="lower left", fontsize=9, framealpha=0.95)

    ax.set_title(
        "SIH26113 Maternity Assist Belt - MECHANICAL ENVELOPE (isometric)\n"
        f"board {W:.0f} x {H:.0f} x {T} mm  |  tallest part "
        f"{tallest[6]} at {tallest[4]:.1f} mm  |  height axis exaggerated "
        f"{ZS:g}x for legibility\n"
        "EXTRUDED FOOTPRINT OUTLINES, NOT A SOLID MODEL - no STEP geometry is "
        "attached to these footprints",
        fontsize=12, pad=16)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.autoscale_view()
    f3d = OUTDIR / "pcb_3d.png"
    fig.savefig(f3d, dpi=200, bbox_inches="tight", facecolor="#fdfdfa")
    plt.close(fig)
    return [f3d]

if __name__ == "__main__":
    raise SystemExit(main())
