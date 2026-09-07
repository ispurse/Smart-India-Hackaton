"""
design.py - The SIH26113 Maternity Assist Belt carrier board, as data.

This module is the single source of truth for:
  * the part list (reference, deviceset, value, both schematic and board
    placement),
  * the netlist,
  * net classes / trace widths,
  * the board outline and placement zones,
  * the GPIO allocation table.

generate_schematic.py, generate_board.py, validate.py and the documentation
generators all read from here, so the .sch, the .brd, the netlist document,
the BOM and the GPIO table can never drift apart.

Coordinates: schematic in mm on a 1.27 mm grid; board in mm with the origin
at the bottom-left corner of the outline.
"""

from __future__ import annotations

from dataclasses import dataclass, field

# ===========================================================================
# BOARD GEOMETRY
# ===========================================================================
BOARD_W = 100.0
BOARD_H = 70.0
BOARD_LAYERS = 4
BOARD_THICKNESS = 1.6           # mm, FR-4
COPPER_OZ = 1                   # 35 um finished outer copper

# 4-layer stack-up.  The move from two layers to four is a deliberate
# departure from the "simple carrier board" reading of the architecture
# diagram; DESIGN_ASSUMPTIONS.md records why.  In short: an AD8232 front end
# amplifying a sub-millivolt biopotential by 1100, a Wi-Fi module and a
# motor driver cannot share two layers and still give the analog section an
# uninterrupted return path.
#   L1  (EAGLE layer 1)   signal, components
#   L2  (EAGLE layer 2)   solid GND plane  <- reference for every L1 track
#   L3  (EAGLE layer 15)  solid 3V3 plane
#   L4  (EAGLE layer 16)  signal
STACKUP = [
    (1, "Top", "signal + components", "35 um"),
    (2, "Route2", "GND plane (solid)", "35 um"),
    (15, "Route15", "3V3 plane (solid)", "35 um"),
    (16, "Bottom", "signal", "35 um"),
]
SIGNAL_LAYERS = (1, 16)
PLANE_LAYERS = {2: "GND", 15: "3V3"}
PLANE_LAYERS_INV = {v: k for k, v in PLANE_LAYERS.items()}

# Plane outline: the whole board minus the antenna block in the top-left
# corner.  Espressif requires all copper - planes included - to be absent
# beneath the module antenna, and an EAGLE polygon cannot carry a hole, so
# the plane is drawn as an L instead.
PLANE_OUTLINE = [
    (0.5, 0.5), (BOARD_W - 0.5, 0.5), (BOARD_W - 0.5, BOARD_H - 0.5),
    (29.5, BOARD_H - 0.5), (29.5, 63.0), (0.5, 63.0),
]

# Espressif requires the module antenna to sit at a board edge with all
# copper (including planes) removed beneath it.  The module is placed so its
# 6 mm antenna area is flush with the top board edge.
ANTENNA_KEEPOUT = (9.0, 63.4, 29.0, 70.0)      # x1, y1, x2, y2

# Zones are advisory boundaries drawn on the Document layer; the numbered
# scheme follows the architecture diagram's blocks.  ECG is deliberately in
# the far corner from the motor driver and the module antenna.
ZONES = [
    ("Z1  POWER ENTRY / CHARGING / 3V3", 4.0, 4.0, 32.0, 36.0),
    ("Z2  ESP32-S3 CORE", 1.0, 40.0, 34.0, 70.0),
    ("Z5  MECHANICAL SENSING", 34.5, 4.0, 63.0, 30.0),
    ("Z4  I2C SENSORS", 34.5, 31.0, 63.0, 49.0),
    ("Z7  USER INPUT / STORAGE", 34.5, 50.0, 63.0, 68.0),
    ("Z3  ECG ANALOG FRONT END", 66.0, 4.0, 98.0, 40.0),
    ("Z6  FET-DRIVEN ALERTS", 66.0, 50.0, 98.0, 68.0),
]

# The top-left corner sits inside the antenna keep-out, so that hole is
# moved to the left-middle edge instead.
MOUNT_HOLES = [(3.0, 3.0), (97.0, 3.0), (2.6, 42.0), (97.0, 67.0)]

# ===========================================================================
# NET CLASSES  (name, trace width mm, min drill mm, min clearance mm)
# ===========================================================================
NET_CLASSES = [
    (0, "default", 0.20, 0.3, 0.15),
    (1, "power", 0.50, 0.4, 0.20),
    (2, "motor", 0.50, 0.4, 0.20),
    (3, "analog_ecg", 0.20, 0.3, 0.20),
]

POWER_NETS = {"GND", "3V3", "VBAT", "VBUS"}
MOTOR_NETS = {"MOTOR_P", "MOTOR_N"}
ECG_NETS = {
    "ECG_LA", "ECG_RA", "ECG_RL", "ECG_LA_F", "ECG_RA_F", "ECG_RLD",
    "ECG_REFIN", "ECG_REFOUT", "ECG_HPSENSE", "ECG_IAOUT", "ECG_SW",
    "ECG_OPP", "ECG_OPM", "ECG_OUT_RAW", "ECG_OUT",
}


def net_class(name: str) -> int:
    if name in POWER_NETS:
        return 1
    if name in MOTOR_NETS:
        return 2
    if name in ECG_NETS:
        return 3
    return 0


# ===========================================================================
# PART LIST
# ===========================================================================
@dataclass
class Part:
    ref: str
    deviceset: str
    value: str
    desc: str
    sheet: int
    sx: float                    # schematic x (mm)
    sy: float
    srot: str = "R0"
    bx: float = 0.0              # board x (mm)
    by: float = 0.0
    brot: str = "R0"
    mpn: str = ""
    manufacturer: str = ""
    package_note: str = ""


PARTS: list[Part] = []


def P(*a, **kw) -> Part:
    p = Part(*a, **kw)
    PARTS.append(p)
    return p


# ---------------------------------------------------------------------------
# SHEET 1 - POWER ENTRY, CHARGING, REGULATION
# ---------------------------------------------------------------------------
P("J1", "JST-PH-2", "LI-PO 3.7V", "Li-Po cell input (protected pack required)",
  1, 25, 175, "R0", 5.0, 26.5, "R90",
  mpn="S2B-PH-K-S", manufacturer="JST")
P("J2", "HDR-1X4", "USB / 5V IN", "5 V charge input + ESP32-S3 native USB D+/D-",
  1, 25, 140, "R0", 7.5, 7.5, "R270",
  mpn="generic 1x4 2.54mm header", manufacturer="-")
P("U1", "TP4056", "TP4056", "1 A linear Li-ion charger, 4.2 V float",
  1, 80, 160, "R0", 17.0, 12.0, "R0",
  mpn="TP4056-42-SOP8-PP", manufacturer="NanJing Top Power")
P("R1", "R-0805", "2k4", "TP4056 PROG: sets 500 mA charge current",
  1, 70, 140, "R90", 21.5, 7.5, "R0")
P("R2", "R-0805", "1k", "CHRG LED current limit", 1, 105, 178, "R0", 12.5, 17.5, "R0")
P("R3", "R-0805", "1k", "STDBY LED current limit", 1, 105, 170, "R0", 12.5, 20.5, "R0")
P("D1", "LED-0805", "RED", "Charging indicator", 1, 118, 178, "R0", 17.5, 17.5, "R0")
P("D2", "LED-0805", "GRN", "Charge-complete indicator", 1, 118, 170, "R0", 17.5, 20.5, "R0")
P("C1", "C-0805", "10u", "VBUS input bulk", 1, 45, 145, "R0", 10.0, 10.0, "R90")
P("C2", "C-0805", "10u", "VBAT bulk at the cell/charger node",
  1, 100, 140, "R0", 12.0, 26.0, "R90")
P("U2", "AP2112K-3.3", "AP2112K-3.3", "600 mA LDO, 3.3 V fixed",
  1, 150, 160, "R0", 8.0, 16.5, "R0")
P("R4", "R-0805", "100k", "LDO EN pull-up to VBAT", 1, 138, 145, "R90", 5.0, 19.5, "R90")
P("J3", "HDR-1X2", "OFF SW", "External latching switch: closed = board OFF",
  1, 130, 120, "R0", 3.8, 12.5, "R90",
  mpn="generic 1x2 2.54mm header", manufacturer="-")
P("C3", "C-0805", "10u", "LDO input cap (AP2112 needs >=1 uF)",
  1, 138, 172, "R0", 11.5, 14.0, "R90")
P("C4", "C-0805", "10u", "LDO output cap", 1, 172, 172, "R0", 16.0, 16.5, "R90")
P("C5", "C-0805", "100n", "LDO output HF bypass", 1, 182, 172, "R0", 19.0, 16.5, "R90")
P("R5", "R-0805", "470k", "VBAT sense divider, upper", 1, 205, 175, "R90", 22.0, 25.0, "R90")
P("R6", "R-0805", "470k", "VBAT sense divider, lower", 1, 205, 160, "R90", 22.0, 22.0, "R90")
P("C6", "C-0805", "100n", "VBAT sense filter / ADC reservoir",
  1, 218, 160, "R0", 24.5, 23.5, "R90")
P("J4", "HDR-1X5", "FUEL GAUGE", "MAX17048 breakout header (I2C, addr 0x36)",
  1, 205, 120, "R0", 24.5, 8.5, "R270",
  mpn="generic 1x5 2.54mm header", manufacturer="-")
P("TP1", "TESTPOINT", "VBAT", "Test point: VBAT", 1, 240, 178, "R0", 14.5, 29.0)
P("TP2", "TESTPOINT", "3V3", "Test point: 3V3", 1, 250, 178, "R0", 18.0, 29.0)
P("TP3", "TESTPOINT", "GND", "Test point: GND", 1, 260, 178, "R0", 21.5, 29.0)
P("TP4", "TESTPOINT", "VBUS", "Test point: VBUS", 1, 270, 178, "R0", 11.0, 29.0)
for _i, (_mx, _my) in enumerate(MOUNT_HOLES, start=1):
    P(f"H{_i}", "MOUNTHOLE-M2", "M2", "M2 mounting hole, GND-stitched",
      1, 240 + 12 * (_i - 1), 130, "R0", _mx, _my)
P("SUPPLY1", "SUPPLY-GND", "GND", "GND rail declaration", 1, 30, 100)
P("SUPPLY2", "SUPPLY-VBAT", "VBAT", "VBAT rail declaration", 1, 45, 100)
P("SUPPLY3", "SUPPLY-VBUS", "VBUS", "VBUS rail declaration", 1, 60, 100)
P("SUPPLY4", "SUPPLY-3V3", "3V3", "3V3 rail declaration", 1, 75, 100)

# ---------------------------------------------------------------------------
# SHEET 2 - ESP32-S3 CORE
# ---------------------------------------------------------------------------
P("U3", "ESP32-S3-WROOM-1", "ESP32-S3-WROOM-1-N8R2",
  "Central MCU: Xtensa LX7 dual core, Wi-Fi + BLE 5, 8 MB flash, 2 MB PSRAM",
  2, 130, 120, "R0", 17.0, 47.25, "R0",
  mpn="ESP32-S3-WROOM-1-N8R2", manufacturer="Espressif Systems")
P("C7", "C-0805", "100n", "ESP32 3V3 HF bypass at pin 2",
  2, 70, 175, "R0", 1.8, 51.5, "R90")
P("C8", "C-0805", "22u", "ESP32 3V3 bulk (Wi-Fi TX current burst)",
  2, 58, 175, "R0", 1.8, 48.0, "R90")
P("R7", "R-0805", "10k", "EN pull-up", 2, 60, 150, "R90", 1.8, 44.5, "R90")
P("C10", "C-0805", "1u", "EN RC delay (power-on reset)", 2, 72, 140, "R0", 1.8, 41.0, "R90")
P("SW2", "SW-TACT-6MM", "RESET", "Reset button (pulls EN low)",
  2, 60, 120, "R0", 33.5, 42.0, "R0",
  mpn="TL1105 family", manufacturer="-")
P("R8", "R-0805", "10k", "IO0 pull-up (boot strap default high)",
  2, 88, 150, "R90", 32.0, 36.5, "R90")
P("SW3", "SW-TACT-6MM", "BOOT", "Boot button (pulls IO0 low)",
  2, 88, 120, "R0", 33.5, 49.5, "R0",
  mpn="TL1105 family", manufacturer="-")
P("J5", "HDR-1X6", "UART PROG", "Fallback UART programming header",
  2, 210, 150, "R0", 16.0, 27.0, "R180",
  mpn="generic 1x6 2.54mm header", manufacturer="-")
P("R9", "R-0805", "1k", "LED_STATUS current limit", 2, 210, 105, "R0", 38.5, 51.5, "R0")
P("D3", "LED-0805", "GRN", "Status LED (IO45)", 2, 224, 105, "R0", 41.5, 51.5, "R0")
P("R10", "R-0805", "1k", "LED_ALERT current limit", 2, 210, 96, "R0", 38.5, 48.0, "R0")
P("D4", "LED-0805", "RED", "Alert LED (IO46)", 2, 224, 96, "R0", 41.5, 48.0, "R0")
P("TP5", "TESTPOINT", "IO3", "Test point: IO3 spare / ANG2_OUT", 2, 250, 80, "R0", 31.0, 33.0, "R0")
P("TP6", "TESTPOINT", "TMP_ALERT", "Test point: TMP117 ALERT (not routed to a GPIO)",
  2, 260, 80, "R0", 49.5, 41.5, "R0")
P("SUPPLY5", "SUPPLY-GND", "GND", "GND rail declaration", 2, 30, 60)
P("SUPPLY6", "SUPPLY-3V3", "3V3", "3V3 rail declaration", 2, 45, 60)

# ---------------------------------------------------------------------------
# SHEET 3 - I2C SENSORS  (bus A = SENSOR, bus B = ANGLE)
# ---------------------------------------------------------------------------
P("R11", "R-0805", "4k7", "I2C_SDA pull-up (bus A)", 3, 40, 175, "R90", 31.0, 41.0, "R90")
P("R12", "R-0805", "4k7", "I2C_SCL pull-up (bus A)", 3, 52, 175, "R90", 34.0, 41.0, "R90")
P("U4", "TMP117", "TMP117", "Digital temperature sensor, I2C addr 0x48",
  3, 100, 175, "R0", 46.5, 34.5, "R0",
  mpn="TMP117AIDRVR", manufacturer="Texas Instruments")
P("C11", "C-0805", "100n", "TMP117 V+ bypass", 3, 82, 165, "R0", 42.5, 34.0, "R90")
P("R13", "R-0805", "10k", "TMP117 ALERT pull-up (open drain)",
  3, 130, 190, "R90", 49.5, 41.5, "R90")
P("U5", "LSM6DSOX", "LSM6DSOX", "6-axis IMU, I2C addr 0x6A",
  3, 100, 130, "R0", 37.0, 34.0, "R0",
  mpn="LSM6DSOXTR", manufacturer="STMicroelectronics")
P("C12", "C-0805", "100n", "LSM6DSOX VDD filter (datasheet note 1)",
  3, 78, 120, "R0", 32.0, 30.5, "R90")
P("C13", "C-0805", "100n", "LSM6DSOX VDDIO filter (datasheet note 1)",
  3, 68, 120, "R0", 32.0, 34.0, "R90")
P("TP7", "TESTPOINT", "IMU_INT1", "Test point: IMU interrupt 1",
  3, 140, 118, "R0", 41.5, 30.0, "R0")
P("R15", "R-0805", "4k7", "ANG_SDA pull-up (bus B)", 3, 40, 90, "R90", 31.0, 27.5, "R90")
P("R16", "R-0805", "4k7", "ANG_SCL pull-up (bus B)", 3, 52, 90, "R90", 34.0, 27.5, "R90")
P("U6", "AS5600", "AS5600", "12-bit magnetic angle sensor, I2C addr 0x36 (fixed)",
  3, 100, 80, "R0", 44.0, 29.0, "R0",
  mpn="AS5600-ASOM", manufacturer="ams-OSRAM")
P("C14", "C-0805", "100n", "AS5600 VDD5V decoupling (datasheet pin 1 note)",
  3, 78, 70, "R0", 39.5, 26.5, "R90")
P("C15", "C-0805", "1u", "AS5600 VDD3V3 decoupling (datasheet pin 2 note)",
  3, 68, 70, "R0", 49.0, 26.5, "R90")
P("TP8", "TESTPOINT", "AS_OUT", "AS5600 analog/PWM OUT (unused, I2C is used)",
  3, 140, 68, "R0", 50.5, 32.0)
P("TP9", "TESTPOINT", "AS_PGO", "AS5600 PGO programming pin (internal pull-up)",
  3, 150, 68, "R0", 50.5, 29.0)
P("J6", "HDR-1X5", "AS5600 SIDE-B", "Second AS5600 (angle bus B + analog OUT)",
  3, 200, 80, "R0", 52.0, 30.0, "R90",
  mpn="generic 1x5 2.54mm header", manufacturer="-")
P("R17", "R-0805", "0R DNP", "Opt-in link: side-B AS5600 analog OUT -> IO3. "
  "Leave unpopulated unless the analog path is used (IO3 is a strapping pin).",
  3, 230, 90, "R0", 47.0, 22.5, "R0")
P("SUPPLY7", "SUPPLY-GND", "GND", "GND rail declaration", 3, 30, 40)
P("SUPPLY8", "SUPPLY-3V3", "3V3", "3V3 rail declaration", 3, 45, 40)

# ---------------------------------------------------------------------------
# SHEET 4 - ECG ANALOG FRONT END
# ---------------------------------------------------------------------------
P("U7", "AD8232", "AD8232", "Single-lead ECG analog front end (Vs 2.0-3.5 V)",
  4, 150, 130, "R0", 65.0, 18.0, "R180",
  mpn="AD8232ACPZ-R7", manufacturer="Analog Devices")
P("J7", "HDR-1X3", "ECG ELECTRODES", "LA / RA / RL electrode leads",
  4, 30, 165, "R0", 76.5, 18.0, "R90",
  mpn="generic 1x3 2.54mm header", manufacturer="-")
P("R18", "R-0805", "330k", "LA patient-protection series R (Vs/10uA)",
  4, 60, 172, "R0", 72.0, 21.5, "R0")
P("R19", "R-0805", "330k", "RA patient-protection series R (Vs/10uA)",
  4, 60, 164, "R0", 72.0, 19.0, "R0")
P("R20", "R-0805", "330k", "RLD output current limit (datasheet: >330k at 3.0 V)",
  4, 60, 150, "R0", 72.0, 24.0, "R0")
P("R21", "R-0805", "10M", "LA DC leads-off bias pull-up", 4, 80, 185, "R90", 75.0, 21.5, "R0")
P("R22", "R-0805", "10M", "RA DC leads-off bias pull-up", 4, 92, 185, "R90", 75.0, 19.0, "R0")
P("R23", "R-0805", "10M", "REFIN divider, upper", 4, 112, 100, "R90", 58.5, 11.5, "R0")
P("R24", "R-0805", "10M", "REFIN divider, lower", 4, 112, 85, "R90", 58.5, 8.5, "R0")
P("C16", "C-0805", "100n", "REFIN filter (settles in ~2.5 s)", 4, 124, 85, "R0", 55.8, 10.0, "R90")
P("C17", "C-0805", "1n", "RLD integrator (RLDFB to RLD)", 4, 90, 140, "R0", 72.0, 13.5, "R0")
P("C18", "C-0805", "220n", "HPF pole 1 cap (HPDRIVE to HPSENSE)",
  4, 190, 175, "R0", 69.0, 11.5, "R0")
P("R25", "R-0805", "10M", "HPF pole 1 resistor (HPSENSE to IAOUT) -> 7.2 Hz",
  4, 205, 185, "R0", 65.5, 8.5, "R0")
P("C19", "C-0805", "220n", "HPF pole 2 cap (IAOUT to SW)", 4, 220, 175, "R0", 69.0, 8.5, "R0")
P("R26", "R-0805", "1M", "HPF pole 2 resistor (SW to REFOUT) -> 0.72 Hz",
  4, 235, 165, "R90", 62.0, 8.5, "R0")
P("R27", "R-0805", "470k", "LPF input resistor", 4, 250, 150, "R0", 62.0, 25.0, "R0")
P("C20", "C-0805", "8n2", "LPF input cap -> ~41 Hz pole", 4, 262, 140, "R0", 58.5, 25.0, "R0")
P("R28", "R-0805", "100k", "Op-amp gain, lower leg (Rg)", 4, 250, 120, "R0", 65.5, 25.0, "R0")
P("R29", "R-0805", "1M", "Op-amp gain, feedback (Rf) -> gain 11", 4, 250, 112, "R0", 69.0, 25.0, "R0")
P("C21", "C-0805", "3n9", "Feedback cap -> ~41 Hz pole (2nd LPF pole)",
  4, 262, 104, "R0", 69.0, 28.0, "R0")
P("R30", "R-0805", "1k", "ADC series isolation", 4, 280, 130, "R0", 72.5, 28.0, "R0")
P("C22", "C-0805", "10n", "ADC input reservoir", 4, 292, 120, "R0", 75.5, 28.0, "R0")
P("R31", "R-0805", "100k", "SDN pull-up: AD8232 enabled by default",
  4, 120, 160, "R90", 56.5, 18.0, "R90")
P("R32", "R-0805", "100k", "FR pull-down: fast restore off by default",
  4, 120, 140, "R90", 56.5, 21.0, "R90")
P("C23", "C-0805", "100n", "AD8232 +VS bypass, close to pin 17",
  4, 140, 190, "R0", 62.0, 11.5, "R0")
P("C24", "C-0805", "1u", "AD8232 +VS bulk", 4, 152, 190, "R0", 65.5, 11.5, "R0")
P("TP10", "TESTPOINT", "ECG_OUT", "Test point: conditioned ECG output",
  4, 305, 130, "R0", 72.5, 31.5, "R0")
P("TP11", "TESTPOINT", "ECG_REF", "Test point: AD8232 REFOUT virtual ground",
  4, 305, 120, "R0", 75.5, 31.5, "R0")
P("SUPPLY9", "SUPPLY-GND", "GND", "GND rail declaration", 4, 30, 60)
P("SUPPLY10", "SUPPLY-3V3", "3V3", "3V3 rail declaration", 4, 45, 60)

# ---------------------------------------------------------------------------
# SHEET 5 - MECHANICAL SENSING
# ---------------------------------------------------------------------------
P("U8", "HX711", "HX711", "24-bit bridge ADC for the load cell",
  5, 110, 160, "R0", 37.0, 16.5, "R0",
  mpn="HX711", manufacturer="Avia Semiconductor")
P("J8", "JST-PH-4", "LOAD CELL", "4-wire bridge: E+, E-, A+, A-",
  5, 30, 165, "R0", 30.0, 3.0, "R0",
  mpn="S4B-PH-K-S", manufacturer="JST")
P("C25", "C-0805", "100n", "HX711 VBG reference bypass", 5, 78, 140, "R0", 31.5, 12.0, "R90")
P("C26", "C-0805", "100n", "HX711 AVDD bypass", 5, 88, 175, "R0", 31.5, 18.0, "R90")
P("C27", "C-0805", "100n", "HX711 DVDD bypass", 5, 98, 175, "R0", 41.0, 18.0, "R90")
P("C28", "C-0805", "10u", "HX711 analog bulk / bridge excitation reservoir",
  5, 68, 175, "R0", 31.5, 21.0, "R90")
P("TP12", "TESTPOINT", "HX_BASE", "HX711 BASE (regulator unused: NC)",
  5, 150, 140, "R0", 45.0, 12.0)
P("TP13", "TESTPOINT", "HX_XO", "HX711 XO (crystal unused: NC)", 5, 160, 140, "R0", 45.0, 15.0)
for _i in range(1, 5):
    P(f"J{8 + _i}", "HDR-1X2", f"FSR{_i}", f"Force-sensing resistor {_i} (belt pressure)",
      5, 190 + 30 * (_i - 1), 185, "R0", 30.0 + 5.5 * (_i - 1), 8.5, "R0",
      mpn="FSR402 + 1x2 header", manufacturer="-")
    P(f"R{32 + _i}", "R-0805", "10k",
      f"FSR{_i} divider resistor (10k = geometric mean of the 2k-100k band)",
      5, 200 + 30 * (_i - 1), 168, "R90", 30.0 + 5.5 * (_i - 1), 9.5, "R90")
    P(f"C{28 + _i}", "C-0805", "10n", f"FSR{_i} anti-alias filter (1.6 kHz)",
      5, 212 + 30 * (_i - 1), 168, "R90", 32.0 + 5.5 * (_i - 1), 11.5, "R90")
P("J13", "HDR-1X2", "STRETCH", "Abdominal stretch / extension sensor",
  5, 190, 130, "R0", 52.0, 8.5, "R0",
  mpn="TBD - see REQUIRES_CONFIRMATION.md", manufacturer="-")
P("R37", "R-0805", "10k",
  "Stretch divider resistor - PLACEHOLDER. Set to the geometric mean of the "
  "chosen sensor's resistance range once that part is fixed.",
  5, 202, 115, "R90", 52.0, 9.5, "R90")
P("C33", "C-0805", "10n", "Stretch anti-alias filter", 5, 214, 115, "R90", 50.0, 11.5, "R90")
P("J14", "HDR-1X2", "PIEZO", "Piezo film fetal-movement sensor",
  5, 250, 130, "R0", 45.0, 3.0, "R0",
  mpn="piezo film + 1x2 header", manufacturer="-")
P("R38", "R-0805", "10M", "Piezo load resistor (sets the ~10 Hz LF corner)",
  5, 258, 115, "R90", 45.0, 7.0, "R90")
P("C34", "C-0805", "100n/50V", "Piezo AC coupling (must withstand the film's "
  "open-circuit transient)", 5, 268, 130, "R0", 48.0, 8.5, "R0")
P("R39", "R-0805", "1M", "Piezo mid-rail bias, upper", 5, 282, 145, "R90", 48.0, 12.5, "R90")
P("R40", "R-0805", "1M", "Piezo mid-rail bias, lower", 5, 282, 118, "R90", 48.0, 10.0, "R90")
P("R41", "R-0805", "100k", "Piezo ADC series current limit", 5, 296, 130, "R0", 51.5, 8.5, "R0")
P("C35", "C-0805", "10n", "Piezo ADC filter (160 Hz)", 5, 308, 118, "R90", 51.5, 13.0, "R90")
P("D5", "DIODE-SOD123", "1N5819HW", "Piezo over-voltage clamp to 3V3",
  5, 320, 140, "R90", 51.5, 16.0, "R90",
  mpn="1N5819HW", manufacturer="generic (Diodes/onsemi/MDD)")
P("D6", "DIODE-SOD123", "1N5819HW", "Piezo under-voltage clamp to GND",
  5, 320, 118, "R90", 48.0, 16.0, "R90",
  mpn="1N5819HW", manufacturer="generic (Diodes/onsemi/MDD)")
P("J15", "HDR-1X3", "HALL / LIMIT", "Hall or mechanical limit switch (rail travel)",
  5, 250, 80, "R0", 38.0, 3.0, "R0",
  mpn="generic 1x3 2.54mm header", manufacturer="-")
P("R42", "R-0805", "10k", "Hall/limit pull-up", 5, 262, 95, "R90", 38.0, 7.0, "R90")
P("C36", "C-0805", "100n", "Hall/limit hardware debounce (~1 ms)",
  5, 274, 68, "R90", 40.5, 9.0, "R90")
P("TP14", "TESTPOINT", "HX_DOUT", "Test point: HX711 serial data out",
  5, 340, 100, "R0", 45.0, 21.0)
P("SUPPLY11", "SUPPLY-GND", "GND", "GND rail declaration", 5, 30, 40)
P("SUPPLY12", "SUPPLY-3V3", "3V3", "3V3 rail declaration", 5, 45, 40)

# ---------------------------------------------------------------------------
# SHEET 6 - FET-DRIVEN ALERTS
# ---------------------------------------------------------------------------
P("Q1", "NMOS-SOT23", "AO3400A", "Low-side switch for the vibration motor",
  6, 110, 165, "R0", 62.0, 49.0, "R0",
  mpn="AO3400A", manufacturer="Alpha & Omega Semiconductor")
P("R43", "R-0805", "100R", "Motor gate series resistor (slew limit)",
  6, 85, 165, "R0", 57.0, 49.0, "R0")
P("R44", "R-0805", "100k", "Motor gate pull-down (fail-safe OFF)",
  6, 97, 150, "R90", 57.0, 45.5, "R90")
P("J16", "HDR-1X2", "VIB MOTOR", "Vibration motor output",
  6, 150, 190, "R0", 70.0, 57.0, "R180",
  mpn="generic 1x2 2.54mm header", manufacturer="-")
P("R45", "R-0805", "0R", "Motor ballast: populate only if the chosen motor is "
  "rated below 4.2 V", 6, 130, 195, "R0", 65.5, 54.0, "R0")
P("D7", "DIODE-SOD123", "1N5819HW", "Motor flyback (cathode to VBAT side)",
  6, 140, 175, "R90", 69.5, 51.0, "R90",
  mpn="1N5819HW", manufacturer="generic (Diodes/onsemi/MDD)")
P("C37", "C-0805", "10u", "Local motor bulk (keeps di/dt out of the shared rail)",
  6, 122, 175, "R0", 62.0, 54.0, "R90")
P("Q2", "NMOS-SOT23", "AO3400A", "Low-side switch for the buzzer",
  6, 110, 100, "R0", 62.0, 44.5, "R0",
  mpn="AO3400A", manufacturer="Alpha & Omega Semiconductor")
P("R46", "R-0805", "100R", "Buzzer gate series resistor", 6, 85, 100, "R0", 57.0, 44.5, "R0")
P("R47", "R-0805", "100k", "Buzzer gate pull-down (fail-safe OFF)",
  6, 97, 85, "R90", 57.0, 41.5, "R90")
P("J17", "HDR-1X2", "BUZZER", "Magnetic or piezo buzzer output",
  6, 150, 125, "R0", 76.5, 47.5, "R90",
  mpn="generic 1x2 2.54mm header", manufacturer="-")
P("D8", "DIODE-SOD123", "1N5819HW", "Buzzer flyback (magnetic buzzers are inductive)",
  6, 140, 110, "R90", 70.5, 44.5, "R90",
  mpn="1N5819HW", manufacturer="generic (Diodes/onsemi/MDD)")
P("C38", "C-0805", "10u", "Local 3V3 bulk at the buzzer FET", 6, 122, 110, "R0", 66.0, 41.5, "R90")
P("TP15", "TESTPOINT", "MOTOR_EN", "Test point: MOTOR_EN gate drive", 6, 200, 150, "R0", 57.0, 55.5)
P("TP16", "TESTPOINT", "BUZZER_EN", "Test point: BUZZER_EN gate drive", 6, 210, 150, "R0", 57.0, 52.5)
P("SUPPLY13", "SUPPLY-GND", "GND", "GND rail declaration", 6, 30, 50)
P("SUPPLY14", "SUPPLY-3V3", "3V3", "3V3 rail declaration", 6, 45, 50)
P("SUPPLY15", "SUPPLY-VBAT", "VBAT", "VBAT rail declaration", 6, 60, 50)

# ---------------------------------------------------------------------------
# SHEET 7 - USER INPUT / STORAGE
# ---------------------------------------------------------------------------
P("SW4", "SW-TACT-6MM", "SOS", "Manual emergency SOS button",
  7, 60, 165, "R0", 46.0, 53.5, "R0",
  mpn="TL1105 family", manufacturer="-")
P("R48", "R-0805", "10k", "SOS pull-up", 7, 48, 185, "R90", 50.5, 50.0, "R90")
P("C39", "C-0805", "100n", "SOS hardware debounce + ESD shunt (~1 ms)",
  7, 78, 150, "R90", 47.5, 50.0, "R90")
P("R49", "R-0805", "1k", "SOS GPIO series protection", 7, 92, 165, "R0", 44.0, 50.0, "R0")
P("J18", "HDR-1X6", "MICROSD SPI", "microSD breakout module (SPI)",
  7, 190, 160, "R0", 35.0, 56.8, "R0",
  mpn="generic microSD SPI breakout + 1x6 header", manufacturer="-")
P("R50", "R-0805", "10k", "SD_CS pull-up (SD spec recommends 10k-100k)",
  7, 165, 185, "R90", 30.0, 53.5, "R0")
P("R51", "R-0805", "10k", "SD_MISO pull-up", 7, 177, 185, "R90", 30.0, 56.0, "R0")
P("TP17", "TESTPOINT", "SOS_GPIO", "Test point: SOS GPIO", 7, 240, 140, "R0", 52.0, 55.0, "R0")
P("TP18", "TESTPOINT", "I2C_SDA", "Test point: sensor-bus SDA", 7, 250, 140, "R0", 52.0, 45.0, "R0")
P("TP19", "TESTPOINT", "I2C_SCL", "Test point: sensor-bus SCL", 7, 260, 140, "R0", 52.0, 42.0, "R0")
P("SUPPLY16", "SUPPLY-GND", "GND", "GND rail declaration", 7, 30, 60)
P("SUPPLY17", "SUPPLY-3V3", "3V3", "3V3 rail declaration", 7, 45, 60)


# ===========================================================================
# NETLIST   net name -> list of (ref, pin)
# ===========================================================================
NETS: dict[str, list[tuple[str, str]]] = {}


def N(net: str, *conns: str) -> None:
    """Add connections written as 'REF.PIN'."""
    lst = NETS.setdefault(net, [])
    for c in conns:
        ref, pin = c.split(".", 1)
        lst.append((ref, pin))


# ---- Ground -----------------------------------------------------------------
N("GND",
  "SUPPLY1.GND", "SUPPLY5.GND", "SUPPLY7.GND", "SUPPLY9.GND",
  "SUPPLY11.GND", "SUPPLY13.GND", "SUPPLY16.GND",
  # Sheet 1
  "J1.2", "J2.4", "U1.GND", "R1.2", "C1.2", "C2.2",
  "U2.GND", "J3.2", "C3.2", "C4.2", "C5.2", "R6.2", "C6.2", "J4.2",
  "TP3.TP", "H1.1", "H2.1", "H3.1", "H4.1",
  # Sheet 2
  "U3.GND@1", "U3.GND@40", "U3.EPAD", "C7.2", "C8.2", "C10.2",
  "SW2.N", "SW3.N", "J5.1", "D3.C", "D4.C",
  # Sheet 3
  "U4.GND", "U4.TPAD", "C11.2", "U5.GND@6", "U5.GND@7", "U5.SDO/SA0",
  "U5.SDx", "U5.SCx", "C12.2", "C13.2",
  "U6.GND", "U6.DIR", "C14.2", "C15.2", "J6.2",
  # Sheet 4
  "U7.GND", "U7.EP", "U7.AC/DC", "R24.2", "C16.2", "R32.2",
  "C22.2", "C23.2", "C24.2",
  # Sheet 5
  "U8.AGND", "U8.VFB", "U8.INB+", "U8.INB-", "U8.XI", "U8.RATE",
  "J8.2", "C25.2", "C26.2", "C27.2", "C28.2",
  "R33.2", "R34.2", "R35.2", "R36.2", "C29.2", "C30.2", "C31.2", "C32.2",
  "R37.2", "C33.2", "J14.2", "R38.2", "R40.2", "C35.2", "D6.A",
  "J15.3", "C36.2",
  # Sheet 6
  "Q1.S", "R44.2", "Q2.S", "R47.2", "C37.2", "C38.2",
  # Sheet 7
  "SW4.N", "C39.2", "J18.2",
  )

# ---- VBUS (5 V charge input) ------------------------------------------------
N("VBUS", "SUPPLY3.VBUS", "J2.1", "U1.VCC", "U1.CE", "C1.1",
  "R2.1", "R3.1", "TP4.TP")

# ---- VBAT (cell / system rail) ---------------------------------------------
N("VBAT", "SUPPLY2.VBAT", "SUPPLY15.VBAT",
  "J1.1", "U1.BAT", "C2.1", "U2.VIN", "R4.1", "C3.1",
  "R5.1", "J4.1", "TP1.TP", "R45.1")

# ---- 3V3 --------------------------------------------------------------------
N("3V3", "SUPPLY4.3V3", "SUPPLY6.3V3", "SUPPLY8.3V3", "SUPPLY10.3V3",
  "SUPPLY12.3V3", "SUPPLY14.3V3", "SUPPLY17.3V3",
  # Sheet 1
  "U2.VOUT", "C4.1", "C5.1", "J4.3", "TP2.TP",
  # Sheet 2
  "U3.3V3", "C7.1", "C8.1", "R7.1", "J5.2", "R8.1",
  # Sheet 3
  "R11.1", "R12.1", "U4.V+", "C11.1", "R13.1",
  "U5.VDD", "U5.VDDIO", "U5.CS", "U5.SDO_AUX", "C12.1", "C13.1",
  "R15.1", "R16.1", "U6.VDD5V", "U6.VDD3V3", "C14.1", "C15.1", "J6.1",
  # Sheet 4
  "U7.+VS", "R21.1", "R22.1", "R23.1", "R31.1", "C23.1", "C24.1",
  # Sheet 5
  "U8.VSUP", "U8.AVDD", "U8.DVDD", "J8.1", "C26.1", "C27.1", "C28.1",
  "J9.1", "J10.1", "J11.1", "J12.1", "J13.1", "R39.1", "D5.C",
  "J15.1", "R42.1",
  # Sheet 6
  "J17.1", "D8.C", "C38.1",
  # Sheet 7
  "R48.1", "J18.1", "R50.1", "R51.1",
  )

# ---- Charging -----------------------------------------------------------
N("CHG_PROG", "U1.PROG", "R1.1")
N("CHG_TEMP", "U1.TEMP")                 # NTC unused: grounded via the net below
N("LED_CHRG_K", "U1.CHRG", "D1.C")
N("LED_CHRG_A", "R2.2", "D1.A")
N("LED_STDBY_K", "U1.STDBY", "D2.C")
N("LED_STDBY_A", "R3.2", "D2.A")
N("LDO_EN", "U2.EN", "R4.2", "J3.1")
N("LDO_NC", "U2.NC")
N("VBAT_SENSE", "R5.2", "R6.1", "C6.1", "U3.IO9")

# ---- ESP32 core ---------------------------------------------------------
N("ESP_EN", "U3.EN", "R7.2", "C10.1", "SW2.P", "J5.5")
N("ESP_IO0", "U3.IO0", "R8.2", "SW3.P", "J5.6")
N("UART_TX", "U3.TXD0", "J5.3")
N("UART_RX", "U3.RXD0", "J5.4")
N("LED_STATUS", "U3.IO45", "R9.1")
N("LED_STATUS_A", "R9.2", "D3.A")
N("LED_ALERT", "U3.IO46", "R10.1")
N("LED_ALERT_A", "R10.2", "D4.A")
N("USB_DM", "U3.IO19", "J2.2")
N("USB_DP", "U3.IO20", "J2.3")

# ---- I2C bus A (SENSOR) -------------------------------------------------
N("I2C_SDA", "U3.IO15", "R11.2", "U4.SDA", "U5.SDA", "J4.4", "TP18.TP")
N("I2C_SCL", "U3.IO16", "R12.2", "U4.SCL", "U5.SCL", "J4.5", "TP19.TP")
N("TMP_ADDR", "U4.ADD0")                 # tied low on the GND net below
N("TMP_ALERT", "U4.ALERT", "R13.2", "TP6.TP")
N("IMU_INT1", "U3.IO17", "U5.INT1", "TP7.TP")
N("IMU_INT2", "U3.IO18", "U5.INT2")
# LSM6DSOX DS12814 Rev.4 Table 1 note 2: "Leave pin electrically
# unconnected and soldered to PCB."  Its own pad satisfies both
# halves of that, so this is a genuine single-pin net rather than a
# link to a test point - which would only add an airwire that means
# nothing.  Declared in validate_erc.py.
N("IMU_OCS_AUX", "U5.OCS_AUX")

# ---- I2C bus B (ANGLE) --------------------------------------------------
N("ANG_SDA", "U3.IO14", "R15.2", "U6.SDA", "J6.3")
N("ANG_SCL", "U3.IO42", "R16.2", "U6.SCL", "J6.4")
N("AS_OUT", "U6.OUT", "TP8.TP")
N("AS_PGO", "U6.PGO", "TP9.TP")
N("ANG2_OUT", "J6.5", "R17.1")
N("IO3_SPARE", "U3.IO3", "R17.2", "TP5.TP")

# ---- ECG ----------------------------------------------------------------
N("ECG_LA", "J7.1", "R18.1")
N("ECG_RA", "J7.2", "R19.1")
N("ECG_RL", "J7.3", "R20.2")
N("ECG_LA_F", "R18.2", "U7.+IN", "R21.2")
N("ECG_RA_F", "R19.2", "U7.-IN", "R22.2")
# The RLD amplifier is turned into an integrator by a single capacitor between
# RLDFB and RLD (AD8232 Rev.A, "Right Leg Drive Amplifier" / Figure 46).  The
# inverting input is driven internally from VCM through 150 k, so no external
# DC feedback resistor is used.
N("ECG_RLD", "U7.RLD", "C17.1", "R20.1")
N("ECG_RLDFB", "U7.RLDFB", "C17.2")
N("ECG_REFIN", "U7.REFIN", "R23.2", "R24.1", "C16.1")
N("ECG_REFOUT", "U7.REFOUT", "R26.1", "C20.2", "R28.2", "TP11.TP")
N("ECG_HPSENSE", "U7.HPSENSE", "C18.2", "R25.1")
N("ECG_HPDRIVE", "U7.HPDRIVE", "C18.1")
N("ECG_IAOUT", "U7.IAOUT", "R25.2", "C19.1")
N("ECG_SW", "U7.SW", "C19.2", "R26.2", "R27.1")
N("ECG_OPP", "U7.OPAMP+", "R27.2", "C20.1")
N("ECG_OPM", "U7.OPAMP-", "R28.1", "R29.1", "C21.1")
N("ECG_OUT_RAW", "U7.OUT", "R29.2", "C21.2", "R30.1")
N("ECG_OUT", "R30.2", "C22.1", "U3.IO1", "TP10.TP")
N("ECG_SDN", "U7.SDN", "R31.2", "U3.IO37")
N("ECG_FR", "U7.FR", "R32.1", "U3.IO39")
N("ECG_LOD_P", "U7.LOD+", "U3.IO35")
N("ECG_LOD_N", "U7.LOD-", "U3.IO36")

# ---- Load cell ----------------------------------------------------------
N("LC_A_P", "J8.3", "U8.INA+")
N("LC_A_N", "J8.4", "U8.INA-")
N("HX_VBG", "U8.VBG", "C25.1")
N("HX_BASE", "U8.BASE", "TP12.TP")
N("HX_XO", "U8.XO", "TP13.TP")
N("HX_DOUT", "U8.DOUT", "U3.IO21", "TP14.TP")
N("HX_SCK", "U8.PD_SCK", "U3.IO38")

# ---- FSRs, stretch, piezo, hall ----------------------------------------
_FSR_GPIO = {1: "IO4", 2: "IO5", 3: "IO6", 4: "IO7"}
for _i in range(1, 5):
    N(f"FSR{_i}_ADC", f"J{8 + _i}.2", f"R{32 + _i}.1", f"C{28 + _i}.1",
      f"U3.{_FSR_GPIO[_i]}")
N("STRETCH_ADC", "J13.2", "R37.1", "C33.1", "U3.IO8")
N("PIEZO_IN", "J14.1", "R38.1", "C34.1")
N("PIEZO_AC", "C34.2", "R39.2", "R40.1", "R41.1")
N("PIEZO_ADC", "R41.2", "C35.1", "D5.A", "D6.C", "U3.IO2")
N("HALL_LIMIT", "J15.2", "R42.2", "C36.1", "U3.IO41")

# ---- Alerts -------------------------------------------------------------
N("MOTOR_EN", "U3.IO47", "R43.1", "TP15.TP")
N("MOTOR_G", "R43.2", "Q1.G", "R44.1")
N("MOTOR_P", "R45.2", "J16.1", "D7.C", "C37.1")
N("MOTOR_N", "J16.2", "Q1.D", "D7.A")
N("BUZZER_EN", "U3.IO48", "R46.1", "TP16.TP")
N("BUZZ_G", "R46.2", "Q2.G", "R47.1")
N("BUZZ_N", "J17.2", "Q2.D", "D8.A")

# ---- User input / storage ----------------------------------------------
N("SOS_BTN", "SW4.P", "R48.2", "C39.1", "R49.1")
N("SOS_GPIO", "R49.2", "U3.IO40", "TP17.TP")
N("SD_SCK", "J18.3", "U3.IO12")
N("SD_MOSI", "J18.4", "U3.IO11")
N("SD_MISO", "J18.5", "U3.IO13", "R51.2")
N("SD_CS", "J18.6", "U3.IO10", "R50.2")

# ---- Pins deliberately tied to GND -------------------------------------
# TP4056 TEMP: temperature sense disabled by grounding (datasheet: "The
#   temperature sense function can be disabled by grounding the TEMP pin").
# TMP117 ADD0: grounded -> I2C address 0x48.
NETS["GND"].extend([("U1", "TEMP"), ("U4", "ADD0")])
for _dead in ("CHG_TEMP", "TMP_ADDR"):
    NETS.pop(_dead, None)

# LDO NC pin: AP2112 pin 4 is "No Connection".  Kept as its own single-pin
# net so it shows up explicitly in the ERC report rather than silently.
# (see documentation/ERC_REPORT.md)


# ===========================================================================
# GPIO ALLOCATION TABLE  (drives GPIO_ASSIGNMENT.md and the ERC checks)
# ===========================================================================
@dataclass
class Gpio:
    pin: str            # module pin name
    pad: str            # module pad number
    func: str
    net: str
    direction: str      # IN / OUT / IO / ANALOG IN / POWER
    boot_critical: bool
    adc: str
    peripheral: str
    component: str
    notes: str = ""


GPIO_TABLE: list[Gpio] = [
    Gpio("IO0", "27", "BOOT strap / boot button", "ESP_IO0", "IO", True, "-", "-",
         "SW3, R8, J5.6",
         "Weak internal pull-up. Held low at reset = download mode."),
    Gpio("IO1", "39", "ECG analog output", "ECG_OUT", "ANALOG IN", False,
         "ADC1_CH0", "ADC1", "U7 via R30/C22",
         "ADC1 is the only ADC usable while the radio is on."),
    Gpio("IO2", "38", "Piezo (fetal movement)", "PIEZO_ADC", "ANALOG IN", False,
         "ADC1_CH1", "ADC1", "J14 chain, D5/D6 clamped", ""),
    Gpio("IO3", "15", "Spare / side-B AS5600 analog OUT", "IO3_SPARE", "ANALOG IN",
         True, "ADC1_CH2", "ADC1", "TP5, R17 (DNP)",
         "STRAPPING (JTAG source select). R17 left unpopulated by default."),
    Gpio("IO4", "4", "FSR1 (belt pressure)", "FSR1_ADC", "ANALOG IN", False,
         "ADC1_CH3", "ADC1", "J9/R33/C29", ""),
    Gpio("IO5", "5", "FSR2 (belt pressure)", "FSR2_ADC", "ANALOG IN", False,
         "ADC1_CH4", "ADC1", "J10/R34/C30", ""),
    Gpio("IO6", "6", "FSR3 (belt pressure)", "FSR3_ADC", "ANALOG IN", False,
         "ADC1_CH5", "ADC1", "J11/R35/C31", ""),
    Gpio("IO7", "7", "FSR4 (belt pressure)", "FSR4_ADC", "ANALOG IN", False,
         "ADC1_CH6", "ADC1", "J12/R36/C32", ""),
    Gpio("IO8", "12", "Stretch sensor", "STRETCH_ADC", "ANALOG IN", False,
         "ADC1_CH7", "ADC1", "J13/R37/C33", "R37 value is a placeholder."),
    Gpio("IO9", "17", "Battery voltage sense", "VBAT_SENSE", "ANALOG IN", False,
         "ADC1_CH8", "ADC1", "R5/R6/C6",
         "470k/470k halves VBAT; 4.2 V cell -> 2.10 V at the pin."),
    Gpio("IO10", "18", "microSD chip select", "SD_CS", "OUT", False,
         "ADC1_CH9 (unused)", "FSPICS0", "J18.6, R50", ""),
    Gpio("IO11", "19", "microSD MOSI", "SD_MOSI", "OUT", False, "ADC2", "FSPID",
         "J18.4", ""),
    Gpio("IO12", "20", "microSD SCK", "SD_SCK", "OUT", False, "ADC2", "FSPICLK",
         "J18.3", ""),
    Gpio("IO13", "21", "microSD MISO", "SD_MISO", "IN", False, "ADC2", "FSPIQ",
         "J18.5, R51", ""),
    Gpio("IO14", "22", "Angle-bus I2C SDA", "ANG_SDA", "IO", False, "ADC2",
         "I2C1", "U6, J6, R15", "Separate bus resolves the 0x36 clash."),
    Gpio("IO15", "8", "Sensor-bus I2C SDA", "I2C_SDA", "IO", False, "ADC2",
         "I2C0", "U4, U5, J4, R11", ""),
    Gpio("IO16", "9", "Sensor-bus I2C SCL", "I2C_SCL", "OUT", False, "ADC2",
         "I2C0", "U4, U5, J4, R12", ""),
    Gpio("IO17", "10", "IMU interrupt 1", "IMU_INT1", "IN", False, "ADC2", "GPIO",
         "U5.INT1", ""),
    Gpio("IO18", "11", "IMU interrupt 2", "IMU_INT2", "IN", False, "ADC2", "GPIO",
         "U5.INT2", ""),
    Gpio("IO19", "13", "USB D-", "USB_DM", "IO", False, "ADC2", "USB-Serial-JTAG",
         "J2.2", "Route as a 90 ohm differential pair with IO20."),
    Gpio("IO20", "14", "USB D+", "USB_DP", "IO", False, "ADC2", "USB-Serial-JTAG",
         "J2.3", ""),
    Gpio("IO21", "23", "HX711 serial data out", "HX_DOUT", "IN", False, "-",
         "GPIO", "U8.DOUT", ""),
    Gpio("IO35", "28", "ECG leads-off, + input", "ECG_LOD_P", "IN", False, "-",
         "GPIO", "U7.LOD+",
         "Free on -N8R2 only. Octal-PSRAM parts reserve IO35/36/37."),
    Gpio("IO36", "29", "ECG leads-off, - input", "ECG_LOD_N", "IN", False, "-",
         "GPIO", "U7.LOD-", "See IO35 note."),
    Gpio("IO37", "30", "ECG shutdown control", "ECG_SDN", "OUT", False, "-",
         "GPIO", "U7.SDN, R31", "R31 keeps the AFE enabled if the GPIO floats."),
    Gpio("IO38", "31", "HX711 clock / power-down", "HX_SCK", "OUT", False, "-",
         "GPIO", "U8.PD_SCK", ""),
    Gpio("IO39", "32", "ECG fast restore", "ECG_FR", "OUT", False, "-",
         "GPIO (was MTCK)", "U7.FR, R32",
         "Pin-JTAG is given up; debugging uses the built-in USB-Serial-JTAG."),
    Gpio("IO40", "33", "SOS button", "SOS_GPIO", "IN", False, "-",
         "GPIO (was MTDO)", "SW4 via R49", ""),
    Gpio("IO41", "34", "Hall / limit switch", "HALL_LIMIT", "IN", False, "-",
         "GPIO (was MTDI)", "J15, R42", ""),
    Gpio("IO42", "35", "Angle-bus I2C SCL", "ANG_SCL", "OUT", False, "-",
         "I2C1 (was MTMS)", "U6, J6, R16", ""),
    Gpio("TXD0", "37", "UART0 TX", "UART_TX", "OUT", False, "-", "UART0",
         "J5.3", "GPIO43."),
    Gpio("RXD0", "36", "UART0 RX", "UART_RX", "IN", False, "-", "UART0",
         "J5.4", "GPIO44."),
    Gpio("IO45", "26", "Status LED (green)", "LED_STATUS", "OUT", True, "-",
         "GPIO", "R9, D3",
         "STRAPPING (VDD_SPI). LED to GND keeps the strap at its default 0."),
    Gpio("IO46", "16", "Alert LED (red)", "LED_ALERT", "OUT", True, "-", "GPIO",
         "R10, D4",
         "STRAPPING (ROM print). LED to GND keeps the strap at its default 0."),
    Gpio("IO47", "24", "Vibration motor enable", "MOTOR_EN", "OUT", False, "-",
         "GPIO", "R43 -> Q1", ""),
    Gpio("IO48", "25", "Buzzer enable", "BUZZER_EN", "OUT", False, "-", "GPIO",
         "R46 -> Q2", ""),
    Gpio("EN", "3", "Chip enable / reset", "ESP_EN", "IN", True, "-", "-",
         "R7, C10, SW2, J5.5", "Must not be left floating."),
    Gpio("3V3", "2", "Module supply", "3V3", "POWER", False, "-", "-",
         "C7, C8", ""),
    Gpio("GND", "1, 40, 41", "Ground (incl. EPAD)", "GND", "POWER", False, "-",
         "-", "Ground plane", "EPAD must be soldered and via-stitched."),
]


# ===========================================================================
# Derived helpers
# ===========================================================================
def part(ref: str) -> Part:
    for p in PARTS:
        if p.ref == ref:
            return p
    raise KeyError(ref)


PART_BY_REF = {p.ref: p for p in PARTS}

SHEET_TITLES = {
    1: "SHEET 1/7 - POWER ENTRY, CHARGING AND 3V3 REGULATION",
    2: "SHEET 2/7 - ESP32-S3 CENTRAL MCU, RESET/BOOT, PROGRAMMING, INDICATORS",
    3: "SHEET 3/7 - I2C SENSORS (TMP117, LSM6DSOX, AS5600) - TWO BUSSES",
    4: "SHEET 4/7 - ECG ANALOG FRONT END (AD8232)",
    5: "SHEET 5/7 - MECHANICAL SENSING (LOAD CELL, FSR, STRETCH, PIEZO, HALL)",
    6: "SHEET 6/7 - FET-DRIVEN ALERTS (VIBRATION MOTOR, BUZZER)",
    7: "SHEET 7/7 - USER INPUT AND STORAGE (SOS, microSD)",
}

PROJECT_TITLE = "SIH26113 - MATERNITY ASSIST BELT - PROTOTYPE CARRIER BOARD"
PROJECT_SUBTITLE = (
    "NOT A MEDICAL DEVICE. Prototype for engineering evaluation only. "
    "Human-connected ECG is NOT isolated - see documentation/README."
)


# ===========================================================================
# PLACEMENT RESOLUTION
#
# The board coordinates above are *placement intent*: each passive is written
# next to the pin it serves.  Hand-picked coordinates inevitably collide once
# real land patterns are involved (an 0805 land pattern is 3.05 mm across, so
# a 3.0 mm pitch overlaps), so a final pass nudges every non-fixed part to the
# nearest legal position.  Fixed parts - ICs, the module, connectors, switches
# and mounting holes - never move: their positions are mechanical decisions.
#
# The pass guarantees, for every part:
#   * copper inside the board outline with EDGE_CLEAR to spare,
#   * COURTYARD_GAP between its copper bounding box and every other part's,
#   * nothing inside the antenna keep-out,
#   * nothing inside a fine-pitch fan-out envelope.
# ===========================================================================
EDGE_CLEAR = 0.40
# 0.9 mm between neighbouring courtyards is more than assembly needs;
# the surplus is deliberate, because a 0.9 mm gap is exactly wide
# enough for one 0.25 mm track plus clearance to pass between two
# passives.  Packing tighter saves area the board does not need and
# costs routing lanes it does.
COURTYARD_GAP = 0.90

# Routing channels kept clear of components.  The ESP32-S3-WROOM-1 presents
# 40 lands on a 1.27 mm pitch across three edges; without a dedicated escape
# corridor outboard of each land row there is simply nowhere for those 40
# signals to go, and the router (or a human) stalls.  These bands are the
# single most important placement constraint on the board.
ESCAPE_CHANNELS = [
    (0.90, 43.0, 9.50, 64.0),      # left of the module's pad column
    (28.50, 40.0, 34.20, 64.0),    # right of the module's pad column
    (8.00, 36.00, 29.00, 44.20),   # below the module's end row
]

# The module's own decoupling and reset network is allowed inside the left
# channel: keeping C7/C8 within ~2 mm of module pin 2 matters more than the
# two track slots they cost, and both are on a plane net anyway.
CHANNEL_EXEMPT = {"C7", "C8", "R7", "C10"}

# Fine-pitch fan-out envelopes (deviceset -> half-size of the reserved box).
# Must stay consistent with FANOUT in generate_board.py.
# Clearance inside a fine-pitch fan-out.
#
# A 0.5 mm-pitch QFN cannot be escaped at 0.15 mm/0.15 mm - there is not
# enough room between the pads, which is why the escape tracks are 0.15 mm
# wide rather than 0.20 mm in the first place.  Inside the fan-out envelope
# of a fine-pitch part the rule is therefore 0.127 mm (5 mil), and outside
# it the general 0.15 mm applies.  0.127 mm is what the board actually
# achieves - the measured minimum, not a round number chosen for slack.
#
# This is a declared, bounded exception, not a fudge: it applies only within
# the named rectangles, it is checked as such by validate_drc.py, and it
# means the board needs a fabricator offering 5 mil / 0.127 mm trace and gap.
# That is a standard option (JLCPCB, PCBWay and most others quote it on
# 4-layer), but it must be selected when ordering - see
# REQUIRES_CONFIRMATION.md.
FINE_PITCH_CLEARANCE = 0.127
GENERAL_CLEARANCE = 0.15

FANOUT_ENVELOPE = {
    "AD8232": 6.6,
    "LSM6DSOX": 4.8,
    "TMP117": 4.1,
    "HX711": 8.0,
}

FIXED_PREFIXES = ("U", "J", "SW", "H")


def _is_fixed(p: Part) -> bool:
    if p.deviceset.startswith("SUPPLY-"):
        return True
    return p.ref.startswith(FIXED_PREFIXES) and not p.ref.startswith("TP")


def _bbox(p: Part, x: float, y: float):
    """Copper bounding box of part `p` if placed at (x, y). None if no package."""
    import geom
    ds = geom.DS[p.deviceset]
    if ds.package is None:
        return None
    xs, ys = [], []
    pads = geom.package_pads(ds.package)
    for pad_name, pd in pads.items():
        px, py = geom.rotate(pd.x, pd.y, p.brot)
        dx, dy, _ = geom.pad_extent(p.deviceset, pad_name, p.brot)
        xs += [x + px - dx / 2, x + px + dx / 2]
        ys += [y + py - dy / 2, y + py + dy / 2]
    return (min(xs), min(ys), max(xs), max(ys))


def _boxes_clear(a, b, gap: float) -> bool:
    return not (a[0] - gap < b[2] and b[0] - gap < a[2]
                and a[1] - gap < b[3] and b[1] - gap < a[3])


def _in_rect(box, rect) -> bool:
    return (box[0] < rect[2] and rect[0] < box[2]
            and box[1] < rect[3] and rect[1] < box[3])


def clearance_exceptions() -> list[tuple[float, float, float, float, float]]:
    """Rectangles where FINE_PITCH_CLEARANCE applies instead of the general
    rule, as (x1, y1, x2, y2, clearance)."""
    out = []
    for p in PARTS:
        h = FANOUT_ENVELOPE.get(p.deviceset)
        if h:
            out.append((p.bx - h, p.by - h, p.bx + h, p.by + h,
                        FINE_PITCH_CLEARANCE))
    return out


def resolve_placement() -> dict:
    """Nudge non-fixed parts to legal positions. Returns a move report."""
    import geom

    FANOUT_KEEPOUTS = []
    for p in PARTS:
        h = FANOUT_ENVELOPE.get(p.deviceset)
        if h:
            FANOUT_KEEPOUTS.append((p.bx - h, p.by - h, p.bx + h, p.by + h))
    keepouts = [ANTENNA_KEEPOUT] + list(ESCAPE_CHANNELS) + FANOUT_KEEPOUTS

    placed: list[tuple[str, tuple]] = []
    for p in PARTS:
        if not _is_fixed(p):
            continue
        b = _bbox(p, p.bx, p.by)
        if b:
            placed.append((p.ref, b))

    # Candidate offsets on a 0.25 mm lattice, nearest first.
    lattice = sorted(
        ((dx * 0.25, dy * 0.25)
         for dx in range(-60, 61) for dy in range(-60, 61)),
        key=lambda o: (o[0] * o[0] + o[1] * o[1], abs(o[0]), abs(o[1])),
    )

    moves: dict[str, tuple[float, float, float]] = {}
    unresolved: list[str] = []
    # Decoupling capacitors first: their distance to the pin they bypass is
    # the thing worth protecting when space gets tight.
    order = sorted((p for p in PARTS if not _is_fixed(p)),
                   key=lambda q: (0 if q.ref.startswith("C") else
                                  1 if q.ref.startswith(("R", "D")) else 2))
    for p in order:
        b0 = _bbox(p, p.bx, p.by)
        if b0 is None:
            continue
        for dx, dy in lattice:
            x, y = p.bx + dx, p.by + dy
            b = _bbox(p, x, y)
            if not (b[0] >= EDGE_CLEAR and b[1] >= EDGE_CLEAR
                    and b[2] <= BOARD_W - EDGE_CLEAR
                    and b[3] <= BOARD_H - EDGE_CLEAR):
                continue
            active = ([ANTENNA_KEEPOUT] + list(FANOUT_KEEPOUTS)
                      if p.ref in CHANNEL_EXEMPT else keepouts)
            if any(_in_rect(b, k) for k in active):
                continue
            if any(not _boxes_clear(b, ob, COURTYARD_GAP) for _, ob in placed):
                continue
            if (dx, dy) != (0.0, 0.0):
                moves[p.ref] = (x, y, (dx * dx + dy * dy) ** 0.5)
            p.bx, p.by = x, y
            placed.append((p.ref, b))
            break
        else:
            unresolved.append(p.ref)
            placed.append((p.ref, b0))
    return {"moved": moves, "unresolved": unresolved,
            "fixed": sum(1 for p in PARTS if _is_fixed(p))}


# ---------------------------------------------------------------------------
# FLOORPLAN
#
# The per-part board coordinates written above were laid out for an earlier,
# smaller outline.  Rather than restating 150 coordinates, each schematic
# sheet - which maps 1:1 onto a placement zone - is translated as a block, so
# every part keeps its position relative to the pin it serves.  Edge-mounted
# parts (connectors that need a cable to leave the board, mounting holes,
# user-operated switches) are then pinned explicitly.
# ---------------------------------------------------------------------------
SHEET_OFFSET = {
    1: (3.0, 3.0),      # Z1 power / charging
    2: (2.0, 10.0),     # Z2 ESP32 core
    3: (6.0, 5.0),      # Z4 I2C sensors
    4: (13.0, 3.0),     # Z3 ECG analog
    5: (6.0, 3.0),      # Z5 mechanical sensing
    6: (13.0, 10.0),    # Z6 alerts
    7: (6.0, 10.0),     # Z7 user input / storage
}

# Parts whose position is a mechanical decision, pinned after the block move.
# Bottom-edge connector row, left-edge programming/battery, top-edge alerts.
EDGE_PLACEMENT = {
    # --- bottom edge: every sensor / power lead leaves here ---------------
    "J2":  (12.0, 3.0, "R0"),      # USB / 5 V charge input
    "J4":  (25.0, 3.0, "R0"),      # fuel-gauge breakout
    "J8":  (38.0, 3.0, "R0"),      # load cell (JST-PH-4)
    "J15": (48.5, 3.0, "R0"),      # hall / limit switch
    "J14": (56.0, 3.0, "R0"),      # piezo (fetal movement)
    # --- FSR + stretch leads: vertical headers so they do not wall off the
    #     board the way a long horizontal row would -----------------------
    "J9":  (35.5, 10.0, "R90"),
    "J10": (35.5, 16.0, "R90"),
    "J11": (35.5, 22.0, "R90"),
    "J12": (35.5, 28.0, "R90"),
    "J13": (61.0, 10.0, "R90"),
    # --- left edge -------------------------------------------------------
    "J5":  (2.3, 30.0, "R90"),     # UART programming header
    "J1":  (2.3, 51.0, "R90"),     # Li-Po battery (JST-PH-2)
    "J3":  (2.3, 12.0, "R90"),     # external on/off switch
    # --- right edge ------------------------------------------------------
    "J7":  (97.2, 21.0, "R90"),    # ECG electrodes
    "J17": (97.2, 57.5, "R90"),    # buzzer
    # --- top edge --------------------------------------------------------
    "J16": (86.0, 67.0, "R180"),   # vibration motor
    "J18": (46.0, 67.0, "R0"),     # microSD SPI module
    "J6":  (63.0, 40.0, "R90"),    # optional second AS5600 (flying lead)
    # --- user-operated switches ------------------------------------------
    # The switch row sits clear of the module's right escape channel
    # (x 28.5-34.2) and leaves 1.5 mm below J18 on the top edge.
    "SW2": (39.0, 54.0, "R0"),     # RESET
    "SW3": (39.0, 61.5, "R0"),     # BOOT
    "SW4": (53.0, 61.5, "R0"),     # SOS
}


def apply_floorplan() -> None:
    for p in PARTS:
        dx, dy = SHEET_OFFSET.get(p.sheet, (0.0, 0.0))
        p.bx += dx
        p.by += dy
    for i, (mx, my) in enumerate(MOUNT_HOLES, start=1):
        h = PART_BY_REF.get(f"H{i}")
        if h:
            h.bx, h.by = mx, my
    for ref, (x, y, rot) in EDGE_PLACEMENT.items():
        q = PART_BY_REF[ref]
        q.bx, q.by, q.brot = x, y, rot


apply_floorplan()

PLACEMENT_REPORT = resolve_placement()
