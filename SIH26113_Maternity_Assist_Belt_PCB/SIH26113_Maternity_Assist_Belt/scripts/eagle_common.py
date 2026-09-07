"""
eagle_common.py - Shared Autodesk EAGLE / Fusion Electronics XML emitters.

SIH26113 - Maternity Assist Belt prototype carrier board.

EAGLE (and Autodesk Fusion Electronics, which uses the same file model) stores
libraries (.lbr), schematics (.sch) and boards (.brd) as XML validated against
`eagle.dtd`.  This module holds:

  * the standard EAGLE layer table (required in every file),
  * small helpers to emit well-formed EAGLE XML elements,
  * IPC-7351B-derived land-pattern generators for the generic packages
    (0805 chip, SOT-23, SOT-23-5, SOD-123, SOIC-8, SOP-16) so that no
    footprint dimension in this project is invented by hand.

All coordinates are millimetres. All EAGLE angles are degrees ("R0".."R270").

Author: generated for the SIH26113 project.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from xml.sax.saxutils import escape

EAGLE_VERSION = "9.6.2"

# ---------------------------------------------------------------------------
# Layer table.  EAGLE refuses to open a file whose <layers> block is missing
# any layer referenced elsewhere in the document, so we always write the full
# standard set.
# ---------------------------------------------------------------------------
LAYERS: list[tuple[int, str, int, int, str, str]] = [
    (1, "Top", 4, 1, "yes", "yes"),
    (2, "Route2", 1, 3, "yes", "yes"),      # inner: solid GND plane
    (15, "Route15", 4, 6, "yes", "yes"),    # inner: solid 3V3 plane
    (16, "Bottom", 1, 1, "yes", "yes"),
    (17, "Pads", 2, 1, "yes", "yes"),
    (18, "Vias", 2, 1, "yes", "yes"),
    (19, "Unrouted", 6, 1, "yes", "yes"),
    (20, "Dimension", 15, 1, "yes", "yes"),
    (21, "tPlace", 7, 1, "yes", "yes"),
    (22, "bPlace", 7, 1, "yes", "yes"),
    (23, "tOrigins", 15, 1, "yes", "yes"),
    (24, "bOrigins", 15, 1, "yes", "yes"),
    (25, "tNames", 7, 1, "yes", "yes"),
    (26, "bNames", 7, 1, "yes", "yes"),
    (27, "tValues", 7, 1, "yes", "yes"),
    (28, "bValues", 7, 1, "yes", "yes"),
    (29, "tStop", 7, 3, "no", "yes"),
    (30, "bStop", 7, 6, "no", "yes"),
    (31, "tCream", 7, 4, "no", "yes"),
    (32, "bCream", 7, 5, "no", "yes"),
    (33, "tFinish", 6, 3, "no", "yes"),
    (34, "bFinish", 6, 6, "no", "yes"),
    (35, "tGlue", 7, 4, "no", "yes"),
    (36, "bGlue", 7, 5, "no", "yes"),
    (37, "tTest", 7, 1, "no", "yes"),
    (38, "bTest", 7, 1, "no", "yes"),
    (39, "tKeepout", 4, 11, "yes", "yes"),
    (40, "bKeepout", 1, 11, "yes", "yes"),
    (41, "tRestrict", 4, 10, "yes", "yes"),
    (42, "bRestrict", 1, 10, "yes", "yes"),
    (43, "vRestrict", 2, 10, "yes", "yes"),
    (44, "Drills", 7, 1, "no", "yes"),
    (45, "Holes", 7, 1, "no", "yes"),
    (46, "Milling", 3, 1, "no", "yes"),
    (47, "Measures", 7, 1, "no", "yes"),
    (48, "Document", 7, 1, "yes", "yes"),
    (49, "Reference", 7, 1, "yes", "yes"),
    (51, "tDocu", 7, 1, "yes", "yes"),
    (52, "bDocu", 7, 1, "yes", "yes"),
    (90, "Modules", 5, 1, "yes", "yes"),
    (91, "Nets", 2, 1, "yes", "yes"),
    (92, "Busses", 1, 1, "yes", "yes"),
    (93, "Pins", 2, 1, "no", "yes"),
    (94, "Symbols", 4, 1, "yes", "yes"),
    (95, "Names", 7, 1, "yes", "yes"),
    (96, "Values", 7, 1, "yes", "yes"),
    (97, "Info", 7, 1, "yes", "yes"),
    (98, "Guide", 6, 1, "yes", "yes"),
]


def n(v: float) -> str:
    """Format a coordinate the way EAGLE does: trimmed decimal, no exponent."""
    s = f"{float(v):.4f}".rstrip("0").rstrip(".")
    return "0" if s in ("", "-0") else s


def esc(s: str) -> str:
    return escape(str(s))


def layers_xml(indent: str = "") -> str:
    out = [f"{indent}<layers>"]
    for num, name, color, fill, vis, act in LAYERS:
        out.append(
            f'{indent}<layer number="{num}" name="{name}" color="{color}" '
            f'fill="{fill}" visible="{vis}" active="{act}"/>'
        )
    out.append(f"{indent}</layers>")
    return "\n".join(out)


SETTINGS_XML = (
    "<settings>\n"
    '<setting alwaysvectorfont="no"/>\n'
    '<setting verticaltext="up"/>\n'
    "</settings>"
)

GRID_XML = (
    '<grid distance="1.27" unitdist="mm" unit="mm" style="lines" multiple="1" '
    'display="no" altdistance="0.1" altunitdist="mm" altunit="mm"/>'
)


# ---------------------------------------------------------------------------
# Primitive dataclasses
# ---------------------------------------------------------------------------
@dataclass
class Smd:
    name: str
    x: float
    y: float
    dx: float
    dy: float
    layer: int = 1
    roundness: int = 0
    rot: str = "R0"
    thermals: str | None = None

    def xml(self) -> str:
        extra = f' roundness="{self.roundness}"' if self.roundness else ""
        if self.rot != "R0":
            extra += f' rot="{self.rot}"'
        if self.thermals:
            extra += f' thermals="{self.thermals}"'
        return (
            f'<smd name="{esc(self.name)}" x="{n(self.x)}" y="{n(self.y)}" '
            f'dx="{n(self.dx)}" dy="{n(self.dy)}" layer="{self.layer}"{extra}/>'
        )


@dataclass
class Pad:
    name: str
    x: float
    y: float
    drill: float
    diameter: float = 0.0
    shape: str = "round"
    rot: str = "R0"

    def xml(self) -> str:
        extra = ""
        if self.diameter:
            extra += f' diameter="{n(self.diameter)}"'
        if self.shape != "round":
            extra += f' shape="{self.shape}"'
        if self.rot != "R0":
            extra += f' rot="{self.rot}"'
        return (
            f'<pad name="{esc(self.name)}" x="{n(self.x)}" y="{n(self.y)}" '
            f'drill="{n(self.drill)}"{extra}/>'
        )


@dataclass
class Wire:
    x1: float
    y1: float
    x2: float
    y2: float
    width: float
    layer: int
    curve: float | None = None

    def xml(self) -> str:
        extra = f' curve="{n(self.curve)}"' if self.curve else ""
        return (
            f'<wire x1="{n(self.x1)}" y1="{n(self.y1)}" x2="{n(self.x2)}" '
            f'y2="{n(self.y2)}" width="{n(self.width)}" layer="{self.layer}"{extra}/>'
        )


@dataclass
class Circle:
    x: float
    y: float
    radius: float
    width: float
    layer: int

    def xml(self) -> str:
        return (
            f'<circle x="{n(self.x)}" y="{n(self.y)}" radius="{n(self.radius)}" '
            f'width="{n(self.width)}" layer="{self.layer}"/>'
        )


@dataclass
class Rect:
    x1: float
    y1: float
    x2: float
    y2: float
    layer: int

    def xml(self) -> str:
        return (
            f'<rectangle x1="{n(self.x1)}" y1="{n(self.y1)}" x2="{n(self.x2)}" '
            f'y2="{n(self.y2)}" layer="{self.layer}"/>'
        )


@dataclass
class Text:
    x: float
    y: float
    size: float
    layer: int
    content: str
    align: str | None = None
    ratio: int = 10
    rot: str = "R0"

    def xml(self) -> str:
        extra = f' ratio="{self.ratio}"'
        if self.rot != "R0":
            extra += f' rot="{self.rot}"'
        if self.align:
            extra += f' align="{self.align}"'
        return (
            f'<text x="{n(self.x)}" y="{n(self.y)}" size="{n(self.size)}" '
            f'layer="{self.layer}"{extra}>{esc(self.content)}</text>'
        )


@dataclass
class Hole:
    x: float
    y: float
    drill: float

    def xml(self) -> str:
        return f'<hole x="{n(self.x)}" y="{n(self.y)}" drill="{n(self.drill)}"/>'


# EAGLE pin electrical directions.  Using the correct one matters: it is what
# drives ERC.  Do NOT default everything to "pas".
#   nc  = not connected      in  = input            out = output (push/pull)
#   io  = bidirectional      oc  = open collector   pwr = power input
#   pas = passive            hiz = high impedance   sup = supply (rail symbol)
PIN_DIRECTIONS = {"nc", "in", "out", "io", "oc", "pwr", "pas", "hiz", "sup"}


@dataclass
class Pin:
    name: str
    x: float
    y: float
    length: str = "middle"          # point | short | middle | long
    direction: str = "pas"
    rot: str = "R0"
    visible: str = "both"           # off | pad | pin | both
    swaplevel: int = 0
    function: str = "none"          # none | dot | clk | dotclk

    def __post_init__(self) -> None:
        if self.direction not in PIN_DIRECTIONS:
            raise ValueError(f"bad EAGLE pin direction {self.direction!r} on {self.name}")

    def xml(self) -> str:
        extra = ""
        if self.length != "long":
            extra += f' length="{self.length}"'
        if self.direction != "io":
            extra += f' direction="{self.direction}"'
        if self.function != "none":
            extra += f' function="{self.function}"'
        if self.swaplevel:
            extra += f' swaplevel="{self.swaplevel}"'
        if self.rot != "R0":
            extra += f' rot="{self.rot}"'
        if self.visible != "both":
            extra += f' visible="{self.visible}"'
        return f'<pin name="{esc(self.name)}" x="{n(self.x)}" y="{n(self.y)}"{extra}/>'


# ---------------------------------------------------------------------------
# Containers
# ---------------------------------------------------------------------------
@dataclass
class Package:
    name: str
    description: str
    items: list = field(default_factory=list)

    def xml(self) -> str:
        body = "\n".join(i.xml() for i in self.items)
        return (
            f'<package name="{esc(self.name)}">\n'
            f"<description>{esc(self.description)}</description>\n"
            f"{body}\n</package>"
        )

    def pad_names(self) -> list[str]:
        return [i.name for i in self.items if isinstance(i, (Smd, Pad))]


@dataclass
class Symbol:
    name: str
    description: str
    items: list = field(default_factory=list)

    def xml(self) -> str:
        body = "\n".join(i.xml() for i in self.items)
        return (
            f'<symbol name="{esc(self.name)}">\n'
            f"<description>{esc(self.description)}</description>\n"
            f"{body}\n</symbol>"
        )

    def pin_names(self) -> list[str]:
        return [i.name for i in self.items if isinstance(i, Pin)]


@dataclass
class DeviceSet:
    """One EAGLE deviceset = one schematic symbol + one or more packages."""

    name: str
    prefix: str
    description: str
    symbol: str
    package: str | None
    connects: dict[str, str] = field(default_factory=dict)   # pin name -> pad name
    uservalue: bool = True
    gate_name: str = "G$1"

    def xml(self) -> str:
        uv = "yes" if self.uservalue else "no"
        out = [
            f'<deviceset name="{esc(self.name)}" prefix="{esc(self.prefix)}" uservalue="{uv}">',
            f"<description>{esc(self.description)}</description>",
            "<gates>",
            f'<gate name="{self.gate_name}" symbol="{esc(self.symbol)}" x="0" y="0"/>',
            "</gates>",
            "<devices>",
        ]
        if self.package:
            out.append(f'<device name="" package="{esc(self.package)}">')
            out.append("<connects>")
            for pin, pad in self.connects.items():
                out.append(
                    f'<connect gate="{self.gate_name}" pin="{esc(pin)}" pad="{esc(pad)}"/>'
                )
            out.append("</connects>")
        else:
            out.append('<device name="">')
        out.append("<technologies>")
        out.append('<technology name=""/>')
        out.append("</technologies>")
        out.append("</device>")
        out.append("</devices>")
        out.append("</deviceset>")
        return "\n".join(out)


# ---------------------------------------------------------------------------
# IPC-7351B-derived generic land patterns
#
# Reference: IPC-7351B "Generic Requirements for Surface Mount Design and Land
# Pattern Standard", Nominal (Level B) density.  Using the standard rather than
# eyeballing a drawing keeps these footprints defensible.
# ---------------------------------------------------------------------------
def chip_package(name: str, description: str, *, body_l: float, body_w: float,
                 pad_l: float, pad_w: float, gap: float,
                 polarised: bool = False, silk_gap: float = 0.25) -> Package:
    """Two-terminal chip component (resistor/capacitor/LED/diode).

    gap = inner-edge-to-inner-edge distance between the two lands.
    """
    cx = gap / 2.0 + pad_l / 2.0
    items: list = [
        Smd("1", -cx, 0, pad_l, pad_w),
        Smd("2", +cx, 0, pad_l, pad_w),
    ]
    # Silkscreen: two short bars outboard of the lands (never over copper).
    sx = cx + pad_l / 2.0 + silk_gap
    sy = max(body_w, pad_w) / 2.0 + 0.1
    items += [
        Wire(-sx, -sy, -sx, sy, 0.12, 21),
        Wire(+sx, -sy, +sx, sy, 0.12, 21),
    ]
    if polarised:
        # Cathode / pin-1 bar on the pin-1 side, plus a courtyard tick.
        items.append(Wire(-sx - 0.25, -sy, -sx - 0.25, sy, 0.2, 21))
    # Assembly body outline (docu layer) + courtyard keepout.
    items += [
        Rect(-body_l / 2, -body_w / 2, body_l / 2, body_w / 2, 51),
        Wire(-sx - 0.35, -sy - 0.35, sx + 0.35, -sy - 0.35, 0.05, 39),
        Wire(sx + 0.35, -sy - 0.35, sx + 0.35, sy + 0.35, 0.05, 39),
        Wire(sx + 0.35, sy + 0.35, -sx - 0.35, sy + 0.35, 0.05, 39),
        Wire(-sx - 0.35, sy + 0.35, -sx - 0.35, -sy - 0.35, 0.05, 39),
        Text(-sx, sy + 0.5, 0.8, 25, ">NAME"),
        Text(-sx, -sy - 1.3, 0.8, 27, ">VALUE"),
    ]
    return Package(name, description, items)


def gullwing_package(name: str, description: str, *, pins_per_side: int,
                     pitch: float, span: float, pad_l: float, pad_w: float,
                     body_l: float, body_w: float) -> Package:
    """Dual-row gull-wing SMD package (SOIC / SOP / TSSOP).

    span = land centre-to-centre across the two rows.
    Pin 1 = top-left; numbering runs down the left row then up the right row
    (the JEDEC convention for SOIC/SOP).
    """
    items: list = []
    x = span / 2.0
    y0 = (pins_per_side - 1) * pitch / 2.0
    for i in range(pins_per_side):
        items.append(Smd(str(i + 1), -x, y0 - i * pitch, pad_l, pad_w))
    for i in range(pins_per_side):
        items.append(
            Smd(str(pins_per_side + i + 1), +x, -y0 + i * pitch, pad_l, pad_w)
        )
    # Silkscreen body outline, broken where the lands are.
    bx, by = body_w / 2.0, body_l / 2.0
    items += [
        Wire(-bx, by, bx, by, 0.12, 21),
        Wire(-bx, -by, bx, -by, 0.12, 21),
        Wire(-bx, by, -bx, by - 0.4, 0.12, 21),
        Wire(-bx, -by, -bx, -by + 0.4, 0.12, 21),
        Wire(bx, by, bx, by - 0.4, 0.12, 21),
        Wire(bx, -by, bx, -by + 0.4, 0.12, 21),
    ]
    # Pin-1 dot, outboard of pad 1 so it stays off copper.
    items.append(Circle(-x - pad_l / 2.0 - 0.35, y0, 0.15, 0.15, 21))
    items += [
        Rect(-bx, -by, bx, by, 51),
        Text(-bx, by + 0.6, 0.9, 25, ">NAME"),
        Text(-bx, -by - 1.5, 0.9, 27, ">VALUE"),
    ]
    return Package(name, description, items)


def sot23_package(name: str, description: str, *, pad_l: float, pad_w: float,
                  span: float, pitch: float, three_pin: bool = True,
                  pin_count: int = 3) -> Package:
    """SOT-23 family.

    SOT-23-3: pads 1,2 on the lower row, pad 3 alone on the upper row.
    SOT-23-5: pads 1,2,3 on the lower row, 4,5 on the upper row (JEDEC TO-178).
    """
    items: list = []
    y = span / 2.0
    # The pads sit on the top and bottom edges, so the RADIAL direction is Y
    # and the TANGENTIAL direction is X.  `pad_l` is the radial dimension and
    # `pad_w` the tangential one, so dx = pad_w and dy = pad_l.  Getting these
    # the wrong way round makes 1.10 mm pads on a 0.95 mm pitch overlap - a
    # short between adjacent pins that looks perfectly plausible in the
    # library editor.
    dx, dy = pad_w, pad_l
    if pin_count == 3:
        items += [
            Smd("1", -pitch / 2.0, -y, dx, dy),
            Smd("2", +pitch / 2.0, -y, dx, dy),
            Smd("3", 0.0, +y, dx, dy),
        ]
    elif pin_count == 5:
        items += [
            Smd("1", -pitch, -y, dx, dy),
            Smd("2", 0.0, -y, dx, dy),
            Smd("3", +pitch, -y, dx, dy),
            Smd("4", +pitch, +y, dx, dy),
            Smd("5", -pitch, +y, dx, dy),
        ]
    else:
        raise ValueError("sot23_package supports pin_count 3 or 5")
    bx, by = 1.45, 1.5
    items += [
        Wire(-bx, -by, bx, -by, 0.12, 21),
        Wire(-bx, by, bx, by, 0.12, 21),
        Wire(-bx, -by, -bx, by, 0.12, 21),
        Wire(bx, -by, bx, by, 0.12, 21),
        Circle(-bx - 0.35, -y, 0.15, 0.15, 21),
        Rect(-bx, -by, bx, by, 51),
        Text(-bx, by + 0.6, 0.8, 25, ">NAME"),
        Text(-bx, -by - 1.4, 0.8, 27, ">VALUE"),
    ]
    return Package(name, description, items)


def header_package(name: str, description: str, *, positions: int,
                   pitch: float = 2.54, drill: float = 1.0,
                   diameter: float = 1.8, rows: int = 1) -> Package:
    """Through-hole pin header, 1 x N (or 2 x N), pin 1 square.

    2.54 mm headers are a de-facto standard geometry; drill 1.0 mm suits the
    0.64 mm square posts used by every common 2.54 mm header.
    """
    items: list = []
    x0 = -(positions - 1) * pitch / 2.0
    idx = 1
    for r in range(rows):
        y = (rows - 1) * pitch / 2.0 - r * pitch
        for c in range(positions):
            shape = "square" if idx == 1 else "round"
            items.append(Pad(str(idx), x0 + c * pitch, y, drill, diameter, shape))
            idx += 1
    hw = (positions - 1) * pitch / 2.0 + pitch / 2.0
    hh = (rows - 1) * pitch / 2.0 + pitch / 2.0
    items += [
        Wire(-hw, -hh, hw, -hh, 0.12, 21),
        Wire(hw, -hh, hw, hh, 0.12, 21),
        Wire(hw, hh, -hw, hh, 0.12, 21),
        Wire(-hw, hh, -hw, -hh, 0.12, 21),
        # Pin-1 chamfer marker.
        Wire(-hw, hh - 0.6, -hw + 0.6, hh, 0.2, 21),
        Text(-hw, hh + 0.4, 0.9, 25, ">NAME"),
        Text(-hw, -hh - 1.5, 0.9, 27, ">VALUE"),
    ]
    return Package(name, description, items)


# ---------------------------------------------------------------------------
# Symbol drawing helpers
# ---------------------------------------------------------------------------
def box_symbol(name: str, description: str, pins: list[Pin], *,
               width: float, height: float,
               name_pos: tuple[float, float] | None = None,
               value_pos: tuple[float, float] | None = None,
               labels: list[Text] | None = None) -> Symbol:
    """Rectangular IC symbol with a pin list already positioned by the caller."""
    hw, hh = width / 2.0, height / 2.0
    items: list = [
        Wire(-hw, -hh, hw, -hh, 0.254, 94),
        Wire(hw, -hh, hw, hh, 0.254, 94),
        Wire(hw, hh, -hw, hh, 0.254, 94),
        Wire(-hw, hh, -hw, -hh, 0.254, 94),
    ]
    npx, npy = name_pos or (-hw, hh + 1.0)
    vpx, vpy = value_pos or (-hw, -hh - 2.2)
    items.append(Text(npx, npy, 1.778, 95, ">NAME"))
    items.append(Text(vpx, vpy, 1.778, 96, ">VALUE"))
    if labels:
        items.extend(labels)
    items.extend(pins)
    return Symbol(name, description, items)


# ---------------------------------------------------------------------------
# Document assembly
# ---------------------------------------------------------------------------
def library_body(description: str, packages: list[Package],
                 symbols: list[Symbol], devicesets: list[DeviceSet],
                 name: str | None = None) -> str:
    """Emit a <library> element (used both standalone and embedded)."""
    attr = f' name="{esc(name)}"' if name else ""
    parts = [f"<library{attr}>", f"<description>{esc(description)}</description>"]
    parts.append("<packages>")
    parts += [p.xml() for p in packages]
    parts.append("</packages>")
    parts.append("<symbols>")
    parts += [s.xml() for s in symbols]
    parts.append("</symbols>")
    parts.append("<devicesets>")
    parts += [d.xml() for d in devicesets]
    parts.append("</devicesets>")
    parts.append("</library>")
    return "\n".join(parts)


def document(inner: str) -> str:
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<!DOCTYPE eagle SYSTEM "eagle.dtd">\n'
        f'<eagle version="{EAGLE_VERSION}">\n'
        "<drawing>\n"
        f"{SETTINGS_XML}\n"
        f"{GRID_XML}\n"
        f"{layers_xml()}\n"
        f"{inner}\n"
        "</drawing>\n"
        "</eagle>\n"
    )
