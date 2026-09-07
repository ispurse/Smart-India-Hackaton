# DESIGN ASSUMPTIONS AND DECISIONS — SIH26113 Maternity Assist Belt

Everything here is a choice that the architecture diagram did not make for
me. Each entry says what was decided, why, and what would change it.

Changes that **depart from the architecture diagram** are marked
**[ARCHITECTURE CHANGE]** and explained. There are seven of them.

---

## 1. Power architecture

### 1.1 A protected battery pack is required — the board has no cell protection

**[ARCHITECTURE CHANGE]** The diagram says "JST → TP4056 **protected**
module". A commercial TP4056 *module* carries a DW01A + FS8205A protection
circuit alongside the charger IC. This design uses the TP4056 as a bare IC, so
that protection is not on the board.

I did not add DW01A + FS8205A because their pinouts could not be verified
from primary documentation in this environment, and guessing on a
lithium-battery protection circuit is not an acceptable engineering risk.

**Consequence:** `J1` must be fed from a Li-Po cell or pack with an
**integrated protection circuit module (PCM)** — over-charge, over-discharge
and over-current. Nearly all 1S Li-Po cells sold for prototyping already have
one; the tell is a small PCB under the yellow tape at the terminal end.

This is repeated in `README.md` and `REQUIRES_CONFIRMATION.md` because getting
it wrong is a fire risk, not a functional bug.

### 1.2 Charge current programmed to 500 mA, not 1 A

`R1` = 2.4 kΩ. The TP4056 datasheet's characteristics table gives
R_PROG = 2.4 k → 500 mA (and 1.2 k → 1000 mA).

At 1 A from a 5 V input into a 3.7 V cell the TP4056 dissipates about 1.3 W.
The SOP-8 package has an exposed radiator, but its dimensions are not given in
the datasheet, so the footprint has **no thermal land** and cannot shed that.
The part has thermal regulation and would simply fold back, but designing to
sit in thermal limit is poor practice. 500 mA charges a 1500–2000 mAh cell in
3–4 hours, which is fine for a wearable that is charged overnight.

**Would change if:** a verified thermal land is added, or a switching charger
replaces the TP4056.

### 1.3 No power-path switching — a documented compromise

The TP4056's `BAT` pin is simultaneously the cell terminal and the system
rail. During charging, system load current flows through the charger, which
disturbs its C/10 termination detection: the charger may terminate early or
re-cycle.

Accepted for a prototype (it is how every TP4056 board works). A production
build should use MCP73871 or BQ24075, which separate the charge path from the
system load path.

### 1.4 AP2112K-3.3 for the 3V3 rail

600 mA guaranteed minimum, and the worst-case simultaneous load is ~510 mA —
see `POWER_BUDGET.md` for the itemised arithmetic. Chosen over a switcher
because an LDO has no switching noise, which matters a great deal 20 mm from
an ECG front end amplifying a sub-millivolt signal by 1100.

**The cost of that choice is stated honestly:** 250 mV dropout at 600 mA means
the 3V3 rail sags as the cell empties. At `VBAT` = 3.3 V the output is about
3.05 V, and the ESP32-S3's minimum is 3.0 V. **Firmware must implement a
low-battery cut-off at ~3.5 V using `VBAT_SENSE` on `IO9`.** Without it the
board will brown out unpredictably at the end of the discharge curve.

### 1.5 Board on/off via an external switch on `J3`

`R4` (100 kΩ) pulls the LDO's `EN` up to `VBAT`, so the default state is ON.
`J3` brings `EN` and `GND` out to a 2-pin header: **closing an external switch
across `J3` turns the board off.**

The polarity is deliberately unusual (jumper fitted = off) and is silkscreened
`OFF SW`. It avoids inventing a slide-switch footprint whose dimensions I
could not verify, and it lets the mechanical team pick any switch and mount it
wherever the enclosure allows.

### 1.6 Battery measurement by divider, not only by fuel gauge

**[ARCHITECTURE CHANGE]** The MAX17048 is off-board (see
`COMPONENT_VERIFICATION.md` §B). In its place:

* `J4` — 5-way header for a MAX17048 breakout, on the sensor I²C bus.
* `R5`/`R6` = 470 k/470 k with `C6` = 100 nF — a plain divider from `VBAT`
  to `IO9`.

Sizing: 470 k/470 k draws 4.5 µA, which is acceptable next to the ESP32-S3's
deep-sleep current. It halves `VBAT`, so a full 4.2 V cell reads 2.10 V — well
inside ADC1's range with 12 dB attenuation and nowhere near the rail, so the
reading stays linear. The 100 nF sits at the ADC pin as a charge reservoir for
the SAR sampling capacitor (~30 pF), so the 235 kΩ source impedance does not
matter; the resulting 23 ms time constant is irrelevant for battery
monitoring.

A divider gives voltage, not state-of-charge. Voltage alone is a poor
fuel gauge on a Li-Po because of the flat mid-curve — hence the breakout
header for teams that want real SoC.

---

## 2. Four layers, not two

**[ARCHITECTURE CHANGE]** The diagram implies a simple carrier board. This is
a 4-layer board: signal / **GND plane** / **3V3 plane** / signal.

Reasons, in order of weight:

1. **The ECG front end needs an uninterrupted return path.** The AD8232
   amplifies a sub-millivolt biopotential by 1100 and carries 10 MΩ
   high-impedance nodes. Its datasheet's own layout guidance says "the use of
   a ground plane significantly improves the noise rejection of the system".
   On two layers, with 81 signal nets and 15 through-hole connectors, the
   bottom layer is necessarily cut to ribbons — there is no continuous
   reference left under the analog section.
2. **The module antenna needs a clean reference too**, and the same argument
   applies.
3. **Power distribution stops competing for signal space.** `3V3` alone has
   36 connections. As a plane it costs zero routing channels; as tracks it
   was the single largest routing failure in the 2-layer attempt (35 branches
   unrouted).
4. **Motor return current is separated from analog return current** by being
   on a different plane region entirely.

Cost: a 4-layer 100 × 70 mm prototype is roughly $2–5 more per board than
2-layer at prototype quantities. That is not a meaningful constraint for a
hackathon build, and it is the difference between an ECG channel that works
and one that does not.

**Measured evidence for the decision:** on two layers the router completed
about 50 of 81 signal nets and left `3V3` with 35 unrouted branches. On four
layers, with the same placement strategy, it completes 75 of 81 and both
power rails are planes.

---

## 3. Board size 100 × 70 mm

Not an aesthetic choice — it is set by part count. 15 through-hole connectors,
150 placed parts, an 18 × 25.5 mm module with 40 pads needing escape
corridors, and four fine-pitch parts needing fan-out envelopes.

An 80 × 60 mm attempt was built and measured first: through-hole connector pad
rows became walls across both signal layers, and the reachability analysis
showed the board split into disconnected regions (only 15,537 of 116,630
passable grid cells reachable from a module pad). At 100 × 70 mm the same
analysis gives 195,655 of 197,710 — effectively one connected region.

A production version on 4 layers with a microSD socket instead of a header,
0402 passives and SMD connectors would fit in roughly 45 × 35 mm.

---

## 4. ESP32-S3 module variant is not interchangeable

**`ESP32-S3-WROOM-1-N8R2` is mandatory.** Datasheet v1.8, Table 3-1 note b:
for modules with Octal SPI PSRAM (the `R8` and `R16V` variants), pins
**IO35, IO36 and IO37 are connected to the PSRAM and are not available**.

This design uses all three (ECG leads-off ×2 and ECG shutdown). Fitting an
N8R8 or N16R8 would short those signals into the PSRAM bus. The requirement
is stated in the BOM, in `GPIO_ASSIGNMENT.md`, and on the board silkscreen
via the part value.

`-N8R2` also keeps IO47/IO48 at 3.3 V. On `R16V` parts VDD_SPI is 1.8 V, so
those two pins are 1.8 V logic — they carry the motor and buzzer gate drives
here and must be 3.3 V.

---

## 5. Two I²C busses — resolving a real address conflict

The architecture diagram shows one shared bus carrying TMP117, LSM6DSOX,
AS5600 and MAX17048. **That bus cannot work as drawn:**

| Device | 7-bit address | Configurable? |
|---|---|---|
| TMP117 | 0x48 | yes — ADD0 selects 0x48/0x49/0x4A/0x4B |
| LSM6DSOX | 0x6A | yes — SA0 selects 0x6A/0x6B |
| AS5600 | **0x36** | **no — fixed** |
| MAX17048 | **0x36** | **no — fixed** |

AS5600 and MAX17048 collide, and neither can be moved. The diagram's own note
("Resolve address conflicts and verify pull-up voltage before finalizing the
schematic") anticipates this.

**[ARCHITECTURE CHANGE]** Resolution — two physically separate busses, using
both of the ESP32-S3's I²C controllers:

| Bus | Pins | Devices |
|---|---|---|
| **SENSOR** (I2C0) | SDA `IO15`, SCL `IO16` | TMP117 0x48, LSM6DSOX 0x6A, `J4` fuel-gauge breakout 0x36 |
| **ANGLE** (I2C1) | SDA `IO14`, SCL `IO42` | AS5600 0x36 (on board), `J6` for a second AS5600 |

0x36 now appears once per bus, which is legal.

### The second AS5600 is still a conflict, and is handled explicitly

The diagram says "one AS5600 per side if needed". Two AS5600s cannot share a
bus — the address is fixed and there is no select pin. `J6` therefore carries
the angle bus **plus a fifth pin wired to `IO3` through `R17` (0 Ω, fitted as
DNP)**, giving three options without committing to one:

1. Read the second sensor's **analog/PWM `OUT`** on `IO3` (ADC1_CH2, and
   PCNT-capable for PWM capture) — fit `R17`.
2. Put a **TCA9548A I²C multiplexer** on the angle bus externally.
3. Bit-bang a **third software I²C bus** on spare pins.

`R17` is unpopulated by default because `IO3` is a strapping pin (JTAG source
select). Driving it before reset is only a risk once eFuses are burned, but
making it opt-in costs nothing.

### I²C pull-up sizing — 4.7 kΩ, with the arithmetic

Not one pull-up pair per device (which would parallel down to ~1.2 kΩ and
exceed the spec sink current) — **one pair per bus**.

* Bus capacitance, sensor bus: 3 devices × ~10 pF + ~20 pF of track ≈ 50–60 pF.
* Rise time with 4.7 kΩ: t_r = 0.8473 × R × C = 0.8473 × 4700 × 60 p ≈ **239 ns**.
* I²C Fast-mode (400 kHz) allows t_r ≤ 300 ns → **passes**, with margin for
  Standard-mode's 1000 ns.
* Sink current when a device pulls low: 3.3 V / 4.7 kΩ = **0.70 mA**, far
  under the 3 mA specified minimum sink.

The angle bus adds a flying lead to `J6` (~100 pF/m, so ~20 pF for 200 mm),
giving ~50 pF — the same arithmetic holds. Both busses are pulled up to
**3V3**, matching every device's supply, so there is no level-shift question.

---

## 6. ECG analog front end

### 6.1 Topology follows the AD8232 datasheet, not the block diagram

The diagram shows "3 electrodes → AD8232 → ESP32 ADC". That is not a circuit.
The implemented design is the datasheet's **DC leads-off, three-electrode
configuration** (Rev. A Figure 50) with a driven RLD electrode (Figure 46),
a **two-pole high-pass filter** (Figure 55) and a low-pass gain stage.

| Block | Components | Value / result | Authority |
|---|---|---|---|
| Patient protection | `R18`, `R19` in series with LA and RA | **330 kΩ** | Datasheet: "place a resistor between the input pin and the electrode that is connected to the subject to ensure that the current flow never exceeds 10 µA. Calculate the value of this resistor to be equal to the supply voltage across the AD8232 divided by 10 µA." 3.3 V / 10 µA = 330 kΩ. **The datasheet's own example figures use 180 kΩ; 330 kΩ is the more conservative value its text demands, and this is a human-connected wearable.** |
| RLD output limit | `R20` in series with RLD | **330 kΩ** | Datasheet: "if the supply used is 3.0 V, this resistor should be greater than 330 kΩ" |
| Input bias / DC leads-off | `R21`, `R22` = 10 MΩ from +IN, −IN to +VS | enables per-electrode leads-off | Figure 50 |
| Leads-off mode select | `AC/DC` (pin 14) → GND | DC mode, 3-electrode | "To use this mode, connect the AC/DC pin to ground" |
| RLD integrator | `C17` = 1 nF between RLDFB and RLD | ~1 kHz crossover, ~26 dB loop gain at 50/60 Hz | "A good starting point is a 1 nF capacitor, which places the crossover frequency at about 1 kHz" |
| Reference | `R23`, `R24` = 10 MΩ divider + `C16` = 100 nF on REFIN | 1.65 V virtual ground | Figure 47; "the use of large resistors is recommended, such as 10 MΩ" |
| HPF pole 1 | `C18` = 220 nF (HPDRIVE→HPSENSE), `R25` = 10 MΩ (HPSENSE→IAOUT) | f = 100/(2π·R·C) = **7.2 Hz** | Figure 53 equation. Note the factor of 100 — the in-amp's gain modifies the usual RC formula |
| HPF pole 2 | `C19` = 220 nF (IAOUT→SW), `R26` = 1 MΩ (SW→REFOUT) | f = 1/(2π·R·C) = **0.72 Hz** | Figure 55 |
| LPF pole 1 + gain | `R27` = 470 k into OPAMP+, `C20` = 8.2 nF to REFOUT | ~41 Hz | designed, arithmetic below |
| LPF pole 2 + gain | `R28` = 100 k (OPAMP−→REFOUT), `R29` = 1 M (feedback), `C21` = 3.9 nF across `R29` | gain 1 + 1M/100k = **11**; pole 1/(2π·1M·3.9n) = **40.8 Hz** | designed |
| ADC interface | `R30` = 1 k, `C22` = 10 nF | low-impedance drive into ADC1_CH0 | — |
| Supply bypass | `C23` = 100 nF at pin 17, `C24` = 1 µF | — | "Place a 0.1 µF capacitor close to the supply pin. A 1 µF capacitor can be used farther away" |

**Total system gain = 100 (in-amp) × 11 (op-amp) = 1100.** With a 0.1–1 mV
abdominal ECG that is 110 mV–1.1 V peak-to-peak, centred on 1.65 V — well
matched to ADC1 with 12 dB attenuation (0–3.1 V) and clear of both rails.

**Pass band ≈ 7–40 Hz.** That is deliberately narrower than diagnostic ECG.

### 6.2 Why the pass band is narrow, and what that means

The datasheet's own 0.5 Hz "Cardiac Monitor Configuration" (Figure 66) is for
"monitoring the shape of the ECG waveform" and "assumes that the patient
remains relatively still". A belt worn by a walking pregnant woman is the
opposite case. The datasheet's exercise configuration (7 Hz two-pole HPF) is
explicitly for motion-artefact rejection, at the price that it "distorts the
ECG waveform significantly. Therefore, it is only suitable to determine the
heart rate, and not to analyze the ECG signal characteristics."

The project needs **maternal heart rate and trends**, not diagnostic
morphology, so motion-artefact rejection is the right trade. This is stated
plainly rather than implied: **this front end is a heart-rate channel, not a
diagnostic ECG.**

Every filter component is 0805 and reworkable. To move toward waveform
monitoring: raise `C18`/`C19` and drop the HPF corner, expand the LPF to
~150 Hz, and expect to fight motion artefact in firmware instead.

### 6.3 Op-amp stage is not a Sallen-Key

Two cascaded single poles (one at the non-inverting input, one across the
feedback resistor) rather than a Sallen-Key. Reasons: a Sallen-Key with a
gain of 11 has a Q that is sensitive to component tolerance and can peak or
oscillate; and the datasheet warns that the unbuffered two-pole HPF "exhibits
higher output impedance at the input of a subsequent low-pass filter, such as
with Sallen-Key filter topologies". The cascade is unconditionally stable and
its response is trivially predictable.

Interaction that is known and accepted: at 20 Hz the HPF's output impedance
is roughly `R26` ∥ X_C19 ≈ 35 kΩ, which adds to `R27` = 470 kΩ and pulls pole 1
from 41 Hz down to about 38 Hz. Under 10 % and in the harmless direction.

### 6.4 Controls brought out to GPIO instead of strapped

| Pin | Net | Default | Why |
|---|---|---|---|
| `SDN` (13) | `ECG_SDN` → `IO37` | `R31` 100 kΩ pull-up → **enabled** | Lets firmware shut the AFE down (<200 nA) between measurements; fails safe to on |
| `FR` (15) | `ECG_FR` → `IO39` | `R32` 100 kΩ pull-down → **disabled** | Fast restore cuts the multi-second settling after electrode attachment; fails safe to off |
| `LOD+` (12) | `ECG_LOD_P` → `IO35` | — | Per-electrode leads-off, so the app can say *which* electrode fell off |
| `LOD−` (11) | `ECG_LOD_N` → `IO36` | — | ditto |

Note the reference settling time: `R23`∥`R24` × `C16` × 5 = 5 MΩ × 100 nF × 5
= **2.5 seconds** after power-up or after leaving shutdown. Firmware must wait
before trusting the first reading.

---

## 7. Mechanical sensing

### 7.1 FSR divider = 10 kΩ, with the reasoning

FSR402 (assumed) is > 1 MΩ unloaded, ~100 kΩ at light touch, and falls to
~2 kΩ at full load. Belt pressure sits in the middle of that.

For a divider `Vout = 3.3 × Rf/(Rfsr + Rf)`, the best resolution is around
the geometric mean of the resistance band of interest: √(2 k × 100 k) ≈ 14 kΩ.
**10 kΩ** is the nearest sensible E-series value:

| FSR | Vout | Comment |
|---|---|---|
| 100 kΩ (light) | 0.30 V | clear of 0 V |
| 10 kΩ (mid) | 1.65 V | mid-scale |
| 2 kΩ (firm) | 2.75 V | clear of the rail |

Full ADC span used, no clipping at either end. Worst-case current 3.3 V/12 kΩ
= 275 µA per sensor, 1.1 mA for all four. `C29`–`C32` = 10 nF give a 100 µs
time constant (1.6 kHz), an appropriate anti-alias for ~100 Hz sampling.

**Would change if:** a different FSR is chosen — recompute as the geometric
mean of its useful band.

### 7.2 Load cell: excitation from AVDD is deliberate, not lazy

`J8` carries E+ → `3V3`, E− → `GND`, A+ → `INA+`, A− → `INA−`. The bridge is
excited from the same rail that powers everything else, which looks like a
noise mistake and is not: **the HX711 uses AVDD as its own ADC reference**, so
the measurement is ratiometric. Excitation-voltage variation cancels out. This
is why every HX711 module works this way.

`RATE` (pin 15) → GND selects **10 Hz** output rather than 80 Hz — lower noise,
and belt tension does not change quickly. `XI` → GND selects the on-chip
oscillator. `VFB` → AGND and `BASE` left open disable the internal regulator,
per the datasheet's "NC when not used" / "connect to AGND when not used".
Channel B inputs are tied to AGND rather than left floating.

`R37` for the stretch sensor is **10 kΩ as a placeholder only** — that sensor's
resistance range is unknown. See `REQUIRES_CONFIRMATION.md`.

### 7.3 Piezo conditioning — the part the block diagram glosses over

"Piezo → ADC" would damage the ESP32 sooner or later. A piezo film driven by a
fetal kick is a high-impedance source that can produce tens of volts
open-circuit. The chain:

| Component | Value | Purpose |
|---|---|---|
| `R38` | 10 MΩ across the element | Bleeds charge and sets the low-frequency corner. With a ~1.5 nF film, 1/(2π·10M·1.5n) ≈ 10 Hz — suits fetal movement (roughly 1–10 Hz) and limits open-circuit voltage build-up |
| `C34` | 100 nF **50 V** | AC couples, blocking the DC offset. The voltage rating is the point |
| `R39`, `R40` | 1 MΩ + 1 MΩ | Biases the coupled signal to mid-rail so the ADC sees both polarities |
| `R41` | 100 kΩ series | Limits current into the clamp and the ESP32's internal ESD diodes |
| `D5`, `D6` | 1N5819HW to `3V3` and from `GND` | Hard clamp at the ADC node. With `R41`, even a 100 V transient injects only ~1 mA — three orders of magnitude inside the diode's 1 A rating |
| `C35` | 10 nF | 160 Hz anti-alias with `R41` |

Clamp orientation is checked by the ERC (`D5` cathode must be on `3V3`, `D6`
anode on `GND`) because a reversed clamp is a dead short across the rail.

---

## 8. Alerts

### 8.1 Motor on `VBAT` with an optional ballast

`R45` is a 0 Ω 0805 in series with the motor's high side. It exists so the
motor's rail can be adapted without cutting tracks: many coin vibration
motors are rated 3.0 V and a full Li-Po at 4.2 V will shorten their life.

**Either** fit a motor rated for 4.2 V and leave `R45` at 0 Ω, **or** keep a
3 V motor and populate `R45` to drop the difference at the motor's rated
current. That requirement is in `REQUIRES_CONFIRMATION.md` because the motor
has not been chosen.

Driven low-side by `Q1` (AO3400A) with `R43` = 100 Ω gate series (slows the
edge, cuts radiated noise near the ECG channel) and `R44` = 100 kΩ gate
pull-down so the FET is off if `IO47` floats. `D7` (1N5819HW) is the flyback,
cathode to `MOTOR_P`. `C37` = 10 µF is local bulk so the motor's current step
is supplied locally rather than pulled through the shared rail.

### 8.2 Buzzer on 3V3, and it works either way

`J17` high side goes to `3V3` (not `VBAT`) because most 3 V magnetic buzzers
do not want 4.2 V. `D8` is a flyback for the inductive case.

If a **passive piezo transducer** is fitted instead, the same circuit drives
it from an LEDC PWM output on `IO48`; the flyback diode is simply never
forward-biased. No board change needed.

### 8.3 Two discrete LEDs instead of an RGB LED

**[ARCHITECTURE CHANGE]** The diagram lists "Status LED/RGB LED". Implemented
as `D3` (green, `IO45`) and `D4` (red, `IO46`), plus the charger's own `D1`
(charging) and `D2` (charge complete) which need no GPIO at all.

A discrete common-anode RGB needs three GPIOs and the pin budget has none
spare. A single-wire addressable RGB (WS2812B / SK6812) needs one pin, but
also **≥ 3.5 V**, which the 3V3 rail cannot supply; driving it from `VBAT`
would put a 3.0–4.2 V device on a 3.3 V logic pin. Not worth the risk for an
indicator.

`IO45` and `IO46` are both strapping pins, and the LED wiring is
strapping-safe: GPIO → resistor → LED anode, cathode → GND. At reset the pin
is high-impedance and the LED cannot conduct below its forward voltage, so the
internal weak pull-down holds both straps at their default 0.

---

## 9. GPIO allocation constraints

Two hard rules shaped the whole allocation (full table in
`GPIO_ASSIGNMENT.md`):

1. **ADC2 is unusable while the radio is active.** All 8 analog signals are
   therefore on ADC1, which is GPIO1–GPIO10 only. 8 of 10 channels used.
2. **IO35/36/37 are free only on quad-PSRAM parts** — hence the -N8R2
   requirement (§4).

Consequences worth noting:

* **Pin-JTAG (IO39–IO42) is given up.** Those four carry signals instead.
  Debugging uses the ESP32-S3's built-in USB-Serial-JTAG on IO19/IO20, which
  is a better debug path anyway.
* **microSD card-detect is not wired.** No pin was available. Firmware detects
  the card by SPI initialisation instead — a card that fails to respond is
  absent.
* **TMP117 `ALERT` is not wired to a GPIO** — pull-up plus test point only.
  The alert condition is readable over I²C by polling.

Nothing is left floating. Every one of the module's 41 pads is driven,
terminated, or brought to a test point; the ERC enforces this.

---

## 10. Grounding: one net, not split AGND/DGND

Single `GND` net and a single continuous plane. **Deliberately not split** —
see `GROUNDING_NOTES.md` for the full argument. Short version: a split plane
forces return current to detour around the split, and the resulting loop area
usually injects more noise into a high-impedance analog front end than the
split removes. Separation here is achieved by *placement* — the ECG block is
in the opposite corner from the motor driver and the antenna — not by cutting
copper.

An `AGND` supply symbol exists in the library and is intentionally unused, so
that anyone extending the design has to make that decision consciously.

---

## 11. microSD as a module header

**[ARCHITECTURE CHANGE]** `J18` is a 6-way header for a standard SPI microSD
breakout, rather than a microSD socket on the board.

Two reasons: no microSD socket land pattern could be verified from primary
documentation here (they are mechanically fussy — push-pull mechanisms,
shield tabs, card-edge keep-outs); and the architecture diagram itself
describes "a prototype carrier-board architecture using module headers", which
this matches. Pull-ups `R50` (CS) and `R51` (MISO) are 10 kΩ, within the SD
specification's recommended 10 k–100 k.

---

## 12. USB as a header, not a receptacle

**[ARCHITECTURE CHANGE]** `J2` is a 4-way header: `VBUS`, `D−`, `D+`, `GND`.
It feeds the charger and the ESP32-S3's native USB.

A USB-C receptacle would be better, but no USB-C land pattern could be
verified here, and a wrong receptacle footprint makes the board
unprogrammable. A short pigtail to a USB-C breakout works at USB 2.0
full-speed (12 Mbit/s). `J5` (UART: GND, 3V3, TXD0, RXD0, EN, IO0) is the
fallback programming path.

`D+`/`D−` are routed as an adjacent pair but **their differential impedance
has not been calculated** — see `REQUIRES_CONFIRMATION.md`. At full speed over
a few centimetres this is not usually a problem, and the UART header is there
if it is.

---

## 13. Protection — what is present and why each item earns its place

Deliberately not padded. Every protection component below has a specific
failure it prevents.

| Protection | Component | The failure it prevents |
|---|---|---|
| ECG patient current limit | `R18`, `R19`, `R20` = 330 kΩ | Fault current into a human, limited to < 10 µA per the datasheet's own rule |
| Piezo over-voltage | `R41` + `D5`/`D6` | Tens of volts from a piezo film reaching an ADC pin |
| Motor inductive kick | `D7` | Drain of `Q1` flying above `VBAT` at turn-off |
| Buzzer inductive kick | `D8` | Same, for a magnetic buzzer |
| FET fail-safe off | `R44`, `R47` = 100 kΩ | Motor or buzzer running at boot while `IO47`/`IO48` are high-impedance |
| SOS button | `R49` = 1 kΩ series + `C39` = 100 nF | ESD on a user-touchable button; also debounces |
| ADC input drive | `R30` = 1 kΩ + `C22` = 10 nF | ADC sampling glitches on the ECG output |
| Reset integrity | `R7` = 10 kΩ + `C10` = 1 µF | Brown-out mis-boot; `EN` must never float |
| Battery | *external PCM required* | Over-charge / over-discharge / over-current (§1.1) |

**Not added, and why:** no TVS array on the sensor headers (they are inside
the enclosure on short leads, and adding capacitance to the FSR dividers would
degrade them); no reverse-polarity FET on `VBUS` (the TP4056 has internal
reverse blocking — "No blocking diode is required due to the internal PMOSFET
architecture"); no fuse (the required protected pack already provides
over-current cut-off).

---

## 14. Placement and routing strategy

* **Zones follow the architecture diagram's blocks**, one zone per schematic
  sheet, so the board reads like the drawing.
* **ECG is in the far corner from the motor driver and the antenna** —
  the two noise sources it cannot tolerate. Roughly 30 mm from the antenna,
  and separated from the motor block by a plane region.
* **ECG nets are pinned to layer 1** wherever the router could manage it, so
  they sit directly above the layer-2 GND plane with no via discontinuities.
  `DRC_REPORT.md` lists any that needed the bottom layer instead.
* **The module antenna is flush with the top board edge**, with all copper —
  planes included — removed beneath it. Since an EAGLE polygon cannot carry a
  hole, both planes are drawn as an L that omits that corner.
* **Escape channels are reserved as component keep-outs** around the module's
  three pad rows. 36 signals leaving a 1.27 mm pitch need somewhere to go;
  this was the single biggest routing constraint on the board.
* **Fine-pitch parts get a splayed, staggered fan-out** before global routing.
  A 0.5 mm QFN cannot be escaped with a 0.25 mm track, and a via needs ~1.4 mm
  of room, so alternate stubs run on to a second radius.

---

## 15. Things I would do differently with more information

1. **Power-path charger** (MCP73871) instead of the TP4056, removing the
   charge-termination interaction entirely.
2. **Buck-boost regulator** instead of the LDO, so the 3V3 rail holds all the
   way to 3.0 V of cell voltage and the usable capacity increases.
3. **USB-C receptacle** with a verified land pattern.
4. **Relocate the TMP117 to a flex tail.** It is on the main board because
   that is where the architecture puts it, but skin temperature is not
   measurable from inside an electronics pod. A short flex with the TMP117 at
   the far end, against the skin, is the only way that channel means anything.
   The I²C bus is already brought to `J4`, so this is a small change.
5. **Second IMU on the thigh**, as the project's own alternatives list
   suggests, for fall detection with fewer false positives. It needs one more
   I²C address, which the LSM6DSOX's SA0 pin can provide (0x6B) with no board
   change beyond a connector.
