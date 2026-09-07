# PCB BUILD GUIDE — SIH26113 Maternity Assist Belt

How to open these files in Autodesk Fusion (Electronics), check them, finish
the last few connections and get boards made.

Written for someone who has used a PCB tool once or twice. If you have never
opened an EDA tool at all, work through steps 1–7 first and stop — that is
enough to confirm the design is sound before you commit to anything.

**Before you start, read `REQUIRES_CONFIRMATION.md`.** Three items there are
marked BLOCKING; one of them is a fire risk.

---

## What you already have, and what is left

| | State |
|---|---|
| Component library (`.lbr`) | Complete. 23 footprints, 28 symbols, 30 devices, all pinouts verified against datasheets |
| Schematic (`.sch`) | Complete. 7 sheets, 167 parts, 84 nets, every pin connected |
| Board (`.brd`) | Placed and routed. 4 layers, both planes poured, exposed pads via-stitched. The exact routed / airwire count is in `DRC_REPORT.md` - it is generated from the router's own output, not asserted here |
| **Left to do** | Finish a handful of airwires (step 13), run Fusion's own ERC and DRC (steps 6 and 15), generate manufacturing files (step 19) |

The exact number of remaining airwires is in `DRC_REPORT.md`, and Fusion will
show them the moment you open the board.

---

## STEP 1 — Install and open Autodesk Fusion

**Do:** install Fusion (the free personal-use licence includes Electronics).
Open it, then `File ▸ New Electronics Design`.

**Check:** the Electronics workspace opens with `Schematic` and `PCB` tabs.

**What goes wrong:** older standalone EAGLE 7.x cannot read these files — they
use the EAGLE 9 XML format. EAGLE 9.x, Fusion Electronics, and any current
Fusion all read them. If Fusion offers "Migrate EAGLE project", say yes.

---

## STEP 2 — Import the library

**Do:** in Fusion, `Library ▸ Open Library Manager ▸ Import ▸`
`libraries/SIH26113_Maternity_Assist_Belt.lbr`, and mark it **In Use**.

Or, in EAGLE 9.x, drop the `.lbr` into your `lbr/` folder and enable it in the
Control Panel.

**Check:** the library appears with 30 devices.

**What goes wrong:** if the schematic later shows "device not found", the
library was not marked In Use. The `.sch` and `.brd` also carry a full
embedded copy of the library, so they open correctly even without this step —
importing it separately is only needed if you want to place *new* parts.

---

## STEP 3 — Verify the library symbols and footprints

Do not skip this. It is where a wrong pin number is cheapest to find.

**Do:** open the library and spot-check the four parts where a mistake would
be expensive:

| Device | Check | Against |
|---|---|---|
| `ESP32-S3-WROOM-1` | 41 pads. Pin 1 is the square pad at the antenna end, 7.49 mm below the module's top edge. Pads 1.5 × 0.9 mm on a 1.27 mm pitch, columns 17.5 mm apart | Espressif datasheet v1.8, Fig. 11-1 |
| `AD8232` | 20 pads + `EP`. Pin 1 = `HPDRIVE`, pin 17 = `+VS`, pin 20 = `HPSENSE`. Numbering runs counter-clockwise from top-left | AD8232 Rev. A, Table 3 |
| `LSM6DSOX` | 14 pads. **Pin 1 is at the top-RIGHT** — the datasheet shows a bottom view, and a footprint is drawn top-down, so it is mirrored | LSM6DSOX DS12814 Rev. 4, Fig. 4 |
| `TMP117` | 6 pads + thermal pad 7. Lands 0.45 × 0.30 mm, rows 1.95 mm apart | TMP117 SNOSD82D, p. 41 |

**Check:** in the library editor, hover a pad — the tooltip gives its name.
Compare against the datasheet page cited in `COMPONENT_VERIFICATION.md`.

**What goes wrong:** the LSM6DSOX mirror is the classic error. If pin 1 ends
up top-left instead of top-right, the part is soldered on backwards and
nothing on the I²C bus responds.

---

## STEP 4 — Open the schematic

> **Open it from `fusion_project/`, not from `schematic/`.** EAGLE and Fusion
> pair a schematic with a board **by filename and directory** - opening
> `foo.brd` makes the tool look for `foo.sch` beside it, and no link is stored
> inside either file. This project keeps them in `schematic/` and `pcb/`, so
> opening either from its own folder loads it *standalone*: the
> schematic/board consistency check cannot run and forward annotation is off.
> `python scripts/make_fusion_project.py` (the last step of `build_all.py`)
> gathers the `.lbr`, `.sch` and `.brd` into **`fusion_project/`** with a
> shared base name. Open that.

**Do:** `File ▸ Open ▸ fusion_project/SIH26113_Maternity_Assist_Belt.sch`.

**Check:**

* seven sheets in the sheet list, titled POWER / ESP32-S3 CORE / I2C SENSORS /
  ECG ANALOG / MECHANICAL SENSING / ALERTS / USER INPUT;
* every part shows a reference designator and a value;
* every pin has a short stub with a green net label on it.

**Why it looks like that.** Connections are made by **named net labels on
short stubs**, not by long drawn wires. EAGLE merges same-named nets within
and across sheets, so this is a complete netlist — it is how dense production
multi-sheet schematics are usually drawn. To trace a net, click a label and
EAGLE highlights every occurrence.

**What goes wrong:** if you see red "unconnected pin" crosses, the library did
not load. Re-do step 2.

---

## STEP 5 — Confirm footprint assignment

**Do:** `Tools ▸ Statistics`, or click any part and read its Device field.

**Check:** every part has a package (they were emitted with one), and the
count matches `documentation/PROJECT_STATISTICS.md`.

**What goes wrong:** nothing should, here — the generator refuses to emit a
part without a footprint. If a part shows no package, the library version is
mismatched.

---

## STEP 6 — Run Fusion's ERC

**Do:** in the schematic, `Tools ▸ ERC`.

**Check:** compare Fusion's list against `documentation/ERC_REPORT.md`.

An independent ERC has already been run (`scripts/validate_erc.py`, 11 rule
groups, **0 errors**), but **Fusion's own ERC has never been run on these
files — no EAGLE installation existed where they were produced.** This step is
where that gets done.

**What to expect.** Fusion will probably report these, and each is
intentional — the reasoning is in `ERC_REPORT.md`:

| Fusion will say | Why it is fine |
|---|---|
| `LDO_NC` has only one pin | AP2112 pin 4 is documented "No Connection" |
| `IMU_OCS_AUX` connects only to a test point | LSM6DSOX datasheet: leave OCS_Aux electrically unconnected but soldered. An isolated land does exactly that |
| `TMP_ALERT`, `AS_OUT`, `AS_PGO`, `HX_BASE`, `HX_XO` go to test points | All are datasheet "NC when not used" or optional-function pins |
| Possibly: no supply for some net | Each rail has a `SUPPLY-*` symbol per sheet; approve if it names one of `GND`, `3V3`, `VBAT`, `VBUS` |

**Approve** those in Fusion's ERC dialog so they stop reappearing.
**Anything else is a real finding — investigate it, do not approve it.**

---

## STEP 7 — Fix ERC errors

**Do:** for each error Fusion reports that is *not* in the table above, click
it to jump to the location and fix it.

**Check:** re-run ERC until only the approved exceptions remain.

**What goes wrong:** the temptation is to approve everything. Don't. An
approved "output conflict" is two drivers fighting, and it will destroy a pin.

---

## STEP 8 — Open the board

**Do:** with the schematic open, switch to the `PCB` tab, or open
`fusion_project/SIH26113_Maternity_Assist_Belt.brd` directly - again from
`fusion_project/`, so Fusion sees the matching pair (step 4).

**Check:**

* board outline 100 × 70 mm;
* 150 components placed inside it, none overlapping;
* an orange hatched rectangle in the top-left — the antenna keep-out;
* dashed blue rectangles labelled Z1–Z7 — the placement zones (documentation
  only, layer 48);
* some yellow airwires. Those are the unrouted connections; step 13 deals with
  them.

**Do this immediately:** `Tools ▸ Ratsnest` (or type `RATSNEST`). Nothing looks
right until you do — this is what makes Fusion compute the copper pours.

**What goes wrong:** if the board opens with *every* connection as an airwire,
the schematic and board have lost their link. Close both, open the `.sch`
first, then switch to the PCB tab.

---

## STEP 9 — Verify the board outline and stack-up

**Do:** check the outline on layer 20 (Dimension), then `Tools ▸ DRC ▸ Layers`
and confirm the setup is `(1*2*15*16)`.

**Check:**

| Layer | Should contain |
|---|---|
| 1 `Top` | tracks, all pads, all components |
| 2 `Route2` | one big **GND** polygon |
| 15 `Route15` | one big **3V3** polygon |
| 16 `Bottom` | tracks only, no components |

Both plane polygons are drawn as an **L** that omits the top-left corner. That
is intentional: Espressif require no copper — planes included — beneath the
module antenna, and an EAGLE polygon cannot carry a hole.

**What goes wrong:** if Fusion reports a 2-layer setup, the design rules did
not load. `Tools ▸ DRC ▸ Load` and pick the rules embedded in the board, or set
layer setup to `(1*2*15*16)` by hand.

---

## STEP 10 — Review the placement

Placement is done, but it is worth understanding before you move anything.

**Do:** look at each zone and read it against `renders/pcb_assembly.png`.

| Zone | Where | Contents |
|---|---|---|
| Z1 | bottom-left | charger `U1`, LDO `U2`, battery `J1`, USB/5 V `J2`, fuel-gauge header `J4` |
| Z2 | left, top | ESP32-S3 module `U3`, decoupling in the strip to its left, UART header `J5` |
| Z5 | bottom-centre | HX711 `U8`, load cell `J8`, FSR headers `J9`–`J12`, piezo and hall conditioning |
| Z4 | centre | TMP117 `U4`, LSM6DSOX `U5`, AS5600 `U6`, both I²C pull-up pairs |
| Z7 | top-centre | SOS `SW4`, RESET `SW2`, BOOT `SW3`, microSD header `J18`, status LEDs |
| Z3 | right, bottom | **AD8232 `U7` and its 25 passives** — the whole ECG chain |
| Z6 | right, top | motor FET `Q1`, buzzer FET `Q2`, their connectors |

**Three placement rules you must not break if you rearrange anything:**

1. **The module antenna stays flush with the top board edge**, with no copper
   beneath it. Moving `U3` down into the board detunes the radio.
2. **Nothing goes in the escape channels** — the reserved bands either side of
   and below the module's pad rows. 36 signals leave a 1.27 mm pitch through
   them; fill a channel and the board becomes unroutable.
3. **Keep ECG away from the motor driver and the antenna.** `U7` is in the
   opposite corner from both for a reason.

**Check:** run `scripts/validate_drc.py` after any change — rule D2 finds
courtyard overlaps that are easy to create and hard to see.

---

## STEP 11 — Route the critical analog signals

Already done, but check the result rather than trusting it.

**Do:** in Fusion, hide every layer except 1, 2 and 17. Look at the ECG block.

**Check:**

* the electrode signals from `J7` reach `R18`/`R19` in a few millimetres —
  that is the unprotected high-impedance part of the path and it must be
  short;
* `R18`/`R19` are positioned symmetrically with respect to `+IN` and `−IN`.
  The datasheet asks for length-matched, symmetric input traces to hold CMRR;
* the high-impedance nodes — `ECG_HPSENSE`, `ECG_IAOUT`, `ECG_SW`,
  `ECG_REFIN`, `ECG_REFOUT` — are short. These are 10 MΩ nodes; every extra
  millimetre picks up noise;
* ECG tracks are on **layer 1**, directly above the layer-2 GND plane.
  `DRC_REPORT.md` lists any that had to use layer 16 instead.

**What goes wrong:** if you re-route these, do not put a via in the middle of
a 10 MΩ node — the via's extra surface area is a leakage and pickup path.

---

## STEP 12 — Route power

Already done. `3V3` and `GND` are planes and need no routing at all;
`VBUS`, `VBAT` and the motor path are 0.50 mm tracks.

**Check:**

* trace widths: `VBUS`/`VBAT`/motor at 0.50 mm (≈ 1.45 A at 10 °C rise, 1 oz
  copper, IPC-2221), signals at 0.20 mm (≈ 0.74 A) — see `POWER_BUDGET.md`;
* the motor's current loop is small: `C37` → `J16` → motor → `Q1` → plane;
* every plane-net pad has its own via to its plane. Click a `GND` pad and
  confirm a via sits within about 0.8 mm.

**What goes wrong:** if you widen a power track, re-run DRC. 0.50 mm tracks in
0.9 mm gaps between passives have little room to grow.

---

## STEP 13 — Finish the remaining airwires

**This is the main job left.**

**Do:** `View ▸ Show/Hide layers`, turn on `Unrouted` (layer 19). Each yellow
line is a connection to complete. Use the interactive router (`ROUTE`, or the
Route tool), pick the net-class width Fusion offers, and draw it.

The list is in `DRC_REPORT.md` with the specific terminal that could not be
reached. All of them are at the four most congested spots on the board: the
ESP32 module (36 signals escaping a 1.27 mm pitch), the AD8232 (0.5 mm QFN),
the LSM6DSOX (0.5 mm LGA) and the HX711 (whose 9 plane pads each take a via
beside the pad).

**Practical hints:**

* Every pad already has a **fan-out stub** — a short escape track ending in
  open space. Start from the end of the stub, not from the pad.
* Use the **bottom layer** freely. It is much emptier than the top, and both
  signal layers sit against a plane, so neither is electrically worse.
* Place a via right at the stub end and continue on layer 16. The stubs are
  **staggered** — alternate ones are longer — specifically so each has room
  for its own via.
* Set the grid to 0.05 mm and enable 45° routing. Fusion's default 90° mode
  wastes space.

**Check:** the `Unrouted` layer is empty, and `Tools ▸ DRC` reports no
"Unrouted" items.

**Rough effort:** each remaining net is a short connection with both ends
already fanned out. Half an hour of interactive routing should clear them.

---

## STEP 14 — Verify the ground plane

**Do:** type `RATSNEST` again after any routing change — Fusion recomputes
pours on demand, not automatically.

**Check:**

* layer 2 is a continuous `GND` pour with no large islands cut off by via
  clusters;
* layer 15 is a continuous `3V3` pour;
* both stop short of the antenna keep-out;
* under the ECG block, layer 2 is **unbroken**. This is the single most
  important electrical property of the board.

**What goes wrong:** a dense row of vias can pinch a plane into two regions.
Fusion shows the result after `RATSNEST` — look for a thin neck, and if you
find one under the analog section, move a via.

---

## STEP 15 — Run Fusion's DRC

**Do:** `Tools ▸ DRC`. The board carries its own rule set
(`SIH26113_4layer`):

| Rule | Value |
|---|---|
| Minimum clearance, all combinations | 0.20 mm |
| Minimum track width | 0.15 mm |
| Minimum drill | 0.30 mm |
| Copper to board edge | 0.40 mm |
| Annular ring | 0.25 × drill, 0.15–0.50 mm |

**Check:** compare against `documentation/DRC_REPORT.md`, which lists what the
independent geometric check found.

**Again, plainly: Fusion's DRC has never been run on these files.** No EAGLE
installation existed where they were produced. `scripts/validate_drc.py`
measures real geometry independently — segment-to-segment distances,
segment-to-pad distances, pad bounding boxes, drill sizes, keep-out
containment — but it is not the same program.

**What to expect:** "Unrouted" items until step 13 is finished. Anything else
needs investigating.

---

## STEP 16 — Fix DRC errors

**Do:** work the list. Clearance violations usually mean nudging one track;
"copper near dimension" means a track wandered toward the edge.

**Check:** DRC clean except for anything you have consciously approved.

**What goes wrong:** approving a clearance error because it is "only slightly
under". 0.15 mm instead of 0.20 mm is often fine and often not — it depends on
the fab. Ask them, or fix it.

---

## STEP 17 — Inspect in 3D

**Do:** in Fusion, `PCB ▸ 3D PCB` (or push the board to a 3D document).

**Check:** components sit where you expect; connectors face outward; the
module is at the board edge.

**Limitation, stated plainly:** **no 3D models are attached to these
footprints.** The library carries footprints and 2D package outlines (layer
51, `tDocu`) but no STEP geometry. Fusion will show generic extrusions from
the silkscreen, which is enough to catch a connector facing the wrong way but
**not** enough for a real interference check.

If you need a proper mechanical check, download STEP models — Espressif
publish one for the WROOM-1, and Fusion's own library has SOIC/SOT/0805
models — and attach them per footprint.

---

## STEP 18 — Check mechanical clearances

**Do:** measure against the enclosure design.

**Check:**

| Item | Value |
|---|---|
| Board | 100 × 70 mm, 1.6 mm FR-4 |
| Tallest part | ESP32-S3-WROOM-1 at 3.1 mm, plus THT connector bodies (~6 mm for the 2.54 mm headers with housings) |
| Mounting holes | M2, at (3, 3), (97, 3), **(2.6, 42)** and (97, 67) |
| Antenna | flush with the top edge, x 9–29 mm — **keep 10 mm clear of metal, battery and wiring** |
| Connector faces | bottom edge: sensors and power. Left edge: battery, UART, on/off. Right edge: ECG electrodes, buzzer. Top edge: motor, microSD |
| Buttons | `SW4` SOS at (52, 63.5) needs a plunger through the enclosure |

**Note `H3` is at (2.6, 42), not the top-left corner** — that corner is inside
the antenna keep-out and a plated hole there would detune the radio. See
`REQUIRES_CONFIRMATION.md` L1.

**What goes wrong:** the battery. A Li-Po pack placed against the antenna will
kill the radio range. Keep it below the board or at the opposite end.

---

## STEP 19 — Generate manufacturing outputs

**Do:** `Manufacturing ▸ CAM Processor`, pick a 4-layer Gerber X2 job (or your
fab's own job file), and generate.

**Check** you get:

| File | Content |
|---|---|
| `*.GTL` / `*.GBL` | top and bottom copper |
| `*.G2L` / `*.G15` (or `.GP1`/`.GP2`) | the two inner planes |
| `*.GTS` / `*.GBS` | solder mask |
| `*.GTO` / `*.GBO` | silkscreen |
| `*.GML` / `*.GKO` | board outline |
| `*.TXT` / `*.DRL` | drill file |
| `*.GTP` | top solder paste — **needed for the stencil** |

**You need a stencil.** Three parts cannot be soldered with an iron: the
AD8232 (0.5 mm QFN with a 2.5 mm exposed pad), the LSM6DSOX (0.5 mm LGA) and
the TMP117 (0.65 mm WSON with a thermal pad). Order the stencil with the
boards.

Specify to the fab:

* 4 layers, 1.6 mm FR-4, 1 oz outer copper;
* minimum track **0.15 mm**; minimum gap **0.127 mm (5 mil)** - the
  measured minimum copper clearance anywhere on the board is
  **0.130 mm**, so a 6 mil (0.152 mm) process will not make this board.
  5 mil is a standard but often non-default option - see
  `REQUIRES_CONFIRMATION.md` H6;
* minimum drill **0.30 mm**;
* HASL or ENIG (ENIG is better for the fine-pitch parts);
* stack-up `(1*2*15*16)` — tell them layers 2 and 15 are **planes**.

**No Gerbers are included in this project.** They need EAGLE's CAM processor,
which was not available. `DRC_REPORT.md` records that as NOT GENERATED.

---

## STEP 20 — Final review before you spend money

Go through `documentation/FINAL_REVIEW.md` — it is a second-pass review of
this design against 27 specific failure modes, with the evidence for each.

Then, specifically:

- [ ] `REQUIRES_CONFIRMATION.md`: all three BLOCKING items resolved
- [ ] The Li-Po cell at `J1` **has integrated protection** (B1)
- [ ] `J1` polarity checked with a meter against the actual pigtail (B1)
- [ ] Motor voltage rating checked, `R45` value decided (B3)
- [ ] Module ordered is **`-N8R2`**, not N8R8 or N16R8 (H5)
- [ ] Tactile switch pin grid confirmed as 6.5 × 4.5 mm (H4)
- [ ] `R37` set for the actual stretch sensor, or accepted as a placeholder (H2)
- [ ] Fusion ERC run, exceptions approved and understood (step 6)
- [ ] Fusion DRC clean (step 15)
- [ ] `Unrouted` layer empty (step 13)
- [ ] Gerbers + drill + **paste** generated and viewed in a Gerber viewer
- [ ] Stencil ordered
- [ ] Fab confirmed they can do **0.127 mm (5 mil) gap**, 0.15 mm track and
      0.30 mm drill on 4 layers (H6 - the measured minimum clearance is
      0.130 mm, so a 6 mil default will fail)

---

## Bring-up order, once the boards arrive

Do not populate everything and apply power. In this order:

1. **Power only** — `U1`, `U2`, `R1`–`R6`, `C1`–`C6`, `D1`, `D2`, `J1`, `J2`,
   `J3`. Apply 5 V to `J2`. Measure `TP2` (`3V3`) = 3.3 V ±1.5 %, `TP1`
   (`VBAT`), `TP4` (`VBUS`). Check `D1` lights with a battery connected.
   **Do not proceed until 3V3 is correct** — every other part is on that rail.
2. **Module** — `U3`, `C7`, `C8`, `R7`, `C10`, `SW2`, `SW3`, `R8`, `J5`.
   Connect USB to `J2` and confirm the ESP32-S3 appears as a serial device.
   Flash something trivial. Confirm `D3`/`D4` blink from `IO45`/`IO46`.
3. **I²C sensors** — `U4`, `U5`, `U6` and their passives. Run an I²C scan on
   both busses. Expect **0x48 and 0x6A on the sensor bus**, **0x36 on the
   angle bus**. If a device is missing, check its orientation first — the
   LSM6DSOX is the usual suspect (step 3).
4. **Mechanical sensing** — `U8` and the FSR/stretch/piezo/hall front ends.
   Verify HX711 readings change when you press the load cell.
5. **Alerts** — `Q1`, `Q2` and their networks. Test with short pulses first;
   confirm the FETs are off at boot before connecting the motor.
6. **ECG last.** Populate `U7` and its 25 passives. Before touching a person:
   check `TP11` (`ECG_REFOUT`) sits at ~1.65 V, wait 2.5 s after power-up for
   the reference to settle, then look at `TP10` (`ECG_OUT`) on a scope —
   it should also idle near 1.65 V. Only then attach electrodes, **on battery
   power with USB disconnected** (`REQUIRES_CONFIRMATION.md` B2).

---

## Regenerating everything from source

The whole project is generated from `scripts/design.py`. To change something,
edit that and re-run:

```bash
python scripts/generate_library.py    # .lbr, with a model self-check
python scripts/validate_erc.py        # ERC (must pass before continuing)
python scripts/generate_schematic.py  # .sch, cross-checked against the model
python scripts/generate_board.py      # place, route, emit .brd
python scripts/validate_drc.py        # DRC on the emitted geometry
python scripts/render.py              # PNG renders of the real files
python scripts/generate_docs.py       # netlist, GPIO table, BOM, reports
```

Or all of it: `python scripts/build_all.py`

The generators cross-check themselves. `generate_schematic.py` re-parses its
own output and asserts the netlist matches the model exactly;
`generate_board.py` does the same for elements and signals. If the model and
the files ever disagree, the build fails rather than emitting something wrong.
