"""
generate_schematic.py - Emit SIH26113_Maternity_Assist_Belt.sch

Connectivity style: every component pin gets a short stub wire terminated by a
net label.  EAGLE merges same-named net segments within and across sheets, so
this produces a single, fully-connected netlist while keeping seven dense
sheets readable.  It is the same technique used on production multi-sheet
EAGLE schematics.

Run:  python scripts/generate_schematic.py
"""

from __future__ import annotations

import pathlib
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import design as D  # noqa: E402
import geom  # noqa: E402
from eagle_common import Text, Wire, document, esc, library_body, n  # noqa: E402
from lib_defs import (  # noqa: E402
    DEVICESETS,
    LIBRARY_DESCRIPTION,
    LIBRARY_NAME,
    PACKAGES,
    SYMBOLS,
)

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "schematic" / f"{LIBRARY_NAME}.sch"

STUB = 3.81           # mm of stub wire between the pin end and its net label
WIRE_W = 0.1524       # EAGLE default net wire width

SHEET_W, SHEET_H = 380.0, 260.0        # drawing frame, mm (~A3 landscape)


def classes_xml() -> str:
    out = ["<classes>"]
    for num, name, width, drill, clearance in D.NET_CLASSES:
        out.append(
            f'<class number="{num}" name="{name}" width="{n(width)}" '
            f'drill="{n(drill)}">'
        )
        out.append(f'<clearance class="{num}" value="{n(clearance)}"/>')
        out.append("</class>")
    out.append("</classes>")
    return "\n".join(out)


def frame(sheet: int) -> list[str]:
    """Drawing frame and title block for one sheet, on the plain layer."""
    items: list = [
        Wire(0, 0, SHEET_W, 0, 0.3, 94),
        Wire(SHEET_W, 0, SHEET_W, SHEET_H, 0.3, 94),
        Wire(SHEET_W, SHEET_H, 0, SHEET_H, 0.3, 94),
        Wire(0, SHEET_H, 0, 0, 0.3, 94),
        # Title block.
        Wire(0, 22, SHEET_W, 22, 0.3, 94),
        Wire(0, 10, SHEET_W, 10, 0.2, 94),
        Text(3, 16, 3.0, 94, D.PROJECT_TITLE),
        Text(3, 12, 2.0, 94, D.SHEET_TITLES[sheet]),
        Text(3, 5.5, 1.8, 94, D.PROJECT_SUBTITLE),
        Text(3, 2.0, 1.8, 94,
             f"{D.BOARD_LAYERS}-layer FR-4 {D.BOARD_THICKNESS} mm "
             f"(L1 sig / L2 GND plane / L15 3V3 plane / L16 sig) | "
             f"board {D.BOARD_W:.0f} x {D.BOARD_H:.0f} mm | "
             f"lib {LIBRARY_NAME}.lbr | sheet {sheet} of 7"),
        Text(SHEET_W - 60, SHEET_H - 8, 3.5, 94, f"SHEET {sheet}/7"),
    ]
    return [i.xml() for i in items]


def block_labels(sheet: int) -> list[str]:
    """Big section captions per sheet, so the printed page reads like a doc."""
    CAPTIONS = {
        1: [(20, 200, "BATTERY / CHARGE INPUT"), (95, 200, "TP4056 CHARGER"),
            (150, 200, "3V3 LDO"), (200, 200, "BATTERY MONITOR")],
        2: [(60, 200, "SUPPLY DECOUPLING"), (120, 200, "ESP32-S3-WROOM-1-N8R2"),
            (205, 200, "PROGRAMMING / RESET / BOOT"), (205, 120, "INDICATORS")],
        3: [(40, 200, "SENSOR BUS I2C0 PULL-UPS"), (100, 200, "TMP117 / LSM6DSOX"),
            (40, 110, "ANGLE BUS I2C1 PULL-UPS"), (100, 110, "AS5600 + SIDE-B")],
        4: [(30, 200, "ELECTRODE INTERFACE + PROTECTION"),
            (150, 200, "AD8232 (Vs = 3V3 ONLY)"),
            (200, 200, "2-POLE HPF"), (255, 200, "2-POLE LPF, GAIN 11")],
        5: [(30, 200, "LOAD CELL BRIDGE"), (110, 200, "HX711 24-BIT ADC"),
            (200, 200, "FSR DIVIDERS"), (250, 160, "PIEZO CONDITIONING"),
            (250, 100, "HALL / LIMIT")],
        6: [(85, 200, "MOTOR DRIVER"), (85, 135, "BUZZER DRIVER")],
        7: [(55, 195, "SOS BUTTON"), (185, 195, "microSD (SPI MODULE)")],
    }
    return [Text(x, y, 2.6, 94, t).xml() for x, y, t in CAPTIONS.get(sheet, [])]


def build_sheet(sheet: int) -> str:
    parts = [p for p in D.PARTS if p.sheet == sheet]
    refs = {p.ref for p in parts}

    plain = frame(sheet) + block_labels(sheet)

    inst = []
    for p in parts:
        inst.append(
            f'<instance part="{esc(p.ref)}" gate="G$1" x="{n(p.sx)}" '
            f'y="{n(p.sy)}"'
            + (f' rot="{p.srot}"' if p.srot != "R0" else "")
            + "/>"
        )

    # Group the connections that live on this sheet, per net.
    per_net: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for net, conns in D.NETS.items():
        for ref, pin in conns:
            if ref in refs:
                per_net[net].append((ref, pin))

    nets_xml = []
    for net in sorted(per_net):
        cls = D.net_class(net)
        seg = [f'<net name="{esc(net)}" class="{cls}">']
        for ref, pin in per_net[net]:
            p = D.PART_BY_REF[ref]
            px, py, (dx, dy) = geom.sch_pin_pos(p.deviceset, pin,
                                                p.sx, p.sy, p.srot)
            ex, ey = px + dx * STUB, py + dy * STUB
            lrot = "R90" if abs(dy) > abs(dx) else "R0"
            # Nudge the label off the wire end so text does not sit on copper.
            lx = ex + (0.0 if lrot == "R90" else (0.8 if dx > 0 else -0.8))
            ly = ey + (0.8 if lrot == "R90" else 0.8)
            seg.append("<segment>")
            seg.append(
                f'<pinref part="{esc(ref)}" gate="G$1" pin="{esc(pin)}"/>'
            )
            seg.append(
                f'<wire x1="{n(px)}" y1="{n(py)}" x2="{n(ex)}" y2="{n(ey)}" '
                f'width="{n(WIRE_W)}" layer="91"/>'
            )
            align = "bottom-right" if (lrot == "R0" and dx < 0) else "bottom-left"
            seg.append(
                f'<label x="{n(lx)}" y="{n(ly)}" size="1.27" layer="95" '
                f'rot="{lrot}" align="{align}" xref="yes"/>'
            )
            seg.append("</segment>")
        seg.append("</net>")
        nets_xml.append("\n".join(seg))

    return (
        "<sheet>\n"
        f"<description>{esc(D.SHEET_TITLES[sheet])}</description>\n"
        "<plain>\n" + "\n".join(plain) + "\n</plain>\n"
        "<instances>\n" + "\n".join(inst) + "\n</instances>\n"
        "<busses/>\n"
        "<nets>\n" + "\n".join(nets_xml) + "\n</nets>\n"
        "</sheet>"
    )


def main() -> int:
    lib = library_body(LIBRARY_DESCRIPTION, PACKAGES, SYMBOLS, DEVICESETS,
                       name=LIBRARY_NAME)

    parts_xml = ["<parts>"]
    for p in sorted(D.PARTS, key=lambda q: (q.sheet, q.ref)):
        val = f' value="{esc(p.value)}"' if p.value else ""
        parts_xml.append(
            f'<part name="{esc(p.ref)}" library="{esc(LIBRARY_NAME)}" '
            f'deviceset="{esc(p.deviceset)}" device=""{val}/>'
        )
    parts_xml.append("</parts>")

    sheets = "\n".join(build_sheet(s) for s in sorted(D.SHEET_TITLES))

    inner = (
        '<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">\n'
        "<libraries>\n" + lib + "\n</libraries>\n"
        "<attributes/>\n"
        "<variantdefs/>\n"
        + classes_xml() + "\n"
        + "\n".join(parts_xml) + "\n"
        "<sheets>\n" + sheets + "\n</sheets>\n"
        "</schematic>"
    )

    xml = document(inner)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(xml, encoding="utf-8")

    # Structural verification: re-parse and confirm the emitted schematic
    # contains exactly the parts, nets and pinrefs the model describes.
    tree = ET.fromstring(xml.split("\n", 2)[2])
    sch = tree.find("./drawing/schematic")
    got_parts = {e.get("name") for e in sch.findall("./parts/part")}
    want_parts = {p.ref for p in D.PARTS}
    assert got_parts == want_parts, f"part mismatch: {want_parts ^ got_parts}"

    pinrefs = defaultdict(set)
    for sh in sch.findall("./sheets/sheet"):
        for net in sh.findall("./nets/net"):
            for pr in net.findall(".//pinref"):
                pinrefs[net.get("name")].add((pr.get("part"), pr.get("pin")))
    want = {k: set(v) for k, v in D.NETS.items()}
    bad = []
    for k in set(want) | set(pinrefs):
        if want.get(k, set()) != pinrefs.get(k, set()):
            bad.append(k)
    assert not bad, f"netlist mismatch on: {bad}"

    nsheets = len(sch.findall("./sheets/sheet"))
    nsegs = len(sch.findall(".//segment"))
    print(f"WROTE {OUT.relative_to(ROOT)}  ({OUT.stat().st_size:,} bytes)")
    print(f"  sheets={nsheets}  parts={len(got_parts)}  "
          f"nets={len(pinrefs)}  segments={nsegs}")
    print("  schematic vs. model cross-check: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
