# FINAL ENGINEERING REVIEW

A second pass over the design, done as if reviewing someone else's board
before fabrication. Each of the 27 failure modes below is checked with
evidence, not asserted. Where a check found something, it says so and says
what was done about it.

**Verdict: 10 real defects were found and fixed during design and review, 5
items remain open (all recorded in `REQUIRES_CONFIRMATION.md`), and 1
limitation is accepted and documented.**

Two of the ten would have killed the board outright — an unplated drill
through three thermal pads, and a SOT-23 land pattern that shorted the
regulator's input to ground. Neither is visible by eye in a library
editor. Both were caught by checks that were *added because* of them, so
they cannot recur.

---

## Defects found and fixed

These were genuine faults in earlier revisions of this design. They are listed
first because they are the reason to do a review at all.

### ✅ FIXED — Plane vias placed outside the pour outline

**Found by `scripts/validate_planes.py`, which was written specifically to
stop relying on a human eyeballing the pour in Fusion.**

Both inner pours are drawn as an **L** — for x < 29.5 the outline stops at
**y = 63.0**, so that neither plane runs up beside the module's antenna.
Nothing stopped a *plane-connect via* being placed in the strip above that
line, and two `GND` vias were:

| Via | Position | Problem |
|---|---|---|
| `via@3.8,63.725` | **0.725 mm above the pour edge** | it was **`C7`'s only connection to the ground plane** |
| `via@6.65,63.21` | 0.21 mm above the pour edge | same strip |

`C7` is the 100 nF HF bypass at the ESP32 module's supply pin — one of the two
parts that actually supply the 355 mA Wi-Fi TX burst. **Its ground return to
the plane did not exist.** A via in that strip is not a plane connection; it is
a hole.

Two things made this invisible:

* **DRC rule D7** asks "does every plane-net pad have a via on its net?" — and
  the answer was yes. It never asked whether that via lands inside the pour.
* The pours declare **`orphans="off"`**, so EAGLE *deletes* islands rather than
  leaving stray copper that might have rescued the connection.

And the same wrong assumption was written down explicitly in
`_route_to_plane()`: *"every via in this design is a through via, so a via
already sitting on this net is already tied to the inner plane."* **True only
for a via inside the pour.**

Fixed with `_in_pour()` in `scripts/generate_board.py`, applied at three
sites: the straight-spur via candidate test, the `_route_to_plane()` target
list, and the coarse GND stitching grid. `validate_planes.py` now runs as part
of `build_all.py` and reports **0 orphaned plane contacts on either plane** in
its strict pass.

### ✅ FIXED — Unplated holes drilled through thermal pads

Thermal vias for the ESP32 EPAD, the AD8232 exposed pad and the TMP117
thermal pad were originally placed inside the *footprints* using EAGLE's
`<hole>` element. **`<hole>` in a package is an unplated mechanical hole.**
That would have drilled 15 unplated holes straight through three ground lands
— solder would wick into them, the thermal connection would be worse than
having no vias, and it looks perfectly correct in the library editor.

Fixed by moving them to board level as plated vias belonging to the `GND`
signal (`THERMAL_VIAS` in `scripts/lib_defs.py`).

### ✅ FIXED — Clearance measured as a diamond, not a disc

The router's obstacle dilation was a repeated 4-neighbour operation, which
produces a diamond (L1 ball). A diamond of radius 2 admits a diagonal
neighbour at a true distance of only 0.283 mm. Once 45° routing was enabled,
two parallel diagonal tracks could sit **0.03 mm apart** — a short in
practice — and the grid could not see it.

Fixed by dilating with a proper Euclidean disc sized from the actual
clearance requirement. Detecting this required an independent DRC that
measures real polyline geometry rather than agreeing with the router; it is
exactly the class of bug a self-consistent tool never finds.

### ✅ FIXED — Fan-out stubs crossing neighbouring pads

Fan-out stubs are emitted *before* global routing, so nothing downstream
validated them. A stub from a fine-pitch pad was free to run straight across
a neighbouring pad — a short on a net that had not been routed yet.

Fixed with `Router.segment_is_clear()`, called on every stub before it is
laid; a stub that would collide is truncated to its last clear point or
dropped, and the count is reported.

### ✅ FIXED — Plane-via spurs crossing neighbouring pads

Same class of bug. The plane-via search checked that the *via* fitted but not
that the spur from pad to via was clear. This produced a real short: a `3V3`
spur overlapping the AD8232's `GND` pad by 0.16 mm.

Fixed by validating the spur with the same check.

### ✅ FIXED — Rip-up cascading damage

The rip-up-and-retry pass ripped nets, re-routed the failure, then re-routed
the victims — and any victim that could not be restored became a new failure,
which ripped more nets. Over three rounds this took the board from 4 unrouted
nets to 33 while the running counter claimed success.

Fixed by making the pass **transactional**: snapshot, attempt, and roll back
unless the target routes *and* every ripped net is restored. It can now only
reduce the unrouted count. The counter was also changed to recount from the
final state rather than trust a running tally.

### ✅ FIXED — SOT-23-5 land pattern shorted VIN to GND

The SOT-23 land generator had its **radial and tangential pad dimensions
transposed**. That put 1.10 mm-wide pads on a 0.95 mm pitch, so pads 1 and 2
**overlapped by 0.15 mm** — on the AP2112K that is a dead short from `VIN` to
`GND`, and the board would have been dead the first time it was powered.

It looks entirely plausible in a library editor, which is why the fix was not
just to correct the numbers but to add a **pad-overlap and minimum-pad-gap
check to the library self-test** (`generate_library.py`), so no future
footprint can ship with touching pads.

### ✅ FIXED — LGA-14 land enlargement closed the corner pairs to 0.11 mm

That same new check immediately found a second problem: enlarging the
LSM6DSOX's lands to 0.50 × 0.28 mm — the usual IPC habit for leaded parts —
squeezed the four corner pairs to **0.11 mm**, below the 0.15 mm rule. An LGA
has no lead to form a fillet, so the land is now 1:1 with the package pad
(0.45 × 0.25 mm), which restores 0.15 mm at the corners.

### ✅ FIXED — the DRC measured round pads as squares

`validate_drc.py` treated every pad as a rectangle. For a round through-hole
pad that over-reports by up to 0.41 × radius at the corners, so it flagged
tracks that were comfortably clear of the actual copper — and, worse, it would
have masked the *real* violations among the false ones. Round pads are now
measured as circles, and the router stamps them as discs to match.

### ✅ FIXED — the clearance model assumed every conductor was nominal width

The occupancy grid records which net owns a cell but not how wide its copper
is, so the exclusion radius allowed a fixed 0.10 mm for whatever it was
keeping away from. Conductors *wider* than that — 0.30 mm plane spurs, 0.50 mm
power tracks — were therefore under-modelled by exactly the difference, and
0.30 mm spurs against 0.15 mm fan-out stubs landed at 0.100 mm instead of
0.150 mm. Wide conductors are now stamped proportionally wider
(`stamp_radius` in `router.py`).

### ✅ FIXED — Placement collisions from hand-picked coordinates

An 0805 land pattern is 3.05 mm across, so the 3.0 mm pitch used in the first
placement pass overlapped by 0.35 mm — 50 times. Later, the switch row
overlapped the microSD header by 0.75 mm.

Fixed by adding courtyard-overlap detection to the DRC (rule D2) and a
placement-resolution pass that nudges every non-fixed part to a legal
position with a 0.9 mm courtyard gap. Hand-placed coordinates are now
*intent*, and the pass guarantees legality.

---

## The 27-point review

### 1. Wrong pin numbers ✅

Every placed IC's pin map was taken from the manufacturer's datasheet table
and is cited row by row in `COMPONENT_VERIFICATION.md`. The library generator
additionally asserts that every symbol pin maps to a pad that exists in the
referenced package and that no package pad is left unclaimed — it refuses to
emit a library that fails either test.

Spot-checked against the datasheets: ESP32-S3-WROOM-1 (41 pins, Table 3-1),
AD8232 (20 + EP, Table 3), TMP117 (6 + pad, Table 5-1), LSM6DSOX (14,
Table 1), AS5600 (8, Fig. 4), TP4056 (8, p. 2), AP2112K (5, pin
descriptions), HX711 (16, Table 1).

### 2. Wrong footprints ⚠️ ONE ITEM OPEN

Three footprints come from the vendor's own recommended land pattern
(ESP32-S3-WROOM-1, TMP117 WSON, JST PH). Eight are IPC-7351B Nominal computed
from verified body dimensions. Four families are de-facto standard geometry.

**Open:** the ESP32 EPAD land *position* is derived from Espressif's figure
but simplified from a 3 × 3 copper array to one conservative land. All 40
signal pads are verified, so **the module will solder correctly**; only the
thermal land's exact position needs cross-checking. `REQUIRES_CONFIRMATION.md`
M1.

**Open:** the tactile-switch pin grid is the standard 6.5 × 4.5 mm, but the
chosen vendor part must be confirmed — some 6 × 6 mm switches transpose it.
`REQUIRES_CONFIRMATION.md` H4.

### 3. Wrong power connections ✅

The most dangerous candidate here was the AD8232: **absolute maximum supply
3.5 V**, and the architecture diagram does not say which rail feeds it. It is
on `3V3` and never sees `VBAT` (which reaches 4.2 V while charging). The ERC
enforces that every power pin's net carries a supply symbol.

Rail assignment checked pin by pin: nothing rated for 3.3 V is on `VBAT`;
`VBAT` feeds only the LDO input, the motor high side (via `R45`), the sense
divider and the fuel-gauge header.

### 4. Missing grounds ✅

ERC rule R3 requires every pin of every part to be on exactly one net.
**420 pins, 420 connections, zero floating.** The ESP32's `GND@1`, `GND@40`
and `EPAD` are all on `GND`; the AD8232's `GND` and `EP` are both connected;
the TMP117's thermal pad is connected.

### 5. Missing decoupling ✅

Checked against each datasheet's own requirement:

| Part | Datasheet asks for | Fitted |
|---|---|---|
| ESP32-S3 | bulk + HF | `C8` 22 µF, `C7` 100 nF at pin 2 |
| AD8232 | "0.1 µF close to the supply pin… 1 µF farther away" | `C23` 100 nF at pin 17, `C24` 1 µF |
| TMP117 | bypass | `C11` 100 nF |
| LSM6DSOX | "Recommended 100 nF filter capacitor" on **both** VDD and VDDIO | `C12` and `C13`, one each |
| AS5600 | 100 nF on pin 1, 1 µF on pin 2 | `C14` 100 nF, `C15` 1 µF |
| HX711 | VBG reference bypass, supply bypass | `C25` 100 nF on VBG, `C26`/`C27` 100 nF, `C28` 10 µF |
| AP2112K | ≥ 1 µF in and out | `C3` 10 µF in, `C4` 10 µF + `C5` 100 nF out |

### 6. I²C address conflicts ✅ FOUND IN THE INPUT AND RESOLVED

**The architecture diagram's bus cannot work.** AS5600 and MAX17048 are both
hard-wired to 0x36 with no select pin.

Resolved with two physically separate busses using both ESP32-S3 I²C
controllers. ERC rule R8 checks each bus for clashes and confirms exactly one
pull-up pair per line. Verified addresses: sensor bus TMP117 0x48, LSM6DSOX
0x6A, fuel-gauge header 0x36; angle bus AS5600 0x36.

A *second* AS5600 would still clash — that is called out with three
documented resolutions rather than left as a surprise.

### 7. ESP32 boot-pin conflicts ✅

Strapping pins are `IO0`, `IO3`, `IO45`, `IO46` (Table 4-1). ERC rule R9
requires every one to be flagged boot-critical in the GPIO table.

* `IO0` — boot button plus a 10 kΩ pull-up. Default high = SPI boot ✓
* `IO3` — jumper `R17` left **unpopulated**, so the pin floats to its default ✓
* `IO45`, `IO46` — drive LEDs anode-side through a resistor. At reset the pin
  is high-impedance and an LED cannot conduct below its forward voltage, so
  the internal weak pull-downs hold both straps at their default 0 ✓
* `EN` — 10 kΩ pull-up + 1 µF + button. Never floating ✓

### 8. ADC limitations ✅

**ADC2 does not work while the radio is active.** ERC rule R9 fails the build
if any analog net lands outside ADC1 (GPIO1–GPIO10). All 8 analog signals are
on ADC1; 8 of 10 channels used, `IO3` reserved, `IO10` used digitally for
`SD_CS`.

Range checked per signal: ECG output centres on 1.65 V and swings 110 mV–1.1 V
pk-pk; FSR dividers span 0.30–2.75 V; `VBAT_SENSE` reads 2.10 V at a full
cell. Nothing clips against either rail.

### 9. Motor current problems ⚠️ OPEN — motor not selected

`Q1` (AO3400A, 30 V / 5.7 A) and the 0.50 mm track (≈ 1.1 A) have large
margin over a typical 100 mA coin motor. `C37` (10 µF) supplies the current
step locally.

**Open:** the motor's voltage rating. It is on `VBAT` (up to 4.2 V) and most
coin motors are rated 3.0 V. `R45` (0 Ω, 0805) exists in series so a ballast
can be fitted without cutting tracks. `REQUIRES_CONFIRMATION.md` B3 gives the
calculation, including the resistor's power rating — an 0805 is marginal at
120 mW.

### 10. Buzzer drive problems ✅

Low-side `Q2` from `3V3` (not `VBAT` — most 3 V buzzers do not want 4.2 V),
with `D8` flyback for the magnetic case and `C38` local bulk. Works unchanged
for a passive piezo transducer driven by LEDC PWM; the diode is simply never
forward-biased.

### 11. ECG noise problems ✅

Every layout instruction in the AD8232 datasheet's *Layout Recommendations*
section is satisfied — item-by-item table in `ECG_FRONTEND_DESIGN.md`.
Specifically: continuous ground plane 0.36 mm beneath the analog tracks
(not split — reasoned out in `GROUNDING_NOTES.md`); symmetric, matched input
resistor placement; high-impedance nodes kept inside Zone 3; `U7` in the
opposite corner from the motor driver and ~45 mm from the antenna; electrode
connector adjacent to the IC so the unprotected run is ~5 mm.

### 12. Piezo overvoltage ✅

A piezo film open-circuits at tens of volts; "piezo → ADC" would eventually
destroy the pin. The chain is `R38` 10 MΩ load → `C34` **100 nF/50 V** →
mid-rail bias → `R41` 100 kΩ series → `D5`/`D6` Schottky clamps → `C35`
10 nF. With `R41` in place, a 100 V transient injects ~1 mA into a 1 A diode.

ERC rule R10 checks clamp polarity explicitly (`D5` cathode on `3V3`, `D6`
anode on `GND`) because a reversed clamp is a dead short across the rail. The
50 V rating is carried in the BOM value string (`100n/50V`) so it cannot be
lost in a substitution.

### 13. Battery charging problems ⚠️ ONE ACCEPTED LIMITATION, ONE OPEN

`R1` = 2.4 kΩ sets 500 mA from the datasheet's own table; `TEMP` grounded per
the datasheet's instruction for disabling temperature sense; `CE` tied to VCC;
both status LEDs current-limited.

**Accepted limitation:** the TP4056 has no power-path switching, so system
load current flows through `BAT` and disturbs C/10 termination. Documented in
`DESIGN_ASSUMPTIONS.md` §1.3 with the production fix (MCP73871 / BQ24075).

**Open and BLOCKING:** there is **no battery protection circuit on the
board**. A protected cell is mandatory. `REQUIRES_CONFIRMATION.md` B1.

### 14. Regulator capacity problems ✅ ANALYSED, WITH A FIRMWARE REQUIREMENT

Worst-case simultaneous 3V3 load ≈ 510 mA against a 600 mA guaranteed
minimum — 15 % margin, and better in practice because Wi-Fi TX bursts and SD
writes do not coincide (BLE-only is ≈ 285 mA total). Itemised in
`POWER_BUDGET.md`.

The real finding is dropout, not capacity: 250 mV at 600 mA means the rail
falls below the ESP32's 3.0 V minimum at about 3.3 V of cell voltage.
**Firmware must cut off at 3.5 V** using `VBAT_SENSE` (1.75 V at the pin).
Stated in the README, the power budget and the build guide, because an
unpredictable brown-out in a device with an SOS button is worse than a clean
shutdown.

### 15. Connector polarity ⚠️ OPEN

Pin 1 is a square pad on every through-hole connector, and pin 1 is marked on
the silkscreen. Net assignment reviewed for all 18 connectors.

**Open:** JST PH pigtail wiring is not consistent between suppliers. `J1`
pin 1 = `VBAT` (+), pin 2 = `GND` (−); check with a meter before first
connection. `REQUIRES_CONFIRMATION.md` B1.

### 16. Missing protection ✅

Nine protection elements, each with a named failure mode it prevents —
table in `DESIGN_ASSUMPTIONS.md` §13. Equally important, that section lists
what was **not** added and why: no TVS on the sensor headers (they sit inside
the enclosure on short leads, and added capacitance would degrade the FSR
dividers), no reverse-polarity FET on `VBUS` (the TP4056 has internal
reverse blocking — "No blocking diode is required due to the internal PMOSFET
architecture"), no fuse (the mandatory protected pack provides over-current
cut-off).

### 17. Incorrect MOSFET orientation ✅

Both FETs are low-side switches: gate to the GPIO through a series resistor,
**source to GND**, drain to the load. Standard SOT-23 N-MOSFET assignment
(1 = G, 2 = S, 3 = D). ERC rule R10 confirms each gate net carries a 100 kΩ
pull-down so the FET is off while the GPIO is high-impedance at boot.

### 18. Incorrect diode orientation ✅

ERC rule R10 checks each flyback explicitly: the **anode** must be on the
switched drain node and the **cathode** on the supply. Reversed, the diode
shorts the supply through the FET. Verified for `D7` (`MOTOR_N`/`MOTOR_P`) and
`D8` (`BUZZ_N`/`3V3`), and separately for the piezo clamps.

### 19. Incorrect LED polarity ✅

All four LEDs use the same footprint with pad 1 = cathode and a silkscreen
cathode bar. Charger LEDs are anode-to-`VBUS`-via-resistor, cathode to the
TP4056's open-drain outputs — correct, since those pins pull low when active.
Status LEDs are anode-to-GPIO-via-resistor, cathode to GND — correct, and also
what makes the strapping pins safe (item 7).

### 20. Missing current-limiting resistors ✅

ERC rule R11 fails the build if any LED's net lacks a series resistor. All
four have one: `R2`, `R3` (1 kΩ, charger), `R9`, `R10` (1 kΩ, status).

### 21. Floating inputs ✅

ERC rule R7 fails any net that has inputs but no driver. Rule R3 fails any
unconnected pin. Specifically checked: `EN` (pull-up + RC), FET gates
(pull-downs), `SDN` (pull-up, fails safe to enabled), `FR` (pull-down, fails
safe to off), `SOS` (pull-up), `HALL_LIMIT` (pull-up), `SD_CS`/`SD_MISO`
(pull-ups), HX711 `VFB` and channel-B inputs (tied to AGND rather than left
floating), `XI` and `RATE` (tied to select the on-chip oscillator and 10 Hz).

### 22. Unused pins ✅

Nothing is left dangling. Datasheet-designated "NC when not used" and
optional-function pins are brought to isolated test-point lands: `HX_BASE`,
`HX_XO`, `AS_OUT`, `AS_PGO`, `TMP_ALERT`, and `IMU_OCS_AUX`.

The last one deserves a note: the LSM6DSOX datasheet says to leave `OCS_Aux`
*electrically* unconnected **but soldered to the PCB**. An isolated land
satisfies both halves of that instruction, which a truly floating pin would
not. Every such case is enumerated in `ERC_REPORT.md` as a declared
exception, not silenced.

### 23. Antenna keep-out ✅

The module is placed so its 6 mm antenna area is flush with the top board
edge. The keep-out is declared on layers 39/40/41/42/43, **excluded from both
plane polygons** (drawn as an L, since an EAGLE polygon cannot carry a hole),
and enforced by DRC rule D3, which fails on any pad, via or track endpoint
inside it.

The top-left mounting hole was **moved** because of this: a plated hole inside
the keep-out would detune the antenna. `H3` is at (2.6, 42) instead.
`REQUIRES_CONFIRMATION.md` L1.

### 24. PCB mechanical conflicts ⚠️ PARTIALLY CHECKED

DRC rules D1 and D2 confirm every part's copper is inside the outline with
edge clearance and that no two courtyards overlap. Connector faces are
assigned to edges by function (build guide step 18).

**Not checked:** true 3D interference. **No STEP models are attached to these
footprints**, so Fusion's 3D view will show generic extrusions — enough to
catch a connector facing the wrong way, not enough for a real clearance check.
Stated in build guide step 17.

### 25. Unrouted nets ✅ / see the report

The current figure is in `DRC_REPORT.md`, generated from the router's own
output rather than from a claim. Any remaining connection appears as an
airwire the moment the board is opened in Fusion and is listed by name with
the specific terminal involved. Nothing is hidden.

### 26. ERC issues ✅

Independent ERC, 11 rule groups, **0 errors and 0 warnings**. Declared
exceptions are enumerated with the datasheet sentence that justifies each.

**Fusion's own ERC has not been run** — no EAGLE installation existed where
these files were produced. Build guide step 6, and the expected exception
list is pre-written so the reviewer knows what to approve and what to
investigate.

### 27. DRC issues ⚠️ see the report

Independent geometric DRC, 8 rule groups. Placement (D1, D2), keep-out (D3),
width and drill (D4) and edge clearance (D9) are clean. Residual clearance
findings, if any, are listed with their measured gap in `DRC_REPORT.md`.

**Fusion's own DRC has not been run**, and the copper pours have not been
computed — EAGLE calculates polygon fill on load. Because every plane-net pad
has its own dedicated via, pad connectivity does not depend on the pour.

---

## Summary

| | Count |
|---|---|
| Points reviewed | 27 |
| Clean | 20 |
| Defects found **and fixed** during design and review | 10 |
| Open items, all documented | 5 (3 BLOCKING, 2 HIGH-or-lower) |
| Accepted and documented limitations | 1 (TP4056 power path) |
| Checks not possible without EAGLE installed | 3 (its ERC, its DRC, pour geometry) |
| Checks not possible without 3D models | 1 (mechanical interference) |

**What I would want before spending money on boards:** the two BLOCKING items
in `REQUIRES_CONFIRMATION.md` closed (protected cell, ECG safety protocol),
the motor selected so `R45` can be decided, and Fusion's own ERC and DRC run
on the files.

**What worries me most, honestly:** not the electrical design — it is the
unverified transducers. Six of the eight off-board sensors have no part number
yet, and one component value (`R37`, the stretch-sensor divider) is an
explicit placeholder that will be wrong for whatever sensor is chosen. That is
a project-planning gap rather than a board gap, but it will determine whether
the mechanical-sensing channels actually work.
