# GROUNDING AND RETURN-CURRENT STRATEGY

## The decision, up front

**One ground net. One continuous plane. No AGND/DGND split.**

Separation between the ECG front end and the noisy circuits is achieved by
**placement and return-path control**, not by cutting copper.

The brief asked for AGND/DGND only "if there is a legitimate reason". After
working through it, there isn't one here — and a split would actively make
this board worse. The reasoning is below, because "we used one ground plane"
is a claim that deserves an argument rather than an assertion.

---

## Stack-up

| EAGLE layer | Role | Copper | Notes |
|---|---|---|---|
| 1 (`Top`) | signal + all components | 35 µm | every ECG track that could be kept here, was |
| 2 (`Route2`) | **solid GND plane** | 35 µm | the reference for every layer-1 track |
| 15 (`Route15`) | **solid 3V3 plane** | 35 µm | the reference for every layer-16 track |
| 16 (`Bottom`) | signal | 35 µm | overflow routing, no components |

Dielectric: 0.36 mm / 0.71 mm / 0.36 mm, total 1.6 mm FR-4.

The important consequence: **layer 1 is 0.36 mm above an unbroken ground
plane.** Every top-side signal, including the whole ECG chain, has a
continuous low-inductance return directly beneath it. That is the single
biggest reason this board is 4-layer and not 2-layer.

---

## Why not split the ground

The intuition behind AGND/DGND is "keep digital return current out of the
analog ground". The intuition is right; the split is usually the wrong
implementation. Three reasons specific to this board:

### 1. Return current follows the signal, not the schematic

Above a few tens of kilohertz, return current does not spread out looking for
the lowest DC resistance. It flows in the plane directly under its own trace,
because that is the lowest-**inductance** path. A digital track's return
current is already confined to a strip a fraction of a millimetre wide beneath
it — it does not wander into the analog section unless you make it.

The corollary is what matters: **if you cut the plane, the return current
cannot follow its trace any more.** It has to detour around the cut, and the
loop enclosed by signal-out and return-back becomes large. That loop is an
antenna, both radiating and receiving. On this board the offenders would be
the SPI bus to the microSD header and the two FET gate drives — precisely the
signals whose harmonics you least want coupling into a 10 MΩ node.

### 2. Any split needs a bridge, and the bridge becomes the problem

A split ground still has to be connected somewhere, or the two sections float
apart and every signal crossing between them has no return at all. The
standard answer is a single narrow bridge near the ADC. That works when
exactly one signal crosses. Here, **eight** signals cross between the analog
and digital domains: `ECG_OUT`, `ECG_SDN`, `ECG_FR`, `ECG_LOD_P`,
`ECG_LOD_N`, plus the 3V3 supply and its two decoupling returns. Routing all
of those over one bridge is not achievable in this floorplan, and any that
miss the bridge get the large-loop problem from §1, only worse.

### 3. The AD8232 has its own analog ground, internally

The part generates `REFOUT` — a buffered mid-supply virtual ground — and every
filter node in the front end references *that*, not board ground. `REFOUT` is
what isolates the signal chain from supply and ground movement. Board ground's
job is simply to be a quiet, low-impedance reference for `REFIN` and the
decoupling; a plane does that better than an island.

The datasheet's own layout guidance says only: *"the use of a ground plane
significantly improves the noise rejection of the system."* Not a split
plane — a ground plane.

---

## What is done instead

### Placement separation

| Block | Zone | Distance from ECG block |
|---|---|---|
| ECG analog front end (`U7` + 25 passives) | Z3, bottom-right, x 66–98 mm | — |
| Module antenna | top-left corner, x 9–29 mm | ≈ 45 mm |
| ESP32-S3 module | Z2, left, x 8–28 mm | ≈ 40 mm |
| Motor + buzzer drivers | Z6, top-right, x 66–98 mm | ≈ 12 mm, with plane between and vertically offset |
| Charger + LDO | Z1, bottom-left | ≈ 35 mm |
| microSD SPI header | Z7, top-centre | ≈ 20 mm |

The ECG electrode connector `J7` is on the right board edge, immediately
beside `U7`, with the 330 kΩ protection resistors between them. The
unprotected, highest-impedance part of the signal path is therefore about
5 mm long.

### Motor return current is confined at its source

`C37` (10 µF) sits at the motor's high side, `Q1`'s source connects to the
plane through its own via, and the motor connector is 8 mm from the FET. The
switched current loop — `C37` → `J16` → motor → `Q1` → plane → back to `C37` —
is small and entirely inside Zone 6. `R43` (100 Ω gate series) slows the
gate edge, which reduces the di/dt that loop has to carry in the first place.

Because the return current stays in that loop, it never traverses the plane
under the ECG section. This is the mechanism that a split plane would be
trying to achieve, obtained without cutting anything.

`C38` does the same job for the buzzer FET on the 3V3 rail.

### Via stitching

Every SMD pad on `GND` gets its **own** plane via, 0.3 mm drill / 0.55 mm pad,
placed within about 0.8 mm of the pad. Nothing relies on a surface pour to
make a ground connection — that is a deliberate choice, because pour-island
connectivity cannot be verified without running EAGLE's polygon calculation,
and an unverified ground connection is not worth the copper it saves.

On top of that, a coarse ~11 mm grid of stitching vias ties layers 1, 2, 15
and 16 together across the whole board, so return current changing layers
always has a nearby path.

Exposed pads are stitched properly, not decoratively:

| Part | Exposed pad | Vias |
|---|---|---|
| `U3` ESP32-S3-WROOM-1 | pad 41, 3.4 mm land | 9 × 0.3 mm on a 1.1 mm grid |
| `U7` AD8232 | `EP`, 2.50 mm SQ | 4 × 0.3 mm |
| `U4` TMP117 | pad 7, 1.0 × 1.6 mm | 2 × 0.3 mm |

> A note on how these are emitted, because it is a real trap: EAGLE's
> `<hole>` element inside a package is an **unplated mechanical hole**.
> Putting thermal "vias" in a footprint that way drills unplated holes
> straight through the ground land — a genuine manufacturing defect that
> looks correct in the library editor. These vias are therefore emitted at
> board level as plated vias belonging to the `GND` signal
> (`THERMAL_VIAS` in `scripts/lib_defs.py`).

### Antenna keep-out cuts *all* copper, planes included

Espressif require the module antenna to sit at a board edge with no copper
beneath it. The module is placed so its 6 mm antenna area is flush with the
top board edge, and the keep-out region (x 9–29 mm, y 63.4–70 mm) is:

* declared on layers 39/40/41/42/43 (keep-out and restrict, top/bottom/via);
* **excluded from both plane polygons** — since an EAGLE polygon cannot carry
  a hole, `PLANE_OUTLINE` is drawn as an L that omits that corner;
* checked by the DRC (rule D3), which fails on any pad, via or track endpoint
  inside it.

A ground plane under a PCB antenna detunes it badly. This is the one place on
the board where absent copper is the requirement.

---

## Where the analog reference actually lives

Worth stating explicitly, because it is easy to look for a star ground that
isn't there:

```
        3V3 ──[R23 10M]──┬── REFIN (pin 18) ──► internal buffer ──► REFOUT (pin 8)
                         │                                              │
        GND ──[R24 10M]──┤                                              │
                         │                                              ├─ HPF pole 2 return (R26)
                       [C16]                                            ├─ LPF pole 1 return (C20)
                       100nF                                            ├─ op-amp gain leg (R28)
                         │                                              └─ input bias (R21/R22 via +VS)
                        GND
```

`REFOUT` is the analog reference for the entire signal chain. Board `GND`
appears in the front end only at: `C16` (reference filter), `R24` (divider
leg), the `+VS` decoupling pair `C23`/`C24`, `AC/DC` (mode select), the
exposed pad, and `C22` (ADC reservoir). Six places, all low-impedance, all
with their own plane via.

The `REFIN` network settles in 5 × (`R23`∥`R24`) × `C16` = 5 × 5 MΩ × 100 nF ≈
**2.5 s**. Firmware must wait that long after power-up, or after leaving
`SDN` shutdown, before the first reading means anything.

---

## Verification status

| Check | Status |
|---|---|
| Plane polygons declared on layers 2 and 15, antenna corner excluded | ✅ present in the `.brd` |
| Every SMD `GND` pad has its own plane via | ✅ enforced in `generate_board.py`; any pad it could not serve is reported and appears in `DRC_REPORT.md` |
| Every SMD `3V3` pad has its own plane via | ✅ same mechanism |
| Exposed pads via-stitched as plated vias | ✅ 15 thermal vias |
| Nothing inside the antenna keep-out | ✅ DRC rule D3 |
| **Plane vias actually land inside the pour** | ✅ **MEASURED** by `scripts/validate_planes.py`. **This caught a real defect** — two `GND` vias, one of them `C7`'s only path to the plane, sat above the pour's y = 63.0 edge. See `FINAL_REVIEW.md`. Now 0 orphaned contacts on either plane |
| **Pour connectivity — does it stay one region?** | ✅ **MEASURED.** `validate_planes.py` punches an antipad (own radius + the declared 0.4 mm isolate) around all 72 through-holes and every via, then labels connected components. Both pours remain one dominant region carrying ≥ 99.9 % of the remaining copper, and **the ECG zone Z3 pour is entirely within that region on both planes.** Live figures: `pcb/plane_result.json` |
| **Exact pour geometry as EAGLE will fill it** | ⚠️ **STILL NOT COMPUTED — TOOL UNAVAILABLE.** `validate_planes.py` measures connectivity of the region EAGLE will fill; it does not reproduce EAGLE's fill algorithm and emits no copper. **Run `RATSNEST` then DRC in Fusion** — build guide step 14 |
| Pessimistic pour-pen check | ⚠️ the script's `realistic` pass inflates every antipad by half the 0.4 mm pour line width, modelling the pen's inability to fill narrow corridors. It typically flags **a small number of vias in dense clusters** whose local area closes up. Those are a *risk indication*, not a certainty — check them in Fusion after `RATSNEST` |
| Plane resonance / impedance modelling | ❌ not attempted; out of scope for a prototype at these frequencies |

---

## If you do decide to split it later

If a future revision genuinely needs an isolated analog ground — for example
if the ECG channel is moved toward diagnostic bandwidth and 0.5 Hz corners —
then do it properly:

1. Split **layer 2 only**, keeping layer 15 whole.
2. Put the split under the 330 kΩ protection resistors, so it lies between the
   patient interface and everything else.
3. Bridge the two sections at exactly one point, directly beneath `R30` (the
   ADC series resistor), and route **every** analog-to-digital signal
   (`ECG_OUT`, `ECG_SDN`, `ECG_FR`, `ECG_LOD_P`, `ECG_LOD_N`) across that
   single bridge. If they cannot all cross there, do not split.
4. Move the 3V3 feed for `U7` so it also crosses at the bridge.
5. Add a keep-out on layers 1 and 16 over the split, so no track crosses it
   anywhere else. A track crossing a plane split is the failure mode this is
   all trying to avoid.

The reason this was not done now is step 3: five signals cross, and one bridge
cannot serve them in this floorplan.
