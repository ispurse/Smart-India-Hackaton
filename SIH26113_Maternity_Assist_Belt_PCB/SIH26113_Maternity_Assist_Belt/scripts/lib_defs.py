"""
lib_defs.py - Single source of truth for the SIH26113 Maternity Assist Belt
EAGLE / Fusion Electronics library.

Every footprint dimension below is either
  (V) taken from the manufacturer's own package-outline / recommended
      land-pattern drawing (source cited inline), or
  (I) computed from IPC-7351B Nominal (Level B) density for a generic
      package family, or
  (S) a de-facto standard geometry (2.54 mm headers, M2 mounting hole).

Nothing here is estimated from a picture of a block diagram.

See ../documentation/COMPONENT_VERIFICATION.md for the full audit trail.
"""

from __future__ import annotations

from eagle_common import (
    Circle,
    DeviceSet,
    Hole,
    Package,
    Pad,
    Pin,
    Rect,
    Smd,
    Symbol,
    Text,
    Wire,
    box_symbol,
    chip_package,
    gullwing_package,
    header_package,
    sot23_package,
)

# EAGLE pin body lengths, in mm, keyed by the length attribute.
PIN_LEN = {"point": 0.0, "short": 2.54, "middle": 5.08, "long": 7.62}

# Short human-readable annotation for each EAGLE electrical direction.  These
# are drawn on layer 97 (Info) inside the symbol so the printed schematic
# states the pin type explicitly, as well as carrying it in the ERC model.
DIR_LABEL = {
    "in": "IN",
    "out": "OUT",
    "io": "I/O",
    "oc": "OC",
    "pwr": "PWR",
    "pas": "PAS",
    "hiz": "HIZ",
    "nc": "NC",
    "sup": "SUP",
}


# ---------------------------------------------------------------------------
# Symbol pin placement helpers
# ---------------------------------------------------------------------------
def _pin(side: str, name: str, hw: float, hh: float, offset: float,
         direction: str, length: str = "middle") -> tuple[Pin, Text]:
    """Create a pin on `side` of a box plus its type annotation text."""
    L = PIN_LEN[length]
    if side == "L":
        p = Pin(name, -hw - L, offset, length=length, direction=direction, rot="R0")
        t = Text(-hw + 0.7, offset - 0.55, 0.9, 97, DIR_LABEL[direction])
    elif side == "R":
        p = Pin(name, hw + L, offset, length=length, direction=direction, rot="R180")
        t = Text(hw - 0.7, offset - 0.55, 0.9, 97, DIR_LABEL[direction],
                 align="bottom-right")
    elif side == "T":
        p = Pin(name, offset, hh + L, length=length, direction=direction, rot="R270")
        t = Text(offset + 0.6, hh - 0.7, 0.9, 97, DIR_LABEL[direction],
                 rot="R90", align="bottom-right")
    elif side == "B":
        p = Pin(name, offset, -hh - L, length=length, direction=direction, rot="R90")
        t = Text(offset - 0.6, -hh + 0.7, 0.9, 97, DIR_LABEL[direction], rot="R90")
    else:
        raise ValueError(side)
    return p, t


def make_ic_symbol(name: str, description: str, width: float,
                   left: list[tuple[str, str]], right: list[tuple[str, str]],
                   *, pitch: float = 2.54, top_pad: float = 2.54,
                   extra: list | None = None) -> Symbol:
    """Build a rectangular IC symbol from ordered (pin_name, direction) lists."""
    rows = max(len(left), len(right))
    height = (rows - 1) * pitch + 2 * top_pad
    hw, hh = width / 2.0, height / 2.0
    y0 = (rows - 1) * pitch / 2.0
    pins: list = []
    labels: list = []
    for i, (pn, d) in enumerate(left):
        p, t = _pin("L", pn, hw, hh, y0 - i * pitch, d)
        pins.append(p)
        labels.append(t)
    for i, (pn, d) in enumerate(right):
        p, t = _pin("R", pn, hw, hh, y0 - i * pitch, d)
        pins.append(p)
        labels.append(t)
    if extra:
        labels.extend(extra)
    return box_symbol(name, description, pins, width=width, height=height,
                      labels=labels)


# ===========================================================================
# PACKAGES
# ===========================================================================
PACKAGES: list[Package] = []


# ---------------------------------------------------------------------------
# (V) ESP32-S3-WROOM-1  -- Espressif datasheet v1.8, Fig. 11-1 "Recommended
#     PCB Land Pattern" + Fig. 10-1 "Physical Dimensions".
#
#     Module body            : 25.5 (Y) x 18.0 (X) x 3.1 mm
#     Antenna area           : 6.0 mm at the +Y end, full width
#     40 castellated lands   : 1.5 mm (radial) x 0.9 mm (tangential)
#     Pitch                  : 1.27 mm
#     Column row spacing     : 17.5 mm centre-to-centre
#     Column pad span        : 16.51 mm (14 pads)
#     End-row pad span       : 13.97 mm (12 pads), 2.015 mm from each side edge
#     Pin 1 centre           : 7.49 mm below the module's +Y (antenna) edge
#     Pin numbering          : 1..14 left column (top->bottom),
#                              15..26 bottom row (left->right),
#                              27..40 right column (bottom->top),
#                              41 = EPAD (GND)
# ---------------------------------------------------------------------------
def _esp32_s3_wroom1() -> Package:
    BODY_X, BODY_Y = 18.0, 25.5
    PITCH = 1.27
    PAD_RADIAL, PAD_TANG = 1.5, 0.9
    COL_SPACING = 17.5
    ANTENNA = 6.0
    Y_PIN1 = BODY_Y / 2.0 - 7.49                      # = +5.26
    END_ROW_Y = -BODY_Y / 2.0 + 0.25                  # = -12.50
    END_ROW_X0 = -BODY_X / 2.0 + 2.015                # = -6.985

    items: list = []
    # Pins 1..14 : left column, top -> bottom.
    for i in range(14):
        items.append(
            Smd(str(i + 1), -COL_SPACING / 2.0, Y_PIN1 - i * PITCH,
                PAD_RADIAL, PAD_TANG)
        )
    # Pins 15..26 : bottom (non-antenna) end row, left -> right.
    for i in range(12):
        items.append(
            Smd(str(15 + i), END_ROW_X0 + i * PITCH, END_ROW_Y,
                PAD_TANG, PAD_RADIAL)
        )
    # Pins 27..40 : right column, bottom -> top.
    y40 = Y_PIN1
    for i in range(14):
        items.append(
            Smd(str(27 + i), +COL_SPACING / 2.0, y40 - (13 - i) * PITCH,
                PAD_RADIAL, PAD_TANG)
        )
    # Pin 41 : EPAD.  Espressif's figure sub-divides the thermal land into a
    # 3x3 copper array (3.7 mm centre span) with vias, purely for solder-paste
    # void control.  We use one conservative solid land inside that envelope
    # plus nine 0.3 mm thermal vias -- electrically identical (all GND).
    EPAD_CX, EPAD_CY, EPAD = -1.25, -2.5, 3.4
    items.append(Smd("41", EPAD_CX, EPAD_CY, EPAD, EPAD, thermals="no"))
    # Thermal vias are NOT put in the package: EAGLE's <hole> is an unplated
    # mechanical hole, which through a thermal land would be a defect.  They
    # are emitted as plated vias on the GND signal by generate_board.py --
    # see THERMAL_VIAS below.

    # Silkscreen: module outline, opened along the pad rows.
    hx, hy = BODY_X / 2.0, BODY_Y / 2.0
    items += [
        Wire(-hx, hy, hx, hy, 0.15, 21),
        Wire(-hx, hy, -hx, Y_PIN1 + PAD_TANG / 2.0 + 0.3, 0.15, 21),
        Wire(hx, hy, hx, Y_PIN1 + PAD_TANG / 2.0 + 0.3, 0.15, 21),
        # Antenna-area boundary marker.
        Wire(-hx, hy - ANTENNA, hx, hy - ANTENNA, 0.15, 21),
        Text(-hx + 1.0, hy - ANTENNA + 1.8, 1.0, 21, "ANTENNA - KEEP CLEAR"),
        # Pin-1 marker, outboard of pad 1.
        Circle(-COL_SPACING / 2.0 - PAD_RADIAL / 2.0 - 0.6, Y_PIN1, 0.25, 0.2, 21),
        # Assembly outline on tDocu.
        Rect(-hx, -hy, hx, hy, 51),
    ]
    # Keepout under the antenna: no copper on any layer, per Espressif's
    # "General Principles of PCB Layout for Modules".
    items += [
        Rect(-hx, hy - ANTENNA, hx, hy, 41),
        Rect(-hx, hy - ANTENNA, hx, hy, 42),
        Rect(-hx, hy - ANTENNA, hx, hy, 43),
        Rect(-hx, hy - ANTENNA, hx, hy, 39),
    ]
    items += [
        Text(-hx, -hy - 1.6, 1.1, 25, ">NAME"),
        Text(-hx, -hy - 3.2, 1.1, 27, ">VALUE"),
    ]
    return Package(
        "ESP32-S3-WROOM-1",
        "Espressif ESP32-S3-WROOM-1 module land pattern. Source: "
        "ESP32-S3-WROOM-1/1U datasheet v1.8 Fig.11-1 + Fig.10-1. "
        "40 lands 1.5x0.9 mm, 1.27 mm pitch, 17.5 mm row spacing, "
        "pin 1 at 7.49 mm from the antenna edge. 6 mm antenna keepout at +Y.",
        items,
    )


PACKAGES.append(_esp32_s3_wroom1())


# ---------------------------------------------------------------------------
# (I) AD8232 : 20-lead LFCSP_WQ, ADI package CP-20-10, JEDEC MO-220-WGGD.
#     Verified from the AD8232 Rev.A outline drawing:
#       body 4.00 SQ, pitch 0.50 BSC, terminal 0.40 long x 0.25 wide,
#       exposed pad 2.50 SQ, height 0.75.
#     ADI does not publish a land pattern in this data sheet, so the lands are
#     IPC-7351B Nominal for QFN 0.50 mm pitch: 0.80 x 0.28 mm, land centre
#     1.75 mm from package centre (0.15 mm toe outside the body edge).
#     Numbering is CCW from the top-left: 1-5 left, 6-10 bottom,
#     11-15 right, 16-20 top (confirmed against the data sheet pin diagram).
# ---------------------------------------------------------------------------
def _lfcsp20() -> Package:
    PITCH = 0.5
    PAD_L, PAD_W = 0.80, 0.28
    CENTRE = 1.75
    EPAD = 2.50
    BODY = 4.00
    items: list = []
    span = (5 - 1) * PITCH / 2.0                       # 1.0
    # 1..5 left column, top -> bottom (pads long in X).
    for i in range(5):
        items.append(Smd(str(1 + i), -CENTRE, span - i * PITCH, PAD_L, PAD_W))
    # 6..10 bottom row, left -> right (pads long in Y).
    for i in range(5):
        items.append(Smd(str(6 + i), -span + i * PITCH, -CENTRE, PAD_W, PAD_L))
    # 11..15 right column, bottom -> top.
    for i in range(5):
        items.append(Smd(str(11 + i), +CENTRE, -span + i * PITCH, PAD_L, PAD_W))
    # 16..20 top row, right -> left.
    for i in range(5):
        items.append(Smd(str(16 + i), +span - i * PITCH, +CENTRE, PAD_W, PAD_L))
    # Exposed pad (pin name "EP") + 4 thermal vias.
    items.append(Smd("EP", 0, 0, EPAD, EPAD, thermals="no"))
    # Thermal vias for this exposed pad are emitted on the GND signal at
    # board level (see THERMAL_VIAS), not as unplated package holes.
    h = BODY / 2.0
    items += [
        # Silkscreen corner brackets only (0.5 mm pitch leaves no room for a
        # continuous outline that clears copper).
        Wire(-h - 0.15, h - 0.5, -h - 0.15, h + 0.15, 0.12, 21),
        Wire(-h - 0.15, h + 0.15, -h + 0.5, h + 0.15, 0.12, 21),
        Wire(h + 0.15, h - 0.5, h + 0.15, h + 0.15, 0.12, 21),
        Wire(h + 0.15, h + 0.15, h - 0.5, h + 0.15, 0.12, 21),
        Wire(-h - 0.15, -h + 0.5, -h - 0.15, -h - 0.15, 0.12, 21),
        Wire(-h - 0.15, -h - 0.15, -h + 0.5, -h - 0.15, 0.12, 21),
        Wire(h + 0.15, -h + 0.5, h + 0.15, -h - 0.15, 0.12, 21),
        Wire(h + 0.15, -h - 0.15, h - 0.5, -h - 0.15, 0.12, 21),
        Circle(-h - 0.55, h - 0.1, 0.18, 0.18, 21),      # pin-1 dot
        Rect(-h, -h, h, h, 51),
        Text(-h, h + 0.6, 0.9, 25, ">NAME"),
        Text(-h, -h - 1.5, 0.9, 27, ">VALUE"),
    ]
    return Package(
        "LFCSP-20-4X4-P050",
        "20-lead LFCSP_WQ 4x4 mm, 0.5 mm pitch, 2.50 mm SQ exposed pad "
        "(ADI CP-20-10 / JEDEC MO-220-WGGD). Body+terminal dims verified from "
        "the AD8232 Rev.A outline drawing; lands are IPC-7351B Nominal "
        "(0.80 x 0.28 mm at 1.75 mm from centre).",
        items,
    )


PACKAGES.append(_lfcsp20())


# ---------------------------------------------------------------------------
# (V) TMP117 : 6-pin WSON, TI package DRV0006B.
#     TI's own "EXAMPLE BOARD LAYOUT" (datasheet SNOSD82D p.41):
#       6 lands 0.45 x 0.30 mm, 0.65 mm pitch, rows 1.95 mm apart,
#       exposed thermal pad 1.6 x 1.0 mm (package outline p.40), body 2.0 SQ.
#     Numbering CCW from top-left: 1 SCL, 2 GND, 3 ALERT (left),
#     4 ADD0, 5 V+, 6 SDA (right).
# ---------------------------------------------------------------------------
def _wson6() -> Package:
    PITCH = 0.65
    PAD_L, PAD_W = 0.45, 0.30
    ROW = 1.95
    items: list = []
    for i in range(3):                                  # 1,2,3 left col
        items.append(Smd(str(1 + i), -ROW / 2.0, PITCH - i * PITCH, PAD_L, PAD_W))
    for i in range(3):                                  # 4,5,6 right col up
        items.append(Smd(str(4 + i), +ROW / 2.0, -PITCH + i * PITCH, PAD_L, PAD_W))
    items.append(Smd("7", 0, 0, 1.0, 1.6, thermals="no"))   # thermal pad
    # Thermal vias emitted on the GND signal at board level (THERMAL_VIAS).
    h = 1.0
    items += [
        Wire(-h - 0.1, h + 0.1, -h + 0.4, h + 0.1, 0.1, 21),
        Wire(h + 0.1, h + 0.1, h - 0.4, h + 0.1, 0.1, 21),
        Wire(-h - 0.1, -h - 0.1, -h + 0.4, -h - 0.1, 0.1, 21),
        Wire(h + 0.1, -h - 0.1, h - 0.4, -h - 0.1, 0.1, 21),
        Circle(-h - 0.45, h - 0.1, 0.15, 0.15, 21),
        Rect(-h, -h, h, h, 51),
        Text(-h, h + 0.5, 0.8, 25, ">NAME"),
        Text(-h, -h - 1.3, 0.8, 27, ">VALUE"),
    ]
    return Package(
        "WSON-6-DRV0006B",
        "TI DRV0006B 6-pin WSON 2.0x2.0 mm, 0.65 mm pitch, thermal pad "
        "1.0x1.6 mm. Lands 0.45x0.30 mm at 1.95 mm row spacing, taken "
        "directly from TI's EXAMPLE BOARD LAYOUT (TMP117 SNOSD82D p.41). "
        "Pad 7 = exposed thermal pad.",
        items,
    )


PACKAGES.append(_wson6())


# ---------------------------------------------------------------------------
# (V/I) LSM6DSOX : LGA-14L, ST package outline DS12814 Rev.4 Fig.28.
#     Body 2.5 (X) x 3.0 (Y) x 0.86 mm.  14 lands 0.475 x 0.25 mm at 0.50 mm
#     pitch: 4-pad rows span 1.5 mm on the 3.0 mm edges, 3-pad rows span
#     1.0 mm on the 2.5 mm edges (both leaving 0.75 mm margins).
#     Land sizes are enlarged to 0.50 x 0.28 mm (IPC-7351B Nominal for LGA);
#     ST's TN0018 land pattern was not retrievable in this environment.
#     Package pad order (BOTTOM view, per Fig.4): pin 1 top-left, 1-4 down the
#     left edge, 5-7 along the bottom, 8-11 up the right edge, 12-14 along the
#     top.  A footprint is drawn in board (TOP) view, i.e. mirrored, so pin 1
#     sits top-RIGHT here.
# ---------------------------------------------------------------------------
def _lga14() -> Package:
    BODY_X, BODY_Y = 2.5, 3.0
    PITCH = 0.5
    # 1:1 with the package pad (0.475 x 0.25), very slightly reduced.
    # Enlarging it to 0.50 x 0.28 - the usual IPC habit for leaded
    # parts - squeezes the four corner pairs (1/14, 4/5, 8/... ) to
    # 0.11 mm, below the 0.15 mm rule.  An LGA has no leads to form a
    # fillet, so a 1:1 land is the right answer anyway.
    PAD_L, PAD_W = 0.45, 0.25
    col_x = BODY_X / 2.0 - PAD_L / 2.0                  # 1.00
    row_y = BODY_Y / 2.0 - PAD_L / 2.0                  # 1.25
    items: list = []
    # 1..4 : right column, top -> bottom (mirrored from the bottom view).
    for i in range(4):
        items.append(Smd(str(1 + i), +col_x, 0.75 - i * PITCH, PAD_L, PAD_W))
    # 5..7 : bottom row, right -> left.
    for i in range(3):
        items.append(Smd(str(5 + i), 0.5 - i * PITCH, -row_y, PAD_W, PAD_L))
    # 8..11 : left column, bottom -> top.
    for i in range(4):
        items.append(Smd(str(8 + i), -col_x, -0.75 + i * PITCH, PAD_L, PAD_W))
    # 12..14 : top row, left -> right.
    for i in range(3):
        items.append(Smd(str(12 + i), -0.5 + i * PITCH, +row_y, PAD_W, PAD_L))
    hx, hy = BODY_X / 2.0, BODY_Y / 2.0
    items += [
        Wire(hx + 0.12, hy + 0.12, hx - 0.3, hy + 0.12, 0.1, 21),
        Wire(hx + 0.12, hy + 0.12, hx + 0.12, hy - 0.3, 0.1, 21),
        Wire(-hx - 0.12, -hy - 0.12, -hx + 0.3, -hy - 0.12, 0.1, 21),
        Wire(-hx - 0.12, -hy - 0.12, -hx - 0.12, -hy + 0.3, 0.1, 21),
        Circle(hx + 0.45, hy - 0.1, 0.15, 0.15, 21),     # pin-1 dot (top-right)
        Rect(-hx, -hy, hx, hy, 51),
        Text(-hx, hy + 0.55, 0.8, 25, ">NAME"),
        Text(-hx, -hy - 1.35, 0.8, 27, ">VALUE"),
    ]
    return Package(
        "LGA-14L-2.5X3.0",
        "ST LGA-14L 2.5x3.0x0.86 mm. Body/pad geometry from LSM6DSOX DS12814 "
        "Rev.4 Fig.28 (14 pads 0.475x0.25 mm, 0.5 mm pitch, 1.5/1.0 mm row "
        "spans). Lands enlarged to 0.50x0.28 mm per IPC-7351B Nominal. "
        "Drawn in board top view (package bottom view mirrored).",
        items,
    )


PACKAGES.append(_lga14())


# ---------------------------------------------------------------------------
# (I) SOIC-8 narrow / SOP-8  -- AS5600 (D 4.90, E 6.00, E1 3.90, e 1.27,
#     verified from AS5600 DS000365 v1-06 outline drawing) and TP4056
#     ("Complete Linear Charger in SOP-8", NanJing Top Power datasheet).
#     IPC-7351B SOIC127P600X175-8N Nominal: land 1.55 x 0.60 mm, span 5.40 mm.
# ---------------------------------------------------------------------------
PACKAGES.append(
    gullwing_package(
        "SOIC-8-N",
        "SOIC-8 narrow (150 mil body). Body 4.90 x 3.90 mm, lead span 6.00 mm, "
        "1.27 mm pitch. Lands 1.55 x 0.60 mm at 5.40 mm span "
        "(IPC-7351B SOIC127P600X175-8N Nominal).",
        pins_per_side=4, pitch=1.27, span=5.40,
        pad_l=1.55, pad_w=0.60, body_l=4.90, body_w=3.90,
    )
)

# ---------------------------------------------------------------------------
# (I) SOP-16 narrow -- HX711 SOP-16L: body 9.90 x 3.90 mm, lead span 6.00 mm,
#     pitch 1.27 mm, lead width 0.39-0.48 mm, foot 1.20-1.60 mm
#     (verified from the HX711 English datasheet "Package Dimensions" page).
#     IPC-7351B SOIC127P600X175-16N Nominal land: 1.55 x 0.60 at 5.40 span.
# ---------------------------------------------------------------------------
PACKAGES.append(
    gullwing_package(
        "SOP-16-N",
        "SOP-16L narrow. Body 9.90 x 3.90 mm, lead span 6.00 mm, 1.27 mm "
        "pitch (HX711 datasheet Package Dimensions). Lands 1.55 x 0.60 mm at "
        "5.40 mm span (IPC-7351B SOIC127P600X175-16N Nominal).",
        pins_per_side=8, pitch=1.27, span=5.40,
        pad_l=1.55, pad_w=0.60, body_l=9.90, body_w=3.90,
    )
)

# ---------------------------------------------------------------------------
# (I) SOT-23-5 / SOT25 -- AP2112K-3.3TRG1.
#     JEDEC TO-178 / EIAJ SC-74A: 0.95 mm pitch, 2.60 mm lead span nominal.
#     IPC-7351B SOT95P280X145-5N Nominal: land 1.10 x 0.60 mm, span 2.60 mm.
# ---------------------------------------------------------------------------
PACKAGES.append(
    sot23_package(
        "SOT-23-5",
        "SOT-23-5 (Diodes 'SOT25', JEDEC TO-178). 0.95 mm pitch, lands "
        "1.10 x 0.60 mm at 2.60 mm row span (IPC-7351B SOT95P280X145-5N "
        "Nominal). Pin order per AP2112 datasheet: 1 VIN, 2 GND, 3 EN, "
        "4 NC, 5 VOUT.",
        pad_l=1.10, pad_w=0.60, span=2.60, pitch=0.95, pin_count=5,
    )
)

# ---------------------------------------------------------------------------
# (I) SOT-23-3 -- N-channel MOSFET (AO3400A and pin-compatible parts).
#     IPC-7351B SOT95P237X112-3N Nominal: land 1.00 x 0.60 mm, span 2.30 mm,
#     1.90 mm between pads 1 and 2.
# ---------------------------------------------------------------------------
PACKAGES.append(
    sot23_package(
        "SOT-23-3",
        "SOT-23-3. Lands 1.00 x 0.60 mm, 2.30 mm row span, 1.90 mm pad 1-2 "
        "spacing (IPC-7351B SOT95P237X112-3N Nominal). Standard N-MOSFET "
        "assignment: 1 = Gate, 2 = Source, 3 = Drain.",
        pad_l=1.00, pad_w=0.60, span=2.30, pitch=1.90, pin_count=3,
    )
)

# ---------------------------------------------------------------------------
# (I) Chip packages, IPC-7351B Nominal.
# ---------------------------------------------------------------------------
PACKAGES.append(
    chip_package("R0805", "0805 (2012 metric) chip resistor. IPC-7351B "
                          "RESC2012X65N Nominal: lands 1.15 x 1.40 mm, "
                          "0.75 mm inner gap.",
                 body_l=2.0, body_w=1.25, pad_l=1.15, pad_w=1.40, gap=0.75)
)
PACKAGES.append(
    chip_package("C0805", "0805 (2012 metric) chip capacitor. IPC-7351B "
                          "CAPC2012X135N Nominal: lands 1.15 x 1.40 mm, "
                          "0.75 mm inner gap.",
                 body_l=2.0, body_w=1.25, pad_l=1.15, pad_w=1.40, gap=0.75)
)
PACKAGES.append(
    chip_package("LED0805", "0805 chip LED, polarised. Pad 1 = cathode "
                            "(marked by the extra silkscreen bar).",
                 body_l=2.0, body_w=1.25, pad_l=1.15, pad_w=1.40, gap=0.75,
                 polarised=True)
)
PACKAGES.append(
    chip_package("SOD-123", "SOD-123 diode. Body 2.65 x 1.60 mm. Lands "
                            "1.20 x 1.10 mm at 1.30 mm inner gap "
                            "(IPC-7351B DIOM2616X110N Nominal). "
                            "Pad 1 = cathode (band).",
                 body_l=2.65, body_w=1.60, pad_l=1.20, pad_w=1.10, gap=1.30,
                 polarised=True)
)


# ---------------------------------------------------------------------------
# (V) JST PH 2.0 mm, top-entry through-hole header (S2B-PH-K-S / S4B-PH-K-S).
#     JST ePH catalogue, "PC board layout and Assembly layout (Through-hole
#     type)": pitch 2.00 +/-0.05, PCB hole diameter 0.7 +0.1/-0 mm,
#     connector outline offset (1.95) x (1.7).
#     Drill is set to 0.8 mm: still inside JST's +0.1 tolerance and it follows
#     JST Note 3 ("when using PCB made of hard fibreglass material, please
#     consider a larger hole diameter").
# ---------------------------------------------------------------------------
def _jst_ph(positions: int) -> Package:
    PITCH = 2.0
    DRILL = 0.8
    DIA = 1.5
    items: list = []
    x0 = -(positions - 1) * PITCH / 2.0
    for i in range(positions):
        items.append(
            Pad(str(i + 1), x0 + i * PITCH, 0.0, DRILL, DIA,
                "square" if i == 0 else "round")
        )
    # Connector body: 2.0*(n-1) + 3.9 wide, 4.5 deep (JST PH top-entry).
    w = (positions - 1) * PITCH + 3.9
    items += [
        Wire(-w / 2, -1.7, w / 2, -1.7, 0.12, 21),
        Wire(w / 2, -1.7, w / 2, 2.8, 0.12, 21),
        Wire(w / 2, 2.8, -w / 2, 2.8, 0.12, 21),
        Wire(-w / 2, 2.8, -w / 2, -1.7, 0.12, 21),
        Wire(-w / 2, -1.7, -w / 2 + 0.8, -1.7, 0.35, 21),   # pin-1 side bar
        Rect(-w / 2, -1.7, w / 2, 2.8, 51),
        Text(-w / 2, 3.1, 0.9, 25, ">NAME"),
        Text(-w / 2, -3.3, 0.9, 27, ">VALUE"),
    ]
    return Package(
        f"JST-PH-{positions}",
        f"JST PH series {positions}-circuit top-entry through-hole header "
        f"(S{positions}B-PH-K-S). 2.00 mm pitch, PCB hole 0.7 +0.1 mm per the "
        f"JST ePH PC-board-layout figure; drill specified 0.8 mm for FR-4. "
        f"Pad 1 is square.",
        items,
    )


PACKAGES.append(_jst_ph(2))
PACKAGES.append(_jst_ph(4))


# ---------------------------------------------------------------------------
# (S) 2.54 mm pin headers.
# ---------------------------------------------------------------------------
for _pos in (2, 3, 4, 5, 6, 8):
    PACKAGES.append(
        header_package(
            f"HDR-1X{_pos}",
            f"1x{_pos} 2.54 mm through-hole pin header. Drill 1.0 mm / pad "
            f"1.8 mm suits the 0.64 mm square posts used by all common "
            f"2.54 mm headers. Pad 1 is square.",
            positions=_pos,
        )
    )


# ---------------------------------------------------------------------------
# (S) 6 x 6 mm through-hole tactile switch, 4 leads on a 6.5 x 4.5 mm grid
#     (TL1105 / B3F-10xx family geometry).  Exact vendor part must be
#     confirmed -- see REQUIRES_CONFIRMATION.md.
#     Leads 1+2 are internally common, as are 3+4.
# ---------------------------------------------------------------------------
def _tact6() -> Package:
    GX, GY = 6.5 / 2.0, 4.5 / 2.0
    items = [
        Pad("1", -GX, +GY, 1.0, 1.6, "square"),
        Pad("2", -GX, -GY, 1.0, 1.6),
        Pad("3", +GX, +GY, 1.0, 1.6),
        Pad("4", +GX, -GY, 1.0, 1.6),
        Wire(-3.0, -3.0, 3.0, -3.0, 0.12, 21),
        Wire(3.0, -3.0, 3.0, 3.0, 0.12, 21),
        Wire(3.0, 3.0, -3.0, 3.0, 0.12, 21),
        Wire(-3.0, 3.0, -3.0, -3.0, 0.12, 21),
        Circle(0, 0, 1.75, 0.12, 21),
        Rect(-3.0, -3.0, 3.0, 3.0, 51),
        Text(-3.0, 3.4, 0.9, 25, ">NAME"),
        Text(-3.0, -4.6, 0.9, 27, ">VALUE"),
    ]
    return Package(
        "TACT-6X6-THT",
        "6.0 x 6.0 mm through-hole tactile switch, 4 leads on a 6.5 x 4.5 mm "
        "grid (TL1105 / B3F-10xx family). Leads 1-2 common, 3-4 common. "
        "Drill 1.0 mm. De-facto standard geometry -- confirm against the "
        "chosen vendor part before fabrication.",
        items,
    )


PACKAGES.append(_tact6())


# ---------------------------------------------------------------------------
# (S) Test point : 1.5 mm round SMD land, and M2 mounting hole.
# ---------------------------------------------------------------------------
PACKAGES.append(
    Package(
        "TESTPOINT-1.5",
        "1.5 mm round SMD test-point land (probe / flying-lead solder point).",
        [
            Smd("TP", 0, 0, 1.5, 1.5, roundness=100),
            Circle(0, 0, 1.1, 0.1, 21),
            Text(0, 1.5, 0.8, 25, ">NAME", align="bottom-center"),
        ],
    )
)
PACKAGES.append(
    Package(
        "MOUNT-M2",
        "M2 mounting hole. 2.2 mm drill for an M2 screw, 4.4 mm annular "
        "copper land (plated, tied to GND) and a 4.6 mm keepout ring.",
        [
            Pad("1", 0, 0, 2.2, 4.4),
            Circle(0, 0, 2.3, 0.15, 21),
            Circle(0, 0, 2.3, 0.05, 39),
            Circle(0, 0, 2.3, 0.05, 41),
            Circle(0, 0, 2.3, 0.05, 42),
        ],
    )
)


# ===========================================================================
# SYMBOLS
# ===========================================================================
SYMBOLS: list[Symbol] = []

# --- ESP32-S3-WROOM-1 -------------------------------------------------------
# Pin names and electrical types are exactly Table 3-1 of the module
# datasheet.  All GPIOs are I/O; EN is an input; GND / 3V3 are power.
# Pins are grouped: power at the top-left, strapping pins flagged, and the
# functional groups kept together so the schematic reads cleanly.
_ESP_LEFT = [
    ("GND@1", "pwr"), ("3V3", "pwr"), ("EN", "in"),
    ("IO0", "io"), ("IO1", "io"), ("IO2", "io"), ("IO3", "io"),
    ("IO4", "io"), ("IO5", "io"), ("IO6", "io"), ("IO7", "io"),
    ("IO8", "io"), ("IO9", "io"), ("IO10", "io"), ("IO11", "io"),
    ("IO12", "io"), ("IO13", "io"), ("IO14", "io"), ("IO15", "io"),
    ("IO16", "io"), ("IO17", "io"),
]
_ESP_RIGHT = [
    ("GND@40", "pwr"), ("EPAD", "pwr"),
    ("IO18", "io"), ("IO19", "io"), ("IO20", "io"), ("IO21", "io"),
    ("IO35", "io"), ("IO36", "io"), ("IO37", "io"), ("IO38", "io"),
    ("IO39", "io"), ("IO40", "io"), ("IO41", "io"), ("IO42", "io"),
    ("TXD0", "io"), ("RXD0", "io"),
    ("IO45", "io"), ("IO46", "io"), ("IO47", "io"), ("IO48", "io"),
]
SYMBOLS.append(
    make_ic_symbol(
        "ESP32-S3-WROOM-1", "Espressif ESP32-S3-WROOM-1 Wi-Fi/BLE module",
        width=33.02, left=_ESP_LEFT, right=_ESP_RIGHT,
        extra=[
            Text(-14.0, -30.0, 1.2, 97, "STRAPPING: IO0 IO3 IO45 IO46"),
            Text(-14.0, -32.0, 1.2, 97, "ADC1 = IO1..IO10 (Wi-Fi safe)"),
            Text(-14.0, -34.0, 1.2, 97, "ADC2 = IO11..IO20 (UNUSABLE with Wi-Fi)"),
            Text(-14.0, -36.0, 1.2, 97, "IO35/36/37: N8R2 only (octal-PSRAM parts reserve them)"),
        ],
    )
)

# --- AD8232 -----------------------------------------------------------------
SYMBOLS.append(
    make_ic_symbol(
        "AD8232", "ADI AD8232 single-lead heart-rate monitor analog front end",
        width=30.48,
        left=[
            ("+VS", "pwr"), ("GND", "pwr"),
            ("+IN", "in"), ("-IN", "in"),
            ("RLDFB", "in"), ("RLD", "out"),
            ("REFIN", "in"), ("REFOUT", "out"),
            ("SDN", "in"), ("AC/DC", "in"), ("FR", "in"),
        ],
        right=[
            ("IAOUT", "out"), ("HPSENSE", "in"), ("HPDRIVE", "out"),
            ("SW", "pas"),
            ("OPAMP+", "in"), ("OPAMP-", "in"), ("OUT", "out"),
            ("LOD+", "out"), ("LOD-", "out"),
            ("EP", "pwr"),
        ],
        extra=[Text(-14.0, -17.0, 1.2, 97, "Vs = 2.0 .. 3.5 V ONLY")],
    )
)

# --- TMP117 -----------------------------------------------------------------
SYMBOLS.append(
    make_ic_symbol(
        "TMP117", "TI TMP117 high-accuracy digital temperature sensor",
        width=22.86,
        left=[("V+", "pwr"), ("GND", "pwr"), ("ADD0", "in")],
        right=[("SDA", "io"), ("SCL", "in"), ("ALERT", "oc"), ("TPAD", "pwr")],
    )
)

# --- LSM6DSOX ---------------------------------------------------------------
SYMBOLS.append(
    make_ic_symbol(
        "LSM6DSOX", "ST LSM6DSOX 6-axis IMU (accelerometer + gyroscope)",
        width=25.4,
        left=[
            ("VDD", "pwr"), ("VDDIO", "pwr"),
            ("GND@6", "pwr"), ("GND@7", "pwr"),
            ("CS", "in"), ("SDO/SA0", "io"),
        ],
        right=[
            ("SDA", "io"), ("SCL", "in"),
            ("INT1", "out"), ("INT2", "out"),
            ("SDx", "io"), ("SCx", "io"),
            ("OCS_AUX", "in"), ("SDO_AUX", "out"),
        ],
        extra=[Text(-11.0, -15.0, 1.2, 97, "Mode 1: I2C (CS=1, SDx/SCx tied)")],
    )
)

# --- AS5600 -----------------------------------------------------------------
SYMBOLS.append(
    make_ic_symbol(
        "AS5600", "ams-OSRAM AS5600 12-bit magnetic rotary position sensor",
        width=25.4,
        left=[("VDD5V", "pwr"), ("VDD3V3", "pwr"), ("GND", "pwr"), ("DIR", "in")],
        right=[("SDA", "io"), ("SCL", "in"), ("OUT", "out"), ("PGO", "in")],
        extra=[Text(-11.0, -9.5, 1.2, 97, "I2C address 0x36 (FIXED)")],
    )
)

# --- TP4056 -----------------------------------------------------------------
SYMBOLS.append(
    make_ic_symbol(
        "TP4056", "NanJing Top Power TP4056 1A Li-ion linear charger",
        width=25.4,
        left=[("VCC", "pwr"), ("GND", "pwr"), ("CE", "in"), ("TEMP", "in")],
        right=[("BAT", "out"), ("PROG", "pas"), ("CHRG", "oc"), ("STDBY", "oc")],
    )
)

# --- AP2112K ----------------------------------------------------------------
SYMBOLS.append(
    make_ic_symbol(
        "AP2112K", "Diodes AP2112K-3.3 600 mA CMOS LDO regulator with enable",
        width=22.86,
        left=[("VIN", "pwr"), ("GND", "pwr"), ("EN", "in")],
        right=[("VOUT", "pwr"), ("NC", "nc")],
    )
)

# --- HX711 ------------------------------------------------------------------
SYMBOLS.append(
    make_ic_symbol(
        "HX711", "Avia Semiconductor HX711 24-bit bridge/load-cell ADC",
        width=27.94,
        left=[
            ("VSUP", "pwr"), ("AVDD", "pwr"), ("DVDD", "pwr"), ("AGND", "pwr"),
            ("BASE", "out"), ("VFB", "in"), ("VBG", "out"),
        ],
        right=[
            ("INA+", "in"), ("INA-", "in"), ("INB+", "in"), ("INB-", "in"),
            ("PD_SCK", "in"), ("DOUT", "out"), ("XI", "in"), ("XO", "io"),
            ("RATE", "in"),
        ],
    )
)

# --- Discretes and connectors ----------------------------------------------
SYMBOLS.append(
    Symbol("R", "Resistor", [
        Wire(-2.54, 0, -1.905, 0, 0.1524, 94),
        Rect(-1.905, -0.762, 1.905, 0.762, 94),
        Wire(1.905, 0, 2.54, 0, 0.1524, 94),
        Text(-2.54, 1.4, 1.778, 95, ">NAME"),
        Text(-2.54, -3.0, 1.778, 96, ">VALUE"),
        Pin("1", -5.08, 0, length="short", direction="pas"),
        Pin("2", 5.08, 0, length="short", direction="pas", rot="R180"),
    ])
)
SYMBOLS.append(
    Symbol("C", "Capacitor (non-polarised)", [
        Wire(-1.27, 0.508, 1.27, 0.508, 0.254, 94),
        Wire(-1.27, -0.508, 1.27, -0.508, 0.254, 94),
        Wire(0, 0.508, 0, 2.54, 0.1524, 94),
        Wire(0, -0.508, 0, -2.54, 0.1524, 94),
        Text(1.9, 0.9, 1.778, 95, ">NAME"),
        Text(1.9, -2.6, 1.778, 96, ">VALUE"),
        Pin("1", 0, 5.08, length="short", direction="pas", rot="R270"),
        Pin("2", 0, -5.08, length="short", direction="pas", rot="R90"),
    ])
)
SYMBOLS.append(
    Symbol("LED", "Light-emitting diode", [
        Wire(-1.27, 1.27, -1.27, -1.27, 0.254, 94),
        Wire(-1.27, 0, 1.27, 1.27, 0.254, 94),
        Wire(1.27, 1.27, 1.27, -1.27, 0.254, 94),
        Wire(1.27, -1.27, -1.27, 0, 0.254, 94),
        Wire(1.9, 1.6, 3.2, 2.9, 0.1524, 94),
        Wire(2.4, 1.1, 3.7, 2.4, 0.1524, 94),
        Text(-2.54, -4.2, 1.778, 95, ">NAME"),
        Text(4.0, -4.2, 1.778, 96, ">VALUE"),
        Text(-1.2, 2.0, 0.9, 97, "K"),
        Text(0.9, 2.0, 0.9, 97, "A"),
        Pin("C", -3.81, 0, length="short", direction="pas"),
        Pin("A", 3.81, 0, length="short", direction="pas", rot="R180"),
    ])
)
SYMBOLS.append(
    Symbol("DIODE", "Diode (Schottky / rectifier)", [
        Wire(-1.27, 1.27, -1.27, -1.27, 0.254, 94),
        Wire(-1.27, 0, 1.27, 1.27, 0.254, 94),
        Wire(1.27, 1.27, 1.27, -1.27, 0.254, 94),
        Wire(1.27, -1.27, -1.27, 0, 0.254, 94),
        Text(-2.54, 2.0, 1.778, 95, ">NAME"),
        Text(-2.54, -4.0, 1.778, 96, ">VALUE"),
        Text(-1.2, -2.4, 0.9, 97, "K"),
        Text(0.9, -2.4, 0.9, 97, "A"),
        Pin("C", -3.81, 0, length="short", direction="pas"),
        Pin("A", 3.81, 0, length="short", direction="pas", rot="R180"),
    ])
)
SYMBOLS.append(
    Symbol("NMOS", "N-channel enhancement MOSFET", [
        Wire(-2.54, 0, -1.27, 0, 0.1524, 94),
        Wire(-1.27, 2.032, -1.27, -2.032, 0.254, 94),        # gate plate
        Wire(-0.508, 2.032, -0.508, 1.016, 0.254, 94),       # channel
        Wire(-0.508, 0.508, -0.508, -0.508, 0.254, 94),
        Wire(-0.508, -1.016, -0.508, -2.032, 0.254, 94),
        Wire(-0.508, 1.524, 2.54, 1.524, 0.1524, 94),        # drain
        Wire(2.54, 1.524, 2.54, 3.81, 0.1524, 94),
        Wire(-0.508, -1.524, 2.54, -1.524, 0.1524, 94),      # source
        Wire(2.54, -1.524, 2.54, -3.81, 0.1524, 94),
        Wire(-0.508, 0, 2.54, 0, 0.1524, 94),                # body
        Wire(2.54, 0, 2.54, -1.524, 0.1524, 94),
        Wire(1.27, 0.508, 2.032, 0, 0.254, 94),              # body diode
        Wire(2.032, 0, 1.27, -0.508, 0.254, 94),
        Text(4.5, 1.8, 1.778, 95, ">NAME"),
        Text(4.5, -0.6, 1.778, 96, ">VALUE"),
        Pin("G", -5.08, 0, length="short", direction="in"),
        Pin("D", 2.54, 6.35, length="short", direction="pas", rot="R270"),
        Pin("S", 2.54, -6.35, length="short", direction="pas", rot="R90"),
    ])
)
SYMBOLS.append(
    Symbol("SWITCH-SPST", "SPST momentary push-button (both lead pairs bonded)", [
        Wire(-2.54, 0, -1.27, 0, 0.1524, 94),
        Wire(-1.27, 0.508, 1.524, 1.778, 0.1524, 94),
        Wire(1.27, 0, 2.54, 0, 0.1524, 94),
        Circle(-1.27, 0, 0.3, 0.1524, 94),
        Circle(1.27, 0, 0.3, 0.1524, 94),
        Wire(0, 1.9, 0, 3.0, 0.1524, 94),
        Wire(-1.0, 3.0, 1.0, 3.0, 0.4, 94),
        Text(-2.54, 4.0, 1.778, 95, ">NAME"),
        Text(-2.54, -3.0, 1.778, 96, ">VALUE"),
        Pin("P", -5.08, 0, length="short", direction="pas"),
        Pin("N", 5.08, 0, length="short", direction="pas", rot="R180"),
    ])
)
SYMBOLS.append(
    Symbol("TESTPOINT", "Test point", [
        Circle(0, 1.27, 0.5, 0.254, 94),
        Wire(0, 0, 0, 0.77, 0.1524, 94),
        Text(1.4, 0.5, 1.524, 95, ">NAME"),
        Pin("TP", 0, -2.54, length="short", direction="pas", rot="R90"),
    ])
)
SYMBOLS.append(
    Symbol("MOUNTHOLE", "Mounting hole (plated, GND-stitched)", [
        Circle(0, 0, 1.27, 0.254, 94),
        Circle(0, 0, 0.6, 0.254, 94),
        Text(2.0, 0.6, 1.524, 95, ">NAME"),
        Pin("1", -3.81, 0, length="short", direction="pas"),
    ])
)


def _connector_symbol(name: str, description: str,
                      pins: list[tuple[str, str]]) -> Symbol:
    """Single-column connector symbol; pin 1 at the top."""
    rows = len(pins)
    height = (rows - 1) * 2.54 + 5.08
    hw, hh = 6.35, height / 2.0
    y0 = (rows - 1) * 2.54 / 2.0
    items: list = [
        Wire(-hw, -hh, hw, -hh, 0.254, 94),
        Wire(hw, -hh, hw, hh, 0.254, 94),
        Wire(hw, hh, -hw, hh, 0.254, 94),
        Wire(-hw, hh, -hw, -hh, 0.254, 94),
        Text(-hw, hh + 0.8, 1.778, 95, ">NAME"),
        Text(-hw, -hh - 2.4, 1.778, 96, ">VALUE"),
        Wire(hw - 1.0, hh - 0.6, hw, hh - 1.6, 0.254, 94),   # pin-1 corner mark
    ]
    for i, (pn, d) in enumerate(pins):
        p, t = _pin("L", pn, hw, hh, y0 - i * 2.54, d)
        items.append(p)
        items.append(t)
    return Symbol(name, description, items)


CONNECTOR_SYMBOLS = {
    "CONN-2": [("1", "pas"), ("2", "pas")],
    "CONN-3": [("1", "pas"), ("2", "pas"), ("3", "pas")],
    "CONN-4": [("1", "pas"), ("2", "pas"), ("3", "pas"), ("4", "pas")],
    "CONN-5": [(str(i), "pas") for i in range(1, 6)],
    "CONN-6": [(str(i), "pas") for i in range(1, 7)],
    "CONN-8": [(str(i), "pas") for i in range(1, 9)],
}
for _nm, _pl in CONNECTOR_SYMBOLS.items():
    SYMBOLS.append(
        _connector_symbol(_nm, f"{len(_pl)}-way connector / header", _pl)
    )

# --- Supply (rail) symbols --------------------------------------------------
# EAGLE names a net from the supply pin, so the pin name IS the net name.
def _supply_symbol(net: str, style: str = "arrow") -> Symbol:
    if style == "gnd":
        items = [
            Wire(-1.905, 0, 1.905, 0, 0.254, 94),
            Wire(-1.27, -0.635, 1.27, -0.635, 0.254, 94),
            Wire(-0.635, -1.27, 0.635, -1.27, 0.254, 94),
            Text(-2.54, -3.4, 1.778, 96, ">VALUE"),
            Pin(net, 0, 2.54, length="short", direction="sup", rot="R270",
                visible="off"),
        ]
    else:
        items = [
            Wire(-1.27, 1.27, 0, 2.54, 0.254, 94),
            Wire(0, 2.54, 1.27, 1.27, 0.254, 94),
            Wire(-1.27, 1.27, 1.27, 1.27, 0.254, 94),
            Text(-2.54, 3.0, 1.778, 96, ">VALUE"),
            Pin(net, 0, 0, length="short", direction="sup", rot="R90",
                visible="off"),
        ]
    return Symbol(f"SUPPLY-{net}", f"{net} supply rail marker", items)


SUPPLY_NETS = [("GND", "gnd"), ("AGND", "gnd"), ("3V3", "arrow"),
               ("VBAT", "arrow"), ("VBUS", "arrow"), ("VCHG", "arrow")]
for _net, _sty in SUPPLY_NETS:
    SYMBOLS.append(_supply_symbol(_net, _sty))


# ===========================================================================
# DEVICE SETS  (symbol pin  ->  package pad)
# ===========================================================================
DEVICESETS: list[DeviceSet] = []

# ESP32-S3-WROOM-1.  Mapping is Table 3-1 of the module datasheet, verbatim.
_ESP_MAP = {
    "GND@1": "1", "3V3": "2", "EN": "3",
    "IO4": "4", "IO5": "5", "IO6": "6", "IO7": "7",
    "IO15": "8", "IO16": "9", "IO17": "10", "IO18": "11",
    "IO8": "12", "IO19": "13", "IO20": "14",
    "IO3": "15", "IO46": "16", "IO9": "17", "IO10": "18",
    "IO11": "19", "IO12": "20", "IO13": "21", "IO14": "22",
    "IO21": "23", "IO47": "24", "IO48": "25", "IO45": "26",
    "IO0": "27", "IO35": "28", "IO36": "29", "IO37": "30",
    "IO38": "31", "IO39": "32", "IO40": "33", "IO41": "34",
    "IO42": "35", "RXD0": "36", "TXD0": "37", "IO2": "38", "IO1": "39",
    "GND@40": "40", "EPAD": "41",
}
DEVICESETS.append(
    DeviceSet(
        "ESP32-S3-WROOM-1", "U",
        "Espressif ESP32-S3-WROOM-1-N8R2. Xtensa LX7 dual-core, Wi-Fi b/g/n + "
        "Bluetooth LE 5, 8 MB flash, 2 MB quad-SPI PSRAM, PCB antenna. "
        "Pin map from datasheet v1.8 Table 3-1. IO35/36/37 are free on the "
        "-N8R2 (quad PSRAM) variant only.",
        "ESP32-S3-WROOM-1", "ESP32-S3-WROOM-1", _ESP_MAP, uservalue=False,
    )
)

DEVICESETS.append(
    DeviceSet(
        "AD8232", "U",
        "Analog Devices AD8232ACPZ-R7 single-lead heart-rate monitor front "
        "end. Supply 2.0-3.5 V. Pin map from AD8232 Rev.A Table 3.",
        "AD8232", "LFCSP-20-4X4-P050",
        {
            "HPDRIVE": "1", "+IN": "2", "-IN": "3", "RLDFB": "4", "RLD": "5",
            "SW": "6", "OPAMP+": "7", "REFOUT": "8", "OPAMP-": "9", "OUT": "10",
            "LOD-": "11", "LOD+": "12", "SDN": "13", "AC/DC": "14", "FR": "15",
            "GND": "16", "+VS": "17", "REFIN": "18", "IAOUT": "19",
            "HPSENSE": "20", "EP": "EP",
        },
        uservalue=False,
    )
)

DEVICESETS.append(
    DeviceSet(
        "TMP117", "U",
        "TI TMP117AIDRVR high-accuracy digital temperature sensor, WSON-6 "
        "(DRV). +/-0.1 C, 1.8-5.5 V, I2C. Pin map from TMP117 SNOSD82D "
        "Table 5-1 (WSON column).",
        "TMP117", "WSON-6-DRV0006B",
        {"SCL": "1", "GND": "2", "ALERT": "3", "ADD0": "4", "V+": "5",
         "SDA": "6", "TPAD": "7"},
        uservalue=False,
    )
)

DEVICESETS.append(
    DeviceSet(
        "LSM6DSOX", "U",
        "ST LSM6DSOXTR 6-axis IMU (3-axis accel + 3-axis gyro), LGA-14L. "
        "Pin map from LSM6DSOX DS12814 Rev.4 Table 1.",
        "LSM6DSOX", "LGA-14L-2.5X3.0",
        {"SDO/SA0": "1", "SDx": "2", "SCx": "3", "INT1": "4", "VDDIO": "5",
         "GND@6": "6", "GND@7": "7", "VDD": "8", "INT2": "9", "OCS_AUX": "10",
         "SDO_AUX": "11", "CS": "12", "SCL": "13", "SDA": "14"},
        uservalue=False,
    )
)

DEVICESETS.append(
    DeviceSet(
        "AS5600", "U",
        "ams-OSRAM AS5600-ASOM 12-bit contactless magnetic rotary position "
        "sensor, SOIC-8. Fixed I2C address 0x36. Pin map from AS5600 "
        "DS000365 v1-06 Figure 4.",
        "AS5600", "SOIC-8-N",
        {"VDD5V": "1", "VDD3V3": "2", "OUT": "3", "GND": "4", "PGO": "5",
         "SDA": "6", "SCL": "7", "DIR": "8"},
        uservalue=False,
    )
)

DEVICESETS.append(
    DeviceSet(
        "TP4056", "U",
        "NanJing Top Power TP4056-42-SOP8-PP 1 A standalone linear Li-ion "
        "charger, 4.2 V float. Pin map from the TP4056 datasheet pin "
        "description (page 2).",
        "TP4056", "SOIC-8-N",
        {"TEMP": "1", "PROG": "2", "GND": "3", "VCC": "4", "BAT": "5",
         "STDBY": "6", "CHRG": "7", "CE": "8"},
        uservalue=False,
    )
)

DEVICESETS.append(
    DeviceSet(
        "AP2112K-3.3", "U",
        "Diodes AP2112K-3.3TRG1 600 mA CMOS LDO, fixed 3.3 V, with enable. "
        "Pin map from AP2112 DS39724 Rev.2-2 pin descriptions (SOT25 column).",
        "AP2112K", "SOT-23-5",
        {"VOUT": "5", "GND": "2", "EN": "3", "NC": "4", "VIN": "1"},
        uservalue=False,
    )
)

DEVICESETS.append(
    DeviceSet(
        "HX711", "U",
        "Avia Semiconductor HX711 24-bit ADC for bridge sensors, SOP-16L. "
        "Pin map from the HX711 English datasheet Table 1.",
        "HX711", "SOP-16-N",
        {"VSUP": "1", "BASE": "2", "AVDD": "3", "VFB": "4", "AGND": "5",
         "VBG": "6", "INA-": "7", "INA+": "8", "INB-": "9", "INB+": "10",
         "PD_SCK": "11", "DOUT": "12", "XO": "13", "XI": "14", "RATE": "15",
         "DVDD": "16"},
        uservalue=False,
    )
)

DEVICESETS.append(
    DeviceSet("R-0805", "R", "Chip resistor, 0805 (2012 metric)", "R", "R0805",
              {"1": "1", "2": "2"})
)
DEVICESETS.append(
    DeviceSet("C-0805", "C", "Chip capacitor, 0805 (2012 metric)", "C", "C0805",
              {"1": "1", "2": "2"})
)
DEVICESETS.append(
    DeviceSet("LED-0805", "D", "Chip LED, 0805. Pad 1 = cathode.",
              "LED", "LED0805", {"C": "1", "A": "2"})
)
DEVICESETS.append(
    DeviceSet("DIODE-SOD123", "D",
              "Schottky/rectifier diode, SOD-123. Pad 1 = cathode (band).",
              "DIODE", "SOD-123", {"C": "1", "A": "2"})
)
DEVICESETS.append(
    DeviceSet("NMOS-SOT23", "Q",
              "N-channel logic-level MOSFET, SOT-23-3. "
              "Standard assignment 1 = Gate, 2 = Source, 3 = Drain.",
              "NMOS", "SOT-23-3", {"G": "1", "S": "2", "D": "3"})
)
DEVICESETS.append(
    DeviceSet("SW-TACT-6MM", "SW",
              "6 x 6 mm through-hole tactile push-button. Leads 1-2 and 3-4 "
              "are internally common, so each symbol pin maps to two pads "
              "(EAGLE multi-pad connect).",
              "SWITCH-SPST", "TACT-6X6-THT", {"P": "1 2", "N": "3 4"})
)
DEVICESETS.append(
    DeviceSet("TESTPOINT", "TP", "1.5 mm SMD test point", "TESTPOINT",
              "TESTPOINT-1.5", {"TP": "TP"}, uservalue=False)
)
DEVICESETS.append(
    DeviceSet("MOUNTHOLE-M2", "H", "M2 plated mounting hole, GND-stitched",
              "MOUNTHOLE", "MOUNT-M2", {"1": "1"}, uservalue=False)
)

# Connectors: JST-PH for the battery, 2.54 mm headers everywhere else.
DEVICESETS.append(
    DeviceSet("JST-PH-2", "J",
              "JST PH 2.00 mm 2-circuit top-entry header (S2B-PH-K-S). "
              "Li-Po battery input.",
              "CONN-2", "JST-PH-2", {"1": "1", "2": "2"})
)
DEVICESETS.append(
    DeviceSet("JST-PH-4", "J",
              "JST PH 2.00 mm 4-circuit top-entry header (S4B-PH-K-S). "
              "Load-cell bridge input.",
              "CONN-4", "JST-PH-4", {"1": "1", "2": "2", "3": "3", "4": "4"})
)
for _pos in (2, 3, 4, 5, 6, 8):
    DEVICESETS.append(
        DeviceSet(
            f"HDR-1X{_pos}", "J",
            f"1x{_pos} 2.54 mm pin header",
            f"CONN-{_pos}", f"HDR-1X{_pos}",
            {str(i): str(i) for i in range(1, _pos + 1)},
        )
    )

for _net, _sty in SUPPLY_NETS:
    DEVICESETS.append(
        DeviceSet(f"SUPPLY-{_net}", "SUPPLY", f"{_net} rail symbol",
                  f"SUPPLY-{_net}", None, {}, uservalue=False)
    )

# ---------------------------------------------------------------------------
# Thermal / exposed-pad vias.
#
# EAGLE cannot hold plated vias inside a package definition (<hole> is an
# UNPLATED mechanical hole, which through a thermal land would be a real
# manufacturing defect).  The board generator therefore emits these as proper
# plated vias belonging to the GND signal, positioned relative to the
# element's origin.
#
#   deviceset -> (via drill mm, via diameter mm, [(dx, dy), ...])
# ---------------------------------------------------------------------------
THERMAL_VIAS: dict[str, tuple[float, float, list[tuple[float, float]]]] = {
    # ESP32-S3-WROOM-1 EPAD, centred at (-1.25, -2.5) in the footprint.
    "ESP32-S3-WROOM-1": (0.3, 0.6, [
        (-1.25 + dx, -2.5 + dy)
        for dx in (-1.1, 0.0, 1.1) for dy in (-1.1, 0.0, 1.1)
    ]),
    # AD8232 exposed pad, 2.50 mm SQ centred on the package origin.
    "AD8232": (0.3, 0.6, [(-0.7, -0.7), (0.7, -0.7), (-0.7, 0.7), (0.7, 0.7)]),
    # TMP117 thermal pad, 1.0 x 1.6 mm centred on the package origin.
    "TMP117": (0.3, 0.55, [(0.0, 0.45), (0.0, -0.45)]),
}

# ---------------------------------------------------------------------------
# Component heights above the board, for the mechanical envelope render and
# the enclosure check.  These footprints carry NO 3D (STEP) geometry, so this
# is a height table, not a solid model - it is enough to size an enclosure and
# to spot a connector that will foul a lid, and no more.
#
#   package -> (height mm, source)
#
# "datasheet" heights are read from the package drawing cited in
# COMPONENT_VERIFICATION.md.  "typical" heights are the usual value for that
# package family and MUST be confirmed against the part actually bought -
# through-hole connector housings in particular vary a lot between vendors.
# ---------------------------------------------------------------------------
PACKAGE_HEIGHT: dict[str, tuple[float, str]] = {
    "ESP32-S3-WROOM-1":   (3.10, "datasheet (v1.8 Fig. 10-1, 3.1 +/-0.15)"),
    "LFCSP-20-4X4-P050":  (0.80, "datasheet (AD8232 Rev.A, 0.80 max)"),
    "WSON-6-DRV0006B":    (0.80, "datasheet (TI DRV0006B, 0.8 max)"),
    "LGA-14L-2.5X3.0":    (0.86, "datasheet (ST DS12814 Fig.28, 0.86 max)"),
    "SOIC-8-N":           (1.75, "typical (JEDEC SOIC narrow, 1.75 max)"),
    "SOP-16-N":           (1.75, "typical (JEDEC SOIC narrow, 1.75 max)"),
    "SOT-23-5":           (1.45, "typical (JEDEC TO-178, 1.45 max)"),
    "SOT-23-3":           (1.12, "typical (SOT-23, 1.12 max)"),
    "R0805":              (0.60, "typical (0805 chip resistor)"),
    "C0805":              (0.90, "typical (0805 MLCC; a 22 uF part can reach 1.4)"),
    "LED0805":            (0.80, "typical (0805 chip LED)"),
    "SOD-123":            (1.10, "typical (SOD-123)"),
    "JST-PH-2":           (6.00, "typical (JST PH top-entry housing)"),
    "JST-PH-4":           (6.00, "typical (JST PH top-entry housing)"),
    "TACT-6X6-THT":       (5.00, "typical (6 mm tactile incl. plunger)"),
    "TESTPOINT-1.5":      (0.00, "bare land"),
    "MOUNT-M2":           (0.00, "mechanical"),
}
# 2.54 mm headers: pin field is 11.6 mm overall but the plastic body is 2.5 mm;
# what matters for a lid is the mated height with a crimp housing on top.
for _pos in (2, 3, 4, 5, 6, 8):
    PACKAGE_HEIGHT[f"HDR-1X{_pos}"] = (
        8.50, "typical (2.54 mm header, mated with a crimp housing)")

LIBRARY_NAME = "SIH26113_Maternity_Assist_Belt"
LIBRARY_DESCRIPTION = (
    "&lt;b&gt;SIH26113 - Maternity Assist Belt&lt;/b&gt;&lt;p&gt;"
    "Prototype carrier-board library. Every footprint is derived from the "
    "manufacturer's package-outline or recommended land-pattern drawing, or "
    "from IPC-7351B Nominal density for generic package families. "
    "Pin electrical types are set for real ERC use - nothing is blanket-"
    "marked passive.&lt;p&gt;"
    "NOT A MEDICAL DEVICE. See documentation/REQUIRES_CONFIRMATION.md."
)
