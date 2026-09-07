<!--
  FULL_INSTRUCTION_TUTORIAL.md
  SIH26113 - Maternity Assist Belt - Prototype Carrier PCB
  The single complete walkthrough: from "I have never opened an EDA tool"
  to "the boards arrived and the ECG channel works".

  This document is hand-written, not generated. The generated documents it
  refers to are marked [generated] and are rebuilt by scripts/build_all.py.
-->

<div align="center">

# 📘 FULL INSTRUCTION TUTORIAL

### SIH26113 — Maternity Assist Belt · Prototype Carrier PCB

**Smart India Hackathon 2026 · Problem Statement SIH26113 · Team Rocket 🚀**

*Everything, A to Z. Every file, every script, every workflow, every number,
every thing that can go wrong — in the order you will actually need it.*

</div>

---

$$\Huge\textcolor{red}{\textsf{⛔ STOP — READ PART 1 FIRST ⛔}}$$

$$\large\textcolor{red}{\textsf{3 BLOCKING items. One of them is a fire risk.}}$$

$$\large\textcolor{orange}{\textsf{6 more must be settled before you spend money on PCBs.}}$$

> [!CAUTION]
> ### 🔴 This board has **no battery-protection circuit** and **no ECG isolation**.
>
> If you connect an **unprotected** lithium cell to `J1`, you have built a fire
> hazard. If you attach ECG electrodes to a person **while USB is plugged in**,
> you have galvanically connected that person to a mains-derived supply through
> 330 kΩ.
>
> Neither of those is a bug. Both are documented, deliberate boundaries of a
> prototype. But you have to know about them **before** you power anything.
>
> **→ Jump straight to [PART 1 — THE BLOCKERS](#part-1--the-blockers-read-this-before-anything-else).**

> [!WARNING]
> ### 🟠 This is **not a medical device** and must never be presented as one.
>
> No IEC 60601-1 and no IEC 60601-2-47 compliance work has been done, and none
> is claimed. This is an engineering prototype for bench evaluation by informed
> participants. It measures a biopotential; it does not diagnose anything.

---

## 🧭 How to read this document

It is long on purpose. You are **not** meant to read it front to back in one
sitting. Pick your route:

| If you are… | Read, in this order | Roughly |
|---|---|---|
| **Judging / evaluating the project** | Part 1 → Part 2 → Part 3 → Part 5 → Part 26 | 30 min |
| **A teammate picking this up cold** | Part 1 → Part 2 → Part 4 → Part 5 → Part 6 → Part 16 | 2 hours |
| **About to open it in Fusion** | Part 1 → Part 3 → Part 13 → Part 19 (Workflow D) | 1 hour, then a day of work |
| **About to order boards** | Part 1 → Part 20 (Workflow E) → Part 29 checklists | 1 hour |
| **About to solder** | Part 21 (Workflow F) → Part 22 (Workflow G) | read fully before you start |
| **Writing the firmware** | Part 9 → Part 23 (Workflow H) → Part 11 | 2 hours |
| **Changing the design** | Part 6 → Part 7 → Part 18 (Workflow C) | 2 hours |
| **Debugging a board that does not work** | Part 24 (Troubleshooting) | as needed |
| **Here to learn how it was engineered** | Part 31 → Part 6 → Part 14 → Part 15 | 1 hour |

### Conventions used everywhere below

| Marker | Meaning |
|---|---|
| 🔴 **BLOCKING** | Can destroy hardware or hurt a person. Resolve before power. |
| 🟠 **HIGH** | Changes a component value or a footprint. Resolve before ordering PCBs. |
| 🟡 **MEDIUM** | Affects performance. Verify before or during bring-up. |
| ⚪ **LOW** | Cosmetic or convenience. |
| ✅ | Verified against primary documentation, or checked by a script that ran. |
| ❌ **NOT EXECUTED** | A tool that would normally check this was **not available**. Never presented as passing. |
| `J1`, `R45`, `U7` | A reference designator — a specific physical part on the board. |
| `VBAT`, `ECG_OUT` | A net name — a specific electrical connection. |
| `IO35` | An ESP32-S3 module pin. |
| **§** | A section in one of the other documents in `documentation/`. |

### The one rule this whole project follows

> **Nothing is claimed as passing a tool that was never run.**
>
> There is no EDA software installed in the environment where these files were
> produced. So the library, schematic and board were generated directly as
> EAGLE 9 XML from a Python model, and *independent* ERC and DRC checkers were
> written and run against the emitted files. Those pass. **Autodesk Fusion's
> own ERC and DRC have not been run**, and every document says so in those
> words. Running them is your job, and it is Part 19 of this tutorial.

---

## 📑 Table of contents

**Front matter**
- [PART 1 — THE BLOCKERS](#part-1--the-blockers-read-this-before-anything-else) 🔴🟠 ← *start here*
- [PART 2 — What this project actually is](#part-2--what-this-project-actually-is)
- [PART 3 — Exactly how complete this is](#part-3--exactly-how-complete-this-is)

**Getting set up**
- [PART 4 — Absolute-beginner setup](#part-4--absolute-beginner-setup)
- [PART 5 — Every single file, explained](#part-5--every-single-file-explained)

**Understanding the machinery**
- [PART 6 — The generated-from-source model](#part-6--the-generated-from-source-model)
- [PART 7 — Every script, explained](#part-7--every-script-explained)

**Understanding the electronics**
- [PART 8 — The circuit, sheet by sheet](#part-8--the-circuit-sheet-by-sheet)
- [PART 9 — GPIO allocation and its two hard constraints](#part-9--gpio-allocation-and-its-two-hard-constraints)
- [PART 10 — Power budget, in full](#part-10--power-budget-in-full)
- [PART 11 — The ECG front end, in depth](#part-11--the-ecg-front-end-in-depth)
- [PART 12 — Grounding and the stack-up](#part-12--grounding-and-the-stack-up)

**Understanding the board**
- [PART 13 — The physical board](#part-13--the-physical-board)
- [PART 14 — How the router works](#part-14--how-the-router-works)
- [PART 15 — Verification: what was checked and how](#part-15--verification-what-was-checked-and-how)

**Workflows — the actual doing**
- [PART 16 — Workflow A: understand it without installing anything](#part-16--workflow-a-understand-it-without-installing-anything)
- [PART 17 — Workflow B: regenerate the entire project](#part-17--workflow-b-regenerate-the-entire-project)
- [PART 18 — Workflow C: change the design](#part-18--workflow-c-change-the-design)
- [PART 19 — Workflow D: open it in Autodesk Fusion, all 20 steps](#part-19--workflow-d-open-it-in-autodesk-fusion-all-20-steps)
- [PART 20 — Workflow E: order the PCB](#part-20--workflow-e-order-the-pcb)
- [PART 21 — Workflow F: assemble the board](#part-21--workflow-f-assemble-the-board)
- [PART 22 — Workflow G: bring-up, in six stages](#part-22--workflow-g-bring-up-in-six-stages)
- [PART 23 — Workflow H: firmware](#part-23--workflow-h-firmware)

**Reference**
- [PART 24 — Troubleshooting encyclopedia](#part-24--troubleshooting-encyclopedia)
- [PART 25 — The seven architecture changes](#part-25--the-seven-architecture-changes)
- [PART 26 — Known limitations, honestly](#part-26--known-limitations-honestly)
- [PART 27 — Glossary](#part-27--glossary)
- [PART 28 — FAQ](#part-28--faq)
- [PART 29 — Printable checklists](#part-29--printable-checklists)
- [PART 30 — Appendices](#part-30--appendices)
- [PART 31 — Engineering log: what was built, what broke, and what it taught](#part-31--engineering-log-what-was-built-what-broke-and-what-it-taught) ← *the routing story and the 11 defects*

---

# PART 1 — THE BLOCKERS (read this before anything else)

$$\Huge\textcolor{red}{\textsf{🔴 BLOCKING — 3 items}}$$

$$\normalsize\textcolor{red}{\textsf{These can destroy hardware or hurt a person. Resolve BEFORE applying power.}}$$

The authoritative, always-current version of this list is
[`documentation/REQUIRES_CONFIRMATION.md`](documentation/REQUIRES_CONFIRMATION.md).
This part reproduces it with more explanation and adds the *how to clear it*
that the source document leaves implicit.

Every item below is a checkbox. **Tick them in the source document as you go**,
so the next person knows where you got to.

---

<table>
<tr><td bgcolor="#b71c1c">

## 🔴 B1 — The Li-Po cell at `J1` **must** have integrated protection

</td></tr>
</table>

> [!CAUTION]
> **There is no battery protection circuit on this board.**
> An unprotected Li-Po cell connected to `J1` is a fire risk.

### What happened and why

The architecture diagram that this project started from said:

> "JST → TP4056 **protected** module"

That word *protected* is doing a lot of work. A commercial **TP4056 module** —
the little red PCB you buy for a dollar — carries **two** circuits:

| On the module | Function |
|---|---|
| **TP4056** | the linear charge controller |
| **DW01A + FS8205A** | the *protection* circuit: over-charge, over-discharge, over-current cut-off |

This design uses the **TP4056 as a bare IC** (`U1`, SOIC-8), because a
board-level charger is the right thing for a real product and because dropping
a purchased module onto a carrier board is not a PCB design. That means the
charge controller is present and **the protection circuit is not**.

Bare DW01A and FS8205A were deliberately **not** added, because their pinouts
could not be verified against primary manufacturer documentation from the
environment these files were produced in. Guessing at the pinout of a lithium
protection circuit — the one circuit whose failure mode is a fire — is not an
acceptable risk. Marking it as an open item is.

### What to confirm

**The cell or pack fitted to `J1` has an integrated protection circuit module
(PCM)** providing all three of:

- over-charge cut-off (typically ~4.25–4.35 V)
- over-discharge cut-off (typically ~2.4–3.0 V)
- over-current / short-circuit cut-off

### How to clear it — step by step

1. **Buy a protected 1S Li-Po pack.** Search terms: *"1S 3.7 V Li-Po with PCM"*,
   *"protected lithium polymer JST-PH"*. Almost every cell sold for
   prototyping already has one — you have to go out of your way to buy a bare
   cell. Bare cells are usually sold as "cell only", "for pack assembly", or
   with bare nickel tabs instead of wires.
2. **Physically verify the PCM is there.** Peel back the yellow Kapton tape at
   the end where the wires exit. You are looking for a **small PCB, roughly
   4 × 12 mm, with a black 6-pin or 8-pin chip and a second larger chip.**
   Two wires leaving a bare foil tab with no PCB = **unprotected, do not use**.
3. **Meter the JST pigtail before the first connection.**

   > 🔴 **JST PH pigtails are NOT consistently wired between suppliers.**
   > Some vendors put + on pin 1, some on pin 2. Reversing this puts the cell
   > backwards across the charger and the whole 3V3 rail.

   - `J1` **pin 1 = `VBAT` (+)**
   - `J1` **pin 2 = `GND` (−)**
   - Pin 1 is the **square pad** on the board silkscreen. Every through-hole
     connector on this board marks pin 1 with a square pad — that is
     manufacturing check item 16.
   - Set a multimeter to DC volts, put the black probe on the pigtail contact
     that will land in pin 2, red on pin 1. **You must read a positive number
     between 3.0 and 4.2 V.** If it reads negative, the pigtail is reversed:
     re-crimp it, or cut and swap the wires. Do not "just remember".
4. Tick B1 in `documentation/REQUIRES_CONFIRMATION.md`.

### If you would rather have protection on the board

That is a legitimate choice and it is a real design change, not a tweak. It
means adding DW01A + FS8205A (or a modern integrated equivalent) to the
library with a **verified** pinout, wiring them between the cell and `VBAT`,
re-running the whole generate chain, and re-routing. Budget a day. See
[Part 18 — Workflow C](#part-18--workflow-c-change-the-design) for how to add
a part to the model.

### What it costs you if you get it wrong

A 1S Li-Po driven past 4.3 V, or shorted, vents and then burns. It is not a
"the board stops working" failure mode. This is the single most consequential
line in the entire project.

---

<table>
<tr><td bgcolor="#b71c1c">

## 🔴 B2 — ECG electrical safety — this is not a medical device

</td></tr>
</table>

> [!CAUTION]
> The ECG channel connects to a **human being**. There is **no galvanic
> isolation** anywhere in that path.

### What the board **does** provide

| Protection | Value | Source of the rule |
|---|---|---|
| Series resistance, each electrode (LA, RA) | **330 kΩ** (`R18`, `R19`) | AD8232 datasheet's own patient-protection guidance |
| Series resistance, driven RLD electrode | **330 kΩ** (`R20`) | AD8232 datasheet: > 330 kΩ at 3.0 V |
| Resulting worst-case fault current | **< 10 µA at 3.3 V** | 3.3 V / 330 kΩ = 10 µA |
| Supply when USB is unplugged | battery only, floating | — |

10 µA is a *very* small number. For scale, the threshold of human perception
for DC current through skin is on the order of a milliamp — a hundred times
larger.

### What the board does **NOT** provide

| Missing | Consequence |
|---|---|
| **Galvanic isolation** between subject and circuit | there is a DC path (through 330 kΩ) from the electrode to the board's ground |
| **Defibrillation protection** | no gas-discharge tubes, no neon lamps, no BAV199-class clamps — which is the AD8232 datasheet's own recommendation *for that case*. If someone is defibrillated while wearing this, the front end is destroyed and the energy path is undefined. |
| **Mains isolation while USB is connected** | 🔴 **this is the one that matters in practice** |

### 🔴 The USB problem, stated plainly

`J2` is the 5 V / USB header. If you plug it into a **mains-powered** USB
supply — a phone charger, a laptop that is itself plugged in, a desktop PC —
then the subject wearing the electrodes is **galvanically connected to that
supply's secondary through 330 kΩ**.

A good USB supply's secondary is isolated from mains and referenced to earth
through its own Y-capacitor. A cheap or failed one may not be. You cannot tell
by looking.

### How to clear it — the protocol

You clear B2 with a **written rule that everyone involved follows**, not with a
purchase.

1. > 🔴 **Electrodes are only ever attached while the board is running on
   > battery, with the USB cable physically unplugged from `J2`.**
   >
   > Not "USB plugged in but the host powered off". Not "USB plugged into a
   > power bank". **Unplugged.** A power bank is defensible but the rule is
   > only useful if it is absolute and unambiguous.
2. **Bench evaluation only, with informed adult participants** who have been
   told what the device is, what it is not, and that it has no medical
   approval.
3. **Never on a person who is pregnant** as part of a demo, despite that being
   the project's eventual target population, until the design has been through
   actual safety engineering. The target application does not license the
   prototype.
4. **Nobody presents it as a medical device** — not in a pitch, not in a
   README, not in a demo video, not verbally. No IEC 60601-1 or IEC 60601-2-47
   compliance work has been done and none is claimed.
5. Write those four lines on a card and tape it inside the enclosure lid.
6. Tick B2 in `documentation/REQUIRES_CONFIRMATION.md`.

### If you need ECG **while** mains-powered

That is a different board. It needs an isolated supply (a medical-grade
isolated DC-DC), an isolated data link (digital isolator or optical), and
patient-connection design to a standard. That is a redesign, not a
modification. Do not try to bolt it on.

---

<table>
<tr><td bgcolor="#b71c1c">

## 🔴 B3 — Vibration motor voltage rating vs. `R45`

</td></tr>
</table>

> [!CAUTION]
> The motor sits directly on `VBAT`, which is **3.0 – 4.2 V**. Most coin ERM
> motors are rated **3.0 V**. Running a 3.0 V motor at 4.2 V will shorten its
> life dramatically and may destroy it.

### The circuit

```
VBAT ──► R45 (0 Ω, 0805) ──► J16 pin 1 ──[ MOTOR ]── J16 pin 2 ──► Q1 drain
                                                                     │
                                              D7 flyback across      │
                                              the motor              │
                       IO47 ──► R43 (100 Ω) ──► Q1 gate              │
                                              R44 (100 kΩ) gate pull-down
                                                                  Q1 source ──► GND
```

- `Q1` = **AO3400A**, N-channel logic-level MOSFET, SOT-23-3, rated **5.7 A**
- `D7` = **1N5819HW** Schottky flyback, anode on the switched drain, cathode
  on the supply — checked by ERC rule R10
- `R44` = 100 kΩ gate pull-down so the FET is **off** if `IO47` floats at boot
- `R45` = **0 Ω 0805**, deliberately present so the motor rail can be adapted
  **without cutting tracks**

`R45` exists for exactly this reason. It is a designed-in escape hatch.

### What to confirm

The motor's **rated voltage** and **rated current**, and its **stall current**.

### How to clear it — the decision table

| Motor rated voltage | Action on `R45` |
|---|---|
| **≥ 4.2 V** | leave `R45` at **0 Ω**. Done. |
| **3.0 V** (most coin ERM types) | **populate `R45`** with a ballast resistor, calculated below |

### Worked example — a 3.0 V / 100 mA coin ERM

**Step 1 — the resistance.**

$$R_{45} = \frac{V_{BAT,max} - V_{motor}}{I_{motor}} = \frac{4.2 - 3.0}{0.1} = 12\ \Omega$$

**Step 2 — the power, which is the part people forget.**

$$P_{R45} = I^2 R = 0.1^2 \times 12 = 0.12\ \text{W} = 120\ \text{mW}$$

An **0805 chip resistor is rated 125 mW**. 120 mW in a 125 mW part is
**marginal** — 96 % of rating, with no derating for ambient temperature inside
a sealed enclosure worn against a body.

**Step 3 — fix the power problem.** Two options, both fine:

| Option | How |
|---|---|
| **Two 24 Ω in parallel** | 24 ‖ 24 = 12 Ω, 60 mW each, both well inside rating. Needs a second pad — you can tack the second resistor on top of the first, or add a footprint (Workflow C). |
| **One 1206 resistor** | 1206 is rated 250 mW. 120 mW is comfortable. An 0805 part fits on a 1206 land but **not** the other way round — so this needs a footprint change in `lib_defs.py` and a re-run. |

**Recommendation:** if you are hand-building one prototype, stack two 24 Ω
0805s. If you are ordering a second batch of boards, change `R45` to 1206 in
the model properly.

**Step 4 — note that the drop only applies at full charge.** At 3.7 V nominal
the motor sees 3.7 − (0.1 × 12) = 2.5 V and runs slightly weak; at 3.0 V it
barely turns. A resistive ballast trades top-end protection for bottom-end
performance. If that bothers you, the correct answer is PWM from `IO47` with a
duty cycle scheduled against the measured `VBAT_SENSE` — the hardware already
supports it, it is purely firmware, and it is described in
[Part 23](#part-23--workflow-h-firmware).

### Also confirm stall current

Coin-ERM **stall current can be 3–4× the running current**. For a 100 mA motor
that is 300–400 mA. Check it against:

| Element | Rating | Margin at 400 mA |
|---|---|---|
| `Q1` AO3400A | **5.7 A** continuous | 14× |
| Motor track, 0.50 mm, 1 oz copper, 10 °C rise | **≈ 1.45 A** (IPC-2221) | 3.6× |
| `R45` if fitted at 12 Ω | 0.4² × 12 = **1.9 W** ← 🔴 | **fails instantly** |

That last row matters: **a stalled motor destroys the ballast resistor**, and
possibly opens it (which is a safe failure) or chars the board (which is not).
If your motor can stall in normal use — a belt-mounted motor pressed against
fabric can — then either drive it in short pulses only, or use PWM without a
ballast, or fit a resistor with real margin.

Tick B3 in `documentation/REQUIRES_CONFIRMATION.md`.

---

$$\Huge\textcolor{orange}{\textsf{🟠 HIGH — 6 items}}$$

$$\normalsize\textcolor{orange}{\textsf{These change a component value or a footprint. Resolve BEFORE ordering PCBs.}}$$

---

<table>
<tr><td bgcolor="#e65100">

## 🟠 H1 — MAX17048 fuel gauge is **not on the board**

</td></tr>
</table>

> [!WARNING]
> The architecture diagram called for a MAX17048 battery fuel gauge. It is not
> placed, because its datasheet could not be retrieved.

**Why.** `analog.com` and every distributor mirror that was tried were either
unreachable or bot-blocked from the network these files were produced on. That
means **neither the MAX17048's pinout nor its land pattern could be verified**.
Drawing an unverified footprint for a part and shipping it in a library is how
you get a board that cannot be assembled. So it was left out and the omission
documented.

Both of its packages are also awkward for a hackathon build: the 8-bump
**0.9 × 1.7 mm WLP is not hand-assemblable at all**, and the TDFN-8 is a
0.5 mm-pitch leadless part.

**Provided instead:**

| Part | What it gives you |
|---|---|
| `J4` — 5-way header (`VBAT`, `GND`, `3V3`, `SDA`, `SCL`) | plug in an off-the-shelf MAX17048 breakout. SparkFun and Adafruit both make one. It sits at **0x36 on the sensor bus**, which is already reserved for it. |
| `R5` / `R6` / `C6` — 470 kΩ / 470 kΩ divider + filter to `IO9` | battery voltage by ADC, **always available**, no gauge required. 4.2 V cell → 2.10 V at the pin. |

**How to clear it.** Decide whether you want the gauge at all.

- **You probably do not need it.** A divider tells you cell voltage. A fuel
  gauge tells you *state of charge*, which is a much better number, but for a
  prototype the voltage is enough — and the firmware needs the voltage anyway
  for the low-battery cut-off (see Part 10).
- **If you want it:** buy a breakout, plug it into `J4`. Zero board changes.
- **If you want it on-board:** obtain the datasheet, verify the TDFN-8 land
  pattern against Analog Devices' own recommended land pattern drawing, add it
  to `lib_defs.py`, and re-run the chain.

---

<table>
<tr><td bgcolor="#e65100">

## 🟠 H2 — Abdominal stretch sensor: `R37` is a **placeholder**

</td></tr>
</table>

> [!WARNING]
> `R37` = 10 kΩ is **a placeholder, not a design value.** It was put there so
> the schematic and board are complete; it is almost certainly wrong for
> whatever sensor you buy.

### The circuit

`J13` brings in a two-terminal resistive stretch sensor. `R37` forms the lower
leg of a divider from `3V3`, `C33` (10 nF) filters it, and the wiper goes to
`IO8` = `ADC1_CH7`.

### Why a placeholder is wrong and what the right value is

A resistive divider has maximum sensitivity when its output sits near
mid-rail. For a sensor that swings between `R_min` (relaxed) and `R_max`
(stretched), the value that centres the output across the whole span is the
**geometric mean**:

$$R_{37} = \sqrt{R_{min} \times R_{max}}$$

This is the same method used for the four FSR dividers, whose 10 kΩ value
**is** derived — see `DESIGN_ASSUMPTIONS.md` §7.1. `R37` just has no sensor to
derive from yet.

### How to clear it

1. Choose the sensor and get its part number.
2. Measure or look up its resistance at **minimum** and **maximum** useful
   extension. Measure it if you can — published figures for conductive-rubber
   stretch sensors are wide.
3. Compute √(R_min × R_max).
4. **Check both extremes do not clip.** Compute the divider output at R_min and
   at R_max and confirm both land between roughly 0.15 V and 3.15 V. The
   ESP32-S3 ADC is not usable right at the rails.
5. Set `R37` in `scripts/design.py` and re-run, **or** just fit the right
   resistor to the built board.

**Good news:** `R37` is a single 0805. This is a **reworkable change, not a
re-spin.** You can order the boards with H2 unresolved.

---

<table>
<tr><td bgcolor="#e65100">

## 🟠 H3 — Load cell: bridge resistance and sensitivity unknown

</td></tr>
</table>

> [!WARNING]
> Two of the load cell's parameters affect the design and neither is known yet.

### The circuit

The board excites the bridge from `3V3` via `J8` (a JST-PH-4) and reads it on
**HX711 channel A at gain 128** — that is ±20 mV full scale, **ratiometric to
AVDD**, which is why exciting from the same 3V3 rail is correct rather than
lazy (see `DESIGN_ASSUMPTIONS.md` §7.2).

| `J8` pin | Signal |
|---|---|
| 1 | **E+** — excitation positive |
| 2 | **E−** — excitation negative |
| 3 | **A+** — signal positive |
| 4 | **A−** — signal negative |

### What to confirm

**1. Bridge resistance** — this affects the power budget.

| Bridge | Excitation current at 3.3 V |
|---|---|
| 350 Ω | **9.4 mA** ← already budgeted as the worst case |
| 1 kΩ | 3.3 mA |

**2. Sensitivity in mV/V** — this decides whether gain 128 is right.

| Cell | Full-scale output at 3.3 V excitation | Verdict at gain 128 (±20 mV) |
|---|---|---|
| 1 mV/V | 3.3 mV | comfortable |
| 2 mV/V | 6.6 mV | fine |
| 6 mV/V | 19.8 mV | **at the limit** |
| > 6 mV/V | > 20 mV | **clips — drop to gain 64** |

Gain is selected by the HX711's clock-pulse count in firmware, so this is a
**software** change, not a hardware one. But you need to know the number.

**3. Wire colours — 🟠 do NOT assume.**

> The red/black/white/green convention is **not universal.** Chinese-sourced
> load cells frequently differ, and getting E and A swapped means the HX711
> reads the excitation rail instead of the bridge output.

**How to identify the pairs with a multimeter, reliably:**

1. Measure resistance between all six wire pairs.
2. The **two highest** readings are the *bridge input* pair (E+/E−) and the
   *bridge output* pair (A+/A−) — in a balanced bridge these are close.
3. The **four lower, roughly equal** readings are the individual arms.
4. Practically: the pair with the **highest** resistance is **E+/E−**. The
   remaining pair of the two "high" readings is **A+/A−**.
5. E+/E− polarity does not matter electrically for excitation, but A+/A−
   polarity determines whether the reading goes up or down under load — and
   that is trivially fixable in firmware. Get E and A right; do not worry
   about which way round A+ and A− are.

---

<table>
<tr><td bgcolor="#e65100">

## 🟠 H4 — Tactile switch footprint (`SW2`, `SW3`, `SW4`)

</td></tr>
</table>

> [!WARNING]
> A transposed switch **will not fit the board**. Check the drawing before you
> order PCBs.

The library footprint `TACT-6X6-THT` is the de-facto standard 6 × 6 mm
through-hole tactile geometry:

| Property | Value |
|---|---|
| Lead grid | **6.5 × 4.5 mm** |
| Drill | 1.0 mm |
| Internal bonding | leads **1–2** common, leads **3–4** common (TL1105 / B3F-10xx family) |

That internal bonding is why the library symbol uses EAGLE's **multi-pad
connect** (`pad="1 2"`): two physical pads, one electrical node. It is correct
and it is also why the schematic shows a two-terminal switch with four pads.

**What goes wrong.** Some 6 × 6 mm switches use **4.5 × 6.5 mm** — the same
grid rotated 90° — and some are 2-lead only. Both are sold as "6×6 tactile".

**How to clear it.** Open your chosen vendor part's mechanical drawing. Find
the lead pitch dimensions. Confirm **6.5 mm in the direction the footprint
expects**. If it is transposed, either:

- buy a different switch (easiest), or
- rotate the placement 90° in `design.py` (`rot` field on the part), or
- edit the footprint in `lib_defs.py` and re-run.

Used for `SW2` = RESET, `SW3` = BOOT, `SW4` = SOS.

---

<table>
<tr><td bgcolor="#e65100">

## 🟠 H5 — ESP32-S3 module variant: `-N8R2` is **not optional**

</td></tr>
</table>

$$\large\textcolor{orange}{\textsf{Order ESP32-S3-WROOM-1-N8R2. Do NOT substitute N8R8 or N16R8.}}$$

> [!WARNING]
> This is the single most likely purchasing mistake on the whole project,
> because the variants look identical and are usually the same price.

### Why

*ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8*, **Table 3-1, note b**: on
Octal-SPI-PSRAM modules (the `R8` and `R16V` variants), **IO35, IO36 and IO37
are connected to the PSRAM and are unavailable**.

This design uses **all three of them**:

| Pin | Net | Function |
|---|---|---|
| `IO35` | `ECG_LOD_P` | ECG leads-off detect, + input |
| `IO36` | `ECG_LOD_N` | ECG leads-off detect, − input |
| `IO37` | `ECG_SDN` | ECG front-end shutdown control |

Fitting an octal-PSRAM part **shorts three ECG control signals into the PSRAM
bus.** The module will probably still boot; the ECG channel will not work and
the PSRAM will be corrupted.

### And a second, quieter reason

`-N8R2` keeps **VDD_SPI at 3.3 V**. That makes `IO47` and `IO48` — the
**vibration motor and buzzer gate drives** — 3.3 V logic. On `R16V` parts
VDD_SPI is 1.8 V, and 1.8 V is not reliably enough to fully enhance an AO3400A
gate. You would get a hot, partially-on FET.

### How to clear it

1. When ordering, read the **full** part number on the listing, not the title.
   The suffix is printed on the module's own shield.
2. `N8` = 8 MB flash. `R2` = **2 MB quad-SPI PSRAM** ← this is what you want.
3. `R8` / `R16V` = 8 MB / 16 MB **octal**-SPI PSRAM ← do not buy.
4. If a supplier ships the wrong one, **do not fit it "just to test"**. It will
   read as a hardware fault in the ECG channel and cost you a day of debugging.

---

<table>
<tr><td bgcolor="#e65100">

## 🟠 H6 — Fabricator must support 5 mil / 0.127 mm trace and gap

</td></tr>
</table>

> [!WARNING]
> **Measured minimum copper clearance anywhere on the board: 0.130 mm.**
> A 6 mil (0.152 mm) process — which is frequently the *default* — cannot make
> this board.

### The numbers to quote the fab

| Parameter | Value |
|---|---|
| Copper layers | **4** |
| Minimum clearance, **measured** | **0.130 mm** |
| Clearance rule, general | 0.15 mm |
| Clearance rule, inside the 4 fine-pitch fan-outs | **0.127 mm (5 mil)** |
| Minimum track | **0.15 mm** (fine-pitch escapes only) |
| Track elsewhere | 0.20 mm signal, 0.50 mm power and motor |
| Minimum drill | **0.30 mm** |
| Board | 100 × 70 mm, 1.6 mm FR-4, 1 oz outer copper |
| Stack-up | `(1*2*15*16)` — layers 2 and 15 are **planes** |

### Why the board needs it — this is physics, not sloppiness

A **0.5 mm-pitch QFN cannot be escaped at 0.15 mm track / 0.15 mm gap.** Do
the arithmetic: 0.5 mm pitch with a 0.25 mm pad leaves 0.25 mm of gap between
adjacent pads. Putting a 0.15 mm track down the middle of that leaves
(0.25 − 0.15) / 2 = **0.05 mm** each side. It does not fit. Narrowing the
escape track to 0.15 mm and allowing 0.127 mm clearance **inside the fan-out
region only** is what makes it fit.

That exception applies **only inside four named rectangles** — around the
AD8232, LSM6DSOX, TMP117 and HX711. `scripts/validate_drc.py` enforces it as a
region, not globally, and any pair between 0.10 and 0.15 mm inside one of them
is printed as a NOTE rather than passed silently. Everywhere else the board
holds **0.154 mm or better** track-to-track.

### How to clear it

1. Go to your fab's ordering page (JLCPCB, PCBWay, Aisler, Eurocircuits…).
2. Set layers = 4.
3. Find the **"Minimum trace/spacing"** or **"Track/Gap"** option. It will
   probably default to **6/6 mil**. Change it to **5/5 mil**.
4. Confirm the price. On JLCPCB and PCBWay, 5 mil on 4 layers is a standard
   option; it may add a small charge or a longer lead time.
5. If a fab will not quote 5 mil, **do not just order it anyway.** They will
   either reject the file or, worse, build it with shorts. Instead see the
   fallback below.

### 🟠 Fallback if your fab is 6 mil only

The design can be widened to 6 mil, but it is real work and it costs you:

- change `FINE_PITCH_CLEARANCE` in `scripts/design.py` from `0.127` to `0.152`
- re-run `python scripts/generate_board.py` (it will re-route from scratch)
- **expect the unrouted-net count to rise above the current 4.** The fan-outs
  are the tightest spots on the board; giving them more clearance means fewer
  escapes fit.
- then finish more nets by hand in Fusion.

It is a viable path, not a dead end. See
[Part 18 — Workflow C](#part-18--workflow-c-change-the-design).

---

$$\Large\textcolor{gold}{\textsf{🟡 MEDIUM — 7 items}}$$

*Verify before or during bring-up. These affect performance, not safety.*
Full text in `documentation/REQUIRES_CONFIRMATION.md`.

| # | Item | One-line summary | How to clear |
|---|---|---|---|
| **M1** | ESP32-S3 EPAD land position | All 40 signal pads are ✅ verified against Espressif Fig. 11-1 including the pin-1 datum (7.49 mm below the antenna edge), so **the module will solder correctly**. The thermal pad is emitted as one conservative 3.4 mm land, deliberately **smaller** than the module's exposed metal, plus 9 plated vias. Espressif sub-divides it into a 3 × 3 array on a 3.7 mm span. | Open the footprint in Fusion against Espressif's downloadable land-pattern file (linked from datasheet §11.1). Worst case if offset ~1 mm: slightly worse thermal contact. **It cannot cause a short.** |
| ✅ **M2** | USB differential-pair impedance | **RESOLVED — calculated, see `documentation/USB_PAIR_ANALYSIS.md`.** The pair is **≈ 165 Ω, not 90 Ω (83 % high)**: it was routed as two ordinary signals with a 0.806 mm closest gap (2.24 × h), so the coupling term collapses to 5.6 % and you have two independent 87 Ω microstrips. | **No action needed.** ESP32-S3 USB is Full Speed only. 255 ps one-way over 44 mm vs a 115 mm conservative critical length at the fastest permitted 4 ns edge → **electrically short by 2.6×**, so it is lumped and the mismatch causes no reflections. Skew 5 ps. For 90 Ω you would need **0.40 mm wide / 0.16 mm gap on one layer**. |
| **M3** | Buzzer type | Drives `J17` low-side from `3V3` through `Q2`, `D8` flyback. **Firmware differs by type.** | **Active magnetic** (own oscillator) → drive `IO48` on/off; `D8` essential. **Passive piezo** → drive `IO48` with LEDC PWM at its resonance, typically 2–4 kHz; `D8` harmless. Confirm current draw; 30 mA budgeted. |
| **M4** | Piezo film capacitance vs `R38` | `R38` = 10 MΩ sets the corner at 1/(2π·10M·C_film). At an assumed ~1.5 nF that is ≈ **10 Hz**, suiting fetal movement (~1–10 Hz). | Measure the film's capacitance. Larger (10 nF+) → corner drops to ~1.6 Hz, which is fine or better. Much smaller → corner rises and low-frequency movement is attenuated; reduce `R38`. **`C34` must be ≥ 50 V rated** (specified `100n/50V`) — a piezo film's open-circuit transient reaches tens of volts. |
| ✅ **M5** | AS5600 3.3 V-mode strapping | **RESOLVED — the design is correct.** *AS5600 Datasheet [v1-06] 2018-Jun-20*, page 9, states verbatim: *"In 3.3V operation, the VDD5V and VDD3V3 pins must be tied together. VDD is the voltage level present at the VDD5V pin."* The board ties both to `3V3`. Per-pin decoupling matches page 3 (100 nF on `VDD5V`, 1 µF on `VDD3V3`). | **No action needed.** |
| **M6** | Magnet for the AS5600 | The AS5600 measures a diametrically-magnetised on-axis magnet. **No magnet mount exists on this PCB** — it is a mechanical-design item. | Specify magnet type (diametric NdFeB, typically 6 × 2.5 mm), air gap 0.5–3 mm, centred over the IC within ~0.25 mm. If it must live at the belt's rail joint instead, move it to a flying lead on `J6` — the angle bus is already brought out there. |
| **M7** | TMP117 measures **pod** temperature, not skin temperature | `U4` is on the main board because that is where the architecture diagram puts it. Inside an electronics pod it measures the pod's internal temperature, influenced by the LDO, the charger and the ESP32. | Decide whether skin temperature is actually required. If yes, **relocate the TMP117 to a short flex tail** with the sensor against the skin — the sensor I²C bus is already on `J4`. **This is a real measurement problem, not a layout nicety.** |

---

$$\Large\textcolor{gray}{\textsf{⚪ LOW — 4 items}}$$

| # | Item | Summary |
|---|---|---|
| **L1** | Mounting holes are not at four corners | `H1` (3, 3), `H2` (97, 3), `H4` (97, 67) are corners. **`H3` is at (2.6, 42)** — mid-left edge — because the top-left corner is inside the module's antenna keep-out and a plated hole there would detune the antenna. Confirm the enclosure accepts that pattern. |
| **L2** | `J3` on/off switch polarity is **inverted** | `R4` pulls the LDO's `EN` up to `VBAT`, so **the default state is ON**, and **closing a switch across `J3` turns the board OFF.** Silkscreened `OFF SW`. Deliberate — it avoids inventing an unverified slide-switch footprint — but it is the opposite of what most people expect. **Tell whoever wires the enclosure.** |
| **L3** | Silkscreen legibility at 1.0 mm | Reference designators use EAGLE's vector font at 0.8–1.1 mm. Most fabs hold 0.8 mm with a 0.15 mm stroke; some do not. Check your fab's minimum, increase the text sizes in `scripts/lib_defs.py` if needed. |
| **L4** | Supplier part numbers absent from the BOM | Deliberate. Distributor stock could not be checked, and a fabricated SKU is worse than a blank field. **Manufacturer** part numbers come from datasheet ordering guides and are correct. Fill in Supplier / Supplier PN / Lifecycle from your own distributor — particularly for the AD8232 (occasionally allocated) and the LSM6DSOX. |

---

## 🔵 And one requirement that is not in the blocker list at all

> [!IMPORTANT]
> ### Firmware **must** implement a low-battery cut-off at 3.5 V.
>
> This is not optional and it is not a nicety. It is a hardware limitation that
> only firmware can cover.

The AP2112K-3.3 LDO has **250 mV typical dropout at 600 mA**. So as the cell
discharges:

| `VBAT` | 3V3 rail output | ESP32-S3 (min 3.0 V) |
|---|---|---|
| 4.2 V (full) | 3.30 V | fine |
| 3.7 V (nominal) | 3.30 V | fine |
| 3.55 V | 3.30 V | at the edge of regulation |
| 3.30 V | ≈ 3.05 V | 🟠 **marginal** |
| 3.10 V | ≈ 2.85 V | 🔴 **below minimum — brown-out** |

**Implement:** read `VBAT_SENSE` on `IO9`. The divider is 470 k / 470 k, so
**3.5 V at the cell reads 1.75 V at the pin.** Below that, stop sampling,
notify the app, and enter deep sleep.

**Why it matters:** without this the board browns out unpredictably at the
bottom of the discharge curve. Unpredictable behaviour in a device with an
**SOS button** is worse than a clean shutdown. Code in
[Part 23](#part-23--workflow-h-firmware).

---

## ✅ The one-page blocker summary

Print this. Tick it.

| | Item | Blocks | Cleared by | Time |
|---|---|---|---|---|
| 🔴 | **B1** Protected cell + JST polarity | **powering the board** | buying a protected pack; one meter check | 10 min |
| 🔴 | **B2** ECG safety protocol | **attaching electrodes** | a written rule everyone follows | 10 min |
| 🔴 | **B3** Motor rating vs `R45` | **connecting the motor** | choosing a motor, then arithmetic | 30 min |
| 🟠 | **H5** Module must be `-N8R2` | **ordering parts** | reading the full part number | 2 min |
| 🟠 | **H6** Fab must quote 5 mil | **ordering PCBs** | one dropdown at the fab | 5 min |
| 🟠 | **H4** Switch pin grid 6.5 × 4.5 mm | **ordering PCBs** | reading a mechanical drawing | 10 min |
| 🟠 | **H2** `R37` stretch divider | *nothing* — reworkable | choosing the sensor | 20 min |
| 🟠 | **H3** Load cell bridge + mV/V | *nothing* — firmware gain | metering the cell | 20 min |
| 🟠 | **H1** MAX17048 decision | *nothing* | decide: breakout, divider only, or add it | 5 min |
| 🔵 | **Low-battery cut-off at 3.5 V** | **reliable operation** | ~15 lines of firmware | 30 min |

**Realistically:** B1, B2, H5, H6, H1 are decisions and purchases you can
settle today. B3, H2, H3, H4 need you to pick parts. Nothing here requires
re-designing the board.

---

# PART 2 — What this project actually is

## The one-paragraph version

This directory contains the **electronics** for the Smart Maternity Band: a
100 × 70 mm, four-layer prototype carrier PCB built around an
**ESP32-S3-WROOM-1-N8R2**, carrying an **AD8232** single-lead ECG front end, an
**LSM6DSOX** 6-axis IMU, an **AS5600** magnetic angle sensor, a **TMP117**
temperature sensor, an **HX711** load-cell ADC, four FSR channels, a stretch
sensor channel, a piezo fetal-movement channel, a vibration motor and buzzer
driver pair, an SOS button, a microSD header, and a **TP4056 + AP2112K-3.3**
Li-Po charge-and-regulate power section. It is a complete verified component
library, a seven-sheet schematic, a placed and largely routed board, and about
eighteen documents explaining every decision — all **generated from a single
Python model** so that nothing can drift out of step.

## The problem it solves

**SIH26113** asks for a maternity assist device. The wider Smart Maternity
Band concept is a dual-layer wearable that combines:

- **mechanical support** — lumbar and abdominal load relief, which is where the
  load cell, the FSR array, the stretch sensor and the angle sensor come in;
- **continuous monitoring** — maternal ECG / heart rate, temperature, posture
  and activity, plus fetal movement.

This board is the electronics pod for that. The parent repository holds the
concept website; this subdirectory is the hardware.

## The seven functional blocks

They map 1:1 onto the seven schematic sheets **and** onto the seven placement
zones on the board. That is deliberate — it means a signal you find on sheet 4
is physically in zone Z3, and you can follow it with your eyes.

| # | Block | Sheet | Zone | Implementation |
|---|---|---|---|---|
| 1 | **Power entry / charging / regulation** | 1 | Z1 (4,4)–(32,36) | Li-Po via JST-PH (`J1`), 5 V charge input (`J2`), **TP4056** charger at 500 mA, **AP2112K-3.3** 600 mA LDO, battery-voltage sense to ADC, fuel-gauge breakout header (`J4`) |
| 2 | **Central MCU** | 2 | Z2 (1,40)–(34,70) | **ESP32-S3-WROOM-1-N8R2** — Wi-Fi + BLE 5, 8 MB flash, 2 MB quad PSRAM, native USB-Serial-JTAG; RESET and BOOT buttons, UART header, two status LEDs |
| 3 | **ECG analog front end** | 4 | Z3 (66,4)–(98,40) | **AD8232** three-electrode configuration with driven right-leg (RLD), two-pole high-pass, gain 1100, per-electrode DC leads-off detection |
| 4 | **I²C sensors** | 3 | Z4 (34.5,31)–(63,49) | **TMP117** temperature, **LSM6DSOX** 6-axis IMU with both interrupts, **AS5600** magnetic angle sensor **on a separate I²C bus** |
| 5 | **Mechanical sensing** | 5 | Z5 (34.5,4)–(63,30) | **HX711** load-cell ADC, 4 × FSR dividers, stretch-sensor divider, piezo conditioning with over-voltage clamps, hall/limit input |
| 6 | **FET-driven alerts** | 6 | Z6 (66,50)–(98,68) | Two N-FET low-side drivers — vibration motor on `VBAT`, buzzer on `3V3` — each with a flyback diode and a fail-safe gate pull-down |
| 7 | **User input / storage** | 7 | Z7 (34.5,50)–(63,68) | SOS button with RC debounce and ESD series resistor, microSD SPI module header |

Plus **19 test points** and **four M2 mounting holes**.

## The numbers, at a glance

| Metric | Value |
|---|---|
| Board outline | **100 × 70 mm** (70 cm²) |
| Copper layers | **4** — L1 signal / **L2 GND plane** / **L15 3V3 plane** / L16 signal |
| Board thickness | 1.6 mm FR-4 |
| Outer copper | 1 oz (35 µm) |
| Schematic sheets | **7** |
| Parts in the model | **167** (150 placed on the board; the difference is supply symbols, which are schematic-only) |
| Library symbols | 28 |
| Library footprints | **23** |
| Library devices | 30 |
| Nets | **84** |
| Pin connections | **420** |
| Test points | 19 |
| Mounting holes | 4 × M2 |
| Track segments emitted | **4 523** |
| Vias | **486** (160 plane-connect, 15 thermal / exposed-pad, rest from routing) |
| Signal nets fully routed | **76 of 80 (95 %)** |
| BOM line items | **75** |
| Measured minimum copper clearance | **0.130 mm** |

## Why it looks like a Python project

Because it is one. There is no EDA software installed where these files were
produced, so instead of drawing a schematic by hand, the project **describes**
the design in `scripts/design.py` and generates the EAGLE files from it.

That started as a constraint and turned into the best thing about the project:

> One model produces the library, the schematic, the board, the netlist
> document, the GPIO table, the BOM, the ERC report, the DRC report, the
> statistics and the renders. **They cannot disagree with each other.**

And the generators verify themselves:

- `generate_schematic.py` **re-parses its own output** and asserts the emitted
  netlist matches the model exactly.
- `generate_board.py` does the same for elements and signals.
- `render.py` draws only primitives it finds by parsing the real `.sch` and
  `.brd` — **so a render cannot show something the board does not have.**

If the model and the files ever diverge, the build **fails** rather than
quietly emitting something wrong.

Full explanation in [Part 6](#part-6--the-generated-from-source-model).

## Three things the architecture diagram got wrong

The input to this whole project was a single architecture image
(`reference/PCB_architecture_source.jpeg`). It was treated as a **starting
point, not as truth** — and it had real bugs. The three biggest:

### 1. An I²C address clash that cannot work

The diagram puts TMP117, LSM6DSOX, AS5600 **and** MAX17048 on one shared bus.

> 🔴 **The AS5600 and the MAX17048 are both hard-wired to address `0x36`, and
> neither has an address-select pin.** Two devices at the same address on the
> same bus is not a performance problem; it is a bus that does not function.

**Resolved** with two physically separate busses, using both of the ESP32-S3's
I²C controllers:

| Bus | Pins | Devices |
|---|---|---|
| **SENSOR** (I2C0) | `IO15` / `IO16` | TMP117 `0x48`, LSM6DSOX `0x6A`, fuel-gauge header `0x36` |
| **ANGLE** (I2C1) | `IO14` / `IO42` | AS5600 `0x36`, plus `J6` for a second one |

A *second* AS5600 still clashes with the first, and that is acknowledged rather
than hidden: `J6` carries the angle bus **plus a fifth pin to `IO3` through a
DNP 0 Ω link (`R17`)**, so you can use the second sensor's analog output, an
external TCA9548A mux, or a software bus — without the board committing you to
one. Full reasoning: `DESIGN_ASSUMPTIONS.md` §5.

### 2. "TP4056 protected module" hid a missing safety circuit

See 🔴 **B1** in Part 1. The diagram's word *protected* referred to a purchased
module's DW01A + FS8205A, which a bare-IC implementation does not have.

### 3. It implied two layers would do

They do not. Measured, not assumed:

| Layers | Nets the router completed (of 81 at the time) |
|---|---|
| 2 | **~50**, and the board's reachable copper split into disconnected regions |
| 4 | **77** |

The AD8232 amplifies a sub-millivolt biopotential by 1100 across 10 MΩ nodes,
and its datasheet asks for a ground plane. With 81 signal nets and 15
through-hole connectors, two layers leaves **no continuous reference under the
analog section**. Cost of going to four layers: a couple of dollars per
prototype board. Full evidence: `DESIGN_ASSUMPTIONS.md` §2.

All seven documented architecture changes are in
[Part 25](#part-25--the-seven-architecture-changes).

---

# PART 3 — Exactly how complete this is

This part exists because "is it done?" is the question that gets answered
dishonestly most often in hardware projects. Here is the honest answer.

## The three levels

| Level | Meaning | Status |
|---|---|---|
| **1 — Architecture** | Blocks and intent | ✅ **Complete** |
| **2 — Electrical schematic + verified library** | Real parts, real pinouts, real values, connectivity checked | ✅ **Complete** |
| **3 — Manufacturable PCB** | Placed, routed, DRC-clean, manufacturing files out | 🟨 **Substantially complete** — geometry is DRC-clean, 4 airwires remain **by choice**, Gerbers need Fusion's CAM |

**This project is at Level 2 complete, Level 3 substantially complete.**

## ✅ What is genuinely done

### The component library

- **23 footprints, 28 symbols, 30 devices.**
- **Every pinout verified against the manufacturer's datasheet.** Not from
  memory, not inferred from the architecture picture.
- Three footprints come from the **vendor's own recommended land-pattern
  drawing** (ESP32-S3-WROOM-1, TMP117 WSON, LSM6DSOX LGA). The rest are
  **IPC-7351B Nominal (Level B)** land patterns derived from verified body
  dimensions.
- Self-check passes: every symbol pin maps to an existing pad, no orphan pads,
  no pad overlaps.

### The schematic

- **7 sheets, 167 parts, 84 nets, 420 pin connections.**
- **Every pin is on exactly one net.** No floating pins, no pin on two nets.
- An independent **11-rule-group ERC passes with 0 errors and 0 warnings**
  (7 informational notes, all explained).
- The generator re-parses its own `.sch` and asserts the netlist matches the
  model exactly. That assertion passes.

### The board

- **4 layers, 100 × 70 mm.** All **150** components placed in the seven
  functional zones.
- **Both power planes poured** (`GND` on L2, `3V3` on L15), drawn as an
  L-shape that omits the antenna corner.
- **Antenna keep-out enforced** — 20 × 6.6 mm at the top edge, no pad, via or
  track inside it, planes cut around it.
- **Exposed pads via-stitched** — 15 thermal vias, all **plated** board-level
  vias (see the defect list below for why that matters).
- **4 523 track segments, 486 vias.**
- Independent geometric DRC: **0 clearance, width, drill, placement, keep-out
  or board-edge violations.** Minimum measured copper clearance **0.130 mm**.

### Routing — and the concession that was made deliberately

**76 of 80 signal nets routed (95 %).** The remaining 4 are **airwires by
choice, not routing failures.**

> **Clearance is prioritised over completeness.** Where the router could only
> finish a net by coming closer than the 0.15 mm rule, it **rips the net out
> and leaves an airwire** instead.
>
> An airwire is **visible in Fusion the moment the board opens** and is a
> minute's work to route by hand. A 0.05 mm gap is **invisible** and might
> reach fabrication.

The four, with the gap each would have needed:

| Net | Came within | Of | Layer |
|---|---|---|---|
| `I2C_SDA` | 0.075 mm | `FSR1_ADC` | 1 |
| `SD_CS` | 0.090 mm | `LED_ALERT` | 1 |
| `SD_MISO` | 0.145 mm | `ESP_EN` | 1 |
| `ESP_EN` | 0.145 mm | `PIEZO_ADC` | 1 |

Finishing them is **step 13** of the build guide and should take under half an
hour — every one is a short connection whose two ends are already fanned out.

### The independent design review

`documentation/FINAL_REVIEW.md` is a second-pass review against **27 specific
failure modes**. It found and fixed **10 real defects** and left 5 items open
and documented. Those ten are worth knowing about because they show what the
review was actually for:

| Defect found | Why it mattered |
|---|---|
| **Unplated holes drilled through thermal pads** | EAGLE's `<hole>` inside a package is an **unplated** mechanical hole. Through a thermal land that is a defect — a hole with no barrel conducts no heat and breaks the pad. Moved to board-level **plated** vias. |
| **Clearance measured as a diamond, not a disc** | The obstacle dilation used Manhattan distance, so diagonal clearances were overstated by up to √2. Replaced with a Euclidean disc. |
| **Fan-out stubs crossing neighbouring pads** | Escape tracks were being drawn straight across an adjacent pad — a short. |
| **Plane-via spurs crossing neighbouring pads** | Same failure in the plane-connection code path. |
| **Rip-up cascading damage** | A non-transactional rip-up took the unrouted count from 4 to **33** while the counter still claimed success. Fixed with snapshot/restore and a recount from final state. |
| 🔴 **SOT-23-5 land pattern shorted VIN to GND** | The pad length and width were swapped, putting 1.10 mm pads on a 0.95 mm pitch. **This is the LDO.** It looked perfectly plausible in the library editor. |
| **LGA-14 land enlargement closed corner pairs to 0.11 mm** | IPC enlargement on a 0.5 mm LGA pushed corner pads together. Reverted to 1:1 with the package pad. |
| **The DRC measured round pads as squares** | Overstated clearance violations near every through-hole pad, masking real ones. |
| **The clearance model assumed every conductor was nominal width** | A 0.50 mm power track was checked as if it were 0.20 mm. |
| **Placement collisions from hand-picked coordinates** | Replaced with a resolver that enforces a 0.90 mm courtyard gap. |
| 🔴 **Plane vias placed outside the pour outline** | The pours are L-shaped — for x < 29.5 they stop at y = 63.0 to stay clear of the antenna. Two `GND` vias sat *above* that edge, and one of them was **`C7`'s only connection to the ground plane** — the HF bypass at the module's supply pin. DRC rule D7 asked "does the pad have a via on its net?" and never asked whether the via lands inside the pour. Found by `validate_planes.py`. |

That SOT-23-5 one is the reason this project has an independent review at all.

## ❌ What has NOT been done — stated plainly

| Item | Status |
|---|---|
| Autodesk EAGLE / Fusion **ERC** | ❌ **NOT EXECUTED — TOOL UNAVAILABLE.** No EAGLE installation existed. An independent ERC was written and run instead. |
| Autodesk EAGLE / Fusion **DRC** | ❌ **NOT EXECUTED — TOOL UNAVAILABLE.** An independent geometric DRC was written and run instead. |
| **Copper-pour geometry** | 🟨 **PARTLY CLOSED.** `scripts/validate_planes.py` now *measures* pour connectivity — it punches an antipad around every through-hole and via, labels connected regions, and checks every plane-net contact lands in the main one. Both pours: **one dominant region ≥ 99.9 %, ECG zone entirely inside it, 0 orphans.** **This check found a real defect** (`C7`'s ground via outside the pour). EAGLE's *exact* fill is still computed on load — run `RATSNEST`. |
| **Gerber / drill files** | ❌ **NOT GENERATED.** Needs EAGLE's CAM processor. |
| **3D / mechanical interference** | ❌ **NOT CHECKED.** No STEP models are attached to these footprints. A height table and an isometric extrusion exist instead. |
| **USB pair impedance** | ✅ **CALCULATED** — `documentation/USB_PAIR_ANALYSIS.md`. ≈ 165 Ω, not 90 Ω, but electrically short by 2.6× at Full Speed so it is not a functional risk. |
| **Component availability** | ❌ **NOT VERIFIED.** Distributor stock could not be checked. `BOM.csv` carries empty Supplier / Supplier PN / Lifecycle columns rather than invented ones. |
| **Physical prototype** | ❌ **NOT BUILT.** **No figure in this project is a measurement.** Every current, voltage and frequency is a datasheet typical or a calculation. |

> **Nothing here is claimed as passing a tool that was never run.**

## The verification summary table

| Check | Tool | Result |
|---|---|---|
| Library model consistency | `generate_library.py` | ✅ PASS |
| Schematic vs. model | `generate_schematic.py` | ✅ PASS — 84 nets, 420 pinrefs, exact match |
| ERC, 11 rule groups | `validate_erc.py` | ✅ **0 errors, 0 warnings** |
| Board vs. model | `generate_board.py` | ✅ PASS — 150 elements, 84 signals |
| DRC, 8 rule groups | `validate_drc.py` | ✅ **0 geometry violations**; min clearance **0.130 mm**. The 4 reported errors are all unrouted nets |
| Routing | `generate_board.py` | 🟨 **76 / 80 (95 %)**, 4 deliberate clearance concessions |
| Independent design review, 27 failure modes | `FINAL_REVIEW.md` | ✅ 10 defects found and fixed, 5 open and documented |
| EAGLE / Fusion ERC | — | ❌ NOT EXECUTED |
| EAGLE / Fusion DRC | — | ❌ NOT EXECUTED |

## What "finishing" this project looks like

**The design work is essentially complete.** What remains is entirely things
that cannot be done from a text editor: decisions, purchases, a licensed EDA
tool, a soldering iron, and a person.

### The critical path, with what each phase is actually blocked on

| # | Phase | Effort | **Blocked on** | Where |
|---|---|---|---|---|
| 1 | 🔴 **Clear the 3 BLOCKING items** | **~1 hour** | buying a **protected** Li-Po; **writing down** the ECG protocol; **picking** a motor | [Part 1](#part-1--the-blockers-read-this-before-anything-else) |
| 2 | 🟠 **Clear H2–H6** | **~1 hour** | picking the stretch sensor, load cell and switch; **a fab quote at 5 mil** | [Part 1](#part-1--the-blockers-read-this-before-anything-else) |
| 3 | Open in Fusion, run **its** ERC + DRC | **half a day** | Fusion installed | [Part 19](#part-19--workflow-d-open-it-in-autodesk-fusion-all-20-steps), steps 6 & 15 |
| 4 | Finish the remaining airwires by hand | **~30 min** | step 3 done first | Part 19, step 13 |
| 5 | Generate + **inspect** Gerbers, drill, paste | **~1 hour** | Fusion's CAM processor | Part 19, step 19 |
| 6 | Order PCBs + **stencil** + parts | 1 hour, then **1–3 weeks lead** | 🟠 **H5 and H6 settled first** | [Part 20](#part-20--workflow-e-order-the-pcb) |
| 7 | Assemble | **1 day** | stencil + reflow or hot air | [Part 21](#part-21--workflow-f-assemble-the-board) |
| 8 | Bring-up, six stages | **2 days** | boards in hand | [Part 22](#part-22--workflow-g-bring-up-in-six-stages) |
| 9 | Firmware | **weeks** | — | [Part 23](#part-23--workflow-h-firmware) |

### The dependency order, because two of these are easy to get wrong

```
  B1/B2/B3  ──────────────┐
  (decisions, ~1 h)       │
                          ▼
  H5 (-N8R2) ────────►  ORDER PARTS ──────┐
  H6 (5 mil) ────────►  ORDER PCBs ───────┤  1-3 weeks lead
  H4 (switch grid) ──►  + STENCIL  ───────┘        │
                                                   ▼
  Install Fusion ──► ERC ──► finish airwires ──► DRC ──► GERBERS
       (step 3)                 (step 4)              (step 5)
                                                   │
                                                   ▼
                              ASSEMBLE ──► BRING-UP ──► FIRMWARE
                               (1 day)      (2 days)     (weeks)
```

> 🟠 **The two easy mistakes, both one dropdown each:**
> **H5** — ordering `-N8R8` instead of `-N8R2`, which kills the ECG channel.
> **H6** — accepting the fab's default 6 mil, which this board fails at
> 0.130 mm measured clearance.
>
> 🔵 **And note steps 5 and 6 are independent of each other.** You can order
> PCBs from the Gerbers only *after* step 5, but you can order the **parts**
> as soon as H5 is settled. Do that early — the AD8232 is occasionally
> allocated (⚪ L4).

### Realistically

| | |
|---|---|
| **Today, at a desk** | steps 1 and 2 — all decisions and purchases, ~2 hours total |
| **This week** | steps 3–5 — Fusion, airwires, Gerbers. About a day of real work |
| **Then 1–3 weeks** | waiting on the fab |
| **Then ~3 days** | assemble and bring up |
| **Then weeks** | firmware |

---

# PART 4 — Absolute-beginner setup

This part assumes **nothing**. If you already have Python and Fusion, skip to
[Part 5](#part-5--every-single-file-explained).

## 4.1 — What you actually need, and when

There are three completely separate toolchains here, and **you do not need all
of them.** Work out which one you are in.

| I want to… | I need | I do **not** need |
|---|---|---|
| **Read and understand the design** | a Markdown viewer and an image viewer. That's it. | Python, Fusion, anything else |
| **Regenerate the files after changing something** | Python 3.11+ with numpy, matplotlib, Pillow | Fusion |
| **Open, inspect, finish and manufacture the board** | Autodesk Fusion (Electronics) | Python |
| **Write the firmware** | ESP-IDF or Arduino-ESP32, and a USB-serial cable | Python, Fusion |
| **Assemble the board** | soldering gear, a stencil, a hotplate or hot-air station | all software |

**Nobody needs all four at once.** Pick the one matching what you are doing
today.

## 4.2 — Getting the files

```bash
git clone <your-repository-url>
```

Then:

```bash
cd Smart-India-Hackaton/SIH26113_Maternity_Assist_Belt
```

Everything for the PCB lives in that one directory. Nothing outside it belongs
to this work.

**If you were handed a ZIP instead:** unzip it somewhere with **no spaces and
no non-ASCII characters in the path**. `C:\work\sih\` is fine.
`C:\Users\Ayşe's Files\New folder (2)\` will cause problems with some EDA
tooling.

## 4.3 — A Markdown viewer (5 minutes, everyone needs this)

Every document in this project is Markdown. You can read them in Notepad, but
you will have a bad time — the tables will be unreadable.

**Pick one:**

| Option | How | Notes |
|---|---|---|
| **VS Code** (recommended) | install it, open the folder, press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd> on any `.md` file | free, cross-platform, also gives you the Python tooling later |
| **GitHub / your Git host** | just browse the repo in a browser | renders the 🔴/🟠 alert blocks properly, which local viewers may not |
| **Typora / Obsidian / MarkText** | open the folder | fine |
| **Any browser + a Markdown extension** | — | fine |

> **Note on the coloured blocks in this document.** The 🔴 red and 🟠 orange
> callouts use GitHub's alert syntax (`> [!CAUTION]`, `> [!WARNING]`) plus
> LaTeX-coloured headings plus emoji. **GitHub renders all three.** Local
> viewers render at least the emoji and the bold. If you see literal
> `[!CAUTION]` text, your viewer does not support alerts — the content is still
> correct, just less shouty. Read Part 1 anyway.

## 4.4 — Python, for regenerating the project

**Only needed if you are going to change the design.** If you are just opening
the existing `.brd` in Fusion, skip this.

### Check whether you already have it

```bash
python --version
```

You want **3.11 or newer**. The project was developed and last run on **Python
3.14.6**. If you get "command not found" or a 2.x/3.8 version, install a
current Python.

### Install Python

| OS | How |
|---|---|
| **Windows** | download from [python.org](https://www.python.org/downloads/) and **tick "Add python.exe to PATH"** during install. Or `winget install Python.Python.3.13` |
| **macOS** | `brew install python@3.13` |
| **Linux (Debian/Ubuntu)** | `sudo apt install python3 python3-pip python3-venv` |

### Install the three dependencies

```bash
python -m pip install numpy matplotlib Pillow
```

Versions last verified working:

| Package | Version | Used by |
|---|---|---|
| `numpy` | 2.5.3 | `router.py` — the occupancy grid and the Euclidean-disc dilation |
| `matplotlib` | 3.11.1 | `render.py` — all 12 PNGs |
| `Pillow` | 12.3.0 | `render.py` — image handling |

**Nothing else is required.** No EDA library, no external binary, no network
access. The EAGLE XML is written with Python's standard library.

### Recommended: use a virtual environment

Keeps this project's packages away from the rest of your system.

```bash
python -m venv .venv
```

Then activate it:

| Shell | Command |
|---|---|
| Windows PowerShell | `.\.venv\Scripts\Activate.ps1` |
| Windows cmd | `.\.venv\Scripts\activate.bat` |
| Git Bash / macOS / Linux | `source .venv/bin/activate` |

Then `python -m pip install numpy matplotlib Pillow`.

### Verify it works

```bash
python scripts/generate_library.py
```

You should see the library self-check pass and
`libraries/SIH26113_Maternity_Assist_Belt.lbr` be rewritten. If that works,
your Python setup is complete.

> **What goes wrong:** `ModuleNotFoundError: No module named 'numpy'` means the
> virtual environment is not active, or you installed into a different Python
> than the one running the script. Check with
> `python -c "import sys; print(sys.executable)"`.

## 4.5 — Autodesk Fusion (Electronics), for the PCB work

### What to install

**Autodesk Fusion.** The Electronics workspace — what used to be sold as
EAGLE — is built into it. The **free personal-use licence includes
Electronics**, which is enough for this entire project.

1. Go to Autodesk's Fusion page and choose the **personal / hobbyist** licence.
2. Create an Autodesk account (free).
3. Download and install. It is a large install; budget 30–60 minutes.
4. Launch it and sign in.
5. Switch to the **Electronics** workspace.

### 🟠 Version compatibility — this matters

| Tool | Reads these files? |
|---|---|
| **Autodesk Fusion** (any current version) | ✅ yes |
| **Autodesk EAGLE 9.x** standalone | ✅ yes |
| **EAGLE 7.x** or older standalone | ❌ **no** — these files use the EAGLE 9 XML format |
| KiCad | ⚠️ partially — KiCad can import EAGLE libraries and schematics, with losses. Not the intended path and not tested. |

If Fusion offers **"Migrate EAGLE project"**, say **yes**.

### What you do NOT need to buy

- No Fusion Electronics paid tier. The personal licence handles a 100 × 70 mm
  4-layer board.
- No third-party libraries. The library is included, and the `.sch` and `.brd`
  each carry a **full embedded copy** of it — so they open correctly even if
  you never import the `.lbr` separately.

## 4.6 — Firmware toolchain

**Only needed once you have hardware.** Two choices:

| Option | Install | Best for |
|---|---|---|
| **ESP-IDF** (recommended) | Espressif's installer, or the VS Code ESP-IDF extension | full control, real projects, proper ADC calibration |
| **Arduino-ESP32** | Arduino IDE → Boards Manager → "esp32 by Espressif" | fastest to a blinking LED |

Board selection: **ESP32S3 Dev Module** with **8 MB flash** and **QSPI
PSRAM enabled**.

### 🟡 Serial port note

This board's `J2` USB header goes to the ESP32-S3's **native USB-Serial-JTAG**
on `IO19`/`IO20`. That means:

- **No CP2102 / CH340 driver is needed.** The MCU *is* the USB device.
- On Windows it appears as a **USB Serial Device (COMx)**. On Linux,
  `/dev/ttyACM0`. On macOS, `/dev/cu.usbmodem*`.
- If it does not appear at all, `J5` (the 6-way UART header) is the documented
  fallback path — see 🟡 M2 and [Part 24](#part-24--troubleshooting-encyclopedia).

## 4.7 — Bench and assembly gear

Listed here so you can order it early — some of it has lead time.

### Minimum to bring up the power stage safely

| Item | Why | Notes |
|---|---|---|
| **Bench power supply with current limit** | 🔴 the single most useful safety tool you can own | set 5 V, limit 100 mA for first power-on. A short shows as the limit engaging, not as smoke. |
| **Multimeter** | measuring `TP1`–`TP4`, and 🔴 **B1's polarity check** | any meter |
| **Fine-tip soldering iron**, 0.4–0.8 mm chisel | everything through-hole and 0805 | temperature-controlled |
| **Solder wick + flux** | you will need both | no-clean flux |
| **Tweezers**, fine | placing 0805s | ESD-safe |

### Required for the three fine-pitch parts

> 🟠 **The AD8232, LSM6DSOX and TMP117 cannot be soldered with an iron.**

| Item | Why |
|---|---|
| **Solder-paste stencil** | order it **with the boards** — see [Part 20](#part-20--workflow-e-order-the-pcb). This is the item people forget. |
| **Leaded solder paste** (Sn63Pb37) or SAC305 | leaded is more forgiving by hand |
| **Hotplate or reflow oven**, *or* a **hot-air rework station** | either works |
| **Stencil jig / frame**, or tape and a stiff card | to hold the stencil aligned |

### Very useful

| Item | Why |
|---|---|
| **Oscilloscope** | 🔵 essentially required for the ECG stage. `TP10` (`ECG_OUT`) and `TP11` (`ECG_REFOUT`) are there specifically for this. |
| **USB microscope** or a loupe | inspecting 0.5 mm-pitch solder joints |
| **Logic analyser** | I²C debugging on `TP18`/`TP19` |
| **ECG electrodes**, disposable Ag/AgCl, 3 off | for `J7` |
| **Diametric NdFeB magnet**, ~6 × 2.5 mm | for the AS5600 — see 🟡 M6 |

## 4.8 — A five-minute sanity check that everything is set up

Run these in order. Each should succeed.

```bash
python --version
```

```bash
python -c "import numpy, matplotlib, PIL; print('deps ok')"
```

```bash
python scripts/validate_erc.py
```

That last one should end with `RESULT: PASS` and `--- ERRORS (0) ---`. If it
does, you have a working Python environment and a valid design model.

```bash
python scripts/validate_drc.py
```

This one ends with `RESULT: FAIL` — **and that is expected.** The four
"errors" are the four deliberately-unrouted nets. Read
[Part 15](#part-15--verification-what-was-checked-and-how) before you worry
about it.

---

# PART 5 — Every single file, explained

There are 54 files. This part covers **all** of them: what it is, why it
exists, when you would read it, and whether it is hand-written or generated.

## 5.1 — The directory tree

```
SIH26113_Maternity_Assist_Belt/
│
├── README.md                      ← the short entry point
├── FULL_INSTRUCTION_TUTORIAL.md   ← this document
│
├── libraries/
│   └── SIH26113_Maternity_Assist_Belt.lbr    EAGLE 9 / Fusion library
│
├── schematic/
│   └── SIH26113_Maternity_Assist_Belt.sch    7 sheets
│
├── pcb/
│   ├── SIH26113_Maternity_Assist_Belt.brd    4-layer board
│   ├── route_report.json                     the router's own output
│   ├── drc_result.json                       DRC findings, machine-readable
│   └── plane_result.json                     plane-pour connectivity
│
├── fusion_project/           ← OPEN THIS IN FUSION
│   ├── *.lbr + *.sch + *.brd  the three files together, same base name,
│   │                          because EAGLE pairs a schematic with a board
│   │                          by filename AND directory  (see 5.8)
│   └── README.md
│
├── documentation/            18 documents — see 5.3
│
├── renders/                  12 PNGs — see 5.4
│
├── reference/
│   └── PCB_architecture_source.jpeg          the input architecture diagram
│
└── scripts/                  16 Python files — see 5.5
```

## 5.2 — The three EDA files (the actual deliverables)

### `libraries/SIH26113_Maternity_Assist_Belt.lbr`

**What:** the EAGLE 9 / Fusion component library. XML, human-readable if you
open it in a text editor.

**Contains:** 23 packages (footprints), 28 symbols (schematic representations),
30 devicesets (the pairing of a symbol with a footprint, plus pin-to-pad
mapping and part attributes).

**Why it exists separately:** so you can place *new* parts from it. The `.sch`
and `.brd` each carry a **full embedded copy**, so they open correctly even if
you never import this file.

**When you touch it:** you don't — it is generated by
`scripts/generate_library.py`. If you need a new footprint, edit
`scripts/lib_defs.py` and re-run.

**How to inspect it:** Fusion → Library Manager → Import. Or read the XML: it
is genuinely legible, and `<package>`, `<symbol>` and `<deviceset>` blocks are
easy to follow.

### `schematic/SIH26113_Maternity_Assist_Belt.sch`

**What:** the seven-sheet schematic.

| Sheet | Title |
|---|---|
| 1/7 | POWER ENTRY, CHARGING AND 3V3 REGULATION |
| 2/7 | ESP32-S3 CENTRAL MCU, RESET/BOOT, PROGRAMMING, INDICATORS |
| 3/7 | I2C SENSORS (TMP117, LSM6DSOX, AS5600) — TWO BUSSES |
| 4/7 | ECG ANALOG FRONT END (AD8232) |
| 5/7 | MECHANICAL SENSING (LOAD CELL, FSR, STRETCH, PIEZO, HALL) |
| 6/7 | FET-DRIVEN ALERTS (VIBRATION MOTOR, BUZZER) |
| 7/7 | USER INPUT AND STORAGE (SOS, microSD) |

**167 parts, 84 nets, 420 pin connections.**

**Generated by:** `scripts/generate_schematic.py`, which then **re-parses its
own output** and asserts the emitted netlist matches the model exactly.

**When you touch it:** never by hand. Edit `design.py`.

### `pcb/SIH26113_Maternity_Assist_Belt.brd`

**What:** the four-layer board.

| Property | Value |
|---|---|
| Outline | 100 × 70 mm on layer 20 |
| `layerSetup` | `(1*2*15*16)` |
| Elements | **150** |
| Signals | **84** |
| Wires | **~4 523** |
| Vias | **486**, all through-hole (`extent="1-16"`) |
| Plane polygons | 2 — `GND` on L2, `3V3` on L15 |
| Design-rule set | `SIH26113_4layer` with `mdWireWire=0.127mm`, `msWidth=0.15mm`, `msDrill=0.3mm` |

**Generated by:** `scripts/generate_board.py`, which places, routes and emits,
then re-parses and cross-checks elements and signals.

## 5.3 — `documentation/` — all 18 documents

Ordered by when you would actually read them.

| # | File | Lines | Written or generated | What it is, and when to read it |
|---|---|---|---|---|
| 1 | 🔴 **`REQUIRES_CONFIRMATION.md`** | 324 | hand-written | **Read this first, before anything else.** Every open item, ordered by consequence: **3 BLOCKING, 6 HIGH, 5 MEDIUM (M2 and M5 now resolved), 5 LOW**, plus a table of items resolved during design so they are not re-opened. Reproduced and expanded in [Part 1](#part-1--the-blockers-read-this-before-anything-else). |
| 2 | **`FINAL_REPORT.md`** | 243 | generated | The single-document summary: what was created, exact file list, components and variants, unresolved components, assumptions, ERC status, DRC status, net and component counts, dimensions, layers, risks, what needs physical verification, and the exact next steps in Fusion. **If you read only one document, read this one.** |
| 3 | **`PCB_BUILD_GUIDE.md`** | ~522 | hand-written | 20 numbered steps from installing Fusion to ordering boards, each with **Do / Check / What goes wrong**. Plus the six-stage bring-up order and the regeneration commands. Expanded in [Part 19](#part-19--workflow-d-open-it-in-autodesk-fusion-all-20-steps). |
| 4 | **`DESIGN_ASSUMPTIONS.md`** | 556 | hand-written | **The most important document for understanding *why*.** 15 numbered sections covering power architecture, the four-layer decision with measured evidence, board size, module variant, the two-I²C-bus resolution, the ECG front end, mechanical sensing, alerts, GPIO constraints, grounding, microSD, USB, protection, placement strategy, and "things I would do differently". Contains all seven **[ARCHITECTURE CHANGE]** markers. |
| 5 | **`COMPONENT_VERIFICATION.md`** | 210 | hand-written | Every part, its verification level, and **the specific document the pinout came from**. Explains how the datasheets were read (including rasterising vector-only drawings at 5× to read dimensions from figures). Sections A–G by part category. Read this if you doubt any pinout. |
| 6 | **`GPIO_ASSIGNMENT.md`** | 66 | generated | All 41 module pins: pad number, function, net, direction, boot-criticality, ADC channel, peripheral, what it connects to, and notes. Plus the pin budget and the strapping-pin analysis. **Essential for firmware.** |
| 7 | **`POWER_BUDGET.md`** | 191 | hand-written | Itemised current budget per rail with the source of every figure, the dropout analysis that produces the 🔵 3.5 V cut-off requirement, charging figures, trace-width justification with IPC-2221 arithmetic, and a deep-sleep estimate. |
| 8 | **`ECG_FRONTEND_DESIGN.md`** | 381 | hand-written | The AD8232 circuit with all the arithmetic: signal chain, supply-rail constraint, patient protection, three-electrode DC leads-off, right-leg drive, reference network, the two-pole high-pass and its factor of 100, the low-pass and gain, source-impedance interaction, resulting response, and the firmware requirements the circuit imposes. |
| 9 | **`USB_PAIR_ANALYSIS.md`** | ~180 | hand-written | The USB differential pair, calculated. Closes 🟡 M2. As-routed ≈ 165 Ω vs the 90 Ω USB asks for, why that is not a functional risk at Full Speed, and the geometry that *would* give 90 Ω. |
| 10 | **`GROUNDING_NOTES.md`** | 219 | hand-written | Why **one** ground net and not a split AGND/DGND, with three specific arguments. Stack-up, placement separation, motor return-current confinement, via stitching, and why the antenna keep-out cuts *all* copper including planes. |
| 11 | **`NETLIST.md`** | 111 | generated | All 84 nets: type, voltage, source, loads, routing status, notes. |
| 12 | **`BOM.md`** | 129 | generated | 75 line items, 150 placements, grouped by value. Manufacturer PNs from datasheet ordering guides. Plus placements-by-package with assembly method, an assembly note, and **"parts NOT on this board"** with the reason for each. |
| 13 | **`BOM.csv`** | — | generated | Machine-readable BOM with three deliberately-empty columns: **Supplier**, **Supplier PN**, **Lifecycle**. See ⚪ L4. |
| 14 | **`ERC_REPORT.md`** | 62 | generated | The 11 rule groups, the full run output (**0 errors, 0 warnings, 7 notes**), and a table of intentional exceptions with why each is acceptable. Leads with the ❌ NOT EXECUTED note about EAGLE's own ERC. |
| 15 | **`DRC_REPORT.md`** | 158 | generated | The 8 rule groups, stack-up as emitted, the clearance rules and the one declared exception, the full run output, routing completeness, the four deliberately-unrouted nets with the gap each would have needed, and what has *not* been verified. |
| 16 | **`MANUFACTURING_CHECK.md`** | 83 | generated | The 19-point pre-fab check with the value the files actually contain. Plus connector accessibility, assembly feasibility, and the mechanical height envelope. |
| 17 | **`FINAL_REVIEW.md`** | 440 | hand-written | The independent second-pass review: **10 defects found and fixed** (each with what it was and why it mattered), then the **27-point review** against specific failure modes with ✅ / ⚠️ per item. |
| 18 | **`PROJECT_STATISTICS.md`** | 77 | generated | Counts and metrics, placements by footprint, and the test-point table. |

> The machine-readable companions to these live in `pcb/`: `route_report.json`, `drc_result.json` and `plane_result.json`.

### The two machine-readable files in `pcb/`

| File | What it is |
|---|---|
| `route_report.json` | the router's own output: per-net status, the reason for each unrouted net, attempt counts, the winning seed |
| `plane_result.json` | plane-pour connectivity per layer per pass: region count, areas, orphaned contacts, ECG-zone membership |
| `drc_result.json` | every DRC finding as structured data, so you can diff it between runs |
| `plane_result.json` | plane-pour connectivity per layer per pass: region count, areas, orphaned contacts, ECG-zone membership |

## 5.4 — `renders/` — all 12 PNGs

**Every one of these is drawn by parsing the real `.sch` / `.brd`** and
rendering the primitives found there. A render **cannot** show something the
files do not contain. That is the point.

| File | What it shows | Use it for |
|---|---|---|
| `schematic_p1.png` | Sheet 1 — power entry, charging, regulation | reviewing the power section without opening Fusion |
| `schematic_p2.png` | Sheet 2 — ESP32-S3 core | checking the module wiring |
| `schematic_p3.png` | Sheet 3 — I²C sensors, both busses | verifying the two-bus split |
| `schematic_p4.png` | Sheet 4 — ECG front end | following the AD8232 signal chain |
| `schematic_p5.png` | Sheet 5 — mechanical sensing | FSR / load cell / piezo / stretch / hall |
| `schematic_p6.png` | Sheet 6 — FET-driven alerts | checking flyback polarity by eye |
| `schematic_p7.png` | Sheet 7 — user input and storage | SOS and microSD |
| `pcb_top.png` | Layer 1 copper, pads, silkscreen | seeing the top-side routing density |
| `pcb_bottom.png` | Layer 16 copper | seeing how much emptier the bottom is |
| `pcb_layers.png` | **all four copper layers** side by side | understanding the stack-up and the plane cut-outs |
| `pcb_assembly.png` | placement + reference designators + zone boxes | **the most useful one for assembly** — print it |
| `pcb_3d.png` | isometric mechanical envelope from the height table | sizing an enclosure, spotting a connector that fouls a lid |

> ⚠️ `pcb_3d.png` is an **extrusion of a height table**, not a solid model.
> Heights are colour-coded by source: datasheet-derived vs. typical. It is
> enough to size an enclosure; it is **not** a 3D interference check, and no
> such check has been done.

## 5.5 — `scripts/` — all 16 Python files

Detailed in [Part 7](#part-7--every-script-explained). Summary here:

| File | Lines | Role |
|---|---|---|
| ★ **`design.py`** | 1 025 | **the single source of truth.** Board dimensions, stack-up, planes, keep-outs, zones, mounting holes, escape channels, clearances, net classes, all 167 parts, all 84 nets, the GPIO table |
| **`lib_defs.py`** | 1 178 | 23 packages, 28 symbols, 30 devicesets, thermal-via definitions, the package height table |
| **`eagle_common.py`** | 592 | the EAGLE layer table, XML emitters, IPC-7351B land-pattern generators |
| **`geom.py`** | 103 | pin/pad geometry and coordinate transforms |
| **`router.py`** | 628 | the grid router: occupancy grids, Euclidean-disc dilation, 8-connected A*, transactional rip-up |
| `generate_library.py` | 175 | → `.lbr`, plus the library self-check |
| `generate_schematic.py` | 222 | → `.sch`, plus the self-cross-check |
| `generate_board.py` | 949 | place + route + emit `.brd`, plus fan-outs, repair and concession passes |
| `validate_erc.py` | 280 | the 11-group independent ERC |
| `validate_drc.py` | 421 | the 8-group independent geometric DRC |
| **`validate_planes.py`** | ~330 | **plane-pour connectivity** — antipad punching, connected-component labelling, per-contact region membership |
| `render.py` | 490 | → all 12 PNGs |
| `generate_docs.py` | 608 | → NETLIST, GPIO_ASSIGNMENT, BOM.md/csv, ERC_REPORT, DRC_REPORT, PROJECT_STATISTICS |
| `gen_reports.py` | 691 | → MANUFACTURING_CHECK (19 items), FINAL_REPORT (15 sections) |
| `make_fusion_project.py` | ~95 | → `fusion_project/` — the `.lbr`/`.sch`/`.brd` in one folder so Fusion pairs them |
| `build_all.py` | ~60 | runs all of the above in the correct order |
| `.gitignore` | 2 | ignores `__pycache__/` and `*.pyc` |

## 5.6 — `reference/PCB_architecture_source.jpeg`

The **input** to the whole project: the architecture diagram this design was
derived from.

Kept deliberately, for two reasons:

1. **Traceability.** Every deviation from it is marked
   **[ARCHITECTURE CHANGE]** in `DESIGN_ASSUMPTIONS.md`, and you can only
   check that against the original.
2. **Honesty about the starting point.** It was treated as a starting point,
   **not as truth** — and it had three real bugs (see
   [Part 2](#part-2--what-this-project-actually-is)).

## 5.7 — Which files are safe to hand-edit

| File | Hand-edit? |
|---|---|
| `scripts/design.py`, `lib_defs.py`, and the other scripts | ✅ **yes — this is where you make changes** |
| `documentation/*.md` marked hand-written | ✅ yes |
| `README.md`, `FULL_INSTRUCTION_TUTORIAL.md` | ✅ yes |
| Anything with `<!-- GENERATED by scripts/... -->` at the top | ❌ **no** — re-run the script; your edit will be overwritten |
| `.lbr`, `.sch`, `.brd` | ⚠️ you *can* edit these in Fusion, and at some point you will have to (finishing the airwires). But then **Fusion becomes the source of truth for that change** and re-running the generators will discard it. See [Part 18](#part-18--workflow-c-change-the-design) for how to handle that fork. |
| `route_report.json`, `drc_result.json`, `plane_result.json` | ❌ no |
| `fusion_project/*` | ⚠️ **these are generated copies.** Editing them is fine — that is what they are for — but `make_fusion_project.py` overwrites them from `libraries/`, `schematic/` and `pcb/`. Once you start working in Fusion, **stop running it.** See 5.8. |
| `renders/*.png` | ❌ no |

> 🟠 **The fork problem, stated early because it will bite you.** The moment
> you route an airwire in Fusion, the `.brd` contains something the model does
> not. Re-running `generate_board.py` will throw that away. Decide, and write
> it down: either **the model is authoritative** (make all changes in
> `design.py`, re-run, re-route by hand each time) or **Fusion is
> authoritative from here on** (stop re-running `generate_board.py`). Both are
> defensible. Mixing them silently is not. [Part 18.7](#187--the-fork-problem-model-vs-fusion)
> covers this properly.

## 5.8 — `fusion_project/` — the folder you actually open

**Why it exists.** EAGLE and Fusion pair a schematic with a board **by
filename and directory**: opening `foo.brd` makes the tool look for `foo.sch`
*beside it*. **No link is stored inside either file.**

This project keeps them in `schematic/` and `pcb/` because that is more
legible to read. The consequence is that opening either one from its own
folder loads it **standalone** — the schematic↔board consistency check cannot
run, and forward/back annotation is off. You would probably not notice until
an edit in one failed to appear in the other.

So `scripts/make_fusion_project.py` copies the `.lbr`, `.sch` and `.brd` into
one flat folder with a shared base name:

```bash
python scripts/make_fusion_project.py
```

It is also the **last step of `build_all.py`**, so it stays current.

| | |
|---|---|
| **Open this** | `fusion_project/SIH26113_Maternity_Assist_Belt.sch` |
| Not this | `schematic/…sch` — loads standalone |
| Canonical source | `libraries/`, `schematic/`, `pcb/` — what the generators write |
| `fusion_project/` is | **copies**, regenerated on demand |

> 🟠 **These are copies, so there are two of each file in the repository.**
> That is a deliberate trade: ~800 KB of duplication buys a folder that opens
> correctly for someone who does not have Python installed. If you would rather
> not commit it, add `fusion_project/` to `.gitignore` and run
> `make_fusion_project.py` after cloning.
>
> **The moment you edit in Fusion, `fusion_project/` becomes the authoritative
> copy** — see [Part 18.7](#187--the-fork-problem-model-vs-fusion).

---

# PART 6 — The generated-from-source model

## 6.1 — Why the project is built this way

A normal PCB project is drawn: you place symbols on a schematic canvas, wire
them, then push them into a layout editor. There was no EDA software available
in the environment where this project was produced, so it was **described**
instead — in Python — and the EAGLE files were generated from that description.

That started as a workaround. It ended up being the strongest property of the
project, for one reason:

> **One model produces the library, the schematic, the board, the netlist
> document, the GPIO table, the BOM, the ERC report, the DRC report, the
> statistics and every render. They cannot disagree with each other.**

In a hand-drawn project, the BOM drifts from the schematic, the GPIO table in
the wiki drifts from the actual netlist, and the "min clearance" figure in the
README drifts from the board. Here, all of those are derived from the same
1 025-line file. If you change a resistor value in `design.py`, the schematic,
the board, the BOM and the netlist document all change together, or the build
fails.

## 6.2 — The self-verification, which is the other half of the idea

Generating files is easy. Generating **correct** files is the problem. So each
generator checks its own output:

| Generator | What it asserts about its own output |
|---|---|
| `generate_library.py` | every symbol pin maps to an existing pad; no orphan pads; no pad overlaps within a package |
| `generate_schematic.py` | **re-parses the emitted `.sch`** and asserts the netlist extracted from it matches the model exactly — 84 nets, 420 pinrefs |
| `generate_board.py` | **re-parses the emitted `.brd`** and asserts elements and signals match the model — 150 elements, 84 signals |
| `validate_drc.py` | deliberately **shares no code with the router**, so it is capable of contradicting it |
| `render.py` | draws **only** primitives found by parsing the real `.sch` / `.brd` — a render cannot show something the files do not contain |

> That last one is worth dwelling on. In most projects a "3D render" is a
> separate artefact that can be beautiful and wrong. Here, if a track is
> missing from the `.brd`, it is missing from `pcb_top.png`. The renders are
> evidence, not marketing.

And `validate_drc.py` not sharing code with `router.py` is the reason the
"clearance measured as a diamond" defect was **found**. The router thought it
was clear; the independent DRC measured it and disagreed.

## 6.3 — `design.py` — the single source of truth

1 025 lines. Everything that defines *this* board, as opposed to how EAGLE
files are written, lives here.

### Board-level constants

```python
BOARD_W        = 100.0     # mm
BOARD_H        = 70.0      # mm
BOARD_LAYERS   = 4
BOARD_THICKNESS = 1.6      # mm FR-4
COPPER_OZ      = 1
```

### The stack-up and the planes

```python
PLANE_LAYERS = {2: "GND", 15: "3V3"}
```

EAGLE layer **2** (`Route2`) carries the solid `GND` pour; layer **15**
(`Route15`) carries the solid `3V3` pour. `layerSetup` in the emitted `.brd` is
`(1*2*15*16)`.

`PLANE_OUTLINE` is the polygon both pours use. It is **L-shaped** — it
deliberately omits the antenna corner, because:

```python
ANTENNA_KEEPOUT = (9.0, 63.4, 29.0, 70.0)   # x1, y1, x2, y2 in mm
```

> 🟡 **The keep-out cuts *all* copper, planes included.** A ground plane under
> a PCB antenna does not "shield" it — it detunes it and kills the range. This
> is why mounting hole `H3` is at (2.6, 42) instead of the top-left corner
> (⚪ L1).

### The seven placement zones

```python
ZONES = [
    ("Z1  POWER ENTRY / CHARGING / 3V3",  4.0,  4.0, 32.0, 36.0),
    ("Z2  ESP32-S3 CORE",                 1.0, 40.0, 34.0, 70.0),
    ("Z5  MECHANICAL SENSING",           34.5,  4.0, 63.0, 30.0),
    ("Z4  I2C SENSORS",                  34.5, 31.0, 63.0, 49.0),
    ("Z7  USER INPUT / STORAGE",         34.5, 50.0, 63.0, 68.0),
    ("Z3  ECG ANALOG FRONT END",         66.0,  4.0, 98.0, 40.0),
    ("Z6  FET-DRIVEN ALERTS",            66.0, 50.0, 98.0, 68.0),
]
```

Each zone corresponds 1:1 to a schematic sheet. **The ECG block (Z3) is in the
far corner from the alerts block (Z6)** — that is the placement half of the
grounding strategy (see [Part 12](#part-12--grounding-and-the-stack-up)).

### Mounting holes

```python
MOUNT_HOLES = [(3.0, 3.0), (97.0, 3.0), (2.6, 42.0), (97.0, 67.0)]
```

Three corners plus one mid-left-edge. See ⚪ L1.

### The escape channels — the most important placement constraint

```python
ESCAPE_CHANNELS = [
    (0.90, 43.0,  9.50, 64.0),    # left of the module's pad column
    (28.50, 40.0, 34.20, 64.0),   # right of the module's pad column
    (8.00, 36.00, 29.00, 44.20),  # below the module's end row
]
CHANNEL_EXEMPT = {"C7", "C8", "R7", "C10"}
```

The comment in the source says it best:

> The ESP32-S3-WROOM-1 presents **40 lands on a 1.27 mm pitch across three
> edges**; without a dedicated escape corridor outboard of each land row there
> is simply nowhere for those 40 signals to go, and the router (or a human)
> stalls. These bands are the **single most important placement constraint on
> the board.**

`CHANNEL_EXEMPT` allows the module's own decoupling (`C7`, `C8`) and its reset
network (`R7`, `C10`) inside the left channel — keeping `C7`/`C8` within ~2 mm
of module pin 2 matters more than the two track slots they cost, and both are
on a plane net anyway.

### The clearance model

```python
FINE_PITCH_CLEARANCE = 0.127   # inside a fan-out envelope
GENERAL_CLEARANCE    = 0.15    # everywhere else
EDGE_CLEAR           = 0.40    # copper to board edge
COURTYARD_GAP        = 0.90    # between component courtyards

FANOUT_ENVELOPE = {
    "AD8232":   6.6,   # half-size, mm
    "LSM6DSOX": 4.8,
    "TMP117":   4.1,
    "HX711":    8.0,
}
```

Those four envelopes are the **only** places the 0.127 mm rule applies. See
🟠 H6 for why the exception is physics rather than a fudge.

### Net classes

```python
NET_CLASSES = [
    # (id, name,         width, drill, clearance)   all mm
    (0, "default",        0.20, 0.3, 0.15),
    (1, "power",          0.50, 0.4, 0.20),
    (2, "motor",          0.50, 0.4, 0.20),
    (3, "analog_ecg",     0.20, 0.3, 0.20),
]

POWER_NETS = {"GND", "3V3", "VBAT", "VBUS"}
MOTOR_NETS = {"MOTOR_P", "MOTOR_N"}
ECG_NETS   = { ... 15 ECG nets ... }
```

`net_class(name)` maps a net name to a class id. `PROJECT_STATISTICS.md` and
`POWER_BUDGET.md` both read their track-width figures **from this table**, so
the documents cannot drift from the board. (They did once — see
[Part 26](#part-26--known-limitations-honestly).)

> **Note the signal and power widths are narrower than the 0.25 / 0.60 mm this
> design started with.** They were reduced *deliberately*: a narrower track
> needs less clearance around it, and that bought back the routing density lost
> when the clearance model was corrected to measure Euclidean distance.
> **Ampacity was never the binding constraint** — 0.50 mm carries ≈ 1.45 A
> against a 620 mA worst case, which is **2.3× margin**.

### Parts

```python
@dataclass
class Part:
    ref: str              # "R45"
    deviceset: str        # "R-0805"
    value: str            # "0R"
    desc: str             # human-readable purpose
    sheet: int            # 1..7
    sx: float; sy: float  # schematic position, mm
    srot: str = "R0"
    bx: float = 0.0       # board position, mm
    by: float = 0.0
    brot: str = "R0"
    mpn: str = ""
    manufacturer: str = ""
    package_note: str = ""
```

Parts are added with a helper that appends to a module-level list:

```python
def P(*a, **kw) -> Part:
    p = Part(*a, **kw)
    PARTS.append(p)
    return p
```

So the part list reads as a literal declaration, sheet by sheet:

```python
# ---- SHEET 4 - ECG ANALOG FRONT END ----
P("R20", "R-0805", "330k", "RLD output current limit (datasheet: >330k at 3.0 V)", ...)
```

**167 parts.** Note that 167 in the model vs **150 placed** on the board — the
difference is supply symbols (`SUPPLY1.GND` etc.), which exist on the schematic
to make power connections legible and have no physical footprint.

### Nets

```python
NETS: dict[str, list[tuple[str, str]]] = {}

def N(net: str, *conns: str) -> None:
    """Add connections written as 'REF.PIN'."""
    lst = NETS.setdefault(net, [])
    for c in conns:
        ref, pin = c.split(".", 1)
        lst.append((ref, pin))
```

So a net is declared by naming every pin on it:

```python
N("GND",
  "SUPPLY1.GND", "SUPPLY5.GND", ...,
  "J1.2", "J2.4", "U1.GND", "R1.2", "C1.2", "C2.2",
  "U3.GND@1", "U3.GND@40", "U3.EPAD", ...
  "H1.1", "H2.1", "H3.1", "H4.1", ...)
```

**84 nets, 420 connections.** Note `U3.GND@1` — EAGLE's syntax for one of
several same-named pins on a symbol.

### The GPIO table

```python
GPIO_TABLE: list[Gpio] = [
    Gpio("IO0", "27", "BOOT strap / boot button", "ESP_IO0", "IO", True, "-", "-",
         "SW3, R8, J5.6",
         "Weak internal pull-up. Held low at reset = download mode."),
    Gpio("IO1", "39", "ECG analog output", "ECG_OUT", "ANALOG IN", False,
         "ADC1_CH0", "ADC1", "U7 via R30/C22",
         "ADC1 is the only ADC usable while the radio is on."),
    ...
]
```

Fields: module pin, physical pad, function, net, direction, **boot-critical**,
ADC channel, peripheral, what it connects to, and notes. This table is what
`GPIO_ASSIGNMENT.md` is generated from, **and** it is what ERC rule R9 checks
the design against — so a GPIO used in a net but missing from this table is an
ERC error, not a documentation gap.

## 6.4 — The floorplan resolver

The per-part board coordinates in `PARTS` were laid out for an earlier, smaller
outline. Rather than restating 150 coordinates, `design.py` translates each
schematic sheet **as a block**:

```python
SHEET_OFFSET = {
    1: (3.0,  3.0),    # Z1 power / charging
    2: (2.0, 10.0),    # Z2 ESP32 core
    3: (6.0,  5.0),    # Z4 I2C sensors
    4: (13.0, 3.0),    # Z3 ECG analog
    5: (6.0,  3.0),    # Z5 mechanical sensing
    6: (13.0, 10.0),   # Z6 alerts
    7: (6.0, 10.0),    # Z7 user input / storage
}
```

Every part keeps its position **relative to the pin it serves** — a decoupling
capacitor stays next to its IC. Then parts whose position is a *mechanical*
decision are pinned explicitly:

```python
EDGE_PLACEMENT = {
    # bottom edge: every sensor / power lead leaves here
    "J2":  (12.0, 3.0, "R0"),      # USB / 5 V charge input
    "J4":  (25.0, 3.0, "R0"),      # fuel-gauge breakout
    "J8":  (38.0, 3.0, "R0"),      # load cell (JST-PH-4)
    "J15": (48.5, 3.0, "R0"),      # hall / limit switch
    "J14": (56.0, 3.0, "R0"),      # piezo
    # FSR + stretch: vertical headers so they do not wall off the board
    "J9":  (35.5, 10.0, "R90"),
    "J10": (35.5, 16.0, "R90"),
    "J11": (35.5, 22.0, "R90"),
    "J12": (35.5, 28.0, "R90"),
    "J13": (61.0, 10.0, "R90"),
    # left edge
    "J5":  (2.3, 30.0, "R90"),     # UART programming header
    "J1":  (2.3, 51.0, "R90"),     # Li-Po battery
    "J3":  (2.3, 12.0, "R90"),     # external on/off switch
    # right edge
    "J7":  (97.2, 21.0, "R90"),    # ECG electrodes
    "J17": (97.2, 57.5, "R90"),    # buzzer
    # top edge
    "J16": (86.0, 67.0, "R180"),   # vibration motor
    "J18": (46.0, 67.0, "R0"),     # microSD SPI module
    "J6":  (63.0, 40.0, "R90"),    # optional second AS5600
}
```

> **Why the FSR headers are vertical and inboard.** A long horizontal row of
> through-hole pads across the board is **a wall through both signal layers**.
> Four vertical 1×2 headers in a column cost far less routing area. That is
> also why manufacturing check item 10 reports 6 interior connectors — all six
> take a flying lead from a belt-mounted transducer, so none of them needs a
> board edge.

Then `resolve_placement()` runs a collision resolver that enforces
`COURTYARD_GAP = 0.90 mm` between every pair of courtyards and respects
`ANTENNA_KEEPOUT`, the escape channels and the fan-out keep-outs. This exists
because the tenth defect found in review was **"placement collisions from
hand-picked coordinates"** — 150 coordinates chosen by hand will always collide
somewhere.

`clearance_exceptions()` returns the four fine-pitch rectangles (derived from
`FANOUT_ENVELOPE`) that `validate_drc.py` uses to apply the 0.127 mm rule
**by region**.

## 6.5 — `lib_defs.py` — the component library definition

1 178 lines. **23 packages, 28 symbols, 30 devicesets.**

### The three vendor-drawing footprints

These were **not** IPC-generated. They come from the manufacturer's own
recommended land-pattern drawing, because a vendor drawing beats a generic
calculation every time:

| Function | Package | Key verified detail |
|---|---|---|
| `_esp32_s3_wroom1()` | ESP32-S3-WROOM-1 | **Y_PIN1 = BODY_Y/2 − 7.49** — the pin-1 datum is 7.49 mm below the antenna edge, from Espressif Fig. 11-1. Getting this datum wrong shifts all 40 pads. |
| `_lfcsp20()` | AD8232 LFCSP-20, 4 × 4 mm, 0.5 mm pitch | with the 2.50 mm exposed pad |
| `_wson6()` | TMP117 WSON-6 (TI DRV0006B) | with the thermal pad |
| `_lga14()` | LSM6DSOX LGA-14L, 2.5 × 3.0 mm | `PAD_L, PAD_W = 0.45, 0.25` — **1:1 with the package pad, no IPC enlargement.** Enlargement closed the corner pairs to 0.11 mm; that was defect #7. |

### `THERMAL_VIAS`

Defines the plated vias that stitch each exposed pad to the ground plane —
**9 for the ESP32 module's EPAD**, plus the AD8232 and TMP117 thermal pads.

> 🔵 **These are board-level vias, not package holes.** EAGLE's `<hole>`
> element inside a package is an **UNPLATED** mechanical hole. Drilling an
> unplated hole through a thermal land conducts no heat and breaks the pad.
> That was defect #1, and it is exactly the kind of thing that looks fine in a
> library editor.

### `PACKAGE_HEIGHT`

Every package's height, **labelled by source** — `"datasheet"` or
`"typical"`. This drives both `pcb_3d.png` and the mechanical envelope table in
`MANUFACTURING_CHECK.md`.

Tallest part: **8.50 mm** — the 2.54 mm headers, mated with a crimp housing.
Minimum internal enclosure height therefore about **11.6 mm** including the
substrate and a little clearance.

## 6.6 — `eagle_common.py` — the EAGLE XML layer

592 lines. This is the file that knows about **EAGLE**, as opposed to knowing
about *this board*.

### The layer table

The standard EAGLE layer numbers, **plus two additions** needed for a 4-layer
board:

```python
(2,  "Route2"),      # inner GND plane
(15, "Route15"),     # inner 3V3 plane
```

### The XML emitters

Functions that write `<smd>`, `<pad>`, `<wire>`, `<polygon>`, `<via>`,
`<text>`, `<hole>`, `<package>`, `<symbol>`, `<deviceset>`, `<element>`,
`<signal>` and the `<designrules>` block.

### The IPC-7351B land-pattern generators

Generic packages (0805, SOT-23, SOIC, SOP, SOD-123, headers, JST-PH) are
generated to **IPC-7351B Nominal (Level B)** from verified body dimensions.

### 🔴 The `sot23_package()` fix, preserved as a comment

This is the single most important comment in the codebase:

```python
# The pads sit on the top and bottom edges, so the RADIAL direction is Y
# and the TANGENTIAL direction is X. ... Getting these the wrong way
# round makes 1.10 mm pads on a 0.95 mm pitch overlap - a short between
# adjacent pins that looks perfectly plausible in the library editor.
dx, dy = pad_w, pad_l
```

**That was defect #6, and the part it affected was `U2`, the 3.3 V LDO.** A
VIN-to-GND short on the regulator would have destroyed every board in the first
batch, and it would have been invisible on screen.

## 6.7 — `geom.py`

103 lines. Pin and pad geometry, and coordinate transforms — rotating a pad set
by R0/R90/R180/R270, computing courtyards, mapping symbol pins to package pads.
Small, boring, and used by everything.

---

# PART 7 — Every script, explained

Fourteen files. Roughly 6 400 lines of Python. Here is what each one does, in
the order the build runs them.

## 7.1 — The build order, and why it is that order

```python
STEPS = [
    ("library",              "generate_library.py",   True),
    ("ERC",                  "validate_erc.py",       True),
    ("schematic",            "generate_schematic.py", True),
    ("board (place + route)","generate_board.py",     True),
    ("DRC",                  "validate_drc.py",       False),  # airwires reported, not fatal
    ("plane integrity",      "validate_planes.py",    False),
    ("renders",              "render.py",             False),
    ("documents",            "generate_docs.py",      True),
    ("reports",              "gen_reports.py",        True),
    ("fusion project folder","make_fusion_project.py",True),
]
```

The third column is **fatal** — whether a non-zero exit stops the build.

**Why this order:**

1. The **library must be valid** before the schematic can reference it.
2. **ERC must pass** before a board is worth routing. There is no point
   spending two minutes routing a design with a floating input.
3. The **board** needs a valid schematic netlist.
4. **DRC** measures the emitted board.
5. **Documents** read the route report and the DRC report that steps 4 and 5
   write — so they must come last.

DRC is marked non-fatal because it *will* report the four deliberate airwires
as errors, and that must not stop the documents from being generated. This is
the one place where "FAIL" is expected.

## 7.2 — `generate_library.py` (175 lines)

**Produces:** `libraries/SIH26113_Maternity_Assist_Belt.lbr`

**Does:**

1. Walks `lib_defs.py`'s package, symbol and deviceset definitions.
2. Emits EAGLE 9 library XML with the full layer table and `eagle.dtd`
   reference.
3. Runs the **library self-check**:
   - every symbol pin maps to an existing pad in the paired package
   - no orphan pads (a pad with no pin, other than thermal/mechanical ones)
   - no pad overlaps within a package ← *this is the check that would have
     caught the SOT-23-5 short, and now does*

**Run it alone:**

```bash
python scripts/generate_library.py
```

**Exit non-zero** if the self-check fails. This is fatal in `build_all.py`.

## 7.3 — `validate_erc.py` (280 lines)

**Produces:** console output, consumed by `generate_docs.py` to write
`ERC_REPORT.md`.

**The eleven rule groups:**

| # | Rule |
|---|---|
| **R1** | reference designators unique; every deviceset exists in the library |
| **R2** | every (part, pin) in the netlist names a pin that actually exists |
| **R3** | every pin of every part is on **exactly one** net — no floating pins, no pin on two nets |
| **R4** | no net has fewer than two connections, except declared no-connects |
| **R5** | every net feeding a power pin also carries a supply symbol |
| **R6** | no net has two or more push-pull outputs |
| **R7** | no net has inputs but no driver |
| **R8** | each I²C line has exactly one pull-up; no address clash **on a bus** |
| **R9** | ESP32-S3: analog only on ADC1; strapping pins flagged; every module pin present in the GPIO table |
| **R10** | MOSFET gates have a pull-down; inductive loads have a **correctly-oriented** flyback diode; clamp polarity |
| **R11** | every LED has a series resistor |

**The declared no-connects:**

```python
DECLARED_NO_CONNECT = {
    "LDO_NC":      ...,   # AP2112 pin 4 is documented "No Connection"
    "IMU_OCS_AUX": ...,   # LSM6DSOX: leave electrically unconnected but soldered
}
```

R5, R6 and R7 skip these. **They are declared explicitly rather than
silenced** — the difference matters, because a silenced warning is
indistinguishable from a missed one.

**Result: ✅ 0 errors, 0 warnings, 7 notes.**

Two of those notes are worth reading:

```
N: [R8] 0x36 is used on BOTH busses (MAX17048 breakout on the sensor bus,
        AS5600 on the angle bus). This is the deliberate resolution of the
        fixed-address clash - they are electrically separate busses.
N: [R10] Q1: flyback D7 present on MOTOR_N
```

R10 checking flyback **orientation** rather than just presence is the reason
this design's diode polarity is verified rather than assumed. A backwards
flyback diode is a dead short across the supply the moment you power up.

**Run it alone:**

```bash
python scripts/validate_erc.py
```

Ends with `RESULT: PASS`. **Fatal in `build_all.py` if it does not.**

## 7.4 — `generate_schematic.py` (222 lines)

**Produces:** `schematic/SIH26113_Maternity_Assist_Belt.sch`

**Does:**

1. Emits seven `<sheet>` elements with the sheet titles from
   `SHEET_TITLES`.
2. Places every part at its `(sx, sy, srot)`.
3. Draws nets as `<segment>`/`<wire>`/`<pinref>` structures.
4. Embeds a **full copy of the library**, so the file opens standalone.
5. **Re-parses its own output** and asserts the extracted netlist matches the
   model exactly.

That last step is the whole point:

```
schematic cross-check PASS — 7 sheets, 167 parts, 84 nets, 420 pinrefs
```

If the emitter had a bug that dropped a `<pinref>`, this assertion catches it.
A hand-drawn schematic has no equivalent safety net.

## 7.5 — `router.py` (628 lines)

The grid router. Explained properly in
[Part 14](#part-14--how-the-router-works) — here is the API surface.

### Key constants

```python
MIN_CLEARANCE      = 0.15
NOMINAL_HALF_WIDTH = 0.100
STEP_ORTHO = 10      # A* cost of an orthogonal step
STEP_DIAG  = 14      # ≈ 10·√2, so 45° is correctly priced
VIA_COST   = 60      # a via costs six orthogonal steps
```

### The clearance model

```python
def exclusion_radius(half_width, strict): ...
def stamp_radius(half_width):
    return max(half_width, 2 * half_width - NOMINAL_HALF_WIDTH)
```

`stamp_radius` is the fix for defect #9 — **the clearance model previously
assumed every conductor was nominal width**, so a 0.50 mm power track was
checked as if it were 0.20 mm.

### The dilation

```python
def _disc_offsets(): ...   # Euclidean disc offsets
def _dilate(...): ...      # dilate obstacles by a disc, not a diamond
```

Defect #2 was that this used **Manhattan** distance, which overstates diagonal
clearance by up to √2. A 0.15 mm rule measured as a diamond permits 0.106 mm
diagonally. Now it is a proper Euclidean disc.

### Transactional rip-up

```python
def snapshot(): ...
def restore(): ...
def rip(net): ...
```

Defect #5 was that rip-up was **not transactional**: an attempt to improve the
routing took the unrouted count from 4 to **33** while the counter still
claimed success. Now every rip-up is a transaction that can be rolled back, and
the final count is recomputed from the final state rather than tracked
incrementally.

### Verification helper

```python
def find_violations(tracks, min_clear, pads, exceptions): ...
def segment_is_clear(..., strict=False): ...
```

## 7.6 — `generate_board.py` (949 lines)

The biggest and most interesting script. **Produces:**
`pcb/SIH26113_Maternity_Assist_Belt.brd` and `pcb/route_report.json`.

### Phase 1 — placement

Calls `design.resolve_placement()`, which applies `SHEET_OFFSET`, then
`EDGE_PLACEMENT`, then resolves collisions to `COURTYARD_GAP = 0.90 mm`.

### Phase 2 — fan-out

Fine-pitch parts get an explicit escape pattern rather than being left to the
router:

```python
FANOUT = {   # r1, r2, spread, stagger, width
    "AD8232":   ...,
    "LSM6DSOX": ...,
    "TMP117":   ...,
    "HX711":    ...,
}
RADIAL_ESCAPE = {   # 3-level and 2-level stagger
    "ESP32-S3-WROOM-1": ...,
    "AS5600":           ...,
    "TP4056":           ...,
}
NO_ESCAPE = { ... }
```

**Why stagger matters:** alternate escape stubs are made *longer* so that each
one has room for **its own via**. Without staggering, the vias collide and only
every other pin can leave the part. This is the single trick that makes a
0.5 mm-pitch QFN routable on four layers.

**45 fine-pitch escapes; 49 coarse-pitch radial stubs.**

### Phase 3 — plane connection

```python
PLANE_NETS = {"GND", "3V3"}
def _route_to_plane(...): ...
```

**Every plane-net pad gets its own dedicated via.** 160 of the 486 vias are
plane-connect vias.

> 🔵 This is why "copper pour NOT COMPUTED" is an acceptable limitation.
> EAGLE calculates polygon fill on load, so the *shape* of the pours is not
> known until you open the board — but **pad connectivity does not depend on
> the pour**, because each pad has its own via straight down to the plane.

### Phase 4 — signal routing

```python
WIDTH_FOR = {0: 0.20, 1: 0.50, 2: 0.50, 3: 0.20}   # by net class
ROUTE_PRIORITY = [ ... ]
ATTEMPTS = 14      # override with SIH_ROUTE_ATTEMPTS
```

Routes in priority order, with **rip-up and retry**, across **14 different net
orderings** (seeds), keeping the best result. **The winning run was seed 8.**

### Phase 5 — geometric repair

A pass that re-measures the emitted geometry and fixes what it can — nudging
segments, moving vias.

### Phase 6 — the concession pass

> **Clearance is prioritised over completeness.** Any net whose only available
> path violates the clearance rule is **ripped out and left as an airwire**,
> with the measured gap recorded as the reason.

That is where the four unrouted nets come from, and why each one is reported
with a number:

```
net I2C_SDA is not fully routed: left unrouted on purpose: every path the
router found came within 0.075 mm of FSR1_ADC on layer 1, below the 0.15 mm
rule. Route it by hand in Fusion.
```

### Phase 7 — emit and cross-check

Writes the `.brd` with the design-rule set `SIH26113_4layer`:

```
mdWireWire = 0.127mm     # min wire-to-wire
msWidth    = 0.15mm      # min width
msDrill    = 0.3mm       # min drill
layerSetup = (1*2*15*16)
```

Then re-parses and asserts **150 elements, 84 signals**.

### Running it

```bash
python scripts/generate_board.py
```

Takes a couple of minutes (14 seeds × full route). To do a single ordering:

```bash
SIH_ROUTE_ATTEMPTS=1 python scripts/generate_board.py
```

On PowerShell:

```powershell
$env:SIH_ROUTE_ATTEMPTS = "1"; python scripts/generate_board.py
```

Or use `python scripts/build_all.py --fast`, which sets it for you.

> ⚠️ **The router is not deterministic across code changes.** Re-running it
> after editing `design.py` will produce a *different* set of 4-ish unrouted
> nets, not the same four. Always re-read `DRC_REPORT.md` after a re-route
> rather than trusting the list in any document — including this one.

## 7.7 — `validate_drc.py` (421 lines)

**Produces:** console output + `pcb/drc_result.json`, consumed by
`generate_docs.py`.

**Deliberately shares no code with `router.py`,** so it can contradict it.

### The eight rule groups

| # | Rule |
|---|---|
| **D1** | every part's copper is inside the outline with edge clearance |
| **D2** | no two component courtyards overlap |
| **D3** | nothing — pad, via or track — inside the antenna keep-out |
| **D4** | minimum track width and minimum drill |
| **D5** | copper clearance, track-to-track and track-to-pad, **per layer**, with the declared fine-pitch exception applied **by region** |
| **D6** | routing completeness, from the router's own report |
| **D7** | every plane-net pad reaches its plane |
| **D9** | board-edge clearance for copper |

### Key implementation details

```python
MIN_CLEAR  = 0.15
EXCEPTIONS = D.clearance_exceptions()   # the 4 fine-pitch rectangles
def seg_circle_dist(...): ...           # round pads measured as circles
```

That `seg_circle_dist` is defect #8's fix: **the DRC previously measured round
pads as squares**, which overstated violations near every through-hole pad and
masked real ones.

### The result

```
--- ERRORS (4) ---     ← all D6 unrouted-net, all deliberate
--- WARNINGS (32) ---  ← all D6 "track copper forms N groups"
--- NOTES (8) ---
  N: [D5] minimum wire-wire clearance on layer 1:  0.154 mm
  N: [D5] minimum wire-wire clearance on layer 16: 0.175 mm
  N: [D5] minimum wire-pad clearance on layer 1:   0.130 mm
  N: [D5] MEASURED MINIMUM COPPER CLEARANCE ANYWHERE ON THE BOARD: 0.130 mm.
          This is the number to quote to the fabricator.
RESULT: FAIL
```

> 🔵 **`RESULT: FAIL` is expected and correct.** There are **zero** clearance,
> width, drill, placement, keep-out or board-edge violations. All four errors
> are unrouted nets. The script does not lower its own bar to produce a PASS,
> which is the right behaviour — see
> [Part 15](#part-15--verification-what-was-checked-and-how).

### About those 32 warnings

Every one says the same thing: *"net X: track copper forms N groups. This is
normal — a multi-drop net reaches each pad separately and the pads join them —
and is reported only so a genuinely stranded stub cannot hide among them.
Confirm with RATSNEST in Fusion."*

A net like `I2C_SCL` touches six pads. The router reaches each pad; the pads
themselves complete the electrical connection. Copper-wise that looks like five
separate groups. It is fine. It is reported anyway so that a *genuinely*
disconnected stub cannot hide in the noise. **Confirming this is what
`RATSNEST` in Fusion is for**, and it is step 14 of the build guide.

## 7.8 — `render.py` (490 lines)

**Produces:** all 12 PNGs in `renders/`.

| Function | Output |
|---|---|
| `render_schematic()` | `schematic_p1.png` … `schematic_p7.png` |
| `render_board()` | `pcb_top.png`, `pcb_bottom.png`, `pcb_layers.png`, `pcb_assembly.png` |
| `render_3d()` | `pcb_3d.png` — isometric at AX = 30°, AY = 150°, Z-scale 2.2, painter's algorithm, heights colour-coded by **datasheet vs. typical** source |

**It parses the emitted `.sch` and `.brd`** and draws only primitives found
there. Marked non-fatal in `build_all.py` — a render failure should not block
documents.

## 7.9 — `generate_docs.py` (608 lines)

**Produces six documents:**

| Output | Source |
|---|---|
| `NETLIST.md` | `D.NETS` + net-type classification |
| `GPIO_ASSIGNMENT.md` | `D.GPIO_TABLE` |
| `BOM.md` + `BOM.csv` | `D.PARTS` grouped by value/deviceset |
| `ERC_REPORT.md` | the run output of `validate_erc.py` |
| `DRC_REPORT.md` | the run output of `validate_drc.py` + `route_report.json` |
| `PROJECT_STATISTICS.md` | counts from the model + widths read from `D.NET_CLASSES` |

`BOM.csv` carries `"Supplier": ""`, `"Supplier PN": ""`, `"Lifecycle": ""` —
**deliberately empty.** See ⚪ L4.

Reading widths from `D.NET_CLASSES` rather than hard-coding them is the fix
for a real drift bug — see [Part 26](#part-26--known-limitations-honestly).

## 7.10 — `gen_reports.py` (691 lines)

**Produces:**

| Output | Function | Content |
|---|---|---|
| `MANUFACTURING_CHECK.md` | `gen_manufacturing_check()` | the **19-item** pre-fab check, connector accessibility, assembly feasibility, mechanical envelope |
| `FINAL_REPORT.md` | `gen_final_report()` | the **15-section** final report |

Helpers: `_erc_drc_sections`, `_count_sections`, `_risk_sections`,
`_next_steps`.

## 7.11 — `build_all.py` (57 lines)

Runs everything in order. Stops on the first **fatal** failure. Prints a
summary of non-fatal steps that reported findings.

```bash
python scripts/build_all.py
```

```bash
python scripts/build_all.py --fast
```

`--fast` sets `SIH_ROUTE_ATTEMPTS=1`, routing with a single ordering instead of
searching 14. **Use it while iterating on the model; do a full run before you
believe a routing number.**

## 7.12 — Script dependency graph

```
                 design.py  ◄── the single source of truth
                     │
        ┌────────────┼───────────────┬──────────────┐
        ▼            ▼               ▼              ▼
   lib_defs.py  validate_erc.py  generate_docs.py  gen_reports.py
        │            │               ▲              ▲
        ▼            │               │              │
 eagle_common.py ────┤               │              │
   │        │        │               │              │
   ▼        ▼        │               │              │
 geom.py  generate_library.py ──► .lbr              │
                     │                              │
                     ▼                              │
            generate_schematic.py ──► .sch          │
                     │                              │
                     ▼                              │
   router.py ──► generate_board.py ──► .brd ────────┤
                     │                  │           │
                     ▼                  ▼           │
            route_report.json    validate_drc.py ───┤
                                        │           │
                                        ▼           │
                                 drc_result.json ───┘
                                        │
                                        ▼
                                    render.py ──► renders/*.png
```

---

# PART 8 — The circuit, sheet by sheet

This part walks the whole design. Every value, and why it is that value.

Open `renders/schematic_p1.png` … `p7.png` alongside this — they are rendered
from the actual `.sch`, so what you see is what is in the file.

---

## 8.1 — Sheet 1: Power entry, charging and 3V3 regulation

### The topology

```
J2 (5 V in) ──► VBUS ──► TP4056 (U1) ──► VBAT ──┬──► AP2112K-3.3 (U2) ──► 3V3
                         500 mA charge          │      600 mA LDO      (plane, L15)
                                                │
      J1 (protected Li-Po pack) ────────────────┤
                                                ├──► R45 ──► J16 vibration motor
                                                └──► R5/R6 divider ──► IO9 (VBAT_SENSE)
```

### The parts

| Ref | Value | Purpose |
|---|---|---|
| `J1` | JST-PH-2, S2B-PH-K-S | 🔴 **Li-Po cell input — protected pack required (B1)** |
| `J2` | 1×4 header | 5 V charge input **+ ESP32-S3 native USB D+/D−** |
| `U1` | **TP4056**-42-SOP8-PP | 1 A linear Li-ion charger, 4.2 V float |
| `R1` | **2k4** | TP4056 `PROG`: **sets 500 mA charge current** |
| `R2`, `R3` | 1k each | CHRG / STDBY LED current limit |
| `D1`, `D2` | RED / GRN 0805 | charging / charge-complete indicators |
| `C1` | 10 µF | `VBUS` input bulk |
| `C2` | 10 µF | `VBAT` bulk at the cell/charger node |
| `U2` | **AP2112K-3.3** | 600 mA LDO, 3.3 V fixed |
| `R4` | 100k | LDO `EN` **pull-up to `VBAT`** ← see ⚪ L2 |
| `J3` | 1×2 header | ⚪ **external latching switch: closed = board OFF** |
| `C3` | 10 µF | LDO input cap (AP2112 needs ≥ 1 µF) |
| `C4` | 10 µF | LDO output cap |
| `C5` | 100 nF | LDO output HF bypass |
| `R5`, `R6` | **470k / 470k** | `VBAT` sense divider |
| `C6` | 100 nF | `VBAT` sense filter / ADC reservoir |
| `J4` | 1×5 header | 🟠 MAX17048 breakout header (I²C, addr 0x36) — see H1 |
| `TP1`–`TP4` | — | `VBAT`, `3V3`, `GND`, `VBUS` test points |
| `H1`–`H4` | M2 | mounting holes, GND-stitched |

### 🔵 Why 500 mA charge current and not 1 A

The TP4056 will do 1 A. `R1` = 2k4 sets it to **500 mA** instead, deliberately.

**The reason is thermal.** Worst-case charger dissipation is at the *start* of
a deeply-discharged charge:

$$P = (V_{in} - V_{bat}) \times I_{chg} = (5 - 3.0) \times 0.5 \approx 1.0\ \text{W}$$

**1.0 W in an SOP-8 with no thermal land will get hot.** At 1 A it would be
2 W, which is not survivable in that package. The TP4056 has thermal
regulation and folds back the current rather than failing, so 1 A would be
*safe* — just slow and hot, with the charge current throttled anyway.

Time to charge 2000 mAh from empty at 500 mA: **≈ 4.5 hours.**

> **If you re-lay the board,** give `U1` copper area on layers 1 and 16, or
> move to a switching charger. `DESIGN_ASSUMPTIONS.md` §1.2.

### 🟡 The charge-termination compromise, stated honestly

There is **no power-path switching**. The system load flows through the `BAT`
pin during charging, which **disturbs the charger's C/10 termination
detection** — the charger sees load current as if the cell were still
accepting charge.

Consequence: charge termination may be late or may cycle. It is not dangerous
with a protected pack (🔴 B1 again — the pack's own over-charge cut-off is the
backstop) but it is a real limitation. The correct fix is a power-path charger
like the MCP73871. `DESIGN_ASSUMPTIONS.md` §1.3.

### ⚪ The inverted on/off switch (L2)

`R4` pulls the LDO's `EN` **up** to `VBAT`. So:

- **default state = ON**
- **closing a switch across `J3` = board OFF**

Silkscreened `OFF SW`. This is deliberate — it avoids inventing an unverified
slide-switch footprint — but it is the **opposite** of what everyone expects.
Tell whoever wires the enclosure.

### The battery-sense divider

`R5` / `R6` = 470k / 470k halves `VBAT` onto `IO9` (`ADC1_CH8`):

| Cell voltage | Voltage at `IO9` |
|---|---|
| 4.2 V (full) | 2.10 V |
| 3.7 V (nominal) | 1.85 V |
| 🔵 **3.5 V (cut-off threshold)** | **1.75 V** |
| 3.0 V | 1.50 V |

470k + 470k = 940 kΩ, drawing **4.5 µA** — negligible, which is why the
divider can be permanently connected rather than switched. `C6` = 100 nF gives
the ADC a charge reservoir so the sample does not load the high-impedance
divider.

> 🔵 This divider is what the **mandatory 3.5 V low-battery cut-off** reads.
> See [Part 10](#part-10--power-budget-in-full).

### TP4056 pins that are grounded deliberately

`TEMP` is tied to `GND`. The datasheet's own instruction for disabling the
temperature-sense function. Not an oversight.

---

## 8.2 — Sheet 2: ESP32-S3 core

### The parts

| Ref | Value | Purpose |
|---|---|---|
| `U3` | 🟠 **ESP32-S3-WROOM-1-N8R2** | Xtensa LX7 dual core, Wi-Fi + BLE 5, 8 MB flash, **2 MB quad PSRAM** |
| `C7` | 100 nF | 3V3 **HF bypass at module pin 2** |
| `C8` | **22 µF** | 3V3 bulk — **the Wi-Fi TX current burst** |
| `R7` | 10k | `EN` pull-up |
| `C10` | 1 µF | `EN` RC delay (power-on reset) |
| `SW2` | tactile | RESET (pulls `EN` low) |
| `R8` | 10k | `IO0` pull-up (boot strap default high) |
| `SW3` | tactile | BOOT (pulls `IO0` low) |
| `J5` | 1×6 header | fallback UART programming header |
| `R9`, `D3` | 1k, GRN | status LED on `IO45` |
| `R10`, `D4` | 1k, RED | alert LED on `IO46` |
| `TP5`, `TP6` | — | `IO3` spare, `TMP_ALERT` |

### 🟠 Why the module variant is not interchangeable (H5)

Covered fully in [Part 1](#part-1--the-blockers-read-this-before-anything-else).
Short version: on octal-PSRAM variants **IO35/36/37 are wired to the PSRAM**,
and this design uses all three for the ECG channel.

### Why `C8` is 22 µF and sits at pin 2

Wi-Fi TX draws a **355 mA burst lasting a few hundred microseconds.** No
regulator responds that fast. `C8` (22 µF bulk) plus `C7` (100 nF HF) at the
module's own supply pin **supply that burst locally**. That is what those two
parts are for, and it is why `C7`/`C8` are in `CHANNEL_EXEMPT` — keeping them
within ~2 mm of pin 2 matters more than the two routing slots they cost.

### 🔵 The strapping-pin problem, and how it is solved

The ESP32-S3 samples four pins at reset to decide how to boot. Three of them
are used in this design:

| Pin | Strap function | Used for | Why it is safe |
|---|---|---|---|
| `IO0` | boot mode | BOOT button + `R8` pull-up | pulled high by default; held low at reset = download mode. That is the *intended* use. |
| `IO3` | JTAG source select | spare / side-B AS5600 analog | `R17` (0 Ω) is **DNP** — left unpopulated, so `IO3` sees only a test point |
| `IO45` | VDD_SPI voltage | status LED (green) | ⬇ see below |
| `IO46` | ROM messages | alert LED (red) | ⬇ see below |

> **The LED trick.** `IO45` and `IO46` drive the LEDs **anode-side** —
> GPIO → resistor → LED anode, LED cathode → GND. At reset the pin is
> **high-impedance**, so the LED **cannot conduct**, so it presents no pull-up.
> The ESP32-S3's internal weak pull-down then holds both straps at their
> default 0.
>
> Wiring the LEDs the other way round (GPIO sinking, LED to 3V3) would pull the
> straps **high** at reset and change the boot configuration. This is a real
> trap and it is checked by ERC rule R9.

### Pin-JTAG is deliberately given up

`IO39`–`IO42` are the pin-JTAG group (MTCK/MTDO/MTDI/MTMS). This design uses
all four for signals — `ECG_FR`, `SOS_GPIO`, `HALL_LIMIT`, `ANG_SCL`.

**That is fine, because the ESP32-S3 has a built-in USB-Serial-JTAG on
`IO19`/`IO20`.** You debug over USB, not over pin-JTAG. The pin budget is
genuinely tight (see [Part 9](#part-9--gpio-allocation-and-its-two-hard-constraints))
and this is where four pins came from.

### `J5` — the fallback programming path

A 6-way header: `GND`, `TXD0`, `RXD0`, `EN`, `IO0`, and 3V3. If USB proves
unreliable, you can program over UART with a plain USB-serial adapter and
manual `EN`/`IO0` control. **This is why M2 was only a MEDIUM item — and M2 is
now resolved: the pair is off-target at ≈ 165 Ω but electrically short at Full
Speed, so it is not expected to cause trouble at all.** See
`documentation/USB_PAIR_ANALYSIS.md`.

---

## 8.3 — Sheet 3: I²C sensors — two busses

### 🔴 The address clash, and its resolution

This is the design's most significant architectural correction. Restated:

> The architecture diagram put **TMP117, LSM6DSOX, AS5600 and MAX17048** on one
> shared bus. **The AS5600 and MAX17048 are both hard-wired to 0x36 with no
> address-select pin.** That bus cannot function.

Resolved by using **both** of the ESP32-S3's I²C controllers:

| Bus | Controller | SDA | SCL | Devices |
|---|---|---|---|---|
| **SENSOR** | I2C0 | `IO15` | `IO16` | TMP117 **0x48**, LSM6DSOX **0x6A**, fuel-gauge header **0x36** |
| **ANGLE** | I2C1 | `IO14` | `IO42` | AS5600 **0x36**, plus `J6` for a second one |

ERC rule R8 checks this: *"no address clash **on a bus**"*. The note it emits
is explicit that 0x36 appears on both busses **deliberately**, because they are
electrically separate.

### The parts

| Ref | Value | Purpose |
|---|---|---|
| `R11`, `R12` | **4k7** each | `I2C_SDA` / `I2C_SCL` pull-ups (bus A — SENSOR) |
| `U4` | **TMP117**AIDRVR | digital temperature sensor, **0x48** |
| `C11` | 100 nF | TMP117 V+ bypass |
| `R13` | 10k | TMP117 `ALERT` pull-up (open drain) |
| `U5` | **LSM6DSOX**TR | 6-axis IMU, **0x6A** |
| `C12` | 100 nF | LSM6DSOX `VDD` filter (datasheet note 1) |
| `C13` | 100 nF | LSM6DSOX `VDDIO` filter (datasheet note 1) |
| `R15`, `R16` | **4k7** each | `ANG_SDA` / `ANG_SCL` pull-ups (bus B — ANGLE) |
| `U6` | **AS5600**-ASOM | 12-bit magnetic angle sensor, **0x36 (fixed)** |
| `C14` | 100 nF | AS5600 `VDD5V` decoupling (datasheet pin 1 note) |
| `C15` | 1 µF | AS5600 `VDD3V3` decoupling (datasheet pin 2 note) |
| `J6` | 1×5 header | optional second AS5600 (angle bus + analog OUT) |
| `R17` | **0 Ω DNP** | opt-in link: side-B AS5600 analog OUT → `IO3` |
| `TP7`–`TP9` | — | `IMU_INT1`, `AS_OUT`, `AS_PGO` |

### Why the pull-ups are 4k7 — with the arithmetic

I²C rise time is set by the pull-up and the bus capacitance:

$$t_r = 0.8473 \times R \times C$$

At 400 kHz (fast mode) the I²C spec allows **300 ns** rise time. With three
devices, the header and ~50 mm of track, estimate **C ≈ 60 pF**:

$$t_r = 0.8473 \times 4700 \times 60\times10^{-12} \approx 239\ \text{ns}$$

Inside 300 ns with margin. And the current when a line is pulled low:

$$I = 3.3 / 4700 = 0.70\ \text{mA per line}$$

Four lines (two busses × two lines) = **2.8 mA worst case**, which is what the
power budget lists. `DESIGN_ASSUMPTIONS.md` §5.

> If you extend a bus off-board on long leads, C rises and you need a smaller
> resistor. 2k2 gives 112 ns at 60 pF and 1.5 mA per line.

### 🟡 The second-AS5600 problem, handled explicitly (not hidden)

A **second** AS5600 still clashes with the first — same fixed 0x36. Rather than
pretend otherwise, `J6` carries:

| `J6` pin | Signal |
|---|---|
| 1 | `3V3` |
| 2 | `GND` |
| 3 | `ANG_SDA` |
| 4 | `ANG_SCL` |
| 5 | `ANG2_OUT` → `R17` (0 Ω, **DNP**) → `IO3` |

So you have **three** options and the board commits you to none of them:

1. Use the second sensor's **analog `OUT`** on pin 5, fit `R17`, read it on
   `IO3` = `ADC1_CH2`. (Remember `IO3` is a strapping pin — that is why `R17`
   is DNP by default.)
2. Add an **external TCA9548A** I²C mux on the angle bus.
3. Bit-bang a **software I²C bus** on spare pins.

### 🟡 `TMP_ALERT` goes to a test point, not a GPIO

The pin budget has **no spare GPIO**. TMP117 alerts are readable over I²C by
polling the configuration register, so the hardware `ALERT` line is a
convenience, not a requirement. `R13` pulls it up, `TP6` makes it probeable.
Declared as an intentional exception in the ERC report.

### ✅ M5 — the AS5600 supply strapping (RESOLVED)

`VDD5V` (pin 1) and `VDD3V3` (pin 2) are **both** tied to `3V3`, with the
datasheet's own per-pin decoupling values (`C14` = 100 nF on pin 1, `C15` =
1 µF on pin 2).

**Confirmed from the primary datasheet** (*AS5600, ams-OSRAM, [v1-06]
2018-Jun-20*, page 9):

> "In 3.3V operation, the VDD5V and VDD3V3 pins must be tied together. VDD is
> the voltage level present at the VDD5V pin."

**The board is correct as designed. No change required.** Page 3 also confirms
the per-pin decoupling: `VDD5V` "requires 100nF", `VDD3V3` "requires an
external 1-μF decoupling capacitor in 5V mode" — matching `C14` and `C15`.

> 🔵 **Bonus, from page 20 of the same document:** in **3.3 V mode the AS5600's
> AGC range is 0–128 counts, not 0–255.** The datasheet asks for the gain to
> sit *"in the center of its range"* for robust performance, so when you set
> the magnet air gap, **target an AGC reading of ≈ 64.** Read the `AGC`
> register and the `STATUS` register (`MH` = too strong, `ML` = too weak,
> `MD` = detected) over I²C. That turns magnet mounting from guesswork into a
> measurement — see 🟡 M6.

### 🟡 M7 — where the TMP117 actually is

`U4` is on the main board because that is where the architecture diagram puts
it. **Inside an electronics pod it measures the pod's internal temperature**,
influenced by the LDO, the charger and the ESP32 — all of which are on the same
board.

If you actually need **skin** temperature, relocate it to a short flex tail.
The sensor I²C bus is already on `J4`, so this is a small change. **This is a
measurement-validity problem, not a layout nicety.**

### 🟡 `IMU_OCS_AUX` — an isolated land, on purpose

The LSM6DSOX datasheet (DS12814 Rev. 4, Table 1 note 2) says to leave
`OCS_Aux` *electrically* unconnected **but soldered to the PCB**. An isolated
land satisfies **both halves** of that instruction — it is soldered, and it
goes nowhere. Declared as a no-connect in `validate_erc.py` rather than
silenced.

---

## 8.4 — Sheet 4: ECG analog front end (AD8232)

The most carefully designed part of the board. Deep dive in
[Part 11](#part-11--the-ecg-front-end-in-depth); here is the sheet.

### The parts, in signal order

| Ref | Value | Purpose |
|---|---|---|
| `J7` | 1×3 header | LA / RA / RL electrode leads |
| `R18` | **330k** | 🔴 LA patient-protection series R (Vs / 10 µA) |
| `R19` | **330k** | 🔴 RA patient-protection series R |
| `R20` | **330k** | 🔴 RLD output current limit (datasheet: > 330k at 3.0 V) |
| `R21` | 10M | LA DC leads-off bias pull-up |
| `R22` | 10M | RA DC leads-off bias pull-up |
| `U7` | **AD8232**ACPZ-R7 | 🔴 single-lead ECG AFE — **Vs 2.0–3.5 V** |
| `C23` | 100 nF | AD8232 `+VS` bypass, **close to pin 17** |
| `C24` | 1 µF | AD8232 `+VS` bulk |
| `R23`, `R24` | 10M / 10M | `REFIN` divider |
| `C16` | 100 nF | `REFIN` filter — 🔵 **settles in ~2.5 s** |
| `C17` | 1 nF | RLD integrator (`RLDFB` → `RLD`) |
| `C18` | 220 nF | HPF pole 1 cap (`HPDRIVE` → `HPSENSE`) |
| `R25` | 10M | HPF pole 1 resistor (`HPSENSE` → `IAOUT`) → **7.2 Hz** |
| `C19` | 220 nF | HPF pole 2 cap (`IAOUT` → `SW`) |
| `R26` | 1M | HPF pole 2 resistor (`SW` → `REFOUT`) → **0.72 Hz** |
| `R27` | 470k | LPF input resistor |
| `C20` | 8n2 | LPF input cap → **~41 Hz pole** |
| `R28` | 100k | op-amp gain, lower leg (Rg) |
| `R29` | 1M | op-amp gain, feedback (Rf) → **gain 11** |
| `C21` | 3n9 | feedback cap → ~41 Hz pole (2nd LPF pole) |
| `R30` | 1k | ADC series isolation |
| `C22` | 10 nF | ADC input reservoir |
| `R31` | 100k | `SDN` pull-up — **AD8232 enabled by default** |
| `R32` | 100k | `FR` pull-down — **fast restore off by default** |
| `TP10` | — | `ECG_OUT`, the conditioned output |
| `TP11` | — | `ECG_REFOUT`, the virtual ground |

### 🔴 The one decision that can destroy the part

$$\large\textcolor{red}{\textsf{The AD8232 supply is 3V3 ONLY. Never VBAT.}}$$

| Parameter | Value |
|---|---|
| AD8232 supply range | **2.0 – 3.5 V** |
| AD8232 **absolute maximum** | **3.5 V** |
| `VBAT` while charging | **4.2 V** |

Putting the AD8232 on `VBAT` exceeds its absolute maximum by 0.7 V **every
time you charge the battery.** It is on `3V3`, and ERC rule R5 checks it.
This is recorded in the "resolved during design" table so it cannot be
re-opened by someone optimising the power tree later.

### 🔴 Patient protection: 330 kΩ, not the datasheet's 180 kΩ

The AD8232 datasheet's rule is **series resistance ≥ Vs / 10 µA**:

$$R_{min} = \frac{3.3}{10 \times 10^{-6}} = 330\ \text{k}\Omega$$

Some reference designs use 180 kΩ, which satisfies the rule at a lower supply.
**330 kΩ is used here** — it satisfies the rule at the full 3.3 V rail with no
arithmetic needed and no dependence on the rail being exactly right.

The cost of 330 kΩ is a source-impedance interaction with the input bias
network, which is **accounted for** in `ECG_FRONTEND_DESIGN.md` rather than
ignored.

### Three-electrode configuration with DC leads-off

`J7` carries three electrodes: **LA**, **RA**, **RL**. That is the AD8232's
Figure 50 topology.

- `R21` / `R22` (10 MΩ each) pull the LA and RA inputs toward the reference,
  so **a disconnected electrode drifts to a rail and the leads-off comparator
  trips**.
- `LOD+` → `IO35`, `LOD−` → `IO36`. Firmware can tell you *which* electrode
  fell off, not just that one did.
- 🟠 Those two pins are **only free on `-N8R2`** (H5).

### Right-leg drive (RLD)

`RLD` → `C17` (1 nF) → `RLDFB` forms an **integrator** (datasheet Fig. 46) that
drives the RL electrode with an inverted common-mode signal. That is what
rejects mains hum without a notch filter.

`R20` = 330 kΩ limits the RLD output current — the datasheet asks for **more
than 330 kΩ at 3.0 V**, and this is the boundary value, chosen so the same
value covers all three electrodes and there is one part number instead of two.

### The reference network and the 🔵 2.5 second wait

`R23` / `R24` (10 MΩ / 10 MΩ) divide `3V3` to give `REFIN` ≈ 1.65 V.
`C16` = 100 nF filters it.

**That RC settles slowly on purpose** — 10 MΩ ∥ 10 MΩ = 5 MΩ with 100 nF gives
τ = 0.5 s, so ~5τ ≈ **2.5 s** to settle.

> 🔵 **Firmware must wait 2.5 s after power-up before trusting an ECG
> reading.** This is not a bug; the slow reference is what keeps the virtual
> ground quiet. It is one of the three non-negotiable firmware jobs.

`REFOUT` is the AD8232's buffered virtual ground and is brought to `TP11` so
you can confirm it sits at ~1.65 V before you attach anything to a person.

### The two-pole high-pass, and the factor of 100

The DC-blocking integrator's corner is **not** 1/(2πRC). The AD8232's internal
gain of 100 appears in the loop:

$$f_{-3dB} = \frac{100}{2\pi R C}$$

**Pole 1** — `C18` = 220 nF, `R25` = 10 MΩ:

$$f = \frac{100}{2\pi \times 10^7 \times 220\times10^{-9}} \approx 7.2\ \text{Hz}$$

**Pole 2** — `C19` = 220 nF, `R26` = 1 MΩ. This one is a *conventional* RC in
the signal path, so no factor of 100:

$$f = \frac{1}{2\pi \times 10^6 \times 220\times10^{-9}} \approx 0.72\ \text{Hz}$$

Getting that factor of 100 wrong is the classic AD8232 mistake — it puts your
high-pass corner at 0.072 Hz instead of 7.2 Hz and the output wanders with
every electrode movement.

### The low-pass and the gain

The AD8232's instrumentation amplifier gives a fixed **gain of 100**. The
on-chip op-amp stage adds:

$$A_{v} = 1 + \frac{R_{29}}{R_{28}} = 1 + \frac{1\text{M}}{100\text{k}} = 11$$

**Total gain = 100 × 11 = 1100.**

Two low-pass poles, both at ~41 Hz:

| Pole | Components |
|---|---|
| 1 | `R27` 470k with `C20` 8n2 |
| 2 | `R29` 1M with `C21` 3n9 |

$$f = \frac{1}{2\pi \times 470\text{k} \times 8.2\text{n}} \approx 41\ \text{Hz}$$

> **It is not a Sallen-Key.** A Sallen-Key needs the op-amp's non-inverting
> input free, and here it is committed to `REFOUT`. This is a two-pole
> cascade with one active stage — see `DESIGN_ASSUMPTIONS.md` §6.3.

### The resulting pass band, and the honest trade-off

**≈ 7 – 40 Hz.**

> 🟡 **That is deliberately narrower than diagnostic ECG (0.05 – 150 Hz).**
>
> It is the AD8232 datasheet's own **motion-artefact-resistant**
> configuration, chosen because *a belt worn by a walking pregnant woman is not
> a resting subject.*
>
> **What you get:** reliable beat detection, reliable heart rate, reliable
> HR variability. What the project actually needs.
>
> **What you do not get:** clinically interpretable waveform morphology. ST
> segments, P-wave detail and T-wave shape are attenuated. **Nothing in this
> project should claim otherwise.**

`ECG_FRONTEND_DESIGN.md` §"If you want to move toward waveform monitoring"
gives the retune path: it is a change of four passive values, not a redesign.

### The controls are on GPIOs, not strapped

| AD8232 pin | Net | GPIO | Default |
|---|---|---|---|
| `SDN` | `ECG_SDN` | `IO37` | `R31` = 100k **pull-up** → AFE **enabled** if the GPIO floats |
| `FR` | `ECG_FR` | `IO39` | `R32` = 100k **pull-down** → fast restore **off** |
| `LOD+` | `ECG_LOD_P` | `IO35` | input |
| `LOD−` | `ECG_LOD_N` | `IO36` | input |

Both defaults are chosen so that **an unprogrammed board behaves sensibly**:
the AFE powers up running, and fast restore — which injects a settling
transient — powers up off.

`SDN` low also gives you a **< 0.2 µA** shutdown state for deep sleep.

### The output to the ADC

`R30` = 1 kΩ in series, `C22` = 10 nF to ground, then `IO1` = `ADC1_CH0`.

The 1 kΩ isolates the AD8232's output from the ADC's sampling capacitor kick;
the 10 nF gives the ADC a local charge reservoir. Standard practice and
cheap insurance.

---

## 8.5 — Sheet 5: Mechanical sensing

Five independent channels. This is the sheet that most directly serves the
"assist belt" half of the project.

### Channel 1 — load cell via HX711

| Ref | Value | Purpose |
|---|---|---|
| `U8` | **HX711** | 24-bit bridge ADC |
| `J8` | JST-PH-4, S4B-PH-K-S | 🟠 4-wire bridge: **E+ (1), E− (2), A+ (3), A− (4)** — see H3 |
| `C25` | 100 nF | `VBG` reference bypass |
| `C26` | 100 nF | `AVDD` bypass |
| `C27` | 100 nF | `DVDD` bypass |
| `C28` | 10 µF | analog bulk / bridge excitation reservoir |
| `TP12` | — | `HX_BASE` (regulator unused: NC) |
| `TP13` | — | `HX_XO` (crystal unused: NC) |
| `TP14` | — | `HX_DOUT` |

Interface: `HX_DOUT` → `IO21`, `HX_SCK` (`PD_SCK`) → `IO38`.

**Excitation from `AVDD` = `3V3` is deliberate, not lazy.** The HX711's
conversion is **ratiometric to AVDD**: if the excitation and the reference are
the same rail, a rail shift cancels out of the reading entirely. Exciting from a
separate regulator would *introduce* an error term.
`DESIGN_ASSUMPTIONS.md` §7.2.

`BASE` and `XO` are datasheet-designated "NC when not used" — the internal
regulator and the external crystal are both unused. They go to test points so
they stay probeable without committing a GPIO. Declared exceptions in the ERC
report.

`PD_SCK` held high also powers the HX711 down to **≈ 0.2 µA**.

### Channel 2 — four FSR (force-sensing resistor) channels

Generated in a loop, `i` = 1…4:

| Ref | Value | Purpose |
|---|---|---|
| `J9`–`J12` | 1×2 headers | FSR1–FSR4 (belt pressure), FSR402 + header |
| `R33`–`R36` | **10k** each | FSR divider resistor |
| `C29`–`C32` | 10 nF each | anti-alias filter (**1.6 kHz**) |

→ `IO4`, `IO5`, `IO6`, `IO7` = `ADC1_CH3`…`CH6`.

**Why 10 kΩ, derived not guessed.** An FSR402's useful band is roughly
**2 kΩ (hard press) to 100 kΩ (light touch)**. The divider value that centres
the output across that whole span is the geometric mean:

$$R = \sqrt{2\text{k} \times 100\text{k}} = \sqrt{2\times10^8} \approx 14\ \text{k}\Omega$$

10 kΩ is the nearest sensible standard value and biases slightly toward
resolution at the higher-force end, which is what a *pressure* measurement
wants. `DESIGN_ASSUMPTIONS.md` §7.1.

**This is the method that 🟠 H2 asks you to apply to `R37`.**

Current at full force, all four: 4 × 3.3 V / 12 kΩ = **1.1 mA**.

Anti-alias corner: 1/(2π × 10k × 10n) = **1.6 kHz** — far above any mechanical
signal, so it removes ADC-input noise without affecting the measurement.

### Channel 3 — abdominal stretch sensor

| Ref | Value | Purpose |
|---|---|---|
| `J13` | 1×2 header | 🟠 stretch / extension sensor — **part TBD, see H2** |
| `R37` | **10k — PLACEHOLDER** | 🟠 divider resistor |
| `C33` | 10 nF | anti-alias filter |

→ `IO8` = `ADC1_CH7`.

> 🟠 **`R37` is explicitly a placeholder.** Set it to √(R_min × R_max) for the
> chosen sensor. See H2. It is one 0805 — **reworkable, not a re-spin.**

### Channel 4 — piezo film, fetal movement

The channel the block diagram glossed over, and the one with the most
engineering in it.

| Ref | Value | Purpose |
|---|---|---|
| `J14` | 1×2 header | piezo film sensor |
| `R38` | **10M** | piezo load resistor — sets the **~10 Hz LF corner** |
| `C34` | **100n / 50 V** | 🟡 AC coupling — **must withstand the film's open-circuit transient** |
| `R39`, `R40` | 1M / 1M | mid-rail bias divider |
| `R41` | 100k | ADC series current limit |
| `C35` | 10 nF | ADC filter (**160 Hz**) |
| `D5` | 1N5819HW | 🔵 over-voltage clamp **to `3V3`** (cathode → 3V3) |
| `D6` | 1N5819HW | 🔵 under-voltage clamp **to `GND`** (anode → GND) |

→ `IO2` = `ADC1_CH1`.

**Why the clamps exist.** A piezo film is a charge source with a very high
open-circuit impedance. Flex it sharply and the open-circuit voltage reaches
**tens of volts** — enough to destroy an ESP32 ADC input. `D5`/`D6` clamp the
node to within a diode drop of the rails.

> 🔵 **Clamp polarity is checked by ERC rule R10:** `D5` cathode → `3V3`,
> `D6` anode → `GND`. Reversed, they would be a permanent short across the
> rail. This is the sort of error that is invisible on a schematic and obvious
> in smoke.

**Why `C34` must be 50 V rated.** Same reason. It sits directly across that
transient. A 16 V 0805 would fail. The BOM specifies `100n/50V` for exactly
this part and no other.

**The LF corner.** `R38` = 10 MΩ across the element sets
1/(2π · 10 M · C_film). At an assumed **~1.5 nF** that is ≈ **10 Hz**, which
suits fetal movement (roughly 1–10 Hz).

🟡 **M4:** measure the film's actual capacitance. Bigger film (10 nF+) →
corner drops to ~1.6 Hz, which is fine or better. Much smaller → the corner
rises and low-frequency movement is attenuated; reduce `R38`.

### Channel 5 — hall / limit switch

| Ref | Value | Purpose |
|---|---|---|
| `J15` | 1×3 header | hall sensor or mechanical limit switch (rail travel) |
| `R42` | 10k | pull-up |
| `C36` | 100 nF | hardware debounce (**~1 ms**) |

→ `IO41`.

Three pins so it accepts either a **two-terminal switch** or a **three-terminal
hall sensor** (`3V3`, output, `GND`) without a board change.

---

## 8.6 — Sheet 6: FET-driven alerts

Two nearly identical low-side switches. The differences matter.

### The vibration motor channel

| Ref | Value | Purpose |
|---|---|---|
| `Q1` | **AO3400A** SOT-23-3 | low-side switch, **5.7 A** rated |
| `R43` | 100 Ω | gate series resistor (slew limit) |
| `R44` | 100k | 🔵 gate **pull-down — fail-safe OFF** |
| `J16` | 1×2 header | motor output |
| `R45` | **0 Ω** | 🔴 **motor ballast — see B3** |
| `D7` | 1N5819HW | flyback, **cathode to the `VBAT` side** |
| `C37` | 10 µF | local motor bulk |
| `TP15` | — | `MOTOR_EN` gate drive |

Gate driven from `IO47`.

**Motor is on `VBAT`, not `3V3`** — deliberately. A motor is a noisy inductive
load and the whole point is to keep its current out of the 3.3 V rail that the
AD8232 lives on. `C37` = 10 µF local bulk keeps the **di/dt out of the shared
rail** at the source.

### The buzzer channel

| Ref | Value | Purpose |
|---|---|---|
| `Q2` | **AO3400A** | low-side switch |
| `R46` | 100 Ω | gate series resistor |
| `R47` | 100k | 🔵 gate pull-down — fail-safe OFF |
| `J17` | 1×2 header | 🟡 buzzer output — **type matters, see M3** |
| `D8` | 1N5819HW | flyback (magnetic buzzers are inductive) |
| `C38` | 10 µF | local `3V3` bulk at the buzzer FET |
| `TP16` | — | `BUZZER_EN` gate drive |

Gate driven from `IO48`. **Buzzer is on `3V3`** — its current is small and
constant enough not to need the motor treatment.

### 🔵 Three things this circuit gets right, and why each matters

**1. The gate pull-downs (`R44`, `R47`) are the fail-safe.**

At boot, before firmware runs, `IO47` and `IO48` are **high-impedance**. Without
a pull-down the gate voltage is undefined — it can float up through leakage and
partially turn the FET on. A partially-on MOSFET dissipates enormously.

> With `R44`/`R47`, **the motor and buzzer are guaranteed off from the instant
> power is applied until firmware deliberately turns them on.** In a device
> worn against a body, a motor that runs at boot is not just a bug.

**2. Flyback diode orientation is checked, not assumed.**

`D7` and `D8`: **anode on the switched drain, cathode on the supply.**

Reversed, the diode is a **permanent forward-biased short across the supply.**
The board dies at power-on. ERC rule R10 checks the orientation, and its output
says so explicitly:

```
N: [R10] Q1: flyback D7 present on MOTOR_N
N: [R10] Q2: flyback D8 present on BUZZ_N
```

**3. `R43`/`R46` = 100 Ω slew limiting.**

Not current limiting — a MOSFET gate takes no steady current. These slow the
switching edge, which reduces the radiated noise from the switching transient.
100 Ω into an AO3400A's ~700 pF gate charge gives a rise time of tens of
nanoseconds: fast enough to keep switching losses negligible, slow enough not
to spray broadband noise across an ECG channel 30 mm away.

### 🟡 M3 — buzzer type changes the firmware

| Type | Firmware | `D8` |
|---|---|---|
| **Active magnetic** (has its own oscillator) | drive `IO48` as simple on/off | **essential** — it is an inductive coil |
| **Passive piezo transducer** | drive `IO48` with **LEDC PWM** at the transducer's resonance, typically 2–4 kHz | harmless |

Confirm its current draw too; **30 mA is budgeted**.

---

## 8.7 — Sheet 7: User input and storage

### The SOS button

| Ref | Value | Purpose |
|---|---|---|
| `SW4` | tactile 6 × 6 mm | 🟠 manual emergency SOS button — see H4 |
| `R48` | 10k | pull-up |
| `C39` | 100 nF | **hardware debounce + ESD shunt (~1 ms)** |
| `R49` | **1k** | 🔵 **GPIO series protection** |
| `TP17` | — | `SOS_GPIO` |

→ `IO40`.

> 🔵 **Why `R49` = 1 kΩ is there.** The SOS button is the one control a user
> presses in an emergency, with a finger, possibly having walked across a
> carpet. **1 kΩ in series with the GPIO plus 100 nF to ground is a
> deliberate ESD network**: the cap shunts the fast edge, the resistor limits
> the current into the pin's internal protection diodes.
>
> It also debounces: 1 kΩ + 10 kΩ pull-up with 100 nF gives roughly a 1 ms
> time constant — long enough to swallow contact bounce, short enough that a
> press feels instant.

**Firmware note:** the pull-up means **pressed = LOW**. Debounce in firmware
as well; the hardware RC helps but does not eliminate bounce.

### microSD as a module header

| Ref | Value | Purpose |
|---|---|---|
| `J18` | 1×6 header | microSD SPI breakout module |
| `R50` | 10k | `SD_CS` pull-up (SD spec recommends 10k–100k) |
| `R51` | 10k | `SD_MISO` pull-up |

SPI on `IO10` (CS), `IO11` (MOSI), `IO12` (SCK), `IO13` (MISO) — the FSPI
peripheral.

**[ARCHITECTURE CHANGE]** `J18` is a **6-way header for a standard SPI microSD
breakout**, not an on-board socket. Two reasons:

1. It matches the architecture diagram's own "module headers" approach.
2. It **avoids an unverified socket land pattern.** microSD push-pull sockets
   have fiddly, vendor-specific land patterns with mechanical retention
   features, and getting one wrong means a socket that will not fit.

`R50`/`R51` pull-ups are the SD specification's own recommendation — they keep
the card's lines defined while the ESP32 is in reset.

### Test points on this sheet

`TP18` (`I2C_SDA`) and `TP19` (`I2C_SCL`) are here rather than on sheet 3
because they are for **bring-up debugging with a logic analyser**, and this is
where the physical space was.

---

## 8.8 — All 19 test points, in one table

📌 **Print this.** It is the fastest debugging aid on the board.

| TP | Signal | What it tells you |
|---|---|---|
| `TP1` | `VBAT` | cell voltage — 3.0–4.2 V |
| `TP2` | `3V3` | 🔵 **the first thing to measure. 3.3 V ±1.5 %.** |
| `TP3` | `GND` | your reference for everything else |
| `TP4` | `VBUS` | 5 V charge input present |
| `TP5` | `IO3_SPARE` | spare ADC / side-B AS5600 analog |
| `TP6` | `TMP_ALERT` | TMP117 alert (not on a GPIO) |
| `TP7` | `IMU_INT1` | IMU interrupt 1 |
| `TP8` | `AS_OUT` | AS5600 analog/PWM out (unused; I²C is used) |
| `TP9` | `AS_PGO` | AS5600 programming pin |
| `TP10` | `ECG_OUT` | 🔵 **the conditioned ECG. Should idle ≈ 1.65 V.** |
| `TP11` | `ECG_REFOUT` | 🔵 **the virtual ground. Must be ≈ 1.65 V before you attach electrodes.** |
| `TP12` | `HX_BASE` | HX711 regulator unused (NC) |
| `TP13` | `HX_XO` | HX711 crystal unused (NC) |
| `TP14` | `HX_DOUT` | HX711 serial data out |
| `TP15` | `MOTOR_EN` | 🔵 **check this is LOW at boot before connecting the motor** |
| `TP16` | `BUZZER_EN` | same, for the buzzer |
| `TP17` | `SOS_GPIO` | SOS line — HIGH idle, LOW pressed |
| `TP18` | `I2C_SDA` | sensor-bus SDA — hook a logic analyser here |
| `TP19` | `I2C_SCL` | sensor-bus SCL |

The brief asked specifically for test points on `VBAT`, `3V3`, `GND`,
`I2C_SDA`, `I2C_SCL`, `ECG_OUT`, `MOTOR_EN`, `BUZZER_EN` and `SOS_GPIO`. All
nine are present, plus ten more.

---

# PART 9 — GPIO allocation and its two hard constraints

The full generated table is in
[`documentation/GPIO_ASSIGNMENT.md`](documentation/GPIO_ASSIGNMENT.md). This
part explains **why it looks like that**, which the table cannot.

Pin numbers and alternate functions are from *ESP32-S3-WROOM-1 & WROOM-1U
Datasheet v1.8*, **Table 3-1**. Strapping behaviour is from Section 4 /
Table 4-1 of the same document.

## 9.1 — Constraint 1: ADC2 is unusable while the radio is on

$$\large\textcolor{orange}{\textsf{Every analog input must land on ADC1 — which is GPIO1–GPIO10 only.}}$$

This is a documented ESP32 family limitation, not a rumour: **ADC2 shares
hardware with the Wi-Fi/BLE radio**, and `adc2_get_raw()` returns an error when
the radio driver holds the lock. There is no workaround that keeps the radio
usable.

**This board has 8 analog signals and ADC1 has 10 channels.** The budget is
tight by design:

| GPIO | ADC1 channel | Analog signal |
|---|---|---|
| `IO1` | CH0 | `ECG_OUT` |
| `IO2` | CH1 | `PIEZO_ADC` |
| `IO3` | CH2 | `IO3_SPARE` (strapping — `R17` DNP) |
| `IO4` | CH3 | `FSR1_ADC` |
| `IO5` | CH4 | `FSR2_ADC` |
| `IO6` | CH5 | `FSR3_ADC` |
| `IO7` | CH6 | `FSR4_ADC` |
| `IO8` | CH7 | `STRETCH_ADC` |
| `IO9` | CH8 | `VBAT_SENSE` |
| `IO10` | CH9 | **used digitally** as `SD_CS` |

**9 of 10 ADC1 channels carry analog. 0 ADC2 channels are used for analog.**

> **This is why `IO10` is the microSD chip select.** It is the only ADC1-capable
> pin used digitally, and CS is the least timing-critical SPI signal — so if
> you ever need a tenth analog channel, that is the one to reclaim.

## 9.2 — Constraint 2: IO35/36/37 are only free on quad-PSRAM parts

Covered in 🟠 **H5**. The three pins carry `ECG_LOD_P`, `ECG_LOD_N` and
`ECG_SDN`.

## 9.3 — The full allocation

| Module pin | Pad | Function | Net | Dir | Boot | Notes |
|---|---|---|---|---|---|---|
| `IO0` | 27 | BOOT strap / button | `ESP_IO0` | IO | 🔴 **YES** | weak internal pull-up; low at reset = download mode |
| `IO1` | 39 | ECG analog out | `ECG_OUT` | ANALOG | no | ADC1_CH0 |
| `IO2` | 38 | piezo / fetal movement | `PIEZO_ADC` | ANALOG | no | ADC1_CH1, `D5`/`D6` clamped |
| `IO3` | 15 | spare / side-B AS5600 | `IO3_SPARE` | ANALOG | 🔴 **YES** | STRAPPING (JTAG source select); `R17` unpopulated |
| `IO4`–`IO7` | 4–7 | FSR1–FSR4 | `FSRn_ADC` | ANALOG | no | ADC1_CH3–CH6 |
| `IO8` | 12 | stretch sensor | `STRETCH_ADC` | ANALOG | no | 🟠 `R37` is a placeholder |
| `IO9` | 17 | battery sense | `VBAT_SENSE` | ANALOG | no | 470k/470k; 4.2 V → 2.10 V |
| `IO10` | 18 | microSD CS | `SD_CS` | OUT | no | ADC1_CH9 unused |
| `IO11` | 19 | microSD MOSI | `SD_MOSI` | OUT | no | FSPID |
| `IO12` | 20 | microSD SCK | `SD_SCK` | OUT | no | FSPICLK |
| `IO13` | 21 | microSD MISO | `SD_MISO` | IN | no | FSPIQ |
| `IO14` | 22 | **angle-bus SDA** | `ANG_SDA` | IO | no | I2C1 — separate bus resolves the 0x36 clash |
| `IO15` | 8 | **sensor-bus SDA** | `I2C_SDA` | IO | no | I2C0 |
| `IO16` | 9 | **sensor-bus SCL** | `I2C_SCL` | OUT | no | I2C0 |
| `IO17` | 10 | IMU interrupt 1 | `IMU_INT1` | IN | no | |
| `IO18` | 11 | IMU interrupt 2 | `IMU_INT2` | IN | no | |
| `IO19` | 13 | **USB D−** | `USB_DM` | IO | no | USB-Serial-JTAG. ✅ M2 resolved: as-routed ≈ 165 Ω, electrically short at FS |
| `IO20` | 14 | **USB D+** | `USB_DP` | IO | no | USB-Serial-JTAG |
| `IO21` | 23 | HX711 data out | `HX_DOUT` | IN | no | |
| `IO35` | 28 | ECG leads-off + | `ECG_LOD_P` | IN | no | 🟠 **free on `-N8R2` only** |
| `IO36` | 29 | ECG leads-off − | `ECG_LOD_N` | IN | no | 🟠 same |
| `IO37` | 30 | ECG shutdown | `ECG_SDN` | OUT | no | 🟠 same; `R31` keeps AFE enabled if floating |
| `IO38` | 31 | HX711 clock / PD | `HX_SCK` | OUT | no | |
| `IO39` | 32 | ECG fast restore | `ECG_FR` | OUT | no | was MTCK — pin-JTAG given up |
| `IO40` | 33 | SOS button | `SOS_GPIO` | IN | no | was MTDO; via `R49` |
| `IO41` | 34 | hall / limit | `HALL_LIMIT` | IN | no | was MTDI |
| `IO42` | 35 | **angle-bus SCL** | `ANG_SCL` | OUT | no | I2C1; was MTMS |
| `TXD0` | 37 | UART0 TX | `UART_TX` | OUT | no | GPIO43 → `J5.3` |
| `RXD0` | 36 | UART0 RX | `UART_RX` | IN | no | GPIO44 → `J5.4` |
| `IO45` | 26 | status LED (green) | `LED_STATUS` | OUT | 🔴 **YES** | STRAPPING (VDD_SPI). LED to GND keeps the strap at 0 |
| `IO46` | 16 | alert LED (red) | `LED_ALERT` | OUT | 🔴 **YES** | STRAPPING (ROM print). Same trick |
| `IO47` | 24 | motor enable | `MOTOR_EN` | OUT | no | → `R43` → `Q1` |
| `IO48` | 25 | buzzer enable | `BUZZER_EN` | OUT | no | → `R46` → `Q2` |
| `EN` | 3 | chip enable / reset | `ESP_EN` | IN | 🔴 **YES** | **must not be left floating** — `R7`/`C10`/`SW2`/`J5.5` |
| `3V3` | 2 | module supply | `3V3` | POWER | no | `C7`, `C8` |
| `GND` | 1, 40, 41 | ground incl. EPAD | `GND` | POWER | no | 🔵 **EPAD must be soldered and via-stitched** |

## 9.4 — The budget

- module pins accounted for: **39** (41 physical pads; `GND@1`, `GND@40` and
  the EPAD share one row)
- signal pins in use: **36** (`EN` plus every GPIO)
- ADC1 channels carrying analog: **9 of 10**
- ADC2 channels used for analog: **0** (deliberate)
- strapping pins in use: `IO0`, `IO3`, `IO45`, `IO46`
- pin-JTAG (`IO39`–`IO42`) **given up** so those four can carry signals

> **Nothing is left floating.** Every module pad is either driven, terminated,
> or brought to a test point. ERC rule R3 enforces this, and rule R9 checks
> every module pin appears in the GPIO table.

## 9.5 — What firmware must know

| Rule | Why |
|---|---|
| 🔵 **Use ADC1 only** (GPIO1–10) | ADC2 fails with the radio on |
| 🔵 **Two I²C busses**, not one | 0x36 appears on both — see §8.3 |
| 🔵 **`SOS_GPIO` is active LOW** | `R48` pull-up |
| 🔵 **Drive `IO47`/`IO48` LOW at startup, explicitly** | belt-and-braces on top of `R44`/`R47` |
| 🔵 **Wait 2.5 s before trusting ECG** | `REFIN` network settling |
| 🔵 **Low-battery cut-off at 1.75 V on `IO9`** | LDO dropout |
| 🔵 **`ECG_SDN` high = enabled** | `R31` pull-up default |
| 🔵 **`ECG_FR` low = fast restore off** | `R32` pull-down default |
| 🔵 Read `LOD+`/`LOD−` to tell **which** electrode fell off | not just that one did |

---

# PART 10 — Power budget, in full

Source document:
[`documentation/POWER_BUDGET.md`](documentation/POWER_BUDGET.md). Every figure
there is a **datasheet typical or a calculation** — nothing has been measured,
because no board exists.

## 10.1 — The rails

| Rail | Voltage | Source | Distribution |
|---|---|---|---|
| `VBUS` | 5 V | `J2` header | tracks, **0.50 mm** |
| `VBAT` | 3.0 – 4.2 V | 1S Li-Po via `J1`, charged by `U1` | tracks, **0.50 mm** |
| `3V3` | 3.3 V ±1.5 % | `U2` AP2112K-3.3 | **inner plane, EAGLE layer 15** |
| `GND` | 0 V | — | **inner plane, EAGLE layer 2** |

## 10.2 — The 3V3 worst case

| Load | Current | Source of the figure |
|---|---|---|
| ESP32-S3 Wi-Fi TX peak | **355 mA** | ESP32-S3-WROOM-1 datasheet v1.8 |
| microSD write peak | **100 mA** *estimate* | typical SD card in SPI mode; card-dependent |
| Buzzer (magnetic, sounding) | **30 mA** *estimate* | typical 3 V magnetic buzzer; 🟡 M3 |
| Load-cell bridge excitation | **9.4 mA** | worst case: 350 Ω bridge at 3.3 V. A 1 kΩ bridge draws 3.3 mA. 🟠 H3 |
| AS5600 | **6.5 mA** | AS5600 DS000365 v1-06 |
| I²C pull-ups, 4 lines low | **2.8 mA** | 4 × 3.3 V / 4.7 kΩ |
| Status + alert LEDs, both on | **2.6 mA** | 2 × (3.3 − 2.0) V / 1 kΩ |
| HX711 | **1.4 mA** | HX711 datasheet |
| FSR dividers ×4, full force | **1.1 mA** | 4 × 3.3 V / 12 kΩ |
| LSM6DSOX, both sensors high-perf | **0.55 mA** | LSM6DSOX DS12814 Rev. 4 |
| Stretch-sensor divider | **0.33 mA** *estimate* | depends on the unselected sensor, 🟠 H2 |
| AD8232 | **0.17 mA** | AD8232 Rev. A |
| `VBAT` sense divider | **4.5 µA** | 4.2 V / 940 kΩ |
| Piezo bias network | **1.65 µA** | 3.3 V / 2 MΩ |
| TMP117, continuous conversion | **6.3 µA** | TMP117 SNOSD82D |
| **Total, everything simultaneous** | **≈ 510 mA** | |
| **AP2112K-3.3 guaranteed minimum** | **600 mA** | AP2112 DS39724 Rev. 2-2 |
| **Margin** | **≈ 15 %** | |

## 10.3 — Is 15 % margin actually enough?

**Yes, and it is more comfortable than 15 % suggests**, because the two big
items do not coincide in practice:

| Item | Reality |
|---|---|
| Wi-Fi TX (355 mA) | a burst of a few **hundred microseconds**. **BLE-only operation — the project's actual link — is about 130 mA**, dropping the total to **~285 mA** |
| microSD writes (100 mA) | buffered by firmware; need not overlap a radio burst |

`C8` (22 µF) plus `C7` (100 nF) at the module's pin 2 supply the radio bursts
locally. That is what those parts are for.

> **Realistic steady state, BLE + all sensors sampling, no motor or buzzer:
> ≈ 155 mA.** With a 2000 mAh cell that is roughly **13 hours** of continuous
> operation, before any duty cycling.

## 10.4 — The dropout problem — the most important section in this part

The AP2112K's dropout is **250 mV typical at 600 mA**. So:

| `VBAT` | 3V3 output | ESP32-S3 (min 3.0 V) |
|---|---|---|
| 4.2 V (full) | 3.30 V | ✅ fine |
| 3.7 V (nominal) | 3.30 V | ✅ fine |
| 3.55 V | 3.30 V | at the edge of regulation |
| 3.30 V | ≈ 3.05 V | 🟠 **marginal** |
| 3.10 V | ≈ 2.85 V | 🔴 **below minimum — brown-out** |

### Required firmware behaviour

$$\large\textcolor{blue}{\textsf{Implement a low-battery cut-off at 3.5 V using VBAT\_SENSE on IO9.}}$$

The divider is 470 k / 470 k, so **3.5 V at the cell reads 1.75 V at the pin.**
Below that: stop sampling, notify the app, enter deep sleep.

**Without this the board browns out unpredictably at the bottom of the
discharge curve — and unpredictable behaviour in a device with an SOS button is
worse than a clean shutdown.**

This limitation is **inherent to an LDO from a single Li-Po cell** and is normal
for ESP32 designs. If the extra ~15 % of cell capacity matters, the fix is a
buck-boost regulator (`DESIGN_ASSUMPTIONS.md` §15).

## 10.5 — The VBAT rail

| Load | Current | Notes |
|---|---|---|
| `3V3` rail input | ≈ 520 mA worst case | LDO input ≈ output + 55 µA quiescent |
| Vibration motor | **100 mA** *estimate* | typical coin ERM; 🔴 B3 |
| `VBAT_SENSE` divider | 4.5 µA | |
| `J4` fuel-gauge breakout | ≈ 25 µA *estimate* | MAX17048 is a 3 µA part; a breakout adds its own regulator |
| **Total** | **≈ 620 mA peak** | |

## 10.6 — Charging

| Parameter | Value | Source |
|---|---|---|
| Input | 5 V at `J2` (`VBUS`) | — |
| Charge current | **500 mA** (`R1` = 2.4 kΩ) | TP4056 characteristics table |
| Float voltage | 4.2 V ±1.5 % | TP4056 datasheet |
| Termination | C/10 = 50 mA | TP4056 datasheet |
| Trickle threshold | 2.9 V | TP4056 datasheet |
| Charger dissipation, worst case | (5 − 3.0) × 0.5 ≈ **1.0 W** | at the start of a deeply-discharged charge |
| Time to charge 2000 mAh from empty | ≈ 4.5 h | |

> **1.0 W in an SOP-8 with no thermal land will get hot.** The TP4056 has
> thermal regulation and folds back the current rather than failing, so this is
> **safe but slow.** It is why 500 mA was chosen over 1 A. Give `U1` copper
> area on layers 1 and 16 if you re-lay the board, or move to a switching
> charger.

## 10.7 — Trace width justification (IPC-2221)

External-layer chart, 1 oz (35 µm) copper, 10 °C rise:

$$I = 0.048 \times \Delta T^{0.44} \times A^{0.725}$$

| Width | Ampacity | Used for |
|---|---|---|
| **0.20 mm** | ≈ **0.74 A** | all signals (net classes `default` and `analog_ecg`) |
| **0.50 mm** | ≈ **1.45 A** | `VBUS`, `VBAT`, motor path (classes `power` and `motor`) |
| **0.15 mm** | ≈ **0.60 A** | fine-pitch fan-out escapes only (AD8232, LSM6DSOX, TMP117, HX711) — a few millimetres long, carrying microamp signal currents |

**Signal and power tracks are narrower than the 0.25 / 0.60 mm this design
started with.** Reduced deliberately: a narrower track needs less clearance
around it, and that bought back the routing density lost when the clearance
model was corrected to measure Euclidean distance.

> **Ampacity was never the binding constraint.** Highest current on any track
> is the motor path at ~100 mA and the `VBAT` feed to the LDO at **620 mA
> peak**. 0.50 mm carries ≈ 1.45 A, so that is **2.3× margin** on the worst
> case.

`3V3` and `GND` are **planes**, so their ampacity is not a constraint at all.

Plane vias are **0.3 mm drill / 0.55 mm pad**. A 0.3 mm via carries roughly
1 A comfortably; each plane-net pad has its own, so no via carries more than
that pad's share.

## 10.8 — Deep sleep

| Item | Current |
|---|---|
| ESP32-S3 deep sleep | ≈ 7 µA |
| **AP2112K quiescent** | **55 µA** ← dominates |
| `VBAT_SENSE` divider | 4.5 µA |
| LSM6DSOX power-down | 3 µA |
| Piezo bias network | 1.65 µA |
| AS5600 low-power mode 3 | ≈ 1.5 µA |
| REFIN divider (`R23`/`R24`) | 0.33 µA |
| ECG input bias (`R21`/`R22`) | 0.33 µA |
| TMP117 shutdown | 0.25 µA |
| AD8232 in shutdown (`SDN` low) | < 0.2 µA |
| HX711 power-down (`PD_SCK` high) | ≈ 0.2 µA |
| **Total** | **≈ 74 µA** |

The AP2112K's own 55 µA **dominates**. That is the price of choosing an LDO for
its noise performance, and it is worth naming: on a 2000 mAh cell, 74 µA is
about **3 years** of shelf life, so it is not a practical problem — but if it
ever became one, **the regulator is where to look, not the sensors.**

> ❌ **Not measured.** All figures are datasheet typicals. Verify on hardware.

---

# PART 11 — The ECG front end, in depth

Sheet-level detail is in [§8.4](#84--sheet-4-ecg-analog-front-end-ad8232). The full
source document is
[`documentation/ECG_FRONTEND_DESIGN.md`](documentation/ECG_FRONTEND_DESIGN.md)
(381 lines). This part covers what the sheet walkthrough could not: dynamic
range, layout compliance, the retune path, and the firmware contract.

## 11.1 — The whole chain in one diagram

```
                  330k          10M
  LA ──[R18]──┬─────────────────[R21]──► REFOUT
              └──► +IN ┐
                       ├─► [ IA, gain 100 ] ──► IAOUT
  RA ──[R19]──┬──► -IN ┘                          │
              └────[R22]──► REFOUT                │
                  10M                             │
                                    HPF pole 1:   │
  RL ◄─[R20]── RLD ◄──[C17 1n]── RLDFB      C18 220n + R25 10M
     330k                                   → 7.2 Hz (×100 rule)
                                                  │
   REFIN ◄── R23/R24 10M+10M from 3V3, C16 100n   │
             (≈1.65 V, settles in ~2.5 s)         │
                                                  ▼
                       HPF pole 2: C19 220n + R26 1M → 0.72 Hz
                                                  │
                                                  ▼
                       LPF + gain 11: R27 470k, C20 8n2,
                                      R28 100k, R29 1M, C21 3n9
                                      → two poles at ~41 Hz
                                                  │
                                                  ▼
                          OUT ──[R30 1k]──┬──► IO1 (ADC1_CH0)
                                          └──[C22 10n]── GND
```

**Total gain: 100 × 11 = 1100. Pass band ≈ 7 – 40 Hz.**

## 11.2 — Dynamic range — does 1100 fit in the ADC?

A surface ECG R-wave at the LA/RA electrode pair is typically
**0.5 – 2 mV peak**.

| Input | × 1100 | Output swing about the 1.65 V reference |
|---|---|---|
| 0.5 mV | 0.55 V | 1.65 ± 0.28 V |
| 1.0 mV | 1.10 V | 1.65 ± 0.55 V |
| 2.0 mV | 2.20 V | 1.65 ± 1.10 V → **0.55 V to 2.75 V** |
| 3.0 mV | 3.30 V | 🟠 **clips** against the rails |

So 1100 is sized for a **1–2 mV** signal and clips somewhere above 2.5 mV.
That is the right choice: a signal large enough to clip is unmistakable on
`TP10`, and an under-amplified signal buried in ADC quantisation noise is much
harder to diagnose.

**ADC resolution.** The ESP32-S3 ADC is 12-bit over ~0–3.1 V ≈ **0.76 mV per
LSB**. Referred back through the gain of 1100 that is **0.69 µV at the
electrode** — far below the electrode's own noise floor, so the ADC is not the
limiting element. Good.

**If your subject's signal is consistently small,** you can raise the gain by
changing `R29`: gain = 100 × (1 + R29/R28). `R29` = 2M gives total gain 2100.
One 0805.

## 11.3 — Layout compliance — what the board actually does for this circuit

The AD8232 datasheet asks for specific layout properties. Here is what was
done, and it is checked:

| Datasheet asks for | This board |
|---|---|
| **A ground plane under the analog section** | ✅ **layer 2 is an unbroken `GND` plane under the whole ECG zone.** This is the single most important electrical property of the board — build guide step 14 exists to verify it. |
| Bypass close to the supply pin | ✅ `C23` (100 nF) placed at pin 17, `C24` (1 µF) bulk alongside |
| Short, guarded high-impedance nodes | ✅ the 10 MΩ nodes (`ECG_REFIN`, `ECG_HPSENSE`) are short and sit inside zone Z3, away from digital traffic |
| Keep switching noise away | ✅ **zone Z3 (ECG, x 66–98, y 4–40) is in the opposite corner from zone Z6 (alerts, x 66–98, y 50–68)** and 26 mm from the ESP32 in Z2 |
| Analog nets in their own net class | ✅ net class 3, `analog_ecg`, **0.20 mm width with 0.20 mm clearance** — wider clearance than the general rule |

> 🔵 **Why the ECG block is where it is.** It is placed as far as the board
> allows from the ESP32 module (the radio and the digital switching) and from
> the two FET drivers (the di/dt). That is a placement decision made
> specifically for this circuit, not an accident of the floorplan.

## 11.4 — Why one ground and not a split AGND/DGND

The full argument is in `GROUNDING_NOTES.md` and summarised in
[Part 12](#part-12--grounding-and-the-stack-up). The short version, because it
comes up every time:

1. **Return current follows the signal, not the schematic.** At any frequency
   above a few kHz, return current takes the path of least *inductance*, which
   is directly under its own trace. A split does not redirect it; it just
   removes the path it wanted.
2. **Any split needs a bridge, and the bridge becomes the problem.** Every
   signal crossing the split must cross at the bridge, or its return current
   takes a long detour and radiates.
3. **The AD8232 has its own analog ground internally.** It is designed for a
   single-ground system.

## 11.5 — The firmware contract this circuit imposes

| # | Requirement | Why |
|---|---|---|
| 1 | 🔵 **Wait ≥ 2.5 s after power-up** before trusting a reading | `R23`/`R24`/`C16` gives τ = 0.5 s; 5τ = 2.5 s |
| 2 | 🔵 **Read on `IO1` = `ADC1_CH0` only** | ADC2 does not work with the radio on |
| 3 | 🔵 **Sample at ≥ 250 Hz** | pass band tops out at 40 Hz; 250 Hz gives >6× oversampling and clean beat timing |
| 4 | 🔵 **Poll `LOD+` (`IO35`) and `LOD−` (`IO36`)** every cycle | tells you *which* electrode came off. Blank the output rather than reporting garbage |
| 5 | 🔵 **`ECG_SDN` (`IO37`) HIGH = enabled** | `R31` pull-up default. Drive it low for deep sleep (< 0.2 µA) |
| 6 | 🔵 **`ECG_FR` (`IO39`) LOW = fast restore off** | `R32` pull-down default. Pulse it high only to recover from saturation, and expect a transient |
| 7 | 🔵 **Expect the DC level at ~1.65 V**, not 0 V | the signal is referenced to `REFOUT`, not ground. Subtract the measured baseline |
| 8 | 🔵 **After `FR` or a leads-off event, discard ~1 s** | the HPF has to re-settle |

## 11.6 — Bench-checking the ECG stage before you touch a person

> 🔴 **B2 applies. Battery power, USB unplugged, informed participants only.**

1. Populate the stage. Power on **from battery**.
2. `TP11` (`ECG_REFOUT`) should read **≈ 1.65 V**. If it does not, stop — the
   reference network is wrong and nothing downstream will work.
3. Wait 2.5 s. `TP10` (`ECG_OUT`) should also idle **≈ 1.65 V** with nothing
   connected, possibly drifting because the inputs are floating through 10 MΩ.
4. Put a scope on `TP10`. Short LA and RA together at `J7`. The output should
   settle and go quiet — that is your noise floor.
5. Only then attach electrodes. A clean lead-I trace should appear within a few
   seconds, with the R-wave giving 0.5–1 V of swing.
6. If you see 50/60 Hz hum dominating: check the RL electrode is actually
   attached. **The RLD circuit is what rejects mains hum**, and it needs that
   third electrode.

## 11.7 — If you want to move toward waveform monitoring

The narrow pass band is a **configuration choice, not a limitation of the
part**. To widen it toward diagnostic ECG you change four passives:

| Change | Effect |
|---|---|
| Increase `C18` and/or `R25` | lowers the HPF pole 1 corner from 7.2 Hz |
| Increase `C19` and/or `R26` | lowers the HPF pole 2 corner from 0.72 Hz |
| Decrease `C20` and `C21` | raises the LPF corner above 41 Hz |

**The cost is motion artefact.** A 0.5 Hz–150 Hz channel on a walking subject
gives you a beautiful waveform when they stand still and an unusable one when
they move. That trade-off is the reason the design is where it is, and it
should be made consciously. `ECG_FRONTEND_DESIGN.md` has the full retune
arithmetic.

---

# PART 12 — Grounding and the stack-up

Source: [`documentation/GROUNDING_NOTES.md`](documentation/GROUNDING_NOTES.md).

## 12.1 — The decision, up front

$$\large\textsf{One ground net. One solid plane. No AGND/DGND split.}$$

This is a deliberate, defended decision, not a default.

## 12.2 — The stack-up

| EAGLE layer | Name | Role | Copper | Dielectric below |
|---|---|---|---|---|
| **1** | `Top` | signal + components | 35 µm | 0.36 mm |
| **2** | `Route2` | 🔵 **`GND` plane (solid)** | 35 µm | 0.71 mm |
| **15** | `Route15` | 🔵 **`3V3` plane (solid)** | 35 µm | 0.36 mm |
| **16** | `Bottom` | signal | 35 µm | — |

Total **1.6 mm FR-4**. `layerSetup = (1*2*15*16)`.

> **Both signal layers sit directly against a plane.** Layer 1 is 0.36 mm from
> the GND plane; layer 16 is 0.36 mm from the 3V3 plane. That means **neither
> signal layer is electrically worse than the other** — which is why the build
> guide tells you to use the bottom layer freely when finishing the airwires.

The 0.71 mm core between the two planes also makes them a **distributed
decoupling capacitor** across the whole board area — a free bonus of a 4-layer
stack.

## 12.3 — Why not split the ground — the three arguments

### 1. Return current follows the signal, not the schematic

At DC, return current spreads out and takes the lowest-resistance path. Above a
few kHz it takes the lowest-**inductance** path, which is **directly underneath
its own trace**, as close as the dielectric allows.

You cannot redirect that by drawing a line on a plane. All a split does is
**remove the path the current wanted to take**, forcing it to detour around the
slot — which increases loop area, which is exactly what radiates.

### 2. Any split needs a bridge, and the bridge becomes the problem

If you split AGND from DGND you must join them somewhere — usually a single
point near the ADC. Then **every signal that crosses the split must also cross
at that bridge**, or its return current takes the long way round.

On this board, signals crossing between the analog and digital regions include
`ECG_OUT`, `ECG_SDN`, `ECG_FR`, `ECG_LOD_P`, `ECG_LOD_N`, both I²C busses, and
all eight ADC lines. Routing all of those through one bridge point is not a
layout; it is a bottleneck that would make the board worse in exactly the way
the split was meant to prevent.

### 3. The AD8232 has its own analog ground, internally

It is a single-supply, single-ground part. Its `REFOUT` **is** the analog
reference for the signal chain, and it is generated on-chip. The datasheet's
own recommendation is a **solid ground plane**, not a split.

## 12.4 — What is done instead

Four things, all of which are more effective than a split:

### Placement separation

| Zone | Contents | Position |
|---|---|---|
| **Z3** | ECG analog front end | x 66–98, **y 4–40** |
| **Z6** | FET-driven alerts (motor, buzzer) | x 66–98, **y 50–68** |
| **Z2** | ESP32-S3 module | x 1–34, y 40–70 |

The ECG block is **10 mm from the alerts block in Y** and **~30 mm from the
module in X**. Noise falls off with distance far more reliably than it is
blocked by a slot in a plane.

### Motor return current is confined at its source

`C37` = 10 µF sits **local to the motor FET**, and the motor runs on `VBAT`
rather than `3V3`.

> 🔵 **This is the actual solution to motor noise.** The switching loop is
> `C37` → motor → `Q1` → `GND` and back to `C37`. Keeping that loop physically
> small keeps the di/dt out of the shared plane entirely. You do not need to
> stop the current reaching the ECG circuit if the current never leaves a
> 5 mm loop in the first place.

Same treatment for the buzzer with `C38`.

### Via stitching

**160 plane-connect vias.** Every plane-net pad gets its own dedicated via
straight down to its plane, plus 15 thermal vias on the exposed pads (9 of them
under the ESP32 module's EPAD).

> 🔵 This is why "copper pour NOT COMPUTED" is an acceptable limitation:
> **pad connectivity does not depend on the pour shape**, because each pad has
> its own via.

### 🟡 The antenna keep-out cuts *all* copper, planes included

```python
ANTENNA_KEEPOUT = (9.0, 63.4, 29.0, 70.0)   # 20 × 6.6 mm, top edge, flush
```

**Both plane polygons are drawn as an L that omits this rectangle.**

> A ground plane under a PCB antenna does **not** shield it. It **detunes** it
> and destroys the range. This is the single most commonly-made mistake with
> ESP32 modules and it is why:
>
> - no pad, via or track is inside the keep-out (DRC rule **D3**);
> - both planes are cut around it;
> - mounting hole `H3` moved to (2.6, 42) instead of the top-left corner
>   (⚪ **L1**) — a plated hole there would have done the same damage.

> 🟠 **Also keep the battery and any metal at least 10 mm away from the
> antenna region** (top edge, x 9–29 mm). A Li-Po pack laid against it will
> cost you most of your radio range. This is an enclosure-design constraint,
> not a PCB one, and it is easy to get wrong when you finally box it up.

## 12.5 — Where the analog reference actually lives

Not on the ground plane. `REFOUT` from the AD8232 — a **buffered 1.65 V virtual
ground** — is the reference for the entire ECG signal chain.

That is why:

- `TP11` exists (probe the reference directly);
- the ECG output idles at ~1.65 V, not 0 V;
- firmware must subtract a measured baseline rather than assuming zero.

The ground plane's job in the analog section is to be a **quiet, continuous
return path**, not to be the signal reference. Those are different jobs and
conflating them is where a lot of analog layout goes wrong.

## 12.6 — Verification status

| Check | Status |
|---|---|
| Plane polygons declared on layers 2 and 15 | ✅ present in the `.brd` |
| Antenna keep-out empty of copper | ✅ DRC rule D3 |
| Every plane-net pad has a via to its plane | ✅ DRC rule D7 |
| **Plane vias land inside the pour** | ✅ **MEASURED** — `validate_planes.py`. 🔴 **This caught a real defect:** two `GND` vias sat above the pour's y = 63.0 edge, one of them `C7`'s only path to the plane. Now 0 orphans |
| **Pour connectivity — one region?** | ✅ **MEASURED** — both pours keep one dominant region carrying ≥ 99.9 % of remaining copper, and **the ECG zone Z3 pour is entirely inside it on both planes.** Live figures in `pcb/plane_result.json` |
| **Pour shape exactly as EAGLE fills it** | ❌ still **NOT COMPUTED** — EAGLE calculates polygons on load. **Run `RATSNEST` in Fusion (build guide step 14).** |

> 🟠 **What to look for in Fusion after `RATSNEST`:** a dense row of vias can
> pinch a plane into two regions. Look for a **thin neck**, and if you find one
> **under the analog section**, move a via. Layer 2 being unbroken under the
> ECG block is the property to protect.

## 12.7 — If you do decide to split it later

`GROUNDING_NOTES.md` has a section on this. In brief: do it as a **moat with a
single deliberate bridge under the ADC**, route every crossing signal over that
bridge, and be prepared to prove with measurements that it improved things.
Most of the time it does not.

---

# PART 13 — The physical board

Look at `renders/pcb_assembly.png` while reading this. It has the zone boxes
and every reference designator.

## 13.1 — The floorplan

```
  y=70 ┌──────────────────────────────────────────────────────────────┐
       │ ▓▓▓ ANTENNA KEEP-OUT ▓▓▓                                     │
  y=68 │ (x 9–29, y 63.4–70)   ┌──────────────┐   ┌────────────────┐  │
       │                       │ Z7  USER     │   │ Z6  ALERTS     │  │
       │  ┌─────────────────┐  │     INPUT /  │   │  Q1 Q2 D7 D8   │  │
       │  │ Z2  ESP32-S3    │  │     STORAGE  │   │  J16 J17 R45   │  │
       │  │     CORE        │  │  SW4 J18     │   └────────────────┘  │
       │  │  U3 C7 C8 R7    │  │  R48-R51     │   y 50–68             │
       │  │  SW2 SW3 J5     │  └──────────────┘                       │
  y=42 │  │  D3 D4 R9 R10   │  ┌──────────────┐   ┌────────────────┐  │
       │  │                 │  │ Z4  I2C      │   │ Z3  ECG        │  │
       │  └─────────────────┘  │     SENSORS  │   │     ANALOG     │  │
       │  x 1–34, y 40–70      │  U4 U5 U6 J6 │   │     FRONT END  │  │
  y=31 │  ┌─────────────────┐  └──────────────┘   │  U7 J7          │  │
       │  │ Z1  POWER /     │  ┌──────────────┐   │  R18-R32        │  │
       │  │     CHARGING    │  │ Z5  MECH     │   │  C16-C24        │  │
       │  │  U1 U2 J1 J2 J3 │  │     SENSING  │   │                 │  │
       │  │  J4 D1 D2 C1-C6 │  │  U8 J8-J15   │   └────────────────┘  │
       │  └─────────────────┘  │  D5 D6       │   x 66–98, y 4–40     │
  y=4  │  x 4–32, y 4–36       └──────────────┘                       │
   y=0 └──────────────────────────────────────────────────────────────┘
       x=0                                                        x=100
```

Mounting holes: `H1` (3, 3) · `H2` (97, 3) · `H3` (2.6, 42) · `H4` (97, 67)

## 13.2 — Why 100 × 70 mm

The design started at **80 × 60 mm**. It grew, and the reason is measured
rather than aesthetic:

| Board | Outcome |
|---|---|
| 80 × 60 mm, 2 layers | ~50 of 81 nets routed; reachable copper split into disconnected regions |
| 80 × 60 mm, 4 layers | better, but the fan-outs had nowhere to escape to |
| **100 × 70 mm, 4 layers** | **76 of 80 nets routed, 0 geometry violations** |

The binding constraint was never component area — it was **escape area** around
the ESP32 module and the four fine-pitch parts. `DESIGN_ASSUMPTIONS.md` §3.

## 13.3 — Zone placement rationale

| Zone | Where | Why there |
|---|---|---|
| **Z1** Power | bottom-left | `J1` (battery) and `J2` (USB) are the two cables most likely to be plugged and unplugged; put them on the left and bottom edges |
| **Z2** ESP32 | top-left | the antenna **must** be at a board edge, and the keep-out has to be a corner region that no plane needs |
| **Z3** ECG | **right, bottom half** | 🔵 as far as possible from Z2 (radio + digital) and Z6 (di/dt) |
| **Z4** I²C sensors | centre | short busses to the module, and the AS5600 needs a magnet position that a centre location does not over-constrain |
| **Z5** Mech sensing | centre-bottom | its transducers all leave via the bottom edge |
| **Z6** Alerts | **right, top half** | 🔵 diagonally opposite the ECG block. Its two headers reach the top and right edges |
| **Z7** User I/O | centre-top | `SW4` (SOS) needs to be reachable by a finger; `J18` (microSD) on the top edge |

## 13.4 — The escape channels

```python
ESCAPE_CHANNELS = [
    (0.90, 43.0,  9.50, 64.0),    # left of the module's pad column
    (28.50, 40.0, 34.20, 64.0),   # right of the module's pad column
    (8.00, 36.00, 29.00, 44.20),  # below the module's end row
]
```

**These are component-free corridors.** They are the **single most important
placement constraint on the board.**

Why: the ESP32-S3-WROOM-1 presents **40 lands on 1.27 mm pitch across three
edges.** Without a dedicated corridor outboard of each land row, those 40
signals have literally nowhere to go — and both an autorouter and a human
stall in exactly the same place.

`CHANNEL_EXEMPT = {"C7", "C8", "R7", "C10"}` allows the module's own decoupling
and reset network inside the left channel. Keeping `C7`/`C8` within ~2 mm of
module pin 2 is worth more than the two track slots they cost, and both are on
a plane net anyway.

## 13.5 — Connector accessibility

**12 of 18 connectors are on a board edge.**

| Edge | Connectors |
|---|---|
| **bottom** (y < 6 mm) | `J14` piezo, `J15` hall, `J2` USB/5 V, `J4` fuel gauge, `J8` load cell |
| **left** (x < 6 mm) | `J1` battery, `J3` off switch, `J5` UART |
| **right** (x > 94 mm) | `J17` buzzer, `J7` ECG electrodes |
| **top** (y > 64 mm) | `J16` motor, `J18` microSD |
| **interior** | `J9`, `J10`, `J11`, `J12` (FSRs), `J13` (stretch), `J6` (2nd AS5600) |

**The six interior ones all take a flying lead** from a belt-mounted
transducer, so none of them needs a board edge.

> 🔵 **And putting the FSR headers in a vertical row inboard was deliberate.**
> A long horizontal row of through-hole pads across the board is **a wall
> through both signal layers.** Four vertical 1×2 headers cost a fraction of
> the routing area. `DESIGN_ASSUMPTIONS.md` §14.

## 13.6 — Assembly feasibility

| Method | Placements |
|---|---|
| hand-solderable | **146** |
| 🟠 **reflow / hot air only** | **3** |
| reflow or hot air (castellated) | 1 |

The three that **cannot** be soldered with an iron:

| Part | Package | Why |
|---|---|---|
| `U7` **AD8232** | LFCSP-20, 4 × 4 mm | **0.5 mm pitch + a 2.50 mm exposed pad** — the pad is under the body |
| `U5` **LSM6DSOX** | LGA-14L, 2.5 × 3.0 mm | **0.5 mm LGA** — no leads at all |
| `U4` **TMP117** | WSON-6 | **0.65 mm pitch + a thermal pad** |

`U3` (ESP32-S3-WROOM-1) is castellated at 1.27 mm — you *can* iron the
perimeter, but the **EPAD must be soldered**, so hot air or reflow is the real
answer.

> 🟠 **Order a stencil with the boards.** This is the item people forget, and
> without it the three parts above are not fittable.

## 13.7 — The mechanical envelope

❌ **No STEP geometry is attached to these footprints.** There is no solid
model and **no 3D interference check has been done.** What exists instead:

| Height | Ref | Package | Source |
|---|---|---|---|
| **8.50 mm** | `J9`, `J7`, `J6`, `J5`, `J2` | 2.54 mm headers | typical (mated with a crimp housing) |
| 6.00 mm | `J8`, `J1` | JST PH | typical (top-entry housing) |
| 5.00 mm | `SW4` | tactile 6 mm | typical (incl. plunger) |
| 3.10 mm | `U3` | ESP32-S3-WROOM-1 | **datasheet** (v1.8 Fig. 10-1, 3.1 ±0.15) |
| 1.75 mm | `U8`, `U6` | SOP-16 / SOIC-8 | typical (JEDEC narrow, 1.75 max) |
| 1.45 mm | `U2` | SOT-23-5 | typical |
| 1.12 mm | `Q1`, `Q2` | SOT-23-3 | typical |
| 1.10 mm | `D7`, `D8` | SOD-123 | typical |
| 0.90 mm | `C8` | C0805 | typical (a 22 µF part can reach 1.4) |
| 0.86 mm | `U5` | LGA-14L | **datasheet** (ST DS12814 Fig. 28) |
| 0.80 mm | `U4` | WSON-6 | **datasheet** (TI DRV0006B) |
| 0.80 mm | `U7` | LFCSP-20 | **datasheet** (AD8232 Rev. A) |
| 0.60 mm | `R9` | R0805 | typical |

**Tallest part: `J9` at 8.5 mm.** Minimum internal enclosure height therefore
about **11.6 mm** including the substrate and a little clearance.

> 🟠 **Enclosure constraints, collected:**
> - ≥ 11.6 mm internal height
> - **keep the battery and any metal ≥ 10 mm from the antenna region** (top
>   edge, x 9–29 mm)
> - four M2 standoffs, but **`H3` is at (2.6, 42), not the top-left corner**
>   (⚪ L1)
> - `J1`, `J3`, `J5` need cable exits on the **left**; `J7`, `J17` on the
>   **right**; five connectors on the **bottom**; two on the **top**
> - `SW2` (RESET) at (33.5, 42), `SW3` (BOOT) at (33.5, 49.5) and `SW4` (SOS)
>   at (46, 53.5) — **`SW4` needs a lid hole and a plunger**

---

# PART 14 — How the router works

You do not need this to use the project. Read it if a re-route surprises you,
or if you want to change the routing behaviour.

## 14.1 — The model

A **0.20 mm occupancy grid** per copper layer, held as numpy arrays. Each cell
is free, occupied by a specific net, or an obstacle.

## 14.2 — Clearance as dilation

Rather than testing every segment against every other segment (O(n²) on ~4 500
segments), the router **dilates** obstacles by the required clearance and then
treats them as solid:

```python
def _disc_offsets(): ...   # Euclidean disc offsets
def _dilate(...): ...
```

> 🔵 **Defect #2 was that this dilation used Manhattan distance** — a diamond
> instead of a disc. A diamond of "radius" 0.15 mm permits only 0.106 mm
> diagonally. It was replaced with a proper **Euclidean disc**, and that
> immediately made previously-"clean" routes fail — correctly.

## 14.3 — Width-aware exclusion

```python
NOMINAL_HALF_WIDTH = 0.100

def stamp_radius(half_width):
    return max(half_width, 2 * half_width - NOMINAL_HALF_WIDTH)
```

> 🔵 **Defect #9 was that the clearance model assumed every conductor was
> nominal width** — so a 0.50 mm power track was checked as if it were
> 0.20 mm. `stamp_radius` scales the exclusion with the actual conductor width.

## 14.4 — The search

**8-connected A\*** — so 45° routing is native rather than an afterthought:

```python
STEP_ORTHO = 10     # orthogonal step
STEP_DIAG  = 14     # ≈ 10·√2 — 45° priced correctly
VIA_COST   = 60     # a via costs six orthogonal steps
```

Pricing the diagonal at 14 rather than 10 is what stops the router from
producing staircases. Pricing a via at 60 makes it prefer to stay on a layer
unless changing genuinely helps.

## 14.5 — Transactional rip-up and retry

```python
def snapshot(): ...
def restore(): ...
def rip(net): ...
```

> 🔵 **Defect #5:** rip-up was **not transactional.** An attempt to improve the
> route took the unrouted count from **4 to 33** while the counter still
> reported success, because it tracked deltas instead of recomputing. Now every
> rip-up is a transaction that can be rolled back, and the final count is
> recomputed from the final state.

## 14.6 — Multi-seed best-of-N

```python
ATTEMPTS = 14      # override with SIH_ROUTE_ATTEMPTS
```

Net ordering dominates the result in a greedy router. So it tries **14
different orderings** and keeps the best. **The winning run was seed 8.**

## 14.7 — Fan-out before routing

Fine-pitch parts are given an explicit escape pattern *before* general routing
starts:

```python
FANOUT = {          # r1, r2, spread, stagger, width
    "AD8232": ..., "LSM6DSOX": ..., "TMP117": ..., "HX711": ...,
}
RADIAL_ESCAPE = {   # 3-level and 2-level stagger
    "ESP32-S3-WROOM-1": ..., "AS5600": ..., "TP4056": ...,
}
```

> 🔵 **The stagger is the trick that makes it work.** Alternate escape stubs
> are made *longer* so each has room for **its own via**. Without staggering,
> the vias collide and only every other pin can leave the part.

**45 fine-pitch escapes; 49 coarse-pitch radial stubs.**

> 🔵 **Defect #3 and #4** were that these stubs — and the plane-via spurs —
> were being drawn **straight across adjacent pads**, i.e. shorts. Both paths
> now check pad occupancy.

## 14.8 — The concession pass

$$\large\textsf{Clearance is prioritised over completeness.}$$

The final pass re-measures the emitted geometry. Any net whose only available
path violates the clearance rule is **ripped out and left as an airwire**, with
the measured gap recorded:

```
net I2C_SDA is not fully routed: left unrouted on purpose: every path the
router found came within 0.075 mm of FSR1_ADC on layer 1, below the 0.15 mm
rule. Route it by hand in Fusion.
```

**Why this is the right behaviour:** an airwire is visible in Fusion the moment
the board opens and takes a minute to route by hand. A 0.075 mm gap is
invisible and might reach fabrication.

## 14.9 — 🟠 The router is not deterministic across code changes

> Re-running after editing `design.py` will produce a **different** set of
> ~4 unrouted nets, not the same four. **Always re-read `DRC_REPORT.md` after
> a re-route** rather than trusting the list in any document, including this
> one.

## 14.10 — Where the four unrouted nets are, and why that is a placement fact

All four terminate on a part whose pads are fanned out at 1.2–1.9 mm:

| Congestion hotspot | Why |
|---|---|
| **ESP32 module** | 36 signals escaping a 1.27 mm pitch across three edges |
| **AD8232** | 0.5 mm QFN with an exposed pad in the middle |
| **LSM6DSOX** | 0.5 mm LGA, no leads |
| **HX711** | 9 plane pads, each taking a via right beside the pad |

> **These are the four most congested spots on the board and they are where a
> human router also spends their time.** The remaining airwires are not a
> failure of the tool; they are the last 5 % that always costs the most.

---

# PART 15 — Verification: what was checked and how

## 15.1 — The philosophy

> **Nothing is claimed as passing a tool that was never run.**

There was no EDA software available. So:

1. **Independent checkers were written** — `validate_erc.py` and
   `validate_drc.py`.
2. `validate_drc.py` **deliberately shares no code with the router**, so it can
   contradict it. (It did. Three times.)
3. Every document that mentions EAGLE's ERC or DRC says
   ❌ **"NOT EXECUTED — TOOL UNAVAILABLE"** in those words.
4. **Running Fusion's own ERC and DRC is your job** — build guide steps 6
   and 15.

## 15.2 — ERC: 11 rule groups, ✅ 0 errors, 0 warnings

Rules listed in [§7.3](#73--validate_ercpy-280-lines). Result:

```
parts            : 167
nets             : 84
pins in design   : 420
net connections  : 420

--- ERRORS (0) ---
--- WARNINGS (0) ---
--- NOTES (7) ---
RESULT: PASS
```

### The seven notes, and why each is information rather than a problem

| Note | Why it is fine |
|---|---|
| `LDO_NC`: intentional single-pin net | AP2112 pin 4 is documented "No Connection" (Diodes DS39724 Rev. 2-2). **Leaving it unconnected is the datasheet's own instruction.** |
| `IMU_OCS_AUX`: intentional single-pin net | LSM6DSOX DS12814 Rev. 4 Table 1 note 2: *"Leave pin electrically unconnected and soldered to PCB."* **Its own pad satisfies both halves of that instruction.** |
| SENSOR (I2C0) addresses: `J4`=0x36, `U4`=0x48, `U5`=0x6A | no clash |
| ANGLE (I2C1) addresses: `U6`=0x36 | no clash |
| 0x36 on **both** busses | 🔵 **the deliberate resolution of the fixed-address clash.** Electrically separate busses. |
| `Q1`: flyback `D7` present on `MOTOR_N` | orientation verified, not just presence |
| `Q2`: flyback `D8` present on `BUZZ_N` | same |

### The intentional exceptions, declared not silenced

| Item | Why it is acceptable |
|---|---|
| `LDO_NC` single-pin | datasheet says "No Connection" |
| `IMU_OCS_AUX` → `TP7` only | isolated land satisfies "unconnected but soldered" |
| `TMP_ALERT` → pull-up + test point, not a GPIO | no spare GPIO; TMP117 alerts are readable over I²C by polling |
| `AS_OUT`, `AS_PGO`, `HX_BASE`, `HX_XO` → test points | all four are datasheet "NC when not used" or optional-function pins |
| `0x36` on both busses | the resolution of a real conflict |

> The difference between **declared** and **silenced** matters. A silenced
> warning is indistinguishable from a missed one. `DECLARED_NO_CONNECT` in
> `validate_erc.py` names each exception explicitly with its datasheet
> citation.

## 15.3 — DRC: 8 rule groups, ✅ 0 geometry violations

Rules listed in [§7.7](#77--validate_drcpy-421-lines). Result:

```
--- ERRORS (4) ---      ← all D6 unrouted-net
--- WARNINGS (32) ---   ← all D6 "track copper forms N groups"
--- NOTES (8) ---
RESULT: FAIL
```

### 🔵 Why `RESULT: FAIL` is the correct output

There are **zero** clearance, width, drill, placement, keep-out or board-edge
violations. All four errors are the four **deliberately unrouted** nets.

**The script does not lower its own bar to produce a PASS.** An unrouted net
*is* a DRC error in every EDA tool, and pretending otherwise would be exactly
the kind of dishonest reporting this project is built to avoid.

### The measured numbers — these are the ones to quote

```
N: [D5] minimum wire-wire clearance on layer 1:  0.154 mm
N: [D5] minimum wire-wire clearance on layer 16: 0.175 mm
N: [D5] minimum wire-pad  clearance on layer 1:  0.130 mm
N: [D5] minimum wire-pad  clearance on layer 16: 0.130 mm
N: [D5] MEASURED MINIMUM COPPER CLEARANCE ANYWHERE ON THE BOARD: 0.130 mm.
        This is the number to quote to the fabricator.
N: [D6] router completed 76 of 80 signal nets
```

Only **two** pairs anywhere on the board are below 0.15 mm, both at 0.130 mm,
and **both are inside a declared fine-pitch fan-out region**:

```
N: [D5] layer 1:  SD_MOSI track to pad J12.1 at 0.130 mm
N: [D5] layer 16: HX_DOUT track to pad J11.1 at 0.130 mm
```

🟠 **This is what 🟠 H6 is about.** Quote 0.130 mm to the fab.

### The 32 warnings, explained once

Every one says: *"net X: track copper forms N groups. This is normal — a
multi-drop net reaches each pad separately and the pads join them — and is
reported only so a genuinely stranded stub cannot hide among them. Confirm with
RATSNEST in Fusion."*

`I2C_SCL` touches six pads. The router reaches each; **the pads themselves
complete the connection.** Copper-wise that looks like five separate groups. It
is fine. It is reported anyway so a genuinely disconnected stub cannot hide in
the noise — and **`RATSNEST` in Fusion is what confirms it** (step 14).

## 15.4 — The four unrouted nets, one more time

| Net | Came within | Of | Layer |
|---|---|---|---|
| `I2C_SDA` | 0.075 mm | `FSR1_ADC` | 1 |
| `SD_CS` | 0.090 mm | `LED_ALERT` | 1 |
| `SD_MISO` | 0.145 mm | `ESP_EN` | 1 |
| `ESP_EN` | 0.145 mm | `PIEZO_ADC` | 1 |

**Each is a short connection with both ends already fanned out.** Half an hour
of interactive routing clears them. Build guide step 13.

## 15.5 — The 19-point manufacturing check

Full table in `MANUFACTURING_CHECK.md`. Highlights and the items that need
*your* action:

| # | Item | Value | Needs you? |
|---|---|---|---|
| 1 | PCB dimensions | 100 × 70 mm (70 cm²) | |
| 2 | Board thickness | 1.6 mm FR-4 | **assumption** |
| 3 | Layer count | 4 — `(1*2*15*16)`, L2 = GND, L15 = 3V3 | |
| 4 | Copper thickness | 1 oz (35 µm) | **assumption** — drives the trace-width calc |
| 5 | Via sizes | drill 0.3 mm, pad 0.55–0.60 mm, 486 vias, all through | |
| 6 | Minimum trace width | 0.15 mm | |
| 7 | 🟠 **Minimum clearance** | **0.130 mm measured** | 🟠 **YES — H6** |
| 8 | Drill sizes | vias 0.3; pads 0.8, 1, 2.2 mm | JST PH 0.8 mm within JST's ø0.7 +0.1 spec |
| 9 | Component courtyard | no overlaps, 0.9 mm min gap | DRC D2 |
| 10 | Connector accessibility | 12 of 18 on an edge | the 6 interior take flying leads |
| 11 | Antenna keep-out | 20 × 6.6 mm, flush, empty | DRC D3 |
| 12 | Mounting holes | 4 × M2, 2.2 mm drill | ⚪ L1: `H3` is mid-edge |
| 13 | 🟠 Assembly feasibility | **3 parts need stencil + reflow** | 🟠 **YES — order the stencil** |
| 14 | ❌ Component availability | **NOT VERIFIED** | ⚪ **YES — L4** |
| 15 | Polarity markings | silkscreen cathode bar; pad 1 = cathode | in the library |
| 16 | Pin 1 markings | dot or chamfer; **pad 1 square** on every THT connector | in the library |
| 17 | Silkscreen readability | 0.8–1.1 mm vector text | ⚪ **assumption — L3** |
| 18 | 🟠 Solder paste / stencil | **required** | 🟠 **YES** |
| 19 | ❌ Manufacturing outputs | **NOT GENERATED** | 🟠 **YES — step 19** |

## 15.6 — The 27-point independent review

`FINAL_REVIEW.md`. Summary of the verdicts:

| ✅ Clean (20 items) | ⚠️ Open or partial (7 items) |
|---|---|
| wrong pin numbers · wrong power connections · missing grounds · missing decoupling · **I²C address conflicts (found in the input and resolved)** · ESP32 boot-pin conflicts · ADC limitations · buzzer drive · ECG noise · piezo overvoltage · regulator capacity (analysed, with a firmware requirement) · missing protection · MOSFET orientation · diode orientation · LED polarity · missing current-limiting resistors · floating inputs · unused pins · antenna keep-out · ERC issues | **#2 wrong footprints** — one item open (🟡 M1, the module EPAD) · **#9 motor current** — open, motor not selected (🔴 B3) · **#13 battery charging** — one accepted limitation (no power path), one open (🔴 B1) · **#15 connector polarity** — open (🔴 B1 JST) · **#24 PCB mechanical conflicts** — partially checked (no 3D model) · **#25 unrouted nets** — see the report · **#27 DRC issues** — see the report |

**Every ⚠️ maps to a numbered item in `REQUIRES_CONFIRMATION.md`.** There are
no orphan concerns.

---

# PART 16 — Workflow A: understand it without installing anything

**Time: 1–2 hours. Software needed: a Markdown viewer.**

Use this if you are evaluating the project, joining the team, or writing about
it.

### Step A1 — Read the blockers

[`documentation/REQUIRES_CONFIRMATION.md`](documentation/REQUIRES_CONFIRMATION.md),
or [Part 1](#part-1--the-blockers-read-this-before-anything-else) of this
document.

**Why first:** it is the only document that can stop you doing something
harmful, and it is short.

### Step A2 — Read the final report

[`documentation/FINAL_REPORT.md`](documentation/FINAL_REPORT.md). 15 sections.
It is the single-document answer to "what exists and what is left".

### Step A3 — Look at the renders

In this order:

1. `renders/pcb_assembly.png` — the board with zone boxes and designators.
   **This is the one that makes the whole thing click.**
2. `renders/pcb_layers.png` — all four copper layers. See the plane cut-outs
   and the antenna keep-out.
3. `renders/schematic_p1.png` through `p7.png` — the circuit, sheet by sheet.
4. `renders/pcb_3d.png` — the mechanical envelope.

**Every one of these is drawn by parsing the real `.sch`/`.brd`.** They cannot
show something the files do not contain.

### Step A4 — Read the two reports that state what was checked

- [`documentation/ERC_REPORT.md`](documentation/ERC_REPORT.md) — ✅ 0 errors,
  0 warnings, and the seven notes explained.
- [`documentation/DRC_REPORT.md`](documentation/DRC_REPORT.md) — 0 geometry
  violations, min clearance 0.130 mm, and the four deliberate airwires.

**Read the ❌ NOT EXECUTED blocks at the top of each.** They are the honest
part.

### Step A5 — Read the design reasoning

- [`documentation/DESIGN_ASSUMPTIONS.md`](documentation/DESIGN_ASSUMPTIONS.md)
  — 15 sections, every decision. Search for `[ARCHITECTURE CHANGE]` to find
  the seven deviations from the input diagram.
- [`documentation/ECG_FRONTEND_DESIGN.md`](documentation/ECG_FRONTEND_DESIGN.md)
  — if you care about the analog.
- [`documentation/GROUNDING_NOTES.md`](documentation/GROUNDING_NOTES.md)
  — if you were about to ask why the ground is not split.

### Step A6 — Read the review

[`documentation/FINAL_REVIEW.md`](documentation/FINAL_REVIEW.md). The 10
defects found and fixed are the most informative part of the whole project —
particularly the SOT-23-5 land pattern that shorted VIN to GND on the LDO.

### Step A7 — If you want to check a specific claim

| Claim | Where to verify it |
|---|---|
| a pinout | `COMPONENT_VERIFICATION.md` — names the exact document |
| a net | `NETLIST.md` |
| a GPIO | `GPIO_ASSIGNMENT.md` |
| a part | `BOM.md` |
| a current | `POWER_BUDGET.md` — each row names its source |
| a dimension | `MANUFACTURING_CHECK.md` or `PROJECT_STATISTICS.md` |
| a routing figure | `DRC_REPORT.md` — generated from the router's own output |

---

# PART 17 — Workflow B: regenerate the entire project

**Time: 5 minutes of your attention, 3–5 minutes of compute.
Software needed: Python 3.11+ with numpy, matplotlib, Pillow.**

Use this to confirm the files match the model, or after any change.

### Step B1 — Set up Python

See [§4.4](#44--python-for-regenerating-the-project).

### Step B2 — Run the whole build

```bash
python scripts/build_all.py
```

**Expected output, step by step:**

```
======================================================================
>>> library  (generate_library.py)
======================================================================
... library self-check PASS

>>> ERC  (validate_erc.py)
... RESULT: PASS

>>> schematic  (generate_schematic.py)
... cross-check PASS - 7 sheets, 167 parts, 84 nets, 420 pinrefs

>>> board (place + route)  (generate_board.py)
... [this is the slow one - 14 seeds]
... cross-check PASS - 150 elements, 84 signals

>>> DRC  (validate_drc.py)
... RESULT: FAIL          ← EXPECTED. 4 unrouted-net errors.

>>> renders  (render.py)
... 12 PNGs written

>>> documents  (generate_docs.py)
>>> reports  (gen_reports.py)

======================================================================
build finished in NNNs
steps with findings to review: DRC
```

> 🔵 **`RESULT: FAIL` on DRC and `steps with findings to review: DRC` are the
> normal, expected outcome.** DRC is marked non-fatal precisely because of the
> four deliberate airwires. See [§15.3](#153--drc-8-rule-groups--0-geometry-violations).

### Step B3 — The fast variant, for iterating

```bash
python scripts/build_all.py --fast
```

Sets `SIH_ROUTE_ATTEMPTS=1` — routes with a single ordering instead of
searching 14. Much faster.

> 🟠 **Use `--fast` while iterating, but do a full run before you believe any
> routing number.** A single-seed route will complete fewer nets than the
> best-of-14.

### Step B4 — Run individual steps

```bash
python scripts/generate_library.py
```

```bash
python scripts/validate_erc.py
```

```bash
python scripts/generate_schematic.py
```

```bash
python scripts/generate_board.py
```

```bash
python scripts/validate_drc.py
```

```bash
python scripts/render.py
```

```bash
python scripts/generate_docs.py
```

```bash
python scripts/gen_reports.py
```

**Order matters.** See [§7.1](#71--the-build-order-and-why-it-is-that-order).

### Step B5 — Check what changed

```bash
git status
```

```bash
git diff --stat
```

> 🟠 **Expect the `.brd` and the DRC/route reports to change even with no model
> edit**, because the router explores 14 orderings and ties break differently.
> The `.lbr`, `.sch`, ERC report, GPIO table, netlist and BOM should be
> **byte-identical** if you changed nothing. **If the `.sch` changes when you
> did not touch the model, that is a bug worth investigating.**

---

# PART 18 — Workflow C: change the design

**Time: minutes to a day depending on the change.**

## 18.1 — The golden rule

$$\large\textsf{Edit scripts/design.py, then re-run. Never edit the .sch or .brd to change the design.}$$

## 18.2 — Worked example 1: change a resistor value

**Task: set `R45` to 12 Ω to clear 🔴 B3.**

Find it in `design.py` (sheet 6 section):

```python
P("R45", "R-0805", "0R", "Motor ballast: populate only if the chosen motor is "
  "rated below 4.2 V", 6, 130, 195, "R0", 65.5, 54.0, "R0")
```

Change the value:

```python
P("R45", "R-0805", "12R", "Motor ballast for a 3.0 V / 100 mA motor. "
  "0.1^2*12 = 120 mW - use two 24R in parallel or a 1206.",
  6, 130, 195, "R0", 65.5, 54.0, "R0")
```

Then:

```bash
python scripts/build_all.py --fast
```

**What updates automatically:** the `.sch`, the `.brd` (value text), `BOM.md`,
`BOM.csv`, `NETLIST.md`, the schematic renders.

**Effort: 2 minutes.** No routing change — the footprint is identical.

## 18.3 — Worked example 2: change a footprint

**Task: change `R45` from 0805 to 1206 for the power rating.**

Two edits.

**1. Add the package and deviceset** in `lib_defs.py`, alongside the existing
0805 definitions. The IPC generator in `eagle_common.py` will produce the land
pattern from the body dimensions — a 1206 is 3.2 × 1.6 mm.

**2. Point the part at it** in `design.py`:

```python
P("R45", "R-1206", "12R", ...)
```

Then a **full** rebuild, because the footprint change moves copper:

```bash
python scripts/build_all.py
```

> 🟠 **Check `validate_drc.py` afterwards.** A bigger part can violate the
> 0.90 mm courtyard gap against its neighbours. `resolve_placement()` will try
> to move things; if it cannot, D2 will report it.

**Effort: 30–60 minutes.**

## 18.4 — Worked example 3: add a whole part

**Task: add a decoupling capacitor.**

**1.** Add it to `PARTS` on the right sheet, with schematic **and** board
coordinates:

```python
P("C40", "C-0805", "100n", "Extra bypass at U8 AVDD",
  5, 92, 168, "R0", 34.0, 19.5, "R90")
```

**2.** Add its pins to the nets:

```python
N("3V3", "C40.1")
N("GND", "C40.2")
```

> 🔵 **Both pins must be on a net.** ERC rule R3 requires every pin to be on
> exactly one net. If you forget, `validate_erc.py` will tell you before the
> board is ever routed — which is the whole reason ERC runs before routing.

**3.** Full rebuild.

**Effort: 15 minutes plus routing.**

## 18.5 — Worked example 4: move a part

For a **connector or an edge-mounted part**, edit `EDGE_PLACEMENT`:

```python
"J7": (97.2, 21.0, "R90"),   # ECG electrodes - right edge
```

For a **whole functional block**, edit `SHEET_OFFSET`:

```python
4: (13.0, 3.0),   # sheet 4 = zone Z3, ECG analog
```

> 🔵 **Moving a sheet moves the whole block, keeping every part's position
> relative to the pin it serves.** That is why the offsets exist — you can
> re-floorplan the board without touching 150 coordinates.

Then full rebuild, then check `validate_drc.py` for D1 (inside outline),
D2 (courtyard), D3 (keep-out).

## 18.6 — Worked example 5: change the board size or layer count

```python
BOARD_W = 110.0
BOARD_H = 80.0
```

Also update, or the geometry will be inconsistent:

| Also update | Why |
|---|---|
| `PLANE_OUTLINE` | the pours are drawn to explicit coordinates |
| `ZONES` | zone boxes are absolute |
| `MOUNT_HOLES` | corners moved |
| `EDGE_PLACEMENT` | edge coordinates moved |
| `ANTENNA_KEEPOUT` | if the module moved |
| `ESCAPE_CHANNELS` | if the module moved |

Then a **full** rebuild with all 14 seeds:

```bash
python scripts/generate_board.py
```

**Effort: an hour, plus re-checking everything.** Going *smaller* will
reduce the routed-net count; going bigger will improve it.

## 18.7 — The fork problem: model vs Fusion

$$\large\textcolor{orange}{\textsf{🟠 Read this before you touch anything in Fusion.}}$$

The moment you route an airwire in Fusion, the `.brd` contains something the
Python model does not. **Re-running `generate_board.py` will discard it.**

**You must pick one, and write the decision down:**

| Option | What it means | Best when |
|---|---|---|
| **A — the model stays authoritative** | all design changes go in `design.py`; you re-run and re-route the airwires by hand **each time** | you expect more design changes |
| **B — Fusion becomes authoritative** | you finish the board in Fusion and **stop running `generate_board.py`.** `design.py` remains the reference for the schematic, BOM and docs | you are done designing and going to fab |

**Recommended sequence:**

1. Make **all** the design changes you intend to make, in `design.py`.
2. Re-run the full build.
3. Check ERC and DRC.
4. **Then** switch to option B: open in Fusion, finish the airwires, and treat
   the `.brd` as final from that point.
5. **Commit the pre-Fusion `.brd` to git first**, so you can always get back to
   a regenerable state.

> Mixing A and B silently is how you lose an afternoon of hand-routing. It is
> not a flaw in the tooling; it is inherent to generating a file that a human
> then edits.

## 18.8 — What to re-check after any change

| Change | Re-check |
|---|---|
| a value | `BOM.md`, the schematic render |
| a footprint | `validate_drc.py` **D2** (courtyard), the library self-check |
| a new part | `validate_erc.py` **R3** (pins on nets), then routing |
| a net | `validate_erc.py` **R4–R8** |
| a GPIO | `GPIO_TABLE` too, or **R9** will fail |
| board size / layers | `PLANE_OUTLINE`, `ZONES`, `MOUNT_HOLES`, `EDGE_PLACEMENT`, then everything |
| a clearance constant | routing completeness — **expect it to change** |

## 18.9 — Adding a footprint from scratch — the rules that were learned the hard way

If you add a package to `lib_defs.py`, these are non-negotiable:

1. 🔴 **Use the vendor's recommended land pattern if one exists.** Three
   footprints in this library do, and they are the three fine-pitch parts —
   which is not a coincidence.
2. 🔴 **Check pad length vs pad width orientation.** Defect #6 was a SOT-23-5
   with these swapped, putting 1.10 mm pads on a 0.95 mm pitch. **It shorted
   VIN to GND on the LDO and looked perfectly plausible on screen.** The
   library self-check now detects pad overlaps — trust it, and read the comment
   in `sot23_package()`.
3. 🔴 **Do not apply IPC enlargement to a fine-pitch LGA.** Defect #7: on the
   LSM6DSOX's 0.5 mm LGA, enlargement closed the corner pairs to 0.11 mm. Use
   **1:1 with the package pad** (`PAD_L, PAD_W = 0.45, 0.25`).
4. 🔴 **Never use `<hole>` inside a package for a thermal via.** EAGLE's
   package `<hole>` is **UNPLATED**. Defect #1. Use board-level plated vias via
   `THERMAL_VIAS`.
5. 🔵 **Add the height** to `PACKAGE_HEIGHT`, labelled `"datasheet"` or
   `"typical"`. It feeds the 3D render and the enclosure table.
6. 🔵 **Mark pad 1**: square pad on through-hole connectors, silkscreen dot or
   chamfer on multi-pin SMD.
7. 🔵 **Run the self-check** — `python scripts/generate_library.py` — and read
   its output.

---

# PART 19 — Workflow D: open it in Autodesk Fusion, all 20 steps

**Time: half a day to a day. Software: Autodesk Fusion (Electronics).**

This expands
[`documentation/PCB_BUILD_GUIDE.md`](documentation/PCB_BUILD_GUIDE.md). Each
step has **Do / Check / What goes wrong**.

> 🔴 **Before you start, read [Part 1](#part-1--the-blockers-read-this-before-anything-else).**
> Three items there are BLOCKING; one of them is a fire risk.
>
> 🟠 **And read [§18.7](#187--the-fork-problem-model-vs-fusion)** — the moment
> you route something here, the `.brd` diverges from the Python model. Commit
> the current `.brd` to git first.

## What you already have, and what is left

| | State |
|---|---|
| Library (`.lbr`) | ✅ complete — 23 footprints, 28 symbols, 30 devices, all pinouts verified |
| Schematic (`.sch`) | ✅ complete — 7 sheets, 167 parts, 84 nets, every pin connected |
| Board (`.brd`) | ✅ placed and routed — 4 layers, both planes poured, exposed pads via-stitched |
| **Left to do** | finish the airwires (**step 13**), run Fusion's own ERC and DRC (**steps 6 and 15**), generate manufacturing files (**step 19**) |

---

## STEP 1 — Install and open Fusion

**Do:** install Fusion (the free personal-use licence includes Electronics).
Open it, then `File ▸ New Electronics Design`.

**Check:** the Electronics workspace opens with `Schematic` and `PCB` tabs.

**What goes wrong:** 🟠 **older standalone EAGLE 7.x cannot read these files** —
they use the EAGLE 9 XML format. EAGLE 9.x, Fusion Electronics and any current
Fusion all read them. If Fusion offers "Migrate EAGLE project", **say yes**.

## STEP 2 — Import the library

**Do:** `Library ▸ Open Library Manager ▸ Import ▸`
`libraries/SIH26113_Maternity_Assist_Belt.lbr`, and mark it **In Use**.

In EAGLE 9.x instead: drop the `.lbr` into your `lbr/` folder and enable it in
the Control Panel.

**Check:** the library appears with **30 devices**.

**What goes wrong:** if the schematic later shows "device not found", the
library was not marked In Use. 🔵 **The `.sch` and `.brd` also carry a full
embedded copy of the library**, so they open correctly even without this step —
importing it separately is only needed if you want to place *new* parts.

## STEP 3 — Verify the library symbols and footprints

**Do:** open these four in the library editor and compare against the
datasheet:

| Check | Why |
|---|---|
| `ESP32-S3-WROOM-1` | 🟡 **M1** — confirm the EPAD land sits within the module's exposed metal, against Espressif's downloadable land-pattern file (datasheet §11.1). The 40 signal pads are already verified including the 7.49 mm pin-1 datum. |
| `LGA-14L-2.5X3.0` | the LSM6DSOX has **no leads** — orientation is easy to get wrong at assembly. Note where pin 1 is marked. |
| `SOT-23-5` | 🔴 this is the LDO, and this footprint had a **VIN-to-GND short** before review. Confirm pads do **not** touch. |
| `TACT-6X6-THT` | 🟠 **H4** — confirm the **6.5 × 4.5 mm** lead grid matches your chosen switch |

**Check:** no pad overlaps; pin 1 markings present.

**What goes wrong:** the LSM6DSOX being placed 180° out at assembly is the
single most likely build error. Note the pin-1 marker **now**, while you can
see it on screen.

## STEP 4 — Open the schematic

> 🔵 **Open it from `fusion_project/`, not from `schematic/`.**
>
> EAGLE and Fusion pair a schematic with a board **by filename and
> directory** — opening `foo.brd` makes the tool look for `foo.sch` in the
> *same* folder. There is no link stored inside either file. This repository
> keeps them in `schematic/` and `pcb/` for legibility, which means opening
> either one from its own folder loads it **standalone**: the schematic/board
> consistency check cannot run and forward/back annotation is off.
>
> `python scripts/make_fusion_project.py` (also the last step of
> `build_all.py`) copies the `.lbr`, `.sch` and `.brd` into
> **`fusion_project/`** with a shared base name. **Open that folder.**

**Do:** open `fusion_project/SIH26113_Maternity_Assist_Belt.sch`.

**Check:** **7 sheets**, with the titles listed in
[§5.3](#53--documentation--all-18-documents). 167 parts.

**What goes wrong:** if a symbol appears as a question mark, step 2 was skipped
*and* the embedded library failed to load — which would mean a corrupted file.
Re-clone.

## STEP 5 — Confirm footprint assignment

**Do:** `Tools ▸ ... ` or open each device; confirm every part has a package.

**Check:** no part shows an unassigned package.

## STEP 6 — 🔵 Run Fusion's ERC

$$\large\textcolor{blue}{\textsf{This is one of the two checks that has NOT been run. It is now your job.}}$$

**Do:** `Tools ▸ ERC`.

**Check:** read every finding. **Expect these, and understand each before you
approve it:**

| Expected finding | Why it is acceptable |
|---|---|
| `LDO_NC` — single-pin net / unconnected pin | AP2112 pin 4 is documented **"No Connection"** (Diodes DS39724 Rev. 2-2) |
| `IMU_OCS_AUX` — single-pin net | LSM6DSOX DS12814 Rev. 4 Table 1 note 2: leave **electrically unconnected but soldered** |
| `TMP_ALERT` — no driver / only a pull-up and a test point | no spare GPIO; TMP117 alerts are readable over I²C |
| `AS_OUT`, `AS_PGO`, `HX_BASE`, `HX_XO` — only a test point | all datasheet "NC when not used" pins |
| Possible warnings about the two 0x36 devices | 🔵 **they are on physically separate busses.** Deliberate. |

**Approve** those. **Do not approve anything else without understanding it.**

> 🔵 The independent 11-group ERC passes with **0 errors, 0 warnings**. If
> Fusion reports something *outside* the table above, that is genuinely new
> information and worth chasing — the independent checker may have a blind
> spot.

## STEP 7 — Fix ERC errors

**Do:** for anything not in the table above, trace it back to `design.py`, fix
it there, re-run `build_all.py`, and re-open.

**Do not** patch it in Fusion — you will lose the fix on the next regenerate.
(Unless you have already committed to option B in
[§18.7](#187--the-fork-problem-model-vs-fusion).)

## STEP 8 — Open the board

**Do:** from the schematic, switch to the board (or open
`fusion_project/SIH26113_Maternity_Assist_Belt.brd`). 🔵 **Again: from
`fusion_project/`, so Fusion sees it as the matching pair — see step 4.**

**Check:** 100 × 70 mm outline, 150 elements, tracks on layers 1 and 16,
plane polygons on layers 2 and 15.

**What goes wrong:** if the board opens with everything piled at the origin, the
`.brd` did not load its element positions — re-clone.

## STEP 9 — Verify the board outline and stack-up

**Do:** check the layer setup.

**Check:**

| Property | Expected |
|---|---|
| Outline | 100 × 70 mm on layer 20 |
| Layer setup | `(1*2*15*16)` |
| Layer 2 | `Route2` — solid `GND` pour |
| Layer 15 | `Route15` — solid `3V3` pour |
| Thickness | 1.6 mm |
| Dielectrics | 0.36 / 0.71 / 0.36 mm |

## STEP 10 — Review the placement

**Do:** turn on the `tPlace` and `tDocu` layers. Compare against
`renders/pcb_assembly.png`.

**Check:**

- the seven zones are recognisable
- ⚪ **`H3` is at (2.6, 42)**, mid-left edge, not the top-left corner (L1)
- the antenna keep-out at the top edge is **empty of everything**
- nothing overlaps

## STEP 11 — Route the critical analog signals

**Do:** if you are re-routing anything by hand, do the ECG nets **first**, on
the top layer, short, and staying over the layer-2 GND plane.

**Check:** `ECG_LA_F`, `ECG_RA_F`, `ECG_REFIN`, `ECG_REFOUT`, `ECG_HPSENSE`,
`ECG_IAOUT` are short and do not run alongside digital traffic.

> 🔵 Those are the 10 MΩ nodes. They are the most noise-sensitive copper on the
> board.

## STEP 12 — Route power

**Do:** confirm `VBAT`, `VBUS` and the motor path are on **0.50 mm** tracks.

**Check:** the `VBAT` feed to the LDO and the motor path both look like power,
not signal.

## STEP 13 — 🔵 Finish the remaining airwires

$$\large\textcolor{blue}{\textsf{This is the main job left. Budget half an hour.}}$$

**Do:** `View ▸ Show/Hide layers`, turn on **`Unrouted` (layer 19)**. Each
yellow line is a connection to complete. Use the interactive router (`ROUTE`),
pick the net-class width Fusion offers, and draw it.

The list is in `DRC_REPORT.md` with the specific terminal that could not be
reached. All of them are at the four most congested spots: the ESP32 module
(36 signals escaping 1.27 mm pitch), the AD8232 (0.5 mm QFN), the LSM6DSOX
(0.5 mm LGA) and the HX711 (9 plane pads each taking a via beside the pad).

**Practical hints — these matter:**

| Hint | Why |
|---|---|
| 🔵 **Every pad already has a fan-out stub** — a short escape track ending in open space. **Start from the end of the stub, not from the pad.** | the hard part is already done for you |
| 🔵 **Use the bottom layer freely.** | it is much emptier than the top, and both signal layers sit against a plane, so neither is electrically worse |
| 🔵 **Place a via right at the stub end** and continue on layer 16. | the stubs are **staggered** — alternate ones are longer — specifically so each has room for its own via |
| 🔵 **Set the grid to 0.05 mm and enable 45° routing.** | Fusion's default 90° mode wastes space |

**Check:** the `Unrouted` layer is **empty**, and `Tools ▸ DRC` reports no
"Unrouted" items.

## STEP 14 — 🔵 Verify the ground plane

**Do:** type **`RATSNEST`** after any routing change. **Fusion recomputes pours
on demand, not automatically.**

**Check:**

- layer 2 is a **continuous `GND` pour** with no large islands cut off by via
  clusters
- layer 15 is a continuous `3V3` pour
- **both stop short of the antenna keep-out**
- 🔵 **under the ECG block, layer 2 is unbroken. This is the single most
  important electrical property of the board.**

**What goes wrong:** a dense row of vias can pinch a plane into two regions.
Look for a **thin neck**, and if you find one under the analog section, **move
a via.**

## STEP 15 — 🔵 Run Fusion's DRC

$$\large\textcolor{blue}{\textsf{The second check that has NOT been run.}}$$

**Do:** `Tools ▸ DRC`. **First load the design rules that are already in the
`.brd`** — the rule set is named `SIH26113_4layer`:

```
mdWireWire = 0.127 mm     (min wire-to-wire)
msWidth    = 0.15 mm      (min width)
msDrill    = 0.3 mm       (min drill)
```

**Check:** zero clearance, width and drill errors.

**What goes wrong:** 🟠 **if Fusion's default rule set is loaded instead
(usually 6 mil / 0.152 mm), you will get a wall of clearance errors inside the
four fine-pitch fan-outs.** Those are the declared 0.127 mm exception — load
the board's own rules before you panic. And note: **if your fab is 6 mil-only,
those errors are real for you** — see the H6 fallback.

## STEP 16 — Fix DRC errors

**Do:** for each error, decide whether it is inside a declared fine-pitch
fan-out (acceptable at ≥ 0.127 mm) or outside one (must be fixed).

The four fan-out regions are around **`U7` AD8232, `U5` LSM6DSOX, `U4` TMP117
and `U8` HX711**.

## STEP 17 — Inspect in 3D

**Do:** Fusion's 3D PCB view.

**Check:** connector orientations look sane; nothing obviously fouls.

> ❌ **This is not an interference check.** No STEP models are attached to these
> footprints. Fusion will show generic bodies or nothing at all. The real
> mechanical data is the height table in
> [§13.7](#137--the-mechanical-envelope).

## STEP 18 — Check mechanical clearances

**Do:** against your enclosure design, check:

- ≥ **11.6 mm** internal height (tallest part `J9` at 8.5 mm)
- the four M2 holes, remembering ⚪ **`H3` is at (2.6, 42)**
- cable exits: left (`J1`, `J3`, `J5`), right (`J7`, `J17`), bottom (five),
  top (two)
- 🔵 **≥ 10 mm clearance from the antenna region** (top edge, x 9–29 mm) to
  the battery and any metal
- lid access to `SW4` (SOS) at (46, 53.5) — it needs a hole and a plunger

## STEP 19 — Generate manufacturing outputs

**Do:** `Manufacturing ▸ CAM Processor`, pick a 4-layer Gerber X2 job (or your
fab's own job file), and generate.

**Check** you get:

| File | Content |
|---|---|
| `*.GTL` / `*.GBL` | top and bottom copper |
| `*.G2L` / `*.G15` (or `.GP1`/`.GP2`) | 🔵 the two inner planes |
| `*.GTS` / `*.GBS` | solder mask |
| `*.GTO` / `*.GBO` | silkscreen |
| `*.GML` / `*.GKO` | board outline |
| `*.TXT` / `*.DRL` | drill file |
| 🟠 `*.GTP` | **top solder paste — needed for the stencil** |

> 🟠 **You need a stencil.** Three parts cannot be soldered with an iron: the
> AD8232, the LSM6DSOX and the TMP117. **Order the stencil with the boards.**

**Specify to the fab:**

- 4 layers, 1.6 mm FR-4, 1 oz outer copper
- minimum track **0.15 mm**
- 🟠 minimum gap **0.127 mm (5 mil)** — the **measured** minimum copper
  clearance is **0.130 mm**, so a 6 mil (0.152 mm) process **will not make this
  board**
- minimum drill **0.30 mm**
- HASL or **ENIG** (ENIG is better for the fine-pitch parts)
- stack-up `(1*2*15*16)` — **tell them layers 2 and 15 are planes**

❌ **No Gerbers are included in this project.** They need EAGLE's CAM processor,
which was not available.

🔵 **Then open the Gerbers in an independent viewer** (gerbv, or your fab's own
online viewer) **before you pay.** Check: four copper layers present, the two
inner ones are planes with the antenna corner cut, the paste layer has openings
for the three fine-pitch parts, and the outline is a closed 100 × 70 mm
rectangle.

## STEP 20 — Final review before you spend money

Go through `documentation/FINAL_REVIEW.md`, then this checklist:

- [ ] 🔴 `REQUIRES_CONFIRMATION.md`: **all three BLOCKING items resolved**
- [ ] 🔴 The Li-Po cell at `J1` **has integrated protection** (B1)
- [ ] 🔴 `J1` polarity **checked with a meter** against the actual pigtail (B1)
- [ ] 🔴 ECG safety protocol **written down and agreed** (B2)
- [ ] 🔴 Motor voltage rating checked, **`R45` value decided** (B3)
- [ ] 🟠 Module ordered is **`-N8R2`**, not N8R8 or N16R8 (H5)
- [ ] 🟠 Tactile switch pin grid confirmed as **6.5 × 4.5 mm** (H4)
- [ ] 🟠 `R37` set for the actual stretch sensor, or accepted as a placeholder (H2)
- [ ] 🟠 Load cell bridge resistance and mV/V known (H3)
- [ ] 🟠 MAX17048 decision made (H1)
- [ ] ✅ Fusion ERC run, exceptions **approved and understood** (step 6)
- [ ] ✅ Fusion DRC clean **against the board's own rule set** (step 15)
- [ ] ✅ `Unrouted` layer **empty** (step 13)
- [ ] ✅ `RATSNEST` run; layer 2 **unbroken under the ECG block** (step 14)
- [ ] ✅ Gerbers + drill + **paste** generated **and viewed in a Gerber viewer**
- [ ] 🟠 **Stencil ordered**
- [ ] 🟠 Fab confirmed **0.127 mm (5 mil) gap**, 0.15 mm track, 0.30 mm drill on 4 layers (H6)

---

# PART 20 — Workflow E: order the PCB

**Time: 2 hours of ordering, then 1–3 weeks of lead time.**

## 20.1 — 🟠 Before you spend money

Clear these first. Every one costs more to fix after the boards arrive:

| | Item | Consequence if wrong |
|---|---|---|
| 🟠 **H6** | fab must quote **5 mil / 0.127 mm gap** on 4 layers | **the board cannot be made**, or is made with shorts |
| 🟠 **H5** | module must be **`-N8R2`** | ECG channel dead, PSRAM corrupted |
| 🟠 **H4** | tactile switch grid **6.5 × 4.5 mm** | switches do not fit |
| 🟠 **item 18** | **order the stencil** | three parts unfittable |
| 🔴 **B1** | protected Li-Po pack | fire risk |
| 🔴 **B3** | motor choice → `R45` | motor destroyed, or resistor burned |

## 20.2 — The fab specification, ready to paste

```
Board name:        SIH26113 Maternity Assist Belt
Dimensions:        100 mm x 70 mm  (rectangular)
Layers:            4
Material:          FR-4
Thickness:         1.6 mm
Copper weight:     1 oz (35 um) outer;  1 oz inner
Stack-up:          L1 signal / L2 GND plane / L15 3V3 plane / L16 signal
                   EAGLE layerSetup (1*2*15*16)
                   Dielectrics 0.36 / 0.71 / 0.36 mm
Min track width:   0.15 mm  (6 mil is NOT sufficient - see below)
Min clearance:     0.127 mm  (5 mil)   *** MEASURED MINIMUM 0.130 mm ***
Min drill:         0.30 mm
Max drill:         2.20 mm  (M2 mounting holes)
Surface finish:    ENIG preferred (HASL acceptable)
Solder mask:       any colour
Silkscreen:        white, min text height 0.8 mm, stroke 0.15 mm
Vias:              all through-hole, 0.3 mm drill / 0.55-0.60 mm pad
                   486 vias
Plated holes:      0.8 mm (JST PH), 1.0 mm (tactile switches),
                   2.2 mm (M2 mounting, plated, GND-connected)
Panelisation:      none required
ALSO REQUIRED:     top-side solder-paste STENCIL
```

> 🟠 **The one line that matters most:** *minimum clearance 0.127 mm (5 mil).*
> The common default is 6 mil. **Change it.**

## 20.3 — Walkthrough: JLCPCB

1. Upload the Gerber ZIP.
2. **Layers: 4.** The price jumps here; that is expected and unavoidable — see
   [§2](#part-2--what-this-project-actually-is) on why four layers.
3. Dimensions should auto-detect as **100 × 70 mm**. If it detects something
   else, your outline layer did not export — go back to step 19.
4. Thickness: **1.6 mm**.
5. **Minimum track/spacing: change from the default to 5/5 mil.**
6. Via hole size: **0.3 mm** (their standard).
7. Surface finish: **ENIG** if you can afford it. The three fine-pitch parts
   solder noticeably better on a flat finish, and HASL on a 0.5 mm-pitch QFN is
   genuinely harder.
8. **Impedance control: not required.** ✅ M2 is resolved — the pair measures
   ≈ 165 Ω rather than 90 Ω, but at Full Speed over 44 mm it is electrically
   short by 2.6×, so controlled impedance buys you nothing here. See
   `documentation/USB_PAIR_ANALYSIS.md`.
9. **Add "SMT Stencil" to the order.** Top side only. Framed if you have a jig;
   frameless is fine with tape and a stiff card.
10. Review their DFM report. **Read it.** Fabs catch things.

## 20.4 — Walkthrough: PCBWay

Same sequence. The 5 mil option is under **"Min Track/Spacing"**. Their
engineering review is thorough and they will email you about anything odd —
answer it rather than clicking through.

## 20.5 — Assembly service (PCBA)? Read this first

You *can* have a fab assemble it, and for the three fine-pitch parts that is
genuinely attractive. But:

| Issue | Reality |
|---|---|
| ⚪ **L4 — no supplier part numbers in the BOM** | you will have to fill in Supplier / Supplier PN yourself. The BOM has empty columns for exactly this. |
| **Generic passives** | most values have blank MPNs — "any part meeting the value and package". Fine for a fab's basic-parts library. |
| **`R45` = 0 Ω** | 🔴 **B3 — do not let them fit 0 Ω if your motor is 3.0 V.** Either resolve B3 first, or mark `R45` DNP and fit it yourself. |
| **`R17` = 0 Ω DNP** | 🔵 **explicitly mark this DNP.** It links a strapping pin. |
| **Off-board transducers** | the load cell, FSRs, stretch sensor, piezo, motor, buzzer and electrodes are **not on the board**. Do not put them in a PCBA BOM. |
| 🟠 **H5** | **check what module they actually stock.** Fabs substitute. `-N8R8` is more common. |

**Recommended hybrid:** have the fab assemble **only** `U4`, `U5`, `U7` (the
three reflow-only parts) plus `U3` if they will, and hand-solder the other
~146 placements yourself. You keep control of the risky choices and skip the
work you cannot do.

## 20.6 — Ordering the components

Order **before** the boards arrive; some parts have lead time.

### The parts that need attention

| Ref | Part | ⚠️ |
|---|---|---|
| `U3` | **ESP32-S3-WROOM-1-N8R2** | 🟠 **H5 — read the full suffix.** Buy 2; they are cheap and the first one may go 180° out |
| `U7` | **AD8232ACPZ-R7** | ⚪ **L4 — occasionally allocated.** Check stock early |
| `U5` | **LSM6DSOXTR** | ⚪ L4 — also worth checking |
| `U4` | TMP117AIDRVR | |
| `U6` | AS5600-ASOM | |
| `U8` | HX711 | usually from Chinese distributors |
| `U1` | TP4056-42-SOP8-PP | bare IC, **not a module** |
| `U2` | AP2112K-3.3 | SOT-23-5 |
| `Q1`, `Q2` | AO3400A ×2 | |
| `D5`–`D8` | 1N5819HW ×4 | SOD-123 |
| `J1` | JST **S2B-PH-K-S** | 🔴 **B1 — and meter the pigtail polarity** |
| `J8` | JST **S4B-PH-K-S** | 🟠 H3 — identify the load cell wires by measurement |
| `SW2`–`SW4` | tactile 6 × 6 mm ×3 | 🟠 **H4 — confirm the 6.5 × 4.5 mm grid** |
| `R45` | 🔴 **see B3** | order 0 Ω **and** a few values of ballast |
| `R37` | 🟠 **see H2** | order a range once the sensor is chosen |
| `C34` | 100 nF **50 V** 0805 | 🟡 **M4 — the voltage rating is not optional** |
| `C8` | 22 µF 0805 | note it may be 1.4 mm tall rather than 0.9 |

### Passives — just buy a kit

50 × 0805 resistors and 38 × 0805 capacitors across ~18 values. An 0805
resistor and capacitor assortment kit is cheaper than ordering the values
individually, and you will want spares.

Values you need, from the BOM:

**Resistors (0805):** 0 Ω, 100 Ω, 1 k, 2k4, 4k7, 10 k, 100 k, 330 k, 470 k,
1 M, 10 M
**Capacitors (0805):** 1 nF, 3n9, 8n2, 10 nF, 100 nF, 100 nF/50 V, 220 nF,
1 µF, 10 µF, 22 µF

### Off-board transducers

| Function | Part |
|---|---|
| Load cell | 🟠 H3 — any 4-wire strain-gauge cell. Note bridge resistance and mV/V |
| FSR × 4 | FSR402 or equivalent |
| Stretch sensor | 🟠 H2 — conductive rubber or equivalent. **Measure R_min and R_max** |
| Piezo film | 🟡 M4 — measure its capacitance |
| Vibration motor | 🔴 **B3 — note the rated voltage and current** |
| Buzzer | 🟡 M3 — note whether it is **active** or **passive** |
| ECG electrodes | disposable Ag/AgCl × 3 |
| Magnet | 🟡 M6 — diametric NdFeB, ~6 × 2.5 mm |
| microSD breakout | any SPI module with a 6-pin header |
| Li-Po pack | 🔴 **B1 — PROTECTED, with a JST-PH pigtail** |

---

# PART 21 — Workflow F: assemble the board

**Time: a full day for the first one. Do not rush it.**

## 21.1 — 🔵 The golden rule of assembly

$$\large\textcolor{blue}{\textsf{Populate in stages and test after each one. Do not build the whole board and apply power.}}$$

Six stages, matching [Part 22](#part-22--workflow-g-bring-up-in-six-stages).
**Each stage ends with a measurement.** If you populate everything and it does
not work, you have 150 suspects.

## 21.2 — The three parts that need reflow, done first

Do the fine-pitch parts **on a bare board**, before anything else is in the
way.

| Part | Package |
|---|---|
| `U7` **AD8232** | LFCSP-20, 0.5 mm pitch, 2.50 mm exposed pad |
| `U5` **LSM6DSOX** | LGA-14L, 0.5 mm, no leads |
| `U4` **TMP117** | WSON-6, 0.65 mm, thermal pad |
| `U3` **ESP32-S3-WROOM-1** | castellated 1.27 mm — perimeter is iron-able, **the EPAD is not** |

### Stencil procedure

1. Tape the bare PCB to a flat surface. Shim it with **scrap boards of the same
   1.6 mm thickness** on all four sides, so the stencil sits flat.
2. Align the stencil to the pads. Use the fiducial-ish features — the M2 holes
   and the board outline — and check a fine-pitch part under magnification
   before you squeegee.
3. Tape one edge of the stencil down as a hinge.
4. Apply paste along one edge. Squeegee at ~45° in **one firm pass**.
5. Lift the stencil **straight up**, not by peeling.
6. **Inspect under magnification.** You want distinct bricks on every 0.5 mm
   pad. Bridged paste on a QFN becomes bridged solder.
7. Place the parts with tweezers. **Check orientation now** — see below.
8. Reflow on a hotplate or in an oven, following the paste's profile. Or hot
   air at ~300 °C, moving constantly, watching for the parts to settle.
9. **Inspect again.** Look for bridges between adjacent pins.

### 🔴 Orientation — the three that will catch you

| Part | The tell |
|---|---|
| `U5` **LSM6DSOX** | **no leads, near-square, and the marking is tiny.** This is the most likely 180° error on the board. Find the pin-1 dot under a microscope and match it to the silkscreen dot **before** you place it. |
| `U7` **AD8232** | LFCSP has a chamfered corner and a pin-1 dot |
| `U4` **TMP117** | WSON-6 — pin-1 dot |
| `U3` module | unmistakable (the antenna end), but **make sure the antenna points off the board edge**, over the keep-out |

## 21.3 — Then the SMD passives, by stage

Hand-solder 0805s with an iron. Tin one pad, place the part, reflow that pad,
then do the other.

**Order:** stage 1 power parts → stage 2 module support → stage 3 sensor
passives → stage 4 mechanical front ends → stage 5 alert drivers → stage 6 ECG
passives.

## 21.4 — Then the through-hole parts

Connectors, switches, mounting hardware.

> 🔵 **Pad 1 is square on every through-hole connector.** That is manufacturing
> check item 16. Use it — especially on `J1` and `J8`, where getting it wrong
> matters.

**Polarised parts:**

| Part | Orientation |
|---|---|
| `J1` JST-PH-2 | 🔴 pin 1 = `VBAT` (+). **Square pad.** Meter the pigtail (B1) |
| `J8` JST-PH-4 | pin 1 = E+, 2 = E−, 3 = A+, 4 = A− |
| `D1`–`D4` LEDs | 🔵 **pad 1 = cathode** on every 2-pin polarised footprint. Silkscreen cathode bar |
| `D5`–`D8` diodes | 🔵 same convention — and 🔴 `D5`/`D6` clamp polarity is what protects the ADC |

## 21.5 — 🔵 The 25 ECG passives go last

`U7`'s 25 supporting passives are the **last** thing you fit, in stage 6, after
everything else is proven. There are two reasons:

1. The ECG stage is the only part that touches a person. You want everything
   else known-good first.
2. If you have to rework anything near zone Z3, you would rather not be working
   around 25 freshly-placed 0805s.

## 21.6 — Inspection before first power

- [ ] No solder bridges — check every fine-pitch part under magnification
- [ ] `U5` orientation confirmed against the pin-1 dot
- [ ] 🔴 **No short between `TP1` (`VBAT`) and `TP3` (`GND`)** — meter it
- [ ] 🔴 **No short between `TP2` (`3V3`) and `TP3` (`GND`)** — meter it
- [ ] No short between `TP4` (`VBUS`) and `TP3`
- [ ] Flux residue cleaned off, especially around the 10 MΩ ECG nodes
      (🔵 **flux is conductive enough to matter at 10 MΩ**)
- [ ] Every polarised part oriented per the silkscreen
- [ ] `R17` **left unpopulated** unless you specifically want the side-B analog
      path
- [ ] 🔴 **`R45` value decided** (B3)

---

# PART 22 — Workflow G: bring-up, in six stages

**Time: two days. Do not skip a stage.**

> 🔵 **Use a bench supply with a current limit** for every stage. Set 5 V,
> limit to just above the expected draw. A short then shows as the limit
> engaging, not as smoke.

---

## Stage 1 — Power only

$$\large\textcolor{blue}{\textsf{Do not proceed until 3V3 is correct. Every other part is on that rail.}}$$

**Populate:** `U1`, `U2`, `R1`–`R6`, `C1`–`C6`, `D1`, `D2`, `J1`, `J2`, `J3`.

**Do:**

1. Apply **5 V to `J2`** from a current-limited supply. Limit to **100 mA**
   initially.
2. Measure at the test points:

| Test point | Expected |
|---|---|
| `TP4` (`VBUS`) | **5 V** |
| `TP2` (`3V3`) | 🔵 **3.3 V ±1.5 %** (3.25 – 3.35 V) |
| `TP3` (`GND`) | 0 V (your reference) |

3. Now connect the **protected** Li-Po pack to `J1`. 🔴 **Meter the pigtail
   polarity first (B1).**
4. `TP1` (`VBAT`) should read the cell voltage, 3.0 – 4.2 V.
5. `D1` (red) should light while charging; `D2` (green) when complete.
6. Disconnect `J2`. `TP2` should still read 3.3 V — the board now runs from the
   cell.
7. Test `J3`: **shorting `J3` should turn the board OFF** (⚪ L2 — this is
   inverted from what you expect). `TP2` drops to 0 V.

**If `TP2` is not 3.3 V:** go to [Part 24](#part-24--troubleshooting-encyclopedia),
"3V3 is wrong or absent".

---

## Stage 2 — The module

**Populate:** `U3`, `C7`, `C8`, `R7`, `C10`, `SW2`, `SW3`, `R8`, `J5`,
`R9`, `R10`, `D3`, `D4`.

**Do:**

1. Power up. Current draw should be tens of mA idle.
2. Connect USB to `J2` and confirm the ESP32-S3 appears as a **serial device**:
   - Windows: "USB Serial Device (COMx)"
   - Linux: `/dev/ttyACM0`
   - macOS: `/dev/cu.usbmodem*`
3. 🔵 **No driver is needed** — this is the ESP32-S3's **native
   USB-Serial-JTAG**, so the MCU *is* the USB device.
4. Flash something trivial (blink).
5. Confirm `D3` (green, `IO45`) and `D4` (red, `IO46`) blink.
6. Test `SW2` (RESET) and `SW3` (BOOT). Holding BOOT while pressing RESET should
   put it into download mode.
7. Read the chip info and **confirm 8 MB flash and 2 MB PSRAM.**

> 🟠 **If it reports 8 MB PSRAM, you have an `-N8R8` module (H5).** Stop. The
> ECG channel will not work. Replace it.

**If no serial device appears:** use `J5` (UART) with a USB-serial adapter —
`J5.3` = TX, `J5.4` = RX, `J5.5` = `EN`, `J5.6` = `IO0`, `J5.1` = `GND`. That
is what the header is for (🟡 M2).

---

## Stage 3 — I²C sensors

**Populate:** `U4`, `U5`, `U6`, `C11`–`C15`, `R11`–`R13`, `R15`, `R16`.

**Do:**

1. Run an **I²C scan on both busses**:

| Bus | Pins | Expect |
|---|---|---|
| SENSOR (I2C0) | SDA `IO15`, SCL `IO16` | 🔵 **0x48** (TMP117) and **0x6A** (LSM6DSOX) |
| ANGLE (I2C1) | SDA `IO14`, SCL `IO42` | 🔵 **0x36** (AS5600) |

2. Read the TMP117 temperature. Should be room temperature ± a couple of
   degrees. 🟡 **M7 — remember it is reading pod temperature.**
3. Read the LSM6DSOX WHO_AM_I register: **should be `0x6C`.**
4. Read accelerometer data. With the board flat, one axis should read ≈ 1 g.
5. Place the magnet over `U6` (🟡 M6 — diametric NdFeB, ~6 × 2.5 mm, 0.5–3 mm
   air gap, centred within ~0.25 mm) and read the AS5600 angle. Rotate the
   magnet; the angle should track.
6. Probe `TP18`/`TP19` with a logic analyser if anything is missing.

> 🔴 **If a device is missing, check its orientation first.** The LSM6DSOX is
> the usual suspect — it is a leadless LGA and 180° out looks identical.

---

## Stage 4 — Mechanical sensing

**Populate:** `U8`, `C25`–`C28`, `J8`–`J15`, `R33`–`R42`, `C29`–`C36`,
`D5`, `D6`, `R37`, `R38`, `C33`, `C34`, `R39`–`R41`, `C35`.

**Do:**

1. 🟠 **H3 — identify the load cell wires by measurement**, not colour. Highest
   resistance pair = E+/E−; the remaining high pair = A+/A−. Wire to `J8`:
   E+ = 1, E− = 2, A+ = 3, A− = 4.
2. Read the HX711 (`HX_DOUT` = `IO21`, `HX_SCK` = `IO38`, channel A,
   gain 128). Verify the reading **changes when you press the load cell.**
3. Read each FSR channel on `IO4`–`IO7`. Pressing an FSR should move its ADC
   value substantially.
4. Read the stretch channel on `IO8`. 🟠 **H2 — if the range is poor, this is
   where you compute the right `R37`.** Record the ADC value at minimum and
   maximum extension and set `R37` = √(R_min × R_max).
5. Read the piezo channel on `IO2`. It should idle near mid-rail (~1.65 V from
   `R39`/`R40`) and spike when you tap the film.
6. Test `J15` (hall/limit): `IO41` should read HIGH idle (`R42` pull-up) and
   LOW when the switch closes.

---

## Stage 5 — Alerts

$$\large\textcolor{red}{\textsf{🔴 Confirm the FETs are OFF at boot before connecting the motor.}}$$

**Populate:** `Q1`, `Q2`, `R43`, `R44`, `R46`, `R47`, `D7`, `D8`, `C37`,
`C38`, `R45`, `J16`, `J17`.

**Do:**

1. 🔴 **With nothing connected to `J16` or `J17`, power up and measure `TP15`
   (`MOTOR_EN`) and `TP16` (`BUZZER_EN`). Both must read 0 V.** That is what
   `R44`/`R47` are for. If either floats high, do not connect a motor.
2. 🔴 **B3 — confirm your `R45` decision** before connecting a motor. See
   [Part 1](#part-1--the-blockers-read-this-before-anything-else).
3. Connect the motor to `J16`. Pulse `IO47` high for **50 ms**, then low. It
   should buzz briefly.
4. Measure the motor voltage while running. Confirm it is at or below the
   motor's rating.
5. Connect the buzzer to `J17`. 🟡 **M3:**
   - **active magnetic** → drive `IO48` on/off
   - **passive piezo** → drive `IO48` with LEDC PWM at 2–4 kHz
6. Confirm both go **off** after a reset.

---

## Stage 6 — ECG, last

> 🔴 **B2 applies from here on. Battery power, USB physically unplugged
> whenever electrodes are attached. Informed participants only. Not a medical
> device.**

**Populate:** `U7` and its 25 passives — `R18`–`R32`, `C16`–`C24`, plus `J7`.

**Do:**

1. Power up **from battery, USB unplugged**.
2. 🔵 **Measure `TP11` (`ECG_REFOUT`). It must read ≈ 1.65 V.** If it does not,
   stop — the reference network is wrong and nothing downstream will work.
3. 🔵 **Wait 2.5 s** for the `REFIN` network to settle.
4. Put a scope on `TP10` (`ECG_OUT`). With nothing connected it should idle
   near 1.65 V, possibly drifting — the inputs are floating through 10 MΩ.
5. **Short LA and RA together at `J7`.** The output should settle and go quiet.
   That trace is your noise floor — record it.
6. Confirm the leads-off detection: `IO35` (`LOD+`) and `IO36` (`LOD−`) should
   indicate a fault with nothing attached, and clear when the electrodes are
   on.
7. **Only then attach electrodes.** LA = `J7.1`, RA = `J7.2`, RL = `J7.3`.
8. A clean lead-I trace should appear within a few seconds. R-wave amplitude
   0.5–1 V of swing about 1.65 V.
9. **If 50/60 Hz hum dominates: check the RL electrode is actually attached.**
   The RLD circuit is what rejects mains hum, and it needs that third
   electrode.
10. Test `ECG_SDN` (`IO37`): driving it low should shut the AFE down and drop
    `TP10` to the rail.

---

## The final integration test

Once all six stages pass:

| Test | Expect |
|---|---|
| All sensors sampling + BLE connected | ≈ **155 mA** steady state |
| Battery life on a 2000 mAh cell | ≈ **13 hours** before duty cycling |
| Deep sleep current | ≈ **74 µA** (the AP2112K's own 55 µA dominates) |
| 🔵 **Low-battery cut-off** | firmware shuts down cleanly at **1.75 V on `IO9`** |
| SOS button | `IO40` reads LOW when pressed |
| Radio range | 🟠 **check the battery is ≥ 10 mm from the antenna region** |

> ❌ **All of those figures are calculations, not measurements.** Measure them
> and write the real numbers down — you will be the first person in this
> project to have any.

---

# PART 23 — Workflow H: firmware

Not a firmware project, but the hardware imposes a contract. Here it is.

## 23.1 — The three non-negotiable jobs

### 1. Low-battery cut-off at 3.5 V

```c
// VBAT_SENSE on IO9 = ADC1_CH8. Divider is 470k/470k, so Vpin = VBAT/2.
// 3.5 V cell  ->  1.75 V at the pin.
#define VBAT_CUTOFF_MV   1750    // millivolts AT THE PIN

int vbat_mv = adc1_read_calibrated_mv(ADC1_CHANNEL_8);
if (vbat_mv < VBAT_CUTOFF_MV) {
    notify_low_battery();        // tell the app while you still can
    stop_all_sampling();
    esp_deep_sleep_start();      // clean shutdown, not a brown-out
}
```

**Why:** the AP2112K's 250 mV dropout means the 3V3 rail sags below the
ESP32-S3's 3.0 V minimum near the bottom of the discharge curve. Without this
the board browns out unpredictably — **bad in a device with an SOS button.**
See [§10.4](#104--the-dropout-problem--the-most-important-section-in-this-part).

### 2. Wait 2.5 s before trusting the ECG

```c
// R23/R24 (10M||10M = 5M) with C16 (100n) gives tau = 0.5 s.
// 5 tau = 2.5 s for REFIN to settle.
vTaskDelay(pdMS_TO_TICKS(2500));
```

### 3. Use ADC1 only

```c
// ADC2 shares hardware with the radio and FAILS while Wi-Fi/BLE is active.
// All 8 analog signals are on ADC1 (GPIO1-GPIO10) for exactly this reason.
```

## 23.2 — Pin definitions, ready to paste

```c
// ---- Analog, ADC1 only ----------------------------------------------
#define PIN_ECG_OUT       1    // ADC1_CH0
#define PIN_PIEZO_ADC     2    // ADC1_CH1
#define PIN_IO3_SPARE     3    // ADC1_CH2  - STRAPPING, R17 is DNP
#define PIN_FSR1          4    // ADC1_CH3
#define PIN_FSR2          5    // ADC1_CH4
#define PIN_FSR3          6    // ADC1_CH5
#define PIN_FSR4          7    // ADC1_CH6
#define PIN_STRETCH       8    // ADC1_CH7
#define PIN_VBAT_SENSE    9    // ADC1_CH8

// ---- microSD, SPI (FSPI) --------------------------------------------
#define PIN_SD_CS        10
#define PIN_SD_MOSI      11
#define PIN_SD_SCK       12
#define PIN_SD_MISO      13

// ---- I2C: TWO SEPARATE BUSSES (0x36 clash) --------------------------
#define PIN_ANG_SDA      14    // I2C1 - AS5600 0x36
#define PIN_ANG_SCL      42    // I2C1
#define PIN_I2C_SDA      15    // I2C0 - TMP117 0x48, LSM6DSOX 0x6A, gauge 0x36
#define PIN_I2C_SCL      16    // I2C0

// ---- IMU interrupts -------------------------------------------------
#define PIN_IMU_INT1     17
#define PIN_IMU_INT2     18

// ---- USB-Serial-JTAG (do not use as GPIO) ---------------------------
// IO19 = USB_DM, IO20 = USB_DP

// ---- HX711 ----------------------------------------------------------
#define PIN_HX_DOUT      21
#define PIN_HX_SCK       38    // also PD_SCK: hold HIGH to power down

// ---- ECG control (free on -N8R2 ONLY) -------------------------------
#define PIN_ECG_LOD_P    35
#define PIN_ECG_LOD_N    36
#define PIN_ECG_SDN      37    // HIGH = enabled (R31 pull-up)
#define PIN_ECG_FR       39    // LOW  = fast restore off (R32 pull-down)

// ---- User I/O -------------------------------------------------------
#define PIN_SOS          40    // ACTIVE LOW (R48 pull-up)
#define PIN_HALL_LIMIT   41    // ACTIVE LOW (R42 pull-up)
#define PIN_LED_STATUS   45    // STRAPPING - drive only, never read
#define PIN_LED_ALERT    46    // STRAPPING - drive only, never read
#define PIN_MOTOR_EN     47
#define PIN_BUZZER_EN    48
```

## 23.3 — I²C initialisation: two busses

```c
// Bus 0 - SENSOR: TMP117 (0x48), LSM6DSOX (0x6A), fuel gauge breakout (0x36)
i2c_config_t sensor_bus = {
    .mode = I2C_MODE_MASTER,
    .sda_io_num = PIN_I2C_SDA,   .scl_io_num = PIN_I2C_SCL,
    .sda_pullup_en = false,      .scl_pullup_en = false,  // R11/R12 = 4k7 on board
    .master.clk_speed = 400000,
};

// Bus 1 - ANGLE: AS5600 (0x36)
i2c_config_t angle_bus = {
    .mode = I2C_MODE_MASTER,
    .sda_io_num = PIN_ANG_SDA,   .scl_io_num = PIN_ANG_SCL,
    .sda_pullup_en = false,      .scl_pullup_en = false,  // R15/R16 = 4k7 on board
    .master.clk_speed = 400000,
};
```

> 🔵 **Disable the internal pull-ups.** The board has 4k7 externals sized for
> 400 kHz at ~60 pF (239 ns rise time). Enabling the ESP32's weak internals as
> well changes the bus impedance for no benefit.
>
> 🔵 **Do not merge these busses in software.** The AS5600 and the fuel-gauge
> breakout are both at 0x36. Two controllers is the whole point.

## 23.4 — Safe startup sequence

```c
void app_main(void) {
    // 1. FIRST: force the two load drivers off, explicitly.
    //    R44/R47 already pull them down in hardware; this is belt and braces.
    gpio_set_direction(PIN_MOTOR_EN,  GPIO_MODE_OUTPUT);
    gpio_set_direction(PIN_BUZZER_EN, GPIO_MODE_OUTPUT);
    gpio_set_level(PIN_MOTOR_EN,  0);
    gpio_set_level(PIN_BUZZER_EN, 0);

    // 2. Check the battery BEFORE bringing anything else up.
    if (read_vbat_mv() < VBAT_CUTOFF_MV) { enter_low_battery_sleep(); }

    // 3. ECG front end: enabled, fast restore off.
    gpio_set_direction(PIN_ECG_SDN, GPIO_MODE_OUTPUT);
    gpio_set_direction(PIN_ECG_FR,  GPIO_MODE_OUTPUT);
    gpio_set_level(PIN_ECG_SDN, 1);   // 1 = enabled
    gpio_set_level(PIN_ECG_FR,  0);   // 0 = fast restore off

    // 4. Busses and sensors.
    init_i2c_busses();
    init_sensors();

    // 5. THEN wait for the ECG reference to settle.
    vTaskDelay(pdMS_TO_TICKS(2500));

    start_sampling();
}
```

## 23.5 — Reading the ECG

```c
// Sample at >= 250 Hz. Pass band is ~7-40 Hz, so 250 Hz gives >6x
// oversampling and clean beat timing.
#define ECG_SAMPLE_HZ   250

void ecg_task(void *arg) {
    // The signal is referenced to REFOUT (~1.65 V), NOT to ground.
    int baseline_mv = 1650;   // refine by measuring TP11 on your board

    while (1) {
        // Leads-off FIRST. Reporting garbage is worse than reporting nothing.
        bool lod_p = gpio_get_level(PIN_ECG_LOD_P);
        bool lod_n = gpio_get_level(PIN_ECG_LOD_N);
        if (lod_p || lod_n) {
            report_leads_off(lod_p, lod_n);   // tells you WHICH electrode
            vTaskDelay(pdMS_TO_TICKS(100));
            continue;
        }

        int mv = adc1_read_calibrated_mv(ADC1_CHANNEL_0);
        int ecg = mv - baseline_mv;           // signed, about the reference
        push_sample(ecg);

        vTaskDelay(pdMS_TO_TICKS(1000 / ECG_SAMPLE_HZ));
    }
}
```

> 🔵 **After a fast-restore pulse or a leads-off event, discard ~1 second** —
> the high-pass filter has to re-settle.

## 23.6 — The vibration motor, done properly

🔴 **B3** gives you two options. The better one is firmware:

```c
// Instead of a resistive ballast, PWM the motor and scale the duty cycle
// against the measured battery voltage. Constant average voltage across
// the whole discharge curve, and no ballast to burn out on stall.
#define MOTOR_RATED_MV  3000

void motor_run(int ms) {
    int vbat_mv = read_vbat_mv() * 2;                  // undo the /2 divider
    int duty    = (MOTOR_RATED_MV * 255) / vbat_mv;    // 0-255
    if (duty > 255) duty = 255;

    ledc_set_duty(MOTOR_CHANNEL, duty);
    ledc_update_duty(MOTOR_CHANNEL);
    vTaskDelay(pdMS_TO_TICKS(ms));
    ledc_set_duty(MOTOR_CHANNEL, 0);
    ledc_update_duty(MOTOR_CHANNEL);
}
```

**With this, leave `R45` at 0 Ω.** You get full torque at low battery, correct
voltage at full charge, and nothing to overheat when the motor stalls.

## 23.7 — The SOS button

```c
// ACTIVE LOW - R48 pulls up. Hardware gives ~1 ms of RC debounce
// (R49 1k + C39 100n) plus ESD protection; still debounce in software.
gpio_set_direction(PIN_SOS, GPIO_MODE_INPUT);
gpio_set_pull_mode(PIN_SOS, GPIO_FLOATING);   // R48 already pulls it up

bool sos_pressed(void) {
    if (gpio_get_level(PIN_SOS) != 0) return false;
    vTaskDelay(pdMS_TO_TICKS(30));
    return gpio_get_level(PIN_SOS) == 0;
}
```

> 🔵 **Require a deliberate long press** — 1 to 2 seconds — before firing an
> SOS. A belt-mounted button will get pressed accidentally, and a false
> emergency alert has a real cost.

## 23.8 — Deep sleep: what to shut down

```c
void enter_deep_sleep(void) {
    gpio_set_level(PIN_MOTOR_EN,  0);
    gpio_set_level(PIN_BUZZER_EN, 0);
    gpio_set_level(PIN_ECG_SDN,   0);   // AD8232 -> < 0.2 uA
    gpio_set_level(PIN_HX_SCK,    1);   // HX711 PD_SCK high -> ~0.2 uA
    tmp117_shutdown();                  // -> 0.25 uA
    lsm6dsox_power_down();              // -> 3 uA
    as5600_low_power_mode(3);           // -> ~1.5 uA
    esp_deep_sleep_start();             // -> ~7 uA
}
// Total ~74 uA. The AP2112K's own 55 uA quiescent dominates and cannot be
// switched off - see POWER_BUDGET.md.
```

## 23.9 — Sensor-specific notes

| Sensor | Note |
|---|---|
| **TMP117** | 0x48. WHO_AM_I / device ID readable. 🟡 **M7 — it measures pod temperature.** Alerts are readable by polling the config register (`TMP_ALERT` is not on a GPIO). |
| **LSM6DSOX** | 0x6A. WHO_AM_I = **0x6C**. Both interrupts wired (`IO17`, `IO18`) — use them rather than polling. |
| **AS5600** | 0x36 **on the angle bus only**. 🟡 M6 — needs a diametric magnet. Analog `OUT` is unused (`TP8`). |
| **HX711** | Channel A, **gain 128** (±20 mV FS, ratiometric to AVDD). 🟠 **H3 — drop to gain 64 if the cell is > 6 mV/V.** `PD_SCK` high = power down. |
| **FSRs** | `IO4`–`IO7`. 10 kΩ dividers, anti-aliased at 1.6 kHz. Non-linear — calibrate empirically, do not expect a formula. |
| **Stretch** | `IO8`. 🟠 **H2 — `R37` is a placeholder.** |
| **Piezo** | `IO2`. Idles at mid-rail. AC-coupled with a ~10 Hz corner (🟡 M4). Look for *transients*, not absolute level. |
| **Fuel gauge** | 0x36 **on the sensor bus** if you fit a breakout at `J4` (🟠 H1). The `R5`/`R6` divider on `IO9` works regardless and is what the cut-off uses. |

---

# PART 24 — Troubleshooting encyclopedia

Organised by symptom. Every entry says what to measure, not just what to
suspect.

---

## 24.1 — Software and build problems

### `ModuleNotFoundError: No module named 'numpy'`

The virtual environment is not active, or you installed into a different Python
than the one running the script.

```bash
python -c "import sys; print(sys.executable)"
```

Compare that to where you ran `pip install`. Then:

```bash
python -m pip install numpy matplotlib Pillow
```

Using `python -m pip` rather than bare `pip` guarantees they match.

### `python: command not found`

Try `python3`. On Windows, Python was installed without "Add to PATH" —
reinstall with that box ticked, or use the full path.

### `validate_drc.py` says `RESULT: FAIL`

🔵 **That is expected and correct.** The four errors are the four
deliberately-unrouted nets. There are **zero** geometry violations. See
[§15.3](#153--drc-8-rule-groups--0-geometry-violations).

### `build_all.py` says `steps with findings to review: DRC`

Same thing. DRC is marked non-fatal for exactly this reason.

### `validate_erc.py` fails after I edited `design.py`

Read the rule number in the message:

| Rule | Meaning | Usual cause |
|---|---|---|
| **R1** | duplicate ref, or unknown deviceset | typo in a `deviceset` name |
| **R2** | a pin name does not exist | wrong pin name in an `N()` call |
| **R3** | a pin is on zero or two nets | 🔵 **you added a part and forgot one of its pins** |
| **R4** | net has < 2 connections | a typo created a net with one pin |
| **R5** | power pin with no supply symbol | missing `SUPPLYn` on that sheet |
| **R6** | two push-pull outputs on a net | genuine conflict |
| **R7** | inputs with no driver | genuine problem |
| **R8** | I²C pull-up count, or an address clash | you put a device on the wrong bus |
| **R9** | GPIO not in `GPIO_TABLE`, or analog on ADC2 | 🔵 **update `GPIO_TABLE` too** |
| **R10** | missing gate pull-down, or bad diode orientation | check which pin is anode |
| **R11** | LED with no series resistor | |

### The router completes fewer nets after my change

Expected if you added parts, made a part bigger, widened clearances, or shrank
the board. The router is greedy and congestion-limited.

**Options:** increase `ATTEMPTS`, adjust `SHEET_OFFSET` to give the congested
zone more room, or just accept more airwires and finish them by hand.

### The `.brd` changes every run even with no model edit

🔵 **Normal.** The router explores 14 orderings and ties break differently.
The `.lbr`, `.sch`, ERC report, GPIO table, netlist and BOM should be
byte-identical. **If the `.sch` changes when you did not touch the model, that
is a bug worth chasing.**

---

## 24.2 — Fusion problems

### "Device not found" when opening the schematic

The library is not marked **In Use**. But note the `.sch` carries a full
embedded copy, so this should not happen — if it does, re-clone the file.

### EAGLE 7.x will not open the files

🟠 Correct — these are **EAGLE 9 XML**. Use Fusion or EAGLE 9.x.

### Fusion's DRC reports dozens of clearance errors

🟠 **You have Fusion's default rule set loaded, not the board's own.**

The `.brd` contains a rule set named **`SIH26113_4layer`** with
`mdWireWire = 0.127 mm`. Fusion's default is usually 6 mil (0.152 mm), which
flags every fine-pitch fan-out.

Load the board's rules first. **If your fab is 6 mil-only, those errors are
real for you** — see the 🟠 H6 fallback.

### The copper pours look wrong or missing

Type **`RATSNEST`**. 🔵 **Fusion computes polygon fill on demand, not
automatically.** Until you do, the pours are just declared outlines.

### A plane looks pinched into two regions

A dense via cluster has necked it. Find the thin neck and move a via. 🔵 **If
it is under the ECG block, fix it** — layer 2 being unbroken there is the
board's most important electrical property.

### There are airwires I did not expect

Read `DRC_REPORT.md` — it lists them by name with the measured gap that caused
each concession. If there are more than four, the board was re-routed after a
model change; the list in the report is authoritative, not the list in any
document.

---

## 24.3 — Hardware: power stage

### 🔴 `TP2` (3V3) reads 0 V

In order:

1. **Is `J3` shorted?** ⚪ **L2 — closing `J3` turns the board OFF.** This
   catches everyone once.
2. Measure `TP1` (`VBAT`). No `VBAT` → the cell is not connected, the pigtail
   is reversed (🔴 B1), or the pack's protection has tripped.
3. Measure the LDO's `EN` pin. `R4` should hold it near `VBAT`. If `EN` is low,
   `R4` is missing or `J3` is closed.
4. Measure the LDO input. Present at the input but not the output → `U2` is
   dead or **misoriented**.
5. 🔴 **Measure resistance from `TP2` to `TP3`.** A near-short means a shorted
   decoupling cap or a solder bridge — and it means `U2` has been in current
   limit, so replace it too.

### 🔴 `TP2` reads 3.3 V but drops under load

The LDO is in dropout, or a downstream short is pulling it.

- Measure `TP1`. If `VBAT` < 3.55 V, this is **the documented dropout
  behaviour** — see [§10.4](#104--the-dropout-problem--the-most-important-section-in-this-part).
  **This is what the 3.5 V cut-off exists to prevent.**
- If `VBAT` is high and 3V3 still sags, something downstream is drawing too
  much. Disconnect stages until it recovers.

### `TP2` reads 3.3 V but the board still browns out

🔵 **You have not implemented the low-battery cut-off.** See
[§23.1](#231--the-three-non-negotiable-jobs).

### The charger does not charge

| Check | Expect |
|---|---|
| `TP4` (`VBUS`) | 5 V |
| `D1` (red) | lit while charging |
| `R1` | 2k4 — sets 500 mA |
| `U1` temperature | 🔵 warm is normal — 1.0 W worst case in an SOP-8 |

**If it charges slowly:** that is by design (500 mA, ~4.5 h for 2000 mAh), and
thermal regulation may be folding it back further. See
[§8.1](#81--sheet-1-power-entry-charging-and-3v3-regulation).

### The charge LED cycles between charging and complete

🟡 **The documented power-path limitation.** The system load flows through
`BAT` during charging and disturbs the C/10 termination detection. Not
dangerous with a protected pack; the fix is a power-path charger.
`DESIGN_ASSUMPTIONS.md` §1.3.

### 🔴 Something got hot / smelled

Disconnect immediately. Then, before re-powering:

1. Meter `TP1`–`TP3` and `TP2`–`TP3` for shorts.
2. Check every polarised part's orientation.
3. 🔴 **Check `D7` and `D8` orientation.** A reversed flyback diode is a
   **permanent short across the supply**. Anode on the switched drain, cathode
   on the supply.
4. 🔴 **Check `D5`/`D6`.** `D5` cathode → `3V3`, `D6` anode → `GND`. Reversed,
   they short the rail.
5. 🔴 **Check `R45`.** If a ballast is fitted and the motor stalled, `R45` has
   been over-dissipating — a 12 Ω at 400 mA stall is **1.9 W** in a 125 mW
   part (B3).

---

## 24.4 — Hardware: the module

### No serial device appears over USB

1. Confirm `TP2` = 3.3 V.
2. 🔵 **No driver is needed** — this is the native USB-Serial-JTAG. If you
   installed a CH340/CP2102 driver expecting to need it, that is not the
   problem.
3. Try a different cable. A charge-only cable has no data lines.
4. Hold `SW3` (BOOT), press and release `SW2` (RESET), release BOOT. That
   forces download mode.
5. Check the `EN` network: `R7` = 10k pull-up, `C10` = 1 µF. 🔵 **`EN` must not
   float.**
6. 🟡 **Fall back to `J5`** (UART) with a USB-serial adapter: `J5.1` = GND,
   `J5.3` = TX, `J5.4` = RX, `J5.5` = `EN`, `J5.6` = `IO0`. **That is what the
   header is for (M2).**

### It boots into download mode every time

`IO0` is being held low. Check `SW3` is not stuck, and `R8` = 10k is fitted.

### It reports 8 MB PSRAM instead of 2 MB

$$\large\textcolor{orange}{\textsf{🟠 You have an -N8R8 module. H5. Replace it.}}$$

`IO35`/`IO36`/`IO37` are wired to the PSRAM on octal parts. The ECG channel
cannot work.

### The LEDs do not blink

`D3` on `IO45`, `D4` on `IO46`, both through 1 kΩ. 🔵 **Both are strapping
pins** — the LEDs are wired anode-to-GPIO so the pin is high-Z at reset and the
LED cannot conduct. If you rewired them cathode-to-GPIO, you have changed the
boot straps.

### It resets randomly

- Brown-out — measure `TP1`. See the cut-off requirement.
- `C8` (22 µF) missing or not close to module pin 2. It supplies the **355 mA
  Wi-Fi TX burst**; without it the rail collapses on every transmit.
- `EN` floating.

---

## 24.5 — Hardware: I²C

### 🔴 Nothing responds on either bus

1. `TP2` = 3.3 V?
2. Probe `TP18`/`TP19` with a scope. **Both should idle HIGH at 3.3 V.** If
   they sit low, a device is holding the bus or there is a short.
3. Check the pull-ups: `R11`/`R12` (sensor bus), `R15`/`R16` (angle bus), all
   4k7.
4. 🔵 **Confirm your firmware disabled the internal pull-ups.**

### One device is missing

$$\large\textcolor{red}{\textsf{🔴 Check orientation FIRST. The LSM6DSOX is the usual suspect.}}$$

It is a **leadless LGA** — 180° out looks identical. Find the pin-1 dot under a
microscope and compare it to the silkscreen dot.

| Device | Address | Bus | If missing |
|---|---|---|---|
| TMP117 | 0x48 | SENSOR | check `U4` orientation, `C11`, and that `ADD0` is grounded |
| LSM6DSOX | 0x6A | SENSOR | 🔴 **orientation.** Then `C12`/`C13`. WHO_AM_I should be 0x6C |
| AS5600 | 0x36 | **ANGLE** | 🔵 **you are probably scanning the wrong bus.** Then check `C14`/`C15` |

### The AS5600 responds but the angle is nonsense

🟡 **M6 — the magnet.** It needs a **diametrically-magnetised** magnet (not
axial), ~6 × 2.5 mm NdFeB, 0.5–3 mm air gap, centred over the IC within
**~0.25 mm**. Read its magnet-status register — it will tell you whether the
field is too weak, too strong, or absent.

### The TMP117 reads too high

🟡 **M7 — it is measuring pod temperature**, not ambient and definitely not
skin. The LDO, charger and ESP32 are all on the same board. This is the
expected behaviour, and it is the reason M7 exists.

---

## 24.6 — Hardware: mechanical sensing

### The HX711 reads a constant value

1. Measure the bridge excitation at `J8` pins 1 and 2 — should be ~3.3 V.
2. 🟠 **H3 — verify E and A are not swapped.** Highest-resistance pair =
   E+/E−; the other high pair = A+/A−. **Do not trust wire colours.**
3. Check `C25`–`C28`.
4. Confirm `PD_SCK` (`IO38`) is being driven **low** — held high powers the
   part down.
5. Confirm the clock-pulse count selects channel A gain 128.

### HX711 readings saturate

🟠 **H3 — the cell is too sensitive for gain 128** (±20 mV FS). Above ~6 mV/V,
**drop to gain 64.** That is a firmware change.

### An FSR channel does not respond

Check the divider resistor (10k) and that the FSR is actually connected. FSRs
are **very** non-linear — a light touch may move the ADC by only a few counts.
Press hard to confirm the channel works at all, then calibrate.

### The stretch channel has almost no range

🟠 **H2 — `R37` = 10 kΩ is a placeholder.** Measure the sensor's resistance at
minimum and maximum extension and set `R37` = √(R_min × R_max). One 0805.

### The piezo channel is dead

1. It idles at **mid-rail (~1.65 V)** from `R39`/`R40`, not at 0 V. Measure it.
2. It is **AC-coupled** through `C34` — you will only see *transients*. Tap the
   film sharply.
3. 🟡 M4 — if low-frequency movement is attenuated, `R38` (10 MΩ) is too high
   for your film's capacitance. Reduce it.
4. 🔴 **Check `D5`/`D6` orientation.** Reversed, they clamp the signal to
   nothing — and short the rail.

---

## 24.7 — Hardware: alerts

### 🔴 The motor or buzzer runs at boot

$$\large\textcolor{red}{\textsf{🔴 Power down now. The gate pull-down is missing or open.}}$$

Check `R44` (motor, 100k) and `R47` (buzzer, 100k). Those resistors are the
**only** thing holding the FETs off between power-on and firmware. A
partially-on MOSFET dissipates enormously.

Measure `TP15` and `TP16` at boot — **both must be 0 V.**

### The motor is weak

- 🔴 **B3 — is `R45` fitted?** A 12 Ω ballast at 3.7 V leaves the motor only
  2.5 V.
- Measure `TP1`. A low cell gives a weak motor.
- **Better answer:** PWM with duty scaled against `VBAT_SENSE` and leave `R45`
  at 0 Ω. See [§23.6](#236--the-vibration-motor-done-properly).

### The motor destroyed itself

🔴 **B3.** A 3.0 V motor on a full 4.2 V cell with `R45` = 0 Ω.

### The buzzer is silent

🟡 **M3 — which type is it?**

- **Active magnetic** → simple on/off on `IO48`. If silent, check `D8`
  orientation and that the part is actually active.
- **Passive piezo** → it needs **PWM at its resonance** (typically 2–4 kHz). A
  DC level does nothing at all.

---

## 24.8 — Hardware: ECG

> 🔴 **B2 applies to every step here. Battery power, USB unplugged.**

### 🔴 `TP11` (`ECG_REFOUT`) is not ≈ 1.65 V

**Stop. Nothing downstream will work.**

1. Check `R23`/`R24` (10 M / 10 M) and `C16` (100 nF).
2. **Wait 2.5 s** — the network settles slowly on purpose (τ = 0.5 s).
3. Confirm `U7` has 3.3 V at pin 17 and `C23`/`C24` are fitted.
4. 🔴 **Confirm `U7` is on `3V3` and NOT on `VBAT`.** The AD8232's absolute
   maximum is **3.5 V**, and `VBAT` reaches 4.2 V while charging. If it was
   ever powered from `VBAT`, the part is probably dead.
5. Check `U7` orientation.

### `TP10` (`ECG_OUT`) sits at a rail

The stage is saturated.

- With no electrodes, the inputs float through 10 MΩ and drift — **that is
  expected.** Short LA and RA at `J7` and it should settle.
- Pulse `ECG_FR` (`IO39`) high briefly to fast-restore, then low. **Discard
  ~1 s afterwards.**
- Confirm `R31` (100k) pulls `SDN` high — the AFE must be **enabled**.

### 🔴 50/60 Hz hum dominates

**Check the RL electrode is actually attached to `J7.3`.**

The RLD circuit is what rejects mains hum, and it needs that third electrode.
This is the single most common ECG complaint and this is almost always the
answer.

Then:

- 🔴 **Is USB plugged in? Unplug it (B2).** Mains-referenced USB is both a
  safety issue *and* a hum source.
- Are the electrodes well adhered? Dry or old gel raises contact impedance
  enormously.
- Check `R20` (330k) on the RLD path.

### The trace is noisy and jumps with movement

Partly expected — **the pass band is deliberately 7–40 Hz for motion-artefact
resistance**, and it still cannot fix a loose electrode.

- Check electrode adhesion.
- Confirm layer 2 is unbroken under zone Z3 (build guide step 14).
- 🔵 **Clean flux residue around the 10 MΩ nodes.** Flux is conductive enough
  to matter at 10 MΩ.

### The waveform is not diagnostic quality

$$\large\textsf{Correct, and by design.}$$

The pass band is ~7–40 Hz. **You get reliable beat detection and heart-rate
variability. You do not get interpretable ST segments, P-wave detail or T-wave
shape.** See [§11.7](#117--if-you-want-to-move-toward-waveform-monitoring) for
the retune path — it is four passive values.

**Nothing in this project should claim diagnostic capability.**

### Leads-off never triggers, or triggers always

`LOD+` = `IO35`, `LOD−` = `IO36`. 🟠 **If both read stuck, check you have an
`-N8R2` module (H5)** — on octal-PSRAM parts these pins are wired to the PSRAM.

Then check `R21`/`R22` (10 M each) are fitted; they are what makes a
disconnected electrode drift to a rail.

---

## 24.9 — Radio problems

### 🟠 Bluetooth/Wi-Fi range is terrible

In order of likelihood:

1. 🟠 **Is the battery lying against the antenna?** Keep the pack and **any
   metal ≥ 10 mm** from the top edge, x 9–29 mm. A Li-Po against the antenna
   costs most of the range. **This is the most common cause and it happens when
   you box it up.**
2. Is there copper in the keep-out? DRC rule D3 says no, but confirm in
   Fusion — and confirm the **planes** are cut around it, not just the signal
   layers.
3. Is the enclosure metal or metallised? Same problem, bigger.
4. Is the antenna end of the module overhanging the board edge as intended?

### The board resets when Wi-Fi transmits

`C8` (22 µF) missing, wrong value, or too far from module pin 2. The 355 mA
burst needs local bulk.

Also check `TP1` — a nearly-flat cell cannot supply the burst through a
dropped-out LDO.

---

## 24.10 — The diagnostic decision tree

```
Board does nothing
├─ TP2 (3V3) = 0 V?
│   ├─ Is J3 closed?  →  L2: CLOSED = OFF. Open it.
│   ├─ TP1 (VBAT) = 0 V?
│   │   ├─ Pigtail reversed?  →  B1. Meter it.
│   │   └─ Pack protection tripped?  →  charge it via J2
│   └─ TP2-TP3 shorted?  →  find the bridge, then replace U2
└─ TP2 = 3.3 V?
    ├─ No serial device?
    │   ├─ Try BOOT+RESET
    │   └─ Fall back to J5 UART  (M2)
    ├─ Reports 8 MB PSRAM?  →  H5. Wrong module. Replace.
    ├─ Motor/buzzer on at boot?  →  R44/R47 missing. POWER DOWN.
    ├─ I2C device missing?
    │   ├─ Right bus?  (AS5600 is on the ANGLE bus)
    │   └─ Orientation?  (LSM6DSOX first)
    └─ ECG dead?
        ├─ TP11 != 1.65 V?  →  reference network, or U7 was on VBAT
        ├─ Waited 2.5 s?
        └─ Hum?  →  RL electrode attached? USB unplugged?
```

---

# PART 25 — The seven architecture changes

The input to this project was one architecture image. It was treated as a
**starting point, not as truth**. Every deviation is marked
**[ARCHITECTURE CHANGE]** in `DESIGN_ASSUMPTIONS.md`. There are **seven**.

> The brief was explicit: *"You have permission to improve the architecture
> where technically necessary, but do not make major changes silently. Document
> every meaningful architectural change and explain why it was necessary."*
> This part is that accounting.

---

## Change 1 — 🔴 "TP4056 protected module" became a bare TP4056 IC

**Section:** `DESIGN_ASSUMPTIONS.md` §1.1

**The diagram said:** "JST → TP4056 **protected** module"

**What was built:** the TP4056 as a bare SOIC-8 IC (`U1`).

**Why:** a board-level charger is the right thing for a real product, and
dropping a purchased module onto a carrier board is not a PCB design.

**🔴 The consequence, which is why this is BLOCKING:** a commercial TP4056
*module* carries **DW01A + FS8205A protection** alongside the charger. A bare
IC does not. **There is therefore no battery protection circuit on this
board.**

Bare DW01A/FS8205A were **not** added because their pinouts could not be
verified from primary documentation, and guessing on a lithium protection
circuit is not an acceptable risk.

**→ A protected cell/pack at `J1` is mandatory. See 🔴 B1.**

---

## Change 2 — 🟠 The MAX17048 fuel gauge is off-board

**Section:** `DESIGN_ASSUMPTIONS.md` §1.6

**The diagram said:** MAX17048 on the shared I²C bus.

**What was built:** `J4`, a 5-way header for an off-the-shelf breakout, plus
`R5`/`R6`/`C6` — a 470 k/470 k divider giving battery voltage on `IO9`
regardless.

**Why:** analog.com and every distributor mirror tried was unreachable or
bot-blocked, so **neither the pinout nor the land pattern could be verified.**
Drawing an unverified footprint and shipping it in a library is how you get a
board that cannot be assembled.

Both MAX17048 packages are also awkward for a hackathon build — the 8-bump
0.9 × 1.7 mm WLP is not hand-assemblable at all.

**The divider is arguably the better outcome:** it always works, needs no
driver, and is what the mandatory 3.5 V cut-off reads. **See 🟠 H1.**

---

## Change 3 — 🔴 One shared I²C bus became two

**Section:** `DESIGN_ASSUMPTIONS.md` §5

**The diagram said:** TMP117, LSM6DSOX, AS5600 and MAX17048 on one bus.

**Why that cannot work:** **the AS5600 and the MAX17048 are both hard-wired to
address `0x36`, and neither has an address-select pin.** Two devices at the same
address on the same bus is not a performance problem; it is a bus that does not
function.

**What was built:**

| Bus | Controller | SDA | SCL | Devices |
|---|---|---|---|---|
| SENSOR | I2C0 | `IO15` | `IO16` | TMP117 0x48, LSM6DSOX 0x6A, gauge header 0x36 |
| ANGLE | I2C1 | `IO14` | `IO42` | AS5600 0x36, plus `J6` |

Costs two extra GPIOs and two extra pull-up pairs. Uses the ESP32-S3's second
I²C controller, which was otherwise idle.

**And the second AS5600 is handled explicitly rather than hidden:** `J6`
carries the angle bus **plus** a fifth pin to `IO3` through a DNP 0 Ω link
(`R17`), so you can use its analog `OUT`, an external TCA9548A, or a software
bus. The board commits you to none of them.

> **This was a real bug in the input, found by checking addresses against
> datasheets rather than trusting a block diagram.**

---

## Change 4 — 🔵 Two layers became four

**Section:** `DESIGN_ASSUMPTIONS.md` §2

**The diagram implied:** a simple carrier board.

**What was built:** signal / **GND plane** / **3V3 plane** / signal.

**Why — and this is measured, not asserted:**

| Layers | Nets the router completed (of 81 at the time) |
|---|---|
| 2 | **~50**, and the board's reachable copper **split into disconnected regions** |
| 4 | **77** |

Plus the electrical argument: the AD8232 amplifies a sub-millivolt biopotential
by **1100** across **10 MΩ** nodes, and its datasheet asks for a ground plane.
With 81 signal nets and 15 through-hole connectors, two layers leaves **no
continuous reference under the analog section**.

**Cost:** a couple of dollars per prototype board.

---

## Change 5 — ⚪ "Status LED / RGB LED" became two discrete LEDs

**Section:** `DESIGN_ASSUMPTIONS.md` §8.3

**The diagram said:** "Status LED / RGB LED".

**What was built:** two discrete 0805 LEDs — `D3` green on `IO45`, `D4` red on
`IO46`, each with a 1 kΩ series resistor.

**Why:**

1. An RGB LED costs **three** GPIOs, and the pin budget has none spare.
2. A WS2812-style addressable LED needs a precise bit-banged protocol and adds
   a firmware dependency for a status indicator.
3. 🔵 **Two discrete LEDs let both strapping pins be wired anode-side**, so at
   reset the pin is high-Z, the LED cannot conduct, and the internal pull-down
   holds the strap at its default 0. That trick does not work as cleanly with a
   common-anode RGB part.

**What you lose:** fewer distinct status colours. Acceptable for a prototype.

---

## Change 6 — ⚪ microSD socket became a module header

**Section:** `DESIGN_ASSUMPTIONS.md` §11

**What was built:** `J18`, a 6-way header for a standard SPI microSD breakout.

**Why:**

1. It matches the architecture diagram's own "module headers" approach.
2. **It avoids an unverified socket land pattern.** microSD push-pull sockets
   have fiddly, vendor-specific land patterns with mechanical retention
   features, and getting one wrong means a socket that will not fit.

`R50`/`R51` (10k) pull-ups follow the SD specification's own recommendation.

---

## Change 7 — ⚪ USB receptacle became a 4-way header

**Section:** `DESIGN_ASSUMPTIONS.md` §12

**What was built:** `J2`, a 4-way header: `VBUS`, `D−`, `D+`, `GND`.

**Why:** a USB-C receptacle land pattern could not be verified, and a wrong
receptacle footprint is unrecoverable — you cannot rework a 0.5 mm-pitch
24-pin connector onto wrong pads.

**What you lose:** convenience. You need a breakout cable or a pigtail.

**What it also gains you:** 🔴 **B2 becomes much easier to comply with.** A
header you have to deliberately plug in is a more visible thing to *unplug*
than a captive receptacle, and B2's entire mitigation is "USB physically
unplugged whenever electrodes are attached."

> ⚪ **§15 of `DESIGN_ASSUMPTIONS.md` lists a USB-C receptacle with a verified
> land pattern as one of the things to do with more information.**

---

# PART 26 — Known limitations, honestly

## 26.1 — Things that are not done

| Item | Status |
|---|---|
| Autodesk EAGLE / Fusion **ERC** | ❌ NOT EXECUTED — TOOL UNAVAILABLE |
| Autodesk EAGLE / Fusion **DRC** | ❌ NOT EXECUTED — TOOL UNAVAILABLE |
| Copper-pour **connectivity** | ✅ **MEASURED** by `validate_planes.py` — both pours stay one dominant region (≥ 99.9 % of remaining copper), ECG zone Z3 entirely within it, **0 orphaned plane contacts**. This check found a real defect (see `FINAL_REVIEW.md`) |
| Copper-pour **exact geometry as EAGLE fills it** | ❌ still NOT COMPUTED — EAGLE calculates on load. Run `RATSNEST` |
| Gerber / drill files | ❌ NOT GENERATED — needs EAGLE's CAM |
| 3D / mechanical interference | ❌ NOT CHECKED — no STEP models attached |
| USB pair impedance | ✅ **CALCULATED** — see `USB_PAIR_ANALYSIS.md`. Off target (165 Ω vs 90 Ω) but electrically short; no action needed |
| Component availability | ❌ NOT VERIFIED |
| Physical prototype | ❌ NOT BUILT — **no figure in this project is a measurement** |
| 4 of 80 signal nets | 🟨 airwires, deliberately |

## 26.2 — Accepted design compromises

| Compromise | Why it was accepted | The proper fix |
|---|---|---|
| **No power-path switching** — system load disturbs charge termination | the TP4056 is cheap, well-understood and adequate for a prototype; a protected pack backstops it | MCP73871 power-path charger |
| **LDO instead of buck-boost** — loses the bottom ~15 % of cell capacity to dropout | LDO noise performance matters for a 10 µV-resolution analog channel | buck-boost, at a noise cost |
| **ECG pass band 7–40 Hz** — not diagnostic | motion-artefact resistance on a walking subject; datasheet's own configuration | four passive values, at a motion-artefact cost |
| **TMP117 on the main board** — measures pod, not skin | that is where the architecture diagram puts it | flex tail (🟡 M7) |
| **One ground net, no split** | correct for this circuit — see [Part 12](#part-12--grounding-and-the-stack-up) | nothing; the split would be worse |
| **`R45` = 0 Ω placeholder** | motor not selected | PWM in firmware (§23.6) |
| **`R37` = 10 kΩ placeholder** | sensor not selected | 🟠 H2 |
| **Headers instead of receptacles** for USB and microSD | unverified land patterns | verified footprints |
| **⚪ `H3` not at a corner** | that corner is in the antenna keep-out | move the antenna to another edge |
| **⚪ `J3` inverted** — closed = OFF | avoids inventing an unverified slide-switch footprint | verified switch footprint |

## 26.3 — 🟠 A drift bug that was found and fixed — worth knowing about

`POWER_BUDGET.md`, `PCB_BUILD_GUIDE.md`, `REQUIRES_CONFIRMATION.md` (B3) and
`PROJECT_STATISTICS.md` all cited **0.60 mm power / 0.25 mm signal** track
widths. The model and the emitted `.brd` were actually **0.50 mm / 0.20 mm** —
they had been narrowed to buy back routing density after the clearance model
was corrected to measure Euclidean distance, and four documents were not
updated.

**Found by:** cross-checking a document against `NET_CLASSES` and the `.brd`
while answering a question about the blockers.

**Fixed by:** recomputing the IPC-2221 ampacity (0.15 → 0.60 A, 0.20 → 0.74 A,
0.50 → 1.45 A), correcting all four documents, and **making
`PROJECT_STATISTICS.md` derive its widths from `D.NET_CLASSES`** so that
particular drift cannot recur.

A second instance was found while writing this tutorial:
**`PCB_BUILD_GUIDE.md` step 19 told the fab "minimum gap 0.20 mm"** when the
board's measured minimum is **0.130 mm**. That is a dangerous instruction — it
would have had the board built to a rule it violates. Corrected, along with the
step-20 checklist.

> 🔵 **The lesson:** generating documents from the model prevents drift *for
> the generated ones*. Hand-written documents still drift, and the only defence
> is periodically cross-checking them against the model. Two real instances in
> this project, both in hand-written files.

## 26.4 — §15: what would be done differently with more information

From `DESIGN_ASSUMPTIONS.md` §15, verbatim in substance:

1. **Power-path charger** (MCP73871) instead of the TP4056, removing the
   charge-termination interaction entirely.
2. **Buck-boost regulator** instead of the LDO, so the 3V3 rail holds all the
   way to 3.0 V of cell voltage and the usable capacity increases.
3. **USB-C receptacle** with a verified land pattern.
4. **Relocate the TMP117 to a flex tail.** Skin temperature is not measurable
   from inside an electronics pod. The I²C bus is already brought to `J4`, so
   this is a small change. 🟡 M7.
5. **Second IMU on the thigh**, as the project's own alternatives list
   suggests, for fall detection with fewer false positives. Needs one more I²C
   address, which the LSM6DSOX's SA0 pin can provide (0x6B) with no board change
   beyond a connector.

## 26.5 — 🔴 What must never be claimed about this board

$$\large\textcolor{red}{\textsf{It is not a medical device. Do not present it as one.}}$$

- **No IEC 60601-1 or IEC 60601-2-47 compliance work has been done and none is
  claimed.**
- The ECG channel has **no galvanic isolation, no defibrillation protection,
  and no mains isolation while USB is connected.**
- The pass band gives heart rate and HRV, **not interpretable waveform
  morphology.**
- Every current, voltage and frequency in this project is a **datasheet typical
  or a calculation.** Nothing has been measured.
- Component and cost figures across the wider project are **internal
  engineering estimates, not a certified BOM.**

The wider Smart Maternity Band project's own documented limitations also apply:
blood pressure and heart rate are hard to measure accurately from a belt form
factor, and predicted delivery date, predicted recovery time and belly-heatmap
visualisation were all explored and **marked not currently feasible.**

---

# PART 27 — Glossary

| Term | Meaning |
|---|---|
| **ADC1 / ADC2** | the ESP32's two analog-to-digital converters. 🔵 **ADC2 does not work while the radio is active.** |
| **Airwire** | an unrouted connection, shown as a straight line. EAGLE calls the layer `Unrouted` (19). |
| **Ampacity** | how much current a track can carry for a given temperature rise. IPC-2221 gives the chart. |
| **Anti-alias filter** | a low-pass filter before an ADC, removing frequencies above half the sample rate. |
| **BLE** | Bluetooth Low Energy. This board's actual link (≈130 mA vs 355 mA for Wi-Fi TX). |
| **BOM** | Bill Of Materials. |
| **Castellated** | a module with half-holes along its edge, so it can be surface-mounted. |
| **Courtyard** | the keep-out area around a component, including assembly tolerance. This board enforces a **0.90 mm gap**. |
| **DNP** | Do Not Populate. `R17` is a 0 Ω DNP link. |
| **DRC** | Design Rule Check — geometry. Clearances, widths, drills. |
| **EPAD** | Exposed Pad. A metal pad under an IC body, for heat and/or ground. **Must be soldered.** |
| **ERC** | Electrical Rule Check — connectivity. Floating pins, output conflicts. |
| **ERM** | Eccentric Rotating Mass — the classic vibration motor. |
| **Fan-out** | short escape tracks from a fine-pitch part's pads into open space, each ending where a via can be placed. |
| **Flyback diode** | a diode across an inductive load, giving the collapsing field somewhere to go. 🔴 **Orientation is critical.** |
| **FR-4** | the standard glass-epoxy PCB substrate. εr ≈ 4.3. |
| **FSR** | Force-Sensing Resistor. Resistance falls as force rises. Very non-linear. |
| **Gerber** | the standard PCB manufacturing file format, one file per layer. |
| **HASL / ENIG** | Hot Air Solder Levelling / Electroless Nickel Immersion Gold. Surface finishes. **ENIG is flatter, better for fine pitch.** |
| **HPF / LPF** | High-Pass Filter / Low-Pass Filter. |
| **I²C** | two-wire bus. 🔴 **Fixed-address devices can clash — that is the bug found in the input diagram.** |
| **IPC-7351B** | the land-pattern standard. Nominal = Level B. |
| **IPC-2221** | the standard giving trace ampacity. |
| **JST-PH** | a 2.0 mm-pitch connector family. `J1` and `J8`. **Pigtail polarity is not consistent between suppliers.** |
| **Keep-out** | an area where nothing is allowed. Here: 20 × 6.6 mm at the top edge for the antenna. |
| **LDO** | Low-DropOut regulator. Quiet but wastes the difference as heat and needs headroom. |
| **LGA** | Land Grid Array. Pads on the bottom, **no leads.** The LSM6DSOX. 🔴 Easy to fit 180° out. |
| **Net class** | a group of nets sharing width/clearance rules. This board has four. |
| **PCM** | Protection Circuit Module — the little PCB inside a protected Li-Po pack. 🔴 **B1.** |
| **QFN / LFCSP** | Quad Flat No-lead. Pads under the body, usually with an EPAD. The AD8232. |
| **Ratiometric** | a measurement referenced to the supply, so supply variation cancels. The HX711 is ratiometric to AVDD. |
| **RATSNEST** | the EAGLE command that recomputes copper pours and airwires. 🔵 **Fusion does not do it automatically.** |
| **Rip-up and retry** | removing a routed net to let another through, then re-routing it. |
| **RLD** | Right Leg Drive. Drives the third ECG electrode with an inverted common-mode signal to reject mains hum. |
| **Slew limiting** | slowing a switching edge (here with 100 Ω gate resistors) to reduce radiated noise. |
| **SOT-23** | a small three- or five-lead transistor package. 🔴 The five-lead version is where the LDO short defect was. |
| **Stencil** | a thin metal sheet with apertures, for applying solder paste. 🟠 **Required for three parts on this board.** |
| **Strapping pin** | a GPIO sampled at reset to set boot configuration. `IO0`, `IO3`, `IO45`, `IO46`. |
| **Test point** | an exposed pad for probing. 19 on this board. |
| **Via** | a plated hole connecting layers. 486 on this board, all through-hole, 0.3 mm drill. |
| **WSON** | a small no-lead package with a thermal pad. The TMP117. |

---

# PART 28 — FAQ

**Q: Can I just order this board and build it?**
🔴 Not yet. Clear the three BLOCKING items, run Fusion's ERC and DRC, finish
the 4 airwires, and generate Gerbers. See
[Part 3](#part-3--exactly-how-complete-this-is) for the effort table.

**Q: Why is there no PCB software file I can just double-click?**
There is: `pcb/SIH26113_Maternity_Assist_Belt.brd`, which opens in Autodesk
Fusion or EAGLE 9.x. The Python is how it was *made*, not how it is *used*.

**Q: Why generate the files instead of drawing them?**
No EDA software was available. It turned out to be a better approach anyway —
one model produces the library, schematic, board, BOM, netlist, GPIO table and
every report, so they cannot disagree. See
[Part 6](#part-6--the-generated-from-source-model).

**Q: Is the DRC failing a problem?**
No. **Zero geometry violations.** The four errors are the four deliberately
unrouted nets, and the checker does not lower its own bar to produce a PASS.
[§15.3](#153--drc-8-rule-groups--0-geometry-violations).

**Q: Why four layers? Two would be cheaper.**
Measured: on two layers the router completed ~50 of 81 nets and the copper
split into disconnected regions. On four it completes 76+. Plus the AD8232
needs a continuous ground plane. Cost is a couple of dollars per board.

**Q: Can I use a 2-layer version?**
Not without a significant redesign — probably splitting into two boards.

**Q: Why is the ECG pass band so narrow?**
Deliberate motion-artefact resistance for a walking subject. You get heart rate
and HRV; you do not get diagnostic morphology.
[§11.7](#117--if-you-want-to-move-toward-waveform-monitoring) has the retune
path.

**Q: Can I use this to monitor a real pregnancy?**
🔴 **No.** It is not a medical device, has no regulatory compliance work behind
it, and the ECG channel has no isolation. Bench evaluation with informed
participants only.

**Q: Why is the fuel gauge missing?**
Its datasheet could not be retrieved, so the footprint could not be verified.
`J4` takes a breakout, and the `R5`/`R6` divider gives you battery voltage
regardless. 🟠 H1.

**Q: Why is there no battery protection on the board?**
The pinouts of DW01A/FS8205A could not be verified, and guessing on a lithium
protection circuit is unacceptable. 🔴 **A protected pack at `J1` is
mandatory — B1.**

**Q: Can I substitute a different ESP32-S3 module?**
🟠 **No. `-N8R2` only.** Octal-PSRAM variants wire `IO35`/`IO36`/`IO37` to the
PSRAM and this design uses all three. H5.

**Q: Why can't I solder three of the parts?**
0.5 mm-pitch QFN with an exposed pad, a 0.5 mm leadless LGA, and a 0.65 mm WSON
with a thermal pad. They need a stencil and reflow or hot air. 🟠 **Order the
stencil with the boards.**

**Q: Do I need a 5 mil fab? That's more expensive.**
Yes — the measured minimum clearance is **0.130 mm**. A 0.5 mm-pitch QFN
cannot be escaped at 6 mil. 🟠 H6 has a fallback if your fab cannot.

**Q: The router left 4 nets unrouted. Is that a failure?**
No — it is a **deliberate concession.** The router prioritises clearance over
completeness: rather than ship a 0.075 mm gap that nobody would see, it leaves
a visible airwire. Half an hour of hand-routing.

**Q: Why is `J3` backwards?**
⚪ **L2.** `R4` pulls the LDO's `EN` up, so default = ON and closing `J3` = OFF.
Deliberate — it avoided inventing an unverified slide-switch footprint.

**Q: Can I move the mounting hole to the corner?**
⚪ **L1.** That corner is inside the antenna keep-out. A plated hole there would
detune the antenna. Move the antenna to a different edge and re-run
`generate_board.py` if you must.

**Q: How long will the battery last?**
Calculated: **≈13 hours** on 2000 mAh with BLE and all sensors, before duty
cycling. Deep sleep **≈74 µA** ≈ 3 years of shelf life. ❌ **Not measured.**

**Q: What is the single most likely mistake someone will make?**
Ordering the wrong ESP32-S3 variant (🟠 H5), or ordering PCBs at the fab's
default 6 mil (🟠 H6). Both are one dropdown.

**Q: What is the single most dangerous mistake?**
Fitting an unprotected Li-Po cell (🔴 B1), or attaching ECG electrodes with USB
plugged in (🔴 B2).

---

# PART 29 — Printable checklists

Tear these out. Tick them.

---

## ✅ Checklist 1 — 🔴 Before you power anything

```
[ ] B1  Li-Po pack at J1 has an integrated PROTECTION circuit (PCM)
        - peeled the tape and SAW the little PCB
[ ] B1  J1 pigtail polarity METERED:  pin 1 = VBAT (+), pin 2 = GND (-)
        - pin 1 is the SQUARE pad
[ ] B2  ECG safety protocol written down and agreed by everyone:
        [ ] electrodes only on battery power, USB PHYSICALLY UNPLUGGED
        [ ] bench evaluation, informed adult participants only
        [ ] never on a pregnant person as a demo
        [ ] never described as a medical device
[ ] B3  Motor voltage rating known;  R45 value decided
[ ] TP1 (VBAT) to TP3 (GND):  no short
[ ] TP2 (3V3)  to TP3 (GND):  no short
[ ] Bench supply with CURRENT LIMIT set, 5 V, 100 mA for first power-on
[ ] D5/D6/D7/D8 orientation checked against the silkscreen
[ ] R44 and R47 (100k gate pull-downs) FITTED
[ ] Flux residue cleaned, especially around the 10 M ohm ECG nodes
```

---

## ✅ Checklist 2 — 🟠 Before you order PCBs

```
[ ] H6  Fab quotes 0.127 mm (5 mil) GAP on 4 layers
        - NOT the 6 mil default.  Measured minimum on this board is 0.130 mm
[ ] H6  Fab quotes 0.15 mm minimum TRACK
[ ] H6  Fab quotes 0.30 mm minimum DRILL
[ ] H4  Tactile switch lead grid confirmed as 6.5 x 4.5 mm
[ ] Fusion ERC run;  every exception understood and approved  (step 6)
[ ] Fusion DRC clean against the board's OWN rule set SIH26113_4layer (step 15)
[ ] Unrouted layer (19) is EMPTY  (step 13)
[ ] RATSNEST run;  layer 2 unbroken under the ECG block  (step 14)
[ ] Gerbers + drill + PASTE generated  (step 19)
[ ] Gerbers opened in an INDEPENDENT viewer and checked:
        [ ] 4 copper layers present
        [ ] layers 2 and 15 are planes, antenna corner cut out
        [ ] paste layer has openings for U4, U5, U7
        [ ] outline is a closed 100 x 70 mm rectangle
[ ] STENCIL added to the order          <-- the item people forget
[ ] Board size confirmed:  100 x 70 mm, 1.6 mm FR-4, 1 oz outer copper
[ ] Stack-up communicated:  (1*2*15*16), layers 2 and 15 are PLANES
```

---

## ✅ Checklist 3 — 🟠 Before you order components

```
[ ] H5  U3 is ESP32-S3-WROOM-1-N8R2
        - read the FULL part number on the listing, not the title
        - NOT N8R8, NOT N16R8
[ ] H5  Ordered 2 modules (the first may go 180 degrees out)
[ ] L4  AD8232 stock checked (occasionally allocated)
[ ] L4  LSM6DSOX stock checked
[ ] B1  Li-Po pack is PROTECTED and has a JST-PH pigtail
[ ] B3  Motor chosen;  rated voltage and current recorded
[ ] B3  R45 ordered:  0 ohm AND a few ballast values
[ ] H2  Stretch sensor chosen;  R_min and R_max measured;  R37 computed
[ ] H3  Load cell chosen;  bridge resistance and mV/V recorded
[ ] M3  Buzzer type known:  ACTIVE magnetic or PASSIVE piezo
[ ] M4  C34 is 100 nF rated >= 50 V   (NOT a 16 V part)
[ ] M6  Diametric NdFeB magnet, ~6 x 2.5 mm
[ ] 0805 resistor and capacitor assortment kits ordered
[ ] Solder paste ordered (Sn63Pb37 is more forgiving by hand)
[ ] 3 x disposable Ag/AgCl ECG electrodes
```

---

## ✅ Checklist 4 — Assembly

```
STAGE 0  -  fine-pitch parts on a bare board
[ ] Stencil aligned;  paste inspected under magnification
[ ] U7 AD8232      placed, pin-1 chamfer matched
[ ] U5 LSM6DSOX    placed  <-- MOST LIKELY 180-degree ERROR ON THE BOARD
[ ] U4 TMP117      placed, pin-1 dot matched
[ ] U3 module      placed, ANTENNA POINTING OFF THE BOARD EDGE
[ ] Reflowed;  re-inspected for bridges between adjacent pins

STAGE 1  -  power
[ ] U1 U2 R1-R6 C1-C6 D1 D2 J1 J2 J3
[ ] TP2 = 3.3 V +/- 1.5 %          <-- DO NOT PROCEED UNTIL THIS PASSES

STAGE 2  -  module support
[ ] C7 C8 R7 C10 SW2 SW3 R8 J5 R9 R10 D3 D4
[ ] Serial device appears;  blink flashed;  8 MB flash / 2 MB PSRAM confirmed

STAGE 3  -  I2C sensors
[ ] U4 U5 U6 C11-C15 R11-R13 R15 R16
[ ] Sensor bus: 0x48 and 0x6A.   Angle bus: 0x36

STAGE 4  -  mechanical sensing
[ ] U8 C25-C28 J8-J15 R33-R42 C29-C36 D5 D6 R37 R38 C33 C34 R39-R41 C35
[ ] HX711 reading changes under load;  all 4 FSRs respond;  piezo spikes

STAGE 5  -  alerts
[ ] Q1 Q2 R43 R44 R46 R47 D7 D8 C37 C38 R45 J16 J17
[ ] TP15 and TP16 BOTH READ 0 V AT BOOT     <-- before connecting the motor

STAGE 6  -  ECG, last
[ ] U7 passives:  R18-R32, C16-C24, J7
[ ] TP11 (REFOUT) = 1.65 V
[ ] Waited 2.5 s;  TP10 idles near 1.65 V
[ ] LA/RA shorted at J7:  output settles quiet  (that is your noise floor)
[ ] ON BATTERY, USB UNPLUGGED, before any electrode touches a person
```

---

## ✅ Checklist 5 — 🔵 Firmware

```
[ ] Low-battery cut-off at 1750 mV on IO9 (= 3.5 V cell)  -> deep sleep
[ ] 2.5 s delay after power-up before trusting any ECG reading
[ ] ADC1 only (GPIO1-10);  ADC2 never used for analog
[ ] TWO separate I2C busses initialised  (0x36 is on both)
[ ] Internal I2C pull-ups DISABLED (4k7 externals are on the board)
[ ] IO47 and IO48 driven LOW explicitly as the first thing in app_main()
[ ] ECG_SDN (IO37) driven HIGH = enabled
[ ] ECG_FR  (IO39) driven LOW  = fast restore off
[ ] LOD+ (IO35) and LOD- (IO36) polled;  report WHICH electrode
[ ] ECG baseline treated as ~1.65 V, not 0 V
[ ] ~1 s discarded after any FR pulse or leads-off event
[ ] ECG sampled at >= 250 Hz
[ ] SOS (IO40) treated as ACTIVE LOW, debounced, LONG PRESS required
[ ] HALL_LIMIT (IO41) treated as ACTIVE LOW
[ ] IO45 / IO46 driven only, never read (strapping pins)
[ ] Motor driven by PWM with duty scaled against VBAT_SENSE (preferred over
    a resistive ballast - see 23.6)
[ ] Buzzer driven per its type:  on/off for active, PWM 2-4 kHz for passive
[ ] Deep sleep shuts down:  ECG_SDN low, HX_SCK high, TMP117, LSM6DSOX, AS5600
```

---

# PART 30 — Appendices

## A30.1 — Command index

| Command | What it does |
|---|---|
| `python scripts/build_all.py` | regenerate everything, in order |
| `python scripts/build_all.py --fast` | same, single routing ordering (faster) |
| `python scripts/generate_library.py` | → `.lbr` + library self-check |
| `python scripts/validate_erc.py` | the 11-group ERC. **Must PASS** |
| `python scripts/generate_schematic.py` | → `.sch` + self-cross-check |
| `python scripts/generate_board.py` | place + route + emit `.brd` |
| `python scripts/validate_drc.py` | the 8-group DRC. **FAIL is expected** |
| `python scripts/validate_planes.py` | **plane-pour connectivity.** Punches antipads, labels regions, checks every plane contact reaches the main region |
| `python scripts/render.py` | → all 12 PNGs |
| `python scripts/generate_docs.py` | → netlist, GPIO, BOM, ERC/DRC reports, statistics |
| `python scripts/gen_reports.py` | → manufacturing check + final report |
| `python scripts/make_fusion_project.py` | → `fusion_project/` — **the folder to open in Fusion** |
| `python -m pip install numpy matplotlib Pillow` | the only three dependencies |

**Environment variable:**

| Variable | Effect |
|---|---|
| `SIH_ROUTE_ATTEMPTS` | number of routing orderings to try. Default **14**. Set to `1` for a fast route. |

## A30.2 — Document index, by question

| Your question | The document |
|---|---|
| 🔴 What must I resolve before powering this? | `REQUIRES_CONFIRMATION.md` |
| What exists and what is left? | `FINAL_REPORT.md` |
| How do I open it in Fusion? | `PCB_BUILD_GUIDE.md` |
| Why was this decided that way? | `DESIGN_ASSUMPTIONS.md` |
| Where did this pinout come from? | `COMPONENT_VERIFICATION.md` |
| Which GPIO does what? | `GPIO_ASSIGNMENT.md` |
| How much current does it draw? | `POWER_BUDGET.md` |
| How does the ECG circuit work? | `ECG_FRONTEND_DESIGN.md` |
| Why is the ground not split? | `GROUNDING_NOTES.md` |
| Is the USB pair 90 Ω? | `USB_PAIR_ANALYSIS.md` |
| Do the ground/3V3 pours stay connected? | run `scripts/validate_planes.py`; results in `pcb/plane_result.json` |
| What is connected to what? | `NETLIST.md` |
| What do I buy? | `BOM.md` / `BOM.csv` |
| Was the connectivity checked? | `ERC_REPORT.md` |
| Was the geometry checked? | `DRC_REPORT.md` |
| Can it be manufactured? | `MANUFACTURING_CHECK.md` |
| What went wrong and got fixed? | `FINAL_REVIEW.md` |
| How big / how many of what? | `PROJECT_STATISTICS.md` |
| Everything, in order? | **this document** |

## A30.3 — All 84 nets

| | | | | | |
|---|---|---|---|---|---|
| `3V3` | `ANG2_OUT` | `ANG_SCL` | `ANG_SDA` | `AS_OUT` | `AS_PGO` |
| `BUZZER_EN` | `BUZZ_G` | `BUZZ_N` | `CHG_PROG` | `ECG_FR` | `ECG_HPDRIVE` |
| `ECG_HPSENSE` | `ECG_IAOUT` | `ECG_LA` | `ECG_LA_F` | `ECG_LOD_N` | `ECG_LOD_P` |
| `ECG_OPM` | `ECG_OPP` | `ECG_OUT` | `ECG_OUT_RAW` | `ECG_RA` | `ECG_RA_F` |
| `ECG_REFIN` | `ECG_REFOUT` | `ECG_RL` | `ECG_RLD` | `ECG_RLDFB` | `ECG_SDN` |
| `ECG_SW` | `ESP_EN` | `ESP_IO0` | `FSR1_ADC` | `FSR2_ADC` | `FSR3_ADC` |
| `FSR4_ADC` | `GND` | `HALL_LIMIT` | `HX_BASE` | `HX_DOUT` | `HX_SCK` |
| `HX_VBG` | `HX_XO` | `I2C_SCL` | `I2C_SDA` | `IMU_INT1` | `IMU_INT2` |
| `IMU_OCS_AUX` | `IO3_SPARE` | `LC_A_N` | `LC_A_P` | `LDO_EN` | `LDO_NC` |
| `LED_ALERT` | `LED_ALERT_A` | `LED_CHRG_A` | `LED_CHRG_K` | `LED_STATUS` | `LED_STATUS_A` |
| `LED_STDBY_A` | `LED_STDBY_K` | `MOTOR_EN` | `MOTOR_G` | `MOTOR_N` | `MOTOR_P` |
| `PIEZO_AC` | `PIEZO_ADC` | `PIEZO_IN` | `SD_CS` | `SD_MISO` | `SD_MOSI` |
| `SD_SCK` | `SOS_BTN` | `SOS_GPIO` | `STRETCH_ADC` | `TMP_ALERT` | `UART_RX` |
| `UART_TX` | `USB_DM` | `USB_DP` | `VBAT` | `VBAT_SENSE` | `VBUS` |

Two of them (`GND`, `3V3`) are **plane nets** carried by an inner pour. Two
(`LDO_NC`, `IMU_OCS_AUX`) are **declared no-connects**. The remaining **80**
require tracks; **76 are routed.**

## A30.4 — The eight ICs, at a glance

| Ref | Part | MPN | Manufacturer | Package | Assembly |
|---|---|---|---|---|---|
| `U1` | TP4056 | TP4056-42-SOP8-PP | NanJing Top Power | SOIC-8-N | hand |
| `U2` | AP2112K-3.3 | AP2112K-3.3TRG1 family | Diodes | SOT-23-5 | hand |
| `U3` | 🟠 **ESP32-S3-WROOM-1-N8R2** | ESP32-S3-WROOM-1-N8R2 | Espressif | castellated | reflow / hot air |
| `U4` | TMP117 | TMP117AIDRVR | Texas Instruments | WSON-6 | 🟠 **reflow only** |
| `U5` | LSM6DSOX | LSM6DSOXTR | STMicroelectronics | LGA-14L | 🟠 **reflow only** |
| `U6` | AS5600 | AS5600-ASOM | ams-OSRAM | SOIC-8-N | hand |
| `U7` | 🔴 **AD8232** (3V3 only!) | AD8232ACPZ-R7 | Analog Devices | LFCSP-20 | 🟠 **reflow only** |
| `U8` | HX711 | HX711 | Avia Semiconductor | SOP-16-N | hand |

## A30.5 — I²C address map

| Address | Device | Bus | Note |
|---|---|---|---|
| **0x36** | AS5600 | **ANGLE** (I2C1) | fixed, no select pin |
| **0x36** | MAX17048 breakout | **SENSOR** (I2C0) | 🟠 H1 — optional, at `J4` |
| **0x48** | TMP117 | SENSOR (I2C0) | `ADD0` grounded |
| **0x6A** | LSM6DSOX | SENSOR (I2C0) | `SDO/SA0` grounded. 0x6B if pulled high |

> 🔵 **0x36 appears on both busses deliberately.** That is the resolution of a
> real conflict in the input architecture, not an oversight.

## A30.6 — Quick numeric reference

| Quantity | Value |
|---|---|
| Board | 100 × 70 mm, 1.6 mm FR-4, 4 layers, 1 oz |
| Stack-up | L1 sig / L2 GND plane / L15 3V3 plane / L16 sig — `(1*2*15*16)` |
| Antenna keep-out | 20 × 6.6 mm at (9, 63.4)–(29, 70) |
| Mounting holes | M2 at (3,3), (97,3), **(2.6,42)**, (97,67) |
| Min clearance, measured | **0.130 mm** |
| Clearance rule | 0.15 mm general / **0.127 mm** in 4 fan-outs |
| Track widths | 0.15 escapes / 0.20 signal / 0.50 power and motor |
| Min drill | 0.30 mm |
| Vias | 486, all through, 0.3 mm drill / 0.55–0.60 mm pad |
| Courtyard gap | 0.90 mm |
| Edge clearance | 0.40 mm |
| Parts / placements | 167 model / **150** on the board |
| Nets / connections | **84** / **420** |
| Tracks | 4 523 segments |
| Routed | **76 / 80** signal nets (95 %) |
| Test points | 19 |
| BOM line items | 75 |
| Tallest part | **8.5 mm** (`J9`) → **11.6 mm** min enclosure height |
| Charge current | 500 mA (`R1` = 2k4) |
| 3V3 worst case | ≈ 510 mA vs a 600 mA LDO → 15 % margin |
| Realistic steady state | ≈ 155 mA → ≈ 13 h on 2000 mAh |
| Deep sleep | ≈ 74 µA |
| 🔵 Low-battery cut-off | **1.75 V at `IO9`** = 3.5 V cell |
| ECG gain | 100 × 11 = **1100** |
| ECG pass band | ≈ **7 – 40 Hz** |
| 🔵 ECG settling time | **2.5 s** |
| ECG virtual ground | ≈ **1.65 V** |
| Patient protection | **330 kΩ** per electrode → < 10 µA |
| I²C pull-ups | 4k7 → 239 ns rise at ~60 pF |

## A30.7 — Where every deliverable lives

| Deliverable | Path |
|---|---|
| Library | `libraries/SIH26113_Maternity_Assist_Belt.lbr` |
| Schematic (7 sheets) | `schematic/SIH26113_Maternity_Assist_Belt.sch` |
| Board (4 layers) | `pcb/SIH26113_Maternity_Assist_Belt.brd` |
| Route report | `pcb/route_report.json` |
| DRC data | `pcb/drc_result.json` |
| Component verification | `documentation/COMPONENT_VERIFICATION.md` |
| GPIO assignment | `documentation/GPIO_ASSIGNMENT.md` |
| Netlist | `documentation/NETLIST.md` |
| BOM | `documentation/BOM.md`, `documentation/BOM.csv` |
| Design assumptions | `documentation/DESIGN_ASSUMPTIONS.md` |
| Grounding notes | `documentation/GROUNDING_NOTES.md` |
| ECG design note | `documentation/ECG_FRONTEND_DESIGN.md` |
| Power budget | `documentation/POWER_BUDGET.md` |
| ERC report | `documentation/ERC_REPORT.md` |
| DRC report | `documentation/DRC_REPORT.md` |
| 🔴 Open items | `documentation/REQUIRES_CONFIRMATION.md` |
| Build guide (20 steps) | `documentation/PCB_BUILD_GUIDE.md` |
| Manufacturing check (19 items) | `documentation/MANUFACTURING_CHECK.md` |
| Final review (27 points) | `documentation/FINAL_REVIEW.md` |
| Final report (15 sections) | `documentation/FINAL_REPORT.md` |
| Statistics | `documentation/PROJECT_STATISTICS.md` |
| Schematic renders | `renders/schematic_p1.png` … `p7.png` |
| Board renders | `renders/pcb_top.png`, `pcb_bottom.png`, `pcb_layers.png`, `pcb_assembly.png`, `pcb_3d.png` |
| Input architecture diagram | `reference/PCB_architecture_source.jpeg` |
| Generators | `scripts/` (16 files) |
| Short entry point | `README.md` |
| **This document** | `FULL_INSTRUCTION_TUTORIAL.md` |

## A30.8 — Attribution and reuse

The datasheets referenced throughout belong to their respective manufacturers
and are **not redistributed** here. Footprint dimensions are derived from
publicly published land-pattern drawings and the **IPC-7351B** standard.
Trace ampacity figures are from **IPC-2221**.

Part of the **Smart Maternity Band** project (Smart India Hackathon 2026,
problem statement **SIH26113**, Team Rocket 🚀). The parent repository holds the
concept website; this directory is the electronics.

---

# PART 31 — Engineering log: what was built, what broke, and what it taught

The rest of this document tells you **what the board is**. This part tells you
**how it got that way** — the decisions, the eleven things that turned out to
be wrong, and the reasoning that found them.

It is here because the mistakes are more instructive than the design. Anyone
can read a finished schematic. Knowing that a SOT-23-5 footprint had its pad
length and width swapped — and that it looked completely fine on screen — is
the thing that makes you check next time.

---

## 31.1 — The starting point, and why it was not trusted

The entire input to this project was **one architecture image**
(`reference/PCB_architecture_source.jpeg`). The brief was explicit that it was
a *starting point*, not a specification, and that nothing in it should be
assumed correct.

That turned out to matter, because it contained three real faults:

| Fault | How it was found | Consequence if trusted |
|---|---|---|
| **TMP117 + LSM6DSOX + AS5600 + MAX17048 on one I²C bus** | checking every device's address against its datasheet | 🔴 **a bus that does not function.** AS5600 and MAX17048 are both hard-wired to `0x36` with no address-select pin |
| **"TP4056 protected module"** | reading what a commercial TP4056 *module* actually contains | 🔴 **no battery protection on the board.** The word "protected" referred to a DW01A + FS8205A that a bare-IC implementation does not have |
| **An implied 2-layer carrier board** | routing it and counting | ~50 of 81 nets routable; copper split into disconnected regions |

**The lesson:** a block diagram encodes *intent*, not *feasibility*. Every
device on a shared bus needs its address checked; every "module" needs its
contents enumerated; every layer count needs to survive an actual routing
attempt.

---

## 31.2 — Why the project is Python instead of mouse-clicks

There was no EDA software in the environment where these files were produced.
So instead of drawing the design, it is **described** in `scripts/design.py`
and the EAGLE 9 XML is generated from that description.

That began as a workaround. It became the best property of the project:

> **One model produces the library, the schematic, the board, the netlist
> document, the GPIO table, the BOM, the ERC report, the DRC report, the
> statistics and every render. They cannot disagree with each other.**

And — more importantly — the generators can **check themselves**:

| Generator | What it asserts about its own output |
|---|---|
| `generate_library.py` | every symbol pin maps to a real pad; no orphan pads; **no pad overlaps** |
| `generate_schematic.py` | re-parses the emitted `.sch` and asserts the netlist matches the model exactly |
| `generate_board.py` | re-parses the emitted `.brd` and asserts elements and signals match |
| `render.py` | draws **only** primitives found in the real files — a render cannot show something the board lacks |
| `validate_drc.py` | **shares no code with the router**, so it is able to contradict it |

That last line is the whole trick, and it paid off three separate times. If
your checker and your generator share a wrong assumption, the checker will
cheerfully confirm the bug.

**The lesson, generalised:** whatever you build, build a second thing that can
disagree with it. Not a test that re-implements the same logic — an
*independent* measurement.

---

## 31.3 — The routing story, in full

This is the part with the most transferable engineering in it.

### Stage 1 — two layers, and the measurement that killed them

The architecture implied a simple carrier board. Two layers was tried first,
because two layers is cheaper and simpler.

| Layers | Nets the router completed (of 81 at the time) |
|---|---|
| 2 | **~50**, and the board's reachable copper **split into disconnected regions** |
| 4 | **77** |

Plus the electrical argument: the AD8232 amplifies a **sub-millivolt**
biopotential by **1100**, across **10 MΩ** nodes, and its datasheet asks for a
ground plane. On two layers there is no continuous reference under the analog
section — the return path is interrupted by every signal that has to cross it.

Four layers cost a couple of dollars per prototype board. **The decision was
made on a measured routing count, not on preference.**

### Stage 2 — the board grew, and not for component area

The design started at **80 × 60 mm** and ended at **100 × 70 mm**.

The binding constraint was never component area. It was **escape area** — the
space needed to get signals *out* of the dense parts:

```python
ESCAPE_CHANNELS = [
    (0.90, 43.0,  9.50, 64.0),    # left of the module's pad column
    (28.50, 40.0, 34.20, 64.0),   # right of the module's pad column
    (8.00, 36.00, 29.00, 44.20),  # below the module's end row
]
```

The ESP32-S3-WROOM-1 presents **40 lands on 1.27 mm pitch across three
edges**. Without a component-free corridor outboard of each land row, those 40
signals have **literally nowhere to go** — and both an autorouter and a human
stall in exactly the same place.

**The lesson:** on a dense board, reserve escape corridors *before* you place
anything. Placement that looks tidy and leaves no exit route is worse than
placement that looks scattered and does.

### Stage 3 — fan-out, and the stagger trick

Fine-pitch parts are given an explicit escape pattern **before** general
routing starts, rather than being left to the router:

| Part | Package | Why it needs help |
|---|---|---|
| AD8232 | 0.5 mm QFN + exposed pad | pads under the body |
| LSM6DSOX | 0.5 mm LGA | no leads at all |
| TMP117 | 0.65 mm WSON + thermal pad | pads under the body |
| HX711 | SOP-16 with 9 plane pads | every plane pad wants a via beside it |

**The trick that makes it work: alternate escape stubs are made *longer*.**

```
without stagger:          with stagger:
  ──○                       ────○
  ──○   ← vias collide      ──○      ← each via has room
  ──○                       ────○
  ──○                       ──○
```

Without staggering, the vias at the stub ends collide and **only every other
pin can leave the part**. With it, all of them can. 45 fine-pitch escapes and
49 coarse-pitch radial stubs exist for this reason.

### Stage 4 — narrower tracks, for a non-obvious reason

Signal tracks went **0.25 → 0.20 mm** and power **0.60 → 0.50 mm**.

**Not for ampacity.** Ampacity was never the binding constraint — 0.50 mm
carries ≈ 1.45 A (IPC-2221, 1 oz, 10 °C rise) against a 620 mA worst case,
which is **2.3× margin**.

They were narrowed because **a narrower track needs less clearance around it**,
and that bought back the routing density lost when the clearance model was
corrected to measure Euclidean distance instead of Manhattan (defect #2
below). Copper you do not use is routing space you do.

### Stage 5 — clearance over completeness

The single most important routing policy in this project:

> **Where the router can only finish a net by coming closer than the clearance
> rule, it rips the net out and leaves an airwire instead.**

Each concession is recorded with the gap it would have needed:

```
net I2C_SDA is not fully routed: left unrouted on purpose: every path the
router found came within 0.075 mm of FSR1_ADC on layer 1, below the 0.15 mm
rule. Route it by hand in Fusion.
```

**Why this is right:** an airwire is **visible** in Fusion the instant the
board opens, appears in EAGLE's own DRC under "Unrouted", and takes a minute
to fix by hand. A 0.075 mm gap is **invisible** and might reach fabrication.

**The lesson:** when a tool has to choose between a loud failure and a quiet
compromise, make it fail loudly. A 95 %-routed board with four named airwires
is a better deliverable than a 100 %-routed board with an unmarked short.

### Stage 6 — the seed search, and knowing when to stop

Net ordering dominates the result in a greedy router, so the router tries
several orderings and keeps the best:

| Attempts | Result |
|---|---|
| 1 seed | 74 / 80 — 6 airwires |
| **14 seeds** | **76 / 80 — 4 airwires** (best was seed 8) |
| 64 seeds | **abandoned** — see below |

A 64-seed search was launched to try to beat 76/80. It was **stopped after
66 CPU-minutes**, and the reasoning is worth recording because it is a
judgement call, not a failure:

| | |
|---|---|
| Cost of the *first* seed | **48.8 s** — measured, and the basis of the estimate |
| Projected total for 64 | ~52 min |
| Actual at abort | **66 CPU-min and still running**, 28 % over, with no progress visibility |
| Expected gain | 76/80 → maybe 77 or 78. **Diminishing returns** |
| Value of that gain | **~5 minutes** of interactive routing in Fusion |

**And here is why the estimate was wrong**, visible once the run was
re-launched with unbuffered logging:

```
attempt seed=0: 74/80 routed,  6 unrouted, 53.9s
attempt seed=1: 67/80 routed, 13 unrouted, 62.4s
attempt seed=2: 66/80 routed, 14 unrouted, 68.8s
attempt seed=3: 71/80 routed,  9 unrouted, 41.5s
```

**Per-seed cost varies by more than 1.6× (41.5 – 68.8 s observed), and it
loosely tracks how badly the seed routes** — a seed that struggles leaves more
nets for the rip-up-and-retry phase to fight over, so it burns *more* time
producing a *worse* result. It is variance, not a trend: seed 3 was both fast
and decent.

Either way, **extrapolating a 64-seed total from seed 0 alone is not a
projection, it is a guess.** The right estimate needs the spread, and you only
get the spread by watching several.

> 🔵 **Two process lessons, not electrical ones.** First: **never estimate a
> batch from its first item** if the per-item cost is state-dependent. Second:
> the original run piped its output through `tail`, which **buffers until the
> pipe closes** — so there was no progress visibility for an hour. Re-running
> with `python -u` writing straight to a log file made the growth obvious in
> two minutes. **If you cannot see progress, you cannot course-correct.**

**The seed search was optimising something that gets finished by hand anyway.**
Spending an hour of compute to save five minutes of human work is a bad trade,
and it was blocking six other tasks. 14 seeds was re-run instead.

**The lesson:** know what the marginal unit of your optimisation is actually
worth *downstream*. And when an estimate is 28 % over with no visibility, the
estimate was wrong — stop and re-plan rather than waiting it out.

> 🟠 **A related trap this exposed.** The first 64-seed run was launched
> *before* the plane-via defect (#11) was found and fixed. Its result would
> have been a better-routed board **with a real electrical fault in it.** When
> it had to be discarded, the previous 76/80 board went with it — because that
> too predated the fix. **A correctness fix invalidates every optimisation
> result that predates it.** Re-run the optimisation, do not reach for the
> cached "better" answer.

### Stage 7 — the router internals, briefly

| Mechanism | Detail |
|---|---|
| Grid | **0.20 mm** occupancy grid per copper layer, numpy arrays |
| Clearance | obstacles **dilated by a Euclidean disc**, then treated as solid — O(n) instead of O(n²) segment-vs-segment |
| Width awareness | `stamp_radius = max(half, 2·half − 0.100)` so a 0.50 mm track is not checked as if it were 0.20 mm |
| Search | **8-connected A\*** with `STEP_ORTHO=10`, `STEP_DIAG=14` (≈10·√2, so 45° is priced correctly and you do not get staircases), `VIA_COST=60` |
| Rip-up | **transactional** — `snapshot()` / `restore()`, with the final count recomputed from final state |

---

## 31.4 — The eleven defects, and what each one teaches

These were all genuine faults in earlier revisions. Full detail in
`documentation/FINAL_REVIEW.md`.

| # | Defect | The transferable lesson |
|---|---|---|
| 1 | **Unplated holes drilled through thermal pads** — EAGLE's `<hole>` inside a *package* is an **unplated** mechanical hole | **Know what your tool's primitives actually mean.** "Hole" and "via" are not synonyms, and the wrong one through a thermal land is a defect that renders correctly on screen |
| 2 | **Clearance measured as a diamond, not a disc** — Manhattan dilation overstates diagonal clearance by up to √2 | **Check the metric, not just the number.** A "0.15 mm rule" measured as an L1 ball permits 0.106 mm diagonally |
| 3 | **Fan-out stubs crossing neighbouring pads** | A path being *free at its endpoints* does not mean it is free along its length |
| 4 | **Plane-via spurs crossing neighbouring pads** | The same bug class in a second code path. **When you fix a geometric bug, grep for every place that geometry is generated** |
| 5 | **Rip-up cascading damage** — took unrouted from 4 to **33** while the counter still reported success | **Never track state incrementally when you can recompute it.** The counter was believed; the board was wrong |
| 6 | 🔴 **SOT-23-5 land pattern shorted VIN to GND** — pad length and width swapped, 1.10 mm pads on 0.95 mm pitch | **This one is why the project has an independent review at all.** It affected `U2`, the 3.3 V LDO — every board in the first batch would have died. **It looked completely plausible in the library editor.** |
| 7 | **LGA-14 IPC enlargement closed corner pairs to 0.11 mm** | **A standard applied blindly is not a standard applied.** IPC enlargement is right for leaded parts and wrong for a 0.5 mm LGA — use 1:1 with the package pad |
| 8 | **The DRC measured round pads as squares** | A checker's own approximations create both false positives *and* false negatives. The false positives were noise that **masked real violations** |
| 9 | **The clearance model assumed every conductor was nominal width** | Defaults leak. A 0.50 mm power track checked as 0.20 mm passes a rule it violates |
| 10 | **Placement collisions from hand-picked coordinates** | 150 coordinates chosen by hand will collide somewhere. Replaced with a resolver enforcing a 0.90 mm courtyard gap |
| 11 | 🔴 **Plane vias placed outside the pour outline** — one of them was **`C7`'s only connection to the ground plane** | **A check that asks the wrong question passes.** DRC rule D7 asked *"does this pad have a via on its net?"* — yes — and never asked *"does that via land inside the pour?"* |

### Defect #11 in detail, because it is the most recent and the most subtle

The inner pours are drawn as an **L** — for x < 29.5 they stop at **y = 63.0**,
so neither plane runs up beside the module's antenna. Nothing prevented a
*plane-connect via* from being placed in the strip above that line, and two
`GND` vias were.

One of them, at `(3.8, 63.725)` — **0.725 mm outside the pour** — was the only
plane connection for **`C7`**, the 100 nF HF bypass at the ESP32's supply pin.
That is one of the two parts that actually supply the **355 mA Wi-Fi TX
burst**. Its ground return to the plane did not exist. It was a hole.

Three things conspired to hide it:

1. **D7 asked the wrong question** (above).
2. The pours declare **`orphans="off"`**, so EAGLE *deletes* islands rather
   than leaving stray copper that might have accidentally rescued it.
3. The wrong assumption was **written down as a justification** in
   `_route_to_plane()`: *"every via in this design is a through via, so a via
   already sitting on this net is already tied to the inner plane."* True —
   **only inside the pour.**

That third point is the real lesson: **a comment explaining why something is
safe is a load-bearing claim.** This one was correct in the general case and
false at the boundary, and it had been sitting there being reassuring.

Found by writing `scripts/validate_planes.py`, which measures what the build
guide had previously asked a human to *eyeball*: punch an antipad around every
through-hole and via, label the connected regions, and check that every
plane-net contact lands in the main one.

---

## 31.5 — Documentation drift, three times

Generated documents cannot drift. **Hand-written ones do**, and this project
caught three instances:

| # | Drift | How it was caught | Fix |
|---|---|---|---|
| 1 | Four documents cited **0.60 mm power / 0.25 mm signal** tracks; the model and `.brd` were **0.50 / 0.20 mm** | cross-checking a document against `NET_CLASSES` while answering a question | corrected all four; **`PROJECT_STATISTICS.md` now derives widths from `D.NET_CLASSES`** |
| 2 | `PCB_BUILD_GUIDE.md` step 19 told the fab **"minimum gap 0.20 mm"**; measured minimum is **0.130 mm** | reading the file while writing this tutorial | corrected; 🔴 **this one would have had boards built to a rule the design violates** |
| 3 | `FINAL_REPORT.md` hard-coded "eighteen documents" and "twelve renders" | counting the files | **`gen_reports.py` now counts them from disk** |

**The lesson:** "generated from a single source of truth" only protects the
generated artefacts. Every number you type by hand into prose is a copy that
will go stale. Where a figure matters, **derive it or point at the thing that
owns it** — which is why the README now says *"see `DRC_REPORT.md` for the
exact figures"* instead of restating the routing count.

---

## 31.6 — Getting datasheets when the network fights you

Primary documentation was the hard requirement — **no pinout in this library
was written from memory**. But analog.com and several distributor mirrors were
unreachable or bot-blocked.

What worked:

| Technique | Used for |
|---|---|
| Manufacturer-authored **mirrors** (vendor PDFs hosted by distributors and universities) | most parts |
| **Rasterising vector-only drawings at 5×** with PyMuPDF, then reading dimensions off the image | land patterns that had no extractable text |
| Downloading the PDF and extracting text **locally** with pypdf when a fetch tool choked on the binary | DW01A, AS5600 |

What did **not** work, and was therefore recorded as unresolved rather than
guessed:

| Part | Outcome |
|---|---|
| **MAX17048** | ❌ unreachable → **not placed.** Replaced with header `J4` for a breakout, plus a 470 k/470 k divider that works regardless (🟠 H1) |
| **FS8205A** | ❌ only distributor listings, which **contradict each other** on S1/S2 and whether the drains are common → the on-board battery-protection option **remains blocked** (🔴 B1) |
| **DW01A** | ✅ eventually verified from the primary datasheet (Rev 1.0, JUN 2009) — but half a protection circuit is not a protection circuit |

**The lesson:** "I could not verify this" is a legitimate, useful engineering
output. An unverified footprint in a library is a board that cannot be
assembled, and it is indistinguishable from a verified one until the parts
arrive.

---

## 31.7 — What was deliberately *not* done

Not everything unfinished is an oversight. These were choices:

| Not done | Because |
|---|---|
| **A Gerber exporter** | The plane layers need polygon fill with a correct antipad around every foreign pad and via. With no Gerber viewer and no fab available, **the output could not be verified** — and a wrong antipad is a short to a plane, i.e. a dead board. Emitting unverifiable manufacturing files is worse than emitting none |
| **On-board battery protection** | FS8205A pinout unverifiable (§31.6). Also a **major** change: the FS8205A switches the cell's *negative* terminal, so `J1` pin 2 stops being system `GND` |
| **A split AGND/DGND** | Analysed and rejected on merit — see [Part 12](#part-12--grounding-and-the-stack-up). Return current follows the signal, not the schematic |
| **Claiming EAGLE's ERC/DRC passed** | They were never run. Every document says **"NOT EXECUTED — TOOL UNAVAILABLE"** in those words |

---

## 31.8 — If you take five things from this project

1. **Build a second thing that can disagree with the first.** Not a test that
   re-implements your logic — an independent measurement. Three defects were
   found only because `validate_drc.py` shares no code with `router.py`, and a
   fourth because `validate_planes.py` measured what a human had been asked to
   eyeball.

2. **Make tools fail loudly rather than compromise quietly.** An airwire you
   can see beats a 0.075 mm gap you cannot.

3. **Check that your check is asking the right question.** D7 asked "is there a
   via on this net?" and passed a board where `C7` had no ground.

4. **Every hand-typed number in prose is a copy that will go stale.** Derive it
   or point at its owner. Three drifts, one of which would have misinformed a
   fabricator.

5. **"I could not verify this" is a deliverable.** Two parts are absent from
   this board for exactly that reason, and both absences are documented with
   what would be needed to close them.

---

<div align="center">

## 🔴 One last time

$$\Large\textcolor{red}{\textsf{This is not a medical device.}}$$

$$\textcolor{red}{\textsf{The cell at J1 must be PROTECTED.}}$$

$$\textcolor{red}{\textsf{Electrodes only on battery power, USB unplugged.}}$$

$$\textcolor{orange}{\textsf{The module must be -N8R2. The fab must quote 5 mil.}}$$

**[→ PART 1 — THE BLOCKERS](#part-1--the-blockers-read-this-before-anything-else)**

---

*Nothing in this project is claimed as passing a tool that was never run.*
*Autodesk Fusion's own ERC and DRC have **NOT** been executed —*
*running them is [Part 19](#part-19--workflow-d-open-it-in-autodesk-fusion-all-20-steps), steps 6 and 15, and it is your job.*

*No figure in this project is a measurement. Go and measure them.*

</div>
