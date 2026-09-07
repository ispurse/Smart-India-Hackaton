# SIH26113 — Maternity Assist Belt · Prototype Carrier PCB

Electronics for the **Smart Maternity Band** (Smart India Hackathon 2026,
problem statement **SIH26113**, Team Rocket 🚀). This directory contains a
complete, verified component library, a seven-sheet schematic, a placed and
largely routed four-layer board, and the engineering documentation behind
every decision — all generated from a single source model so nothing can
drift out of step.

> ## ⚠️ Read this first
>
> **This is not a medical device.** It is a prototype for engineering
> evaluation. The ECG channel connects to a human being and has **no galvanic
> isolation**, **no defibrillation protection**, and no regulatory compliance
> work behind it. Use it on battery power with USB disconnected, with informed
> participants only.
>
> **The board has no battery-protection circuit.** The cell fitted to `J1`
> **must** have an integrated protection module. An unprotected Li-Po here is
> a fire risk. See `documentation/REQUIRES_CONFIRMATION.md` items **B1** and
> **B2** before you power anything.

---

## Where this stands — honestly

The brief distinguishes three levels of completion. Being precise about which
one this is matters more than claiming the highest.

| Level | Meaning | Status |
|---|---|---|
| **1 — Architecture** | Blocks and intent | ✅ Complete |
| **2 — Electrical schematic + verified library** | Real parts, real pinouts, real values, connectivity checked | ✅ **Complete** |
| **3 — Manufacturable PCB** | Placed, routed, DRC-clean, manufacturing files out | 🟨 **Substantially complete** — geometry is DRC-clean, 4 airwires remain by choice, Gerbers need Fusion's CAM |

**What is genuinely done:**

- Component library with **every pinout verified against the manufacturer's
  datasheet** — 23 footprints, 28 symbols, 30 devices. Three footprints come
  from the vendor's own recommended land-pattern drawing; the rest are
  IPC-7351B-derived from verified body dimensions. Nothing was drawn from
  memory or inferred from the architecture picture.
- Seven-sheet schematic, **167 parts, 84 nets, 420 pin connections, every pin
  connected exactly once**. An independent 11-group ERC passes with **0
  errors**.
- Four-layer board, 100 × 70 mm, all 150 components placed in functional
  zones, both power planes poured, antenna keep-out enforced, exposed pads
  via-stitched.
- Routing: **see `documentation/DRC_REPORT.md` for the exact figures** —
  they are generated from the router's own output rather than asserted
  here. Any remaining connection appears as an airwire the moment the
  board is opened in Fusion, is listed by name with the reason, and is
  step 13 of the build guide.
- **Clearance is prioritised over completeness.** Where the router could
  only finish a net by coming closer than the 0.15 mm rule, it leaves the
  net as an airwire instead. An airwire is visible and gets hand-routed;
  a 0.05 mm gap is invisible and might reach fabrication.

**What has NOT been done, stated plainly:**

| Item | Status |
|---|---|
| Autodesk EAGLE / Fusion **ERC** | **NOT EXECUTED — TOOL UNAVAILABLE.** No EAGLE installation existed where these files were produced. An independent ERC was written and run instead. |
| Autodesk EAGLE / Fusion **DRC** | **NOT EXECUTED — TOOL UNAVAILABLE.** An independent geometric DRC was written and run instead. |
| Copper-pour geometry | 🟨 **PARTLY CLOSED.** `scripts/validate_planes.py` measures pour *connectivity*: both pours keep one dominant region (≥ 99.9 % of remaining copper), the ECG zone is entirely inside it, and **0 plane contacts are orphaned**. It found a real defect doing so — see `FINAL_REVIEW.md`. EAGLE's exact fill is still computed on load; run `RATSNEST`. |
| Gerber / drill files | **NOT GENERATED.** Needs EAGLE's CAM processor. |
| 3D / mechanical interference | **NOT CHECKED.** No STEP models are attached to these footprints. |
| USB pair impedance | ✅ **CALCULATED** — `documentation/USB_PAIR_ANALYSIS.md`. As-routed ≈ 165 Ω, not the 90 Ω USB asks for, but electrically short by 2.6× at Full Speed so it is not a functional risk. |
| Physical prototype | **NOT BUILT.** No figure in this project is a measurement. |

Nothing here is claimed as passing a tool that was never run.

---

## Files

```
SIH26113_Maternity_Assist_Belt/
├── README.md                     ← you are here
├── FULL_INSTRUCTION_TUTORIAL.md  ← the complete A-to-Z walkthrough
│
├── libraries/
│   └── SIH26113_Maternity_Assist_Belt.lbr      EAGLE 9 / Fusion library
│
├── schematic/
│   └── SIH26113_Maternity_Assist_Belt.sch      7 sheets
│
├── fusion_project/               ← OPEN THIS FOLDER IN FUSION
│   └── .lbr + .sch + .brd together, same base name, so Fusion
│       pairs the schematic with the board  (generated; see its README)
│
├── pcb/
│   ├── SIH26113_Maternity_Assist_Belt.brd      4-layer board
│   ├── route_report.json                       router's own output
│   ├── drc_result.json                         DRC findings, machine-readable
│   └── plane_result.json                       plane-pour connectivity
│
├── documentation/
│   ├── COMPONENT_VERIFICATION.md   every pinout + footprint, with its source
│   ├── DESIGN_ASSUMPTIONS.md       every decision, and the 7 architecture changes
│   ├── ECG_FRONTEND_DESIGN.md      the AD8232 circuit, with the arithmetic
│   ├── GROUNDING_NOTES.md          why one ground plane and not a split
│   ├── POWER_BUDGET.md             itemised current budget, dropout analysis
│   ├── USB_PAIR_ANALYSIS.md        differential impedance, calculated
│   ├── GPIO_ASSIGNMENT.md          all 41 module pins            [generated]
│   ├── NETLIST.md                  all 84 nets                   [generated]
│   ├── BOM.md / BOM.csv            bill of materials             [generated]
│   ├── ERC_REPORT.md               rules + result                [generated]
│   ├── DRC_REPORT.md               rules + result + airwire list [generated]
│   ├── MANUFACTURING_CHECK.md      19-point pre-fab check        [generated]
│   ├── PROJECT_STATISTICS.md       counts and metrics            [generated]
│   ├── FINAL_REPORT.md             the 15-point final report     [generated]
│   ├── FINAL_REVIEW.md             27-point independent review
│   ├── PCB_BUILD_GUIDE.md          20 steps, Fusion to fabrication
│   └── REQUIRES_CONFIRMATION.md    open items, worst first
│
├── renders/
│   ├── schematic_p1..p7.png        rendered from the actual .sch
│   ├── pcb_top.png                 rendered from the actual .brd
│   ├── pcb_bottom.png
│   ├── pcb_layers.png              all four copper layers
│   ├── pcb_assembly.png            placement + designators + zones
│   └── pcb_3d.png                  isometric mechanical envelope
│
├── reference/
│   └── PCB_architecture_source.jpeg   the input architecture diagram
│
└── scripts/                        the whole project is generated from these
    ├── design.py                   ★ single source of truth
    ├── lib_defs.py                 packages, symbols, devices
    ├── eagle_common.py             EAGLE XML emitters, IPC-7351B generators
    ├── geom.py                     pin/pad geometry and transforms
    ├── router.py                   grid router with rip-up and re-route
    ├── generate_library.py         → .lbr
    ├── generate_schematic.py       → .sch
    ├── generate_board.py           → .brd  (place + route)
    ├── validate_erc.py             ERC
    ├── validate_drc.py             DRC
    ├── validate_planes.py          plane-pour connectivity
    ├── make_fusion_project.py      → fusion_project/
    ├── render.py                   → renders/
    ├── generate_docs.py            → generated documents
    ├── gen_reports.py              → manufacturing check + final report
    └── build_all.py                run the lot
```

> ### 📘 New here? Read [`FULL_INSTRUCTION_TUTORIAL.md`](FULL_INSTRUCTION_TUTORIAL.md)
>
> A single ~7,500-line walkthrough covering everything in this directory: the
> blockers in red and orange up front, absolute-beginner setup, every file,
> every script, the circuit sheet by sheet, and eight workflows from
> "understand it without installing anything" through ordering, assembly,
> bring-up and firmware. This README is the short version.
>
> **Part 31 is the engineering log** — the routing story (two layers to four,
> escape channels, the fan-out stagger trick, clearance-over-completeness, and
> when to abandon a seed search), all **11 defects** found in review with what
> each one teaches, and the three documentation drifts. Read it if you want to
> know *how* the board got this way rather than just what it is.

**Start with [`documentation/FINAL_REPORT.md`](documentation/FINAL_REPORT.md)**
for the one-document summary of what exists, what is verified and what is
left, then **[`documentation/PCB_BUILD_GUIDE.md`](documentation/PCB_BUILD_GUIDE.md)**
to take it from installing Fusion to ordering boards in 20 steps.

---

## What the board does

Seven functional blocks, matching the architecture diagram:

| Block | Implementation |
|---|---|
| **Power entry** | Li-Po via JST-PH (`J1`), 5 V charge input (`J2`), **TP4056** charger at 500 mA, **AP2112K-3.3** 600 mA LDO, battery-voltage sense to ADC, fuel-gauge breakout header |
| **Central MCU** | **ESP32-S3-WROOM-1-N8R2** — Wi-Fi + BLE 5, 8 MB flash, 2 MB PSRAM, native USB-Serial-JTAG |
| **ECG** | **AD8232** three-electrode front end with driven RLD, two-pole HPF, gain 1100, per-electrode leads-off detection |
| **Motion / angle** | **LSM6DSOX** 6-axis IMU with both interrupts; **AS5600** magnetic angle sensor on a separate I²C bus |
| **Mechanical sensing** | **HX711** load-cell ADC, 4 × FSR dividers, stretch-sensor divider, piezo conditioning with over-voltage clamps, hall/limit input |
| **Alerts** | Two N-FET low-side drivers (vibration motor on `VBAT`, buzzer on `3V3`) with flyback diodes and fail-safe gate pull-downs |
| **User I/O** | SOS button with RC debounce and ESD series resistor, RESET, BOOT, microSD SPI module header, two status LEDs plus two charger LEDs |

Plus 19 test points and four M2 mounting holes.

---

## Things worth knowing before you build it

### The architecture diagram had a bug — an I²C address clash

The diagram puts TMP117, LSM6DSOX, AS5600 and MAX17048 on one shared bus.
**That cannot work:** the AS5600 and the MAX17048 are both hard-wired to
address **0x36**, and neither has an address-select pin.

Resolved with two physically separate busses, using both of the ESP32-S3's
I²C controllers:

| Bus | Pins | Devices |
|---|---|---|
| **SENSOR** (I2C0) | `IO15` / `IO16` | TMP117 `0x48`, LSM6DSOX `0x6A`, fuel-gauge header `0x36` |
| **ANGLE** (I2C1) | `IO14` / `IO42` | AS5600 `0x36`, plus `J6` for a second one |

A *second* AS5600 still clashes with the first. `J6` therefore carries the
angle bus plus a fifth pin to `IO3` through a DNP 0 Ω link, so you can use the
second sensor's analog output, an external TCA9548A mux, or a software bus —
without the board committing you to one. Full reasoning in
`DESIGN_ASSUMPTIONS.md` §5.

### The module part number is not interchangeable

**`ESP32-S3-WROOM-1-N8R2`. Not N8R8. Not N16R8.**

On Octal-SPI-PSRAM variants, IO35/IO36/IO37 are wired to the PSRAM and
unavailable (datasheet v1.8, Table 3-1 note b). This design uses all three.
Fitting the wrong variant shorts ECG signals into the PSRAM bus.

### Four layers, not two — and why that was necessary

The diagram implies a simple carrier board. This is signal / **GND plane** /
**3V3 plane** / signal.

The AD8232 amplifies a sub-millivolt biopotential by 1100 across 10 MΩ nodes,
and its datasheet asks for a ground plane. With 81 signal nets and 15
through-hole connectors, two layers leaves no continuous reference under the
analog section — measured, not assumed: on two layers the router completed
~50 of 81 nets and the board's reachable copper split into disconnected
regions. On four layers it completes 77. Cost is a couple of dollars per
prototype board.

### The ECG channel is a heart-rate channel

Pass band ≈ 7–40 Hz, deliberately narrower than diagnostic ECG. That is the
datasheet's own motion-artefact-resistant configuration, chosen because a belt
worn by a walking pregnant woman is not a resting subject. It gives reliable
beat detection and HR variability. It does **not** give clinically
interpretable waveform morphology, and nothing in this project should say
otherwise. Reasoning and the retune path: `ECG_FRONTEND_DESIGN.md`.

### Firmware has three non-negotiable jobs

1. **Low-battery cut-off at 3.5 V** using `VBAT_SENSE` on `IO9`
   (reads 1.75 V at the pin). The LDO's 250 mV dropout means the 3V3 rail
   sags below the ESP32's 3.0 V minimum near the bottom of the discharge
   curve. Without this the board browns out unpredictably — bad in a device
   with an SOS button. See `POWER_BUDGET.md`.
2. **Wait 2.5 s** after power-up before trusting an ECG reading; the AD8232's
   reference network needs it.
3. **Use ADC1 only** (GPIO1–10) for analog. ADC2 does not work while the radio
   is active — which is why all 8 analog signals are on ADC1's 10 channels.

### Three parts need reflow

The AD8232 (0.5 mm QFN with a 2.5 mm exposed pad), LSM6DSOX (0.5 mm LGA) and
TMP117 (0.65 mm WSON with a thermal pad) cannot be soldered with an iron.
**Order a stencil with the boards.** Everything else is 0805, SOT-23,
SOIC/SOP-1.27 or through-hole.

---

## Regenerating everything

The project is generated from `scripts/design.py`. Change that, then:

```bash
python scripts/build_all.py
```

Or step by step:

```bash
python scripts/generate_library.py    # .lbr + library model self-check
python scripts/validate_erc.py        # ERC — must pass before continuing
python scripts/generate_schematic.py  # .sch, cross-checked against the model
python scripts/generate_board.py      # place, route, emit .brd
python scripts/validate_drc.py        # DRC on the emitted geometry
python scripts/render.py              # PNGs, drawn from the real files
python scripts/generate_docs.py       # netlist, GPIO table, BOM, ERC/DRC reports
python scripts/gen_reports.py         # manufacturing check + final report
```

Requires Python 3.11+ with `numpy`, `matplotlib` and `Pillow`.

**Why generated rather than hand-drawn.** One model produces the library, the
schematic, the board, the netlist document, the GPIO table and the BOM, so
they cannot disagree with each other. The generators also verify themselves:
`generate_schematic.py` re-parses its own output and asserts the emitted
netlist matches the model exactly, and `generate_board.py` does the same for
elements and signals. If the model and the files ever diverge, the build fails
rather than quietly emitting something wrong.

Renders are produced by parsing the emitted `.sch` and `.brd` and drawing the
primitives they contain — so a render cannot show something the board does
not have.

---

## Verification summary

| Check | Tool | Result |
|---|---|---|
| Library model consistency | `generate_library.py` | ✅ PASS — every symbol pin maps to an existing pad, no orphan pads, no pad overlaps |
| Schematic vs. model | `generate_schematic.py` | ✅ PASS — 84 nets, 420 pinrefs, exact match |
| ERC, 11 rule groups | `validate_erc.py` | ✅ **0 errors, 0 warnings** |
| Board vs. model | `generate_board.py` | ✅ PASS — 150 elements, 84 signals |
| DRC, 8 rule groups | `validate_drc.py` | ✅ **0 clearance, width, drill, placement, keep-out or board-edge violations.** Every reported error is an unrouted net. **Measured minimum clearance and the airwire list: `documentation/DRC_REPORT.md`** — generated from the emitted geometry, not asserted here |
| Routing | `generate_board.py` | 🟨 **See `documentation/DRC_REPORT.md` for the current figures.** The remaining airwires are all deliberate clearance concessions, not routing failures — each is named with the gap it would have had. Re-routing after any model change produces a *different* set, which is why the number is not repeated here |
| Plane-pour connectivity | `validate_planes.py` | ✅ **PASS** — both pours keep one dominant region (≥ 99.9 % of remaining copper), the ECG zone Z3 pour is entirely inside it, **0 orphaned plane contacts**. Live figures: `pcb/plane_result.json` |
| Independent design review, 27 failure modes | `FINAL_REVIEW.md` | ✅ **11 defects found and fixed**, 5 items left open and documented |
| EAGLE / Fusion ERC | — | ❌ NOT EXECUTED — tool unavailable |
| EAGLE / Fusion DRC | — | ❌ NOT EXECUTED — tool unavailable |

---

## Context

Part of the **Smart Maternity Band** project — a dual-layer wearable combining
mechanical lumbar and abdominal support with continuous maternal and fetal
monitoring. The parent repository holds the concept website; this directory is
the electronics.

Component and cost figures across the project are internal engineering
estimates, not a certified BOM. The wider project's own documented limitations
apply — blood pressure and heart rate are hard to measure accurately from a
belt form factor, and predicted delivery date, predicted recovery time and
belly heatmap visualisation were all explored and marked not currently
feasible.

**Licence / reuse:** the datasheets referenced here belong to their respective
manufacturers and are not redistributed. Footprint dimensions are derived from
publicly published land-pattern drawings and the IPC-7351B standard.
