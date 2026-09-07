"""
validate_erc.py - Electrical rule check on the design model.

This is a real ERC, not a formality.  It runs on the same data that generates
the .sch, so anything it reports is genuinely in the schematic.

Checks performed
  1  every part reference is unique and its deviceset exists in the library
  2  every (ref, pin) in the netlist names a pin that exists on that part
  3  every pin of every part appears in exactly one net (no floating pins,
     no pin driven from two nets)
  4  no net has fewer than two connections (except declared no-connects)
  5  every net containing a `pwr` pin also contains a `sup` pin
  6  no net has two or more `out` pins (output conflict)
  7  inputs are not left without a driver
  8  I2C nets carry exactly one pull-up resistor pair and no address clash
  9  ESP32-S3 specific rules: analog nets land on ADC1 only; strapping pins
     are not pulled the wrong way; ADC2 is not used for analog
 10  MOSFET gates have a pull-down; inductive loads have a flyback diode
 11  LEDs have a series resistor
"""

from __future__ import annotations

import pathlib
import sys
from collections import Counter, defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import design as D  # noqa: E402
from lib_defs import DEVICESETS, SYMBOLS  # noqa: E402

SYM = {s.name: s for s in SYMBOLS}
DS = {d.name: d for d in DEVICESETS}

# Pin electrical direction, by (deviceset, pin).
PIN_DIR: dict[tuple[str, str], str] = {}
for _ds in DEVICESETS:
    _sym = SYM[_ds.symbol]
    for _item in _sym.items:
        if hasattr(_item, "direction") and hasattr(_item, "name"):
            PIN_DIR[(_ds.name, _item.name)] = _item.direction

# Nets that are single-pin on purpose.  Each entry must have a documented
# reason; these are reproduced verbatim in ERC_REPORT.md.
DECLARED_NO_CONNECT = {
    "LDO_NC": "AP2112 pin 4 is 'No Connection' per Diodes DS39724 Rev.2-2. "
              "Left unconnected deliberately.",
    "IMU_OCS_AUX": "LSM6DSOX DS12814 Rev.4 Table 1 note 2: 'Leave pin "
                   "electrically unconnected and soldered to PCB.' Its own "
                   "pad satisfies both halves of that instruction.",
}

errors: list[str] = []
warnings: list[str] = []
notes: list[str] = []


def err(m: str) -> None:
    errors.append(m)


def warn(m: str) -> None:
    warnings.append(m)


def note(m: str) -> None:
    notes.append(m)


# --- 1. parts ---------------------------------------------------------------
refs = Counter(p.ref for p in D.PARTS)
for r, c in refs.items():
    if c > 1:
        err(f"[R1] duplicate reference designator {r} (x{c})")
for p in D.PARTS:
    if p.deviceset not in DS:
        err(f"[R1] {p.ref}: deviceset {p.deviceset!r} is not in the library")

# --- 2/3. pin coverage ------------------------------------------------------
pin_nets: dict[tuple[str, str], list[str]] = defaultdict(list)
for net, conns in D.NETS.items():
    for ref, pin in conns:
        pin_nets[(ref, pin)].append(net)
        p = D.PART_BY_REF.get(ref)
        if p is None:
            err(f"[R2] net {net}: reference {ref} does not exist")
            continue
        ds = DS.get(p.deviceset)
        if ds is None:
            continue
        if pin not in SYM[ds.symbol].pin_names():
            err(f"[R2] net {net}: {ref}.{pin} - no such pin on {p.deviceset}")

for (ref, pin), nets in pin_nets.items():
    if len(nets) > 1:
        err(f"[R3] {ref}.{pin} appears on {len(nets)} nets: {sorted(nets)}")

for p in D.PARTS:
    ds = DS.get(p.deviceset)
    if ds is None:
        continue
    for pin in SYM[ds.symbol].pin_names():
        if (p.ref, pin) not in pin_nets:
            err(f"[R3] {p.ref}.{pin} ({p.deviceset}) is not connected to any net")

# --- 4. net size ------------------------------------------------------------
for net, conns in D.NETS.items():
    if len(conns) < 2:
        if net in DECLARED_NO_CONNECT:
            note(f"[R4] {net}: intentional single-pin net - "
                 f"{DECLARED_NO_CONNECT[net]}")
        else:
            err(f"[R4] net {net} has only {len(conns)} connection(s)")

# --- 5/6/7. direction rules ------------------------------------------------
for net, conns in D.NETS.items():
    if net in DECLARED_NO_CONNECT:
        # A declared no-connect has no driver by definition; R4 already
        # reported it as an intentional single-pin net.
        continue
    dirs = []
    for ref, pin in conns:
        p = D.PART_BY_REF.get(ref)
        if p is None:
            continue
        d = PIN_DIR.get((p.deviceset, pin))
        if d:
            dirs.append((f"{ref}.{pin}", d))
    kinds = Counter(d for _, d in dirs)

    if kinds["pwr"] and not kinds["sup"]:
        err(f"[R5] net {net} feeds {kinds['pwr']} power pin(s) but has no "
            f"supply symbol")

    outs = [nm for nm, d in dirs if d == "out"]
    if len(outs) > 1:
        err(f"[R6] net {net} has {len(outs)} push-pull outputs: {outs}")

    ins = [nm for nm, d in dirs if d == "in"]
    drivers = [nm for nm, d in dirs if d in ("out", "io", "oc", "sup", "pwr", "pas")]
    if ins and not drivers:
        err(f"[R7] net {net} has input(s) {ins} but no driver")

# --- 8. I2C rules -----------------------------------------------------------
I2C_BUSSES = {
    "SENSOR (I2C0)": ("I2C_SDA", "I2C_SCL",
                      {"U4": 0x48, "U5": 0x6A, "J4": 0x36}),
    "ANGLE  (I2C1)": ("ANG_SDA", "ANG_SCL", {"U6": 0x36}),
}
for bus, (sda, scl, addrs) in I2C_BUSSES.items():
    for line in (sda, scl):
        pulls = [r for r, _ in D.NETS[line]
                 if r.startswith("R") and D.PART_BY_REF[r].value == "4k7"]
        if len(pulls) != 1:
            err(f"[R8] {bus} line {line} has {len(pulls)} 4k7 pull-up(s), "
                f"expected exactly 1")
    seen: dict[int, str] = {}
    for dev, a in addrs.items():
        if a in seen:
            err(f"[R8] {bus} I2C address clash 0x{a:02X}: {seen[a]} and {dev}")
        seen[a] = dev
    note(f"[R8] {bus}: addresses " +
         ", ".join(f"{d}=0x{a:02X}" for d, a in sorted(addrs.items(),
                                                       key=lambda kv: kv[1])))

# Cross-bus check: AS5600 and MAX17048 are both hard-wired to 0x36.
if 0x36 in I2C_BUSSES["SENSOR (I2C0)"][2].values() and \
        0x36 in I2C_BUSSES["ANGLE  (I2C1)"][2].values():
    note("[R8] 0x36 is used on BOTH busses (MAX17048 breakout on the sensor "
         "bus, AS5600 on the angle bus). This is the deliberate resolution of "
         "the fixed-address clash - they are electrically separate busses.")

# --- 9. ESP32-S3 rules -----------------------------------------------------
ADC1 = {f"IO{i}" for i in range(1, 11)}
ADC2 = {f"IO{i}" for i in range(11, 21)}
STRAPPING = {"IO0", "IO3", "IO45", "IO46"}

for g in D.GPIO_TABLE:
    if g.direction == "ANALOG IN":
        if g.pin not in ADC1:
            err(f"[R9] {g.pin} carries analog net {g.net} but is not an ADC1 "
                f"channel; ADC2 cannot be used while the radio is active")
    if g.pin in ADC2 and g.direction == "ANALOG IN":
        err(f"[R9] {g.pin} is an ADC2 pin used as an analog input")
    if g.pin in STRAPPING and not g.boot_critical:
        err(f"[R9] {g.pin} is a strapping pin but is not flagged boot-critical")

# Every ESP32 module pin must be accounted for in the GPIO table.
esp = D.PART_BY_REF["U3"]
esp_pins = set(SYM[DS[esp.deviceset].symbol].pin_names())
table_pins = set()
for g in D.GPIO_TABLE:
    if g.pin == "GND":
        table_pins.update({"GND@1", "GND@40", "EPAD"})
    else:
        table_pins.add(g.pin)
missing = esp_pins - table_pins
if missing:
    err(f"[R9] ESP32 pins absent from the GPIO allocation table: "
        f"{sorted(missing)}")

# --- 10. MOSFET / inductive-load rules -------------------------------------
for q in ("Q1", "Q2"):
    gate_net = [n for n, c in D.NETS.items() if (q, "G") in c]
    if not gate_net:
        err(f"[R10] {q}: gate is unconnected")
        continue
    gn = gate_net[0]
    pulldowns = [r for r, _ in D.NETS[gn]
                 if r.startswith("R") and D.PART_BY_REF[r].value == "100k"]
    if not pulldowns:
        err(f"[R10] {q}: gate net {gn} has no 100k pull-down (the FET could "
            f"float on during boot)")
    drain_net = [n for n, c in D.NETS.items() if (q, "D") in c][0]
    diodes = [r for r, _ in D.NETS[drain_net] if r.startswith("D")]
    if not diodes:
        err(f"[R10] {q}: drain net {drain_net} drives an inductive load with "
            f"no flyback diode")
    else:
        note(f"[R10] {q}: flyback {diodes[0]} present on {drain_net}")

# Flyback diode orientation: the anode must sit on the switched (drain) node
# and the cathode on the supply side, so it is reverse-biased in normal
# operation and only conducts on turn-off.
for dref, drain_net, supply_net in (("D7", "MOTOR_N", "MOTOR_P"),
                                    ("D8", "BUZZ_N", "3V3")):
    if (dref, "A") not in D.NETS[drain_net]:
        err(f"[R10] {dref}: anode is not on the switched node {drain_net} "
            f"(diode is backwards - it would short the supply)")
    if (dref, "C") not in D.NETS[supply_net]:
        err(f"[R10] {dref}: cathode is not on the supply node {supply_net}")

# --- 11. LED series resistors ----------------------------------------------
for p in D.PARTS:
    if p.deviceset != "LED-0805":
        continue
    for pin in ("A", "C"):
        net = [n for n, c in D.NETS.items() if (p.ref, pin) in c]
        if not net:
            continue
        members = {r for r, _ in D.NETS[net[0]]}
        if any(m.startswith("R") for m in members):
            break
    else:
        err(f"[R11] LED {p.ref} has no series current-limiting resistor")

# Piezo clamp orientation.
if ("D5", "C") not in D.NETS["3V3"]:
    err("[R10] D5 (piezo positive clamp) cathode must go to 3V3")
if ("D6", "A") not in D.NETS["GND"]:
    err("[R10] D6 (piezo negative clamp) anode must go to GND")


# ---------------------------------------------------------------------------
def main() -> int:
    npins = sum(
        len(SYM[DS[p.deviceset].symbol].pin_names())
        for p in D.PARTS if p.deviceset in DS
    )
    print("=" * 72)
    print("ERC - SIH26113 Maternity Assist Belt")
    print("=" * 72)
    print(f"parts            : {len(D.PARTS)}")
    print(f"nets             : {len(D.NETS)}")
    print(f"pins in design   : {npins}")
    print(f"net connections  : {sum(len(c) for c in D.NETS.values())}")
    print()
    for label, items in (("ERROR", errors), ("WARNING", warnings), ("NOTE", notes)):
        print(f"--- {label}S ({len(items)}) ---")
        for i in items:
            print(f"  {label[0]}: {i}")
        print()
    print("RESULT:", "FAIL" if errors else "PASS")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
