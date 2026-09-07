# ECG ANALOG FRONT END — DESIGN NOTE

> **This is not a medical device.** It is a prototype heart-rate channel for
> engineering evaluation. It has no galvanic isolation, no defibrillation
> protection, and no regulatory compliance work behind it. Read
> `REQUIRES_CONFIRMATION.md` item B2 before connecting it to a person.

The architecture diagram says "3 electrodes → AD8232 → ESP32 ADC". That is a
block, not a circuit. This note is the circuit, and why each value is what it
is.

Every value below traces to the *AD8232 Data Sheet Rev. A*. Where a value was
designed rather than copied, the arithmetic is shown.

---

## Signal chain

```
   J7.1 LA ──[R18 330k]──┬──────────────► +IN  (pin 2)
                         └──[R21 10M]──► +VS      (DC leads-off bias)

   J7.2 RA ──[R19 330k]──┬──────────────► −IN  (pin 3)
                         └──[R22 10M]──► +VS      (DC leads-off bias)

   J7.3 RL ◄─[R20 330k]───────────────── RLD  (pin 5)
                                          └──[C17 1n]── RLDFB (pin 4)

                   ┌──────────── AD8232 ────────────┐
   in-amp gain 100 │  IAOUT (19) ─┐                 │
                   │              │  two-pole HPF   │
   HPDRIVE (1) ──[C18 220n]──► HPSENSE (20)         │   pole 1: 7.2 Hz
   HPSENSE (20) ──[R25 10M]──► IAOUT (19)           │
   IAOUT (19) ──[C19 220n]──► SW (6)                │   pole 2: 0.72 Hz
   SW (6) ──[R26 1M]──► REFOUT (8)                  │
                   └─────────────────────────────────┘
                          │
                          ▼  SW node = HPF output
             ──[R27 470k]──┬──► OPAMP+ (7)              pole: ~41 Hz
                        [C20 8n2]
                           └──► REFOUT

             OPAMP− (9) ──[R28 100k]──► REFOUT          gain = 1 + 1M/100k = 11
             OPAMP− (9) ──[R29 1M]────► OUT (10)
             OPAMP− (9) ──[C21 3n9]───► OUT (10)        pole: 40.8 Hz

             OUT (10) ──[R30 1k]──┬──► ECG_OUT ──► ESP32 IO1 (ADC1_CH0)
                               [C22 10n]
                                  └──► GND

   Reference:  3V3 ──[R23 10M]──┬── REFIN (18)   →  REFOUT (8) = 1.65 V
                                │
               GND ──[R24 10M]──┤
                                │
                             [C16 100n]
                                │
                               GND

   Supply:     3V3 ──┬──[C23 100n]──GND   (at pin 17)
                     └──[C24 1u]────GND

   Control:    SDN  (13) ── ECG_SDN   ← IO37, R31 100k pull-up  → enabled
               FR   (15) ── ECG_FR    ← IO39, R32 100k pull-down → disabled
               AC/DC(14) ── GND                                  → DC leads-off
               LOD+ (12) ── ECG_LOD_P → IO35
               LOD− (11) ── ECG_LOD_N → IO36
               EP        ── GND (4 thermal vias)
```

---

## Supply rail — the one decision that can destroy the part

**The AD8232's absolute maximum supply is 3.5 V.** It is on the regulated
**3V3** rail and never sees `VBAT`, which reaches 4.2 V while charging.

The datasheet is explicit: *"It can also operate from rechargeable lithium-ion
batteries, but the designer must take into account that the voltage during a
charge cycle may exceed the absolute maximum ratings of the AD8232. To avoid
damage to the part, use a power switch or a low power, low dropout
regulator."*

The architecture diagram does not say which rail feeds it. Wiring it to `VBAT`
would work on the bench and destroy the part the first time someone plugged in
a charger.

---

## Patient protection — 330 kΩ, and why not the datasheet's 180 kΩ

The datasheet's example circuits (Figures 62, 64, 66) all show 180 kΩ series
resistors. Its *Input Protection* text says something stricter:

> *"As a safety measure, place a resistor between the input pin and the
> electrode that is connected to the subject to ensure that the current flow
> never exceeds 10 µA. Calculate the value of this resistor to be equal to the
> supply voltage across the AD8232 divided by 10 µA."*

3.3 V / 10 µA = **330 kΩ**. The 180 kΩ figures correspond to the 5 mA
continuous-current limit the part itself can survive, not the 10 µA
subject-safety rule. For a wearable in contact with a pregnant woman, the
stricter number is the right one, so `R18`, `R19` and `R20` are all 330 kΩ.

For the driven electrode the datasheet gives the same number independently:
*"if the supply used is 3.0 V, this resistor should be greater than 330 kΩ to
account for component and supply variations."* — hence `R20` = 330 kΩ.

Cost of the choice: 330 kΩ against the in-amp's 10 kΩ input resistance is a
small gain error, and it raises source impedance slightly. Both are
irrelevant next to a factor-of-1.8 improvement in fault-current limiting.

---

## Three-electrode configuration with DC leads-off

Per datasheet Figure 50 and the *DC Leads Off Detection* section:

* `R21`, `R22` (10 MΩ) pull `+IN` and `−IN` up to `+VS`;
* `AC/DC` (pin 14) is tied to **GND**, selecting DC mode — *"To use this mode,
  connect the AC/DC pin to ground."*
* the third electrode is driven by `RLD`, which is what keeps the subject
  inside the in-amp's common-mode range.

The advantage of DC mode over AC mode is per-electrode reporting: *"it is
possible to indicate which electrode is disconnected"*, via `LOD+` and `LOD−`
separately. Both go to GPIOs, so the app can say *"the left electrode has come
off"* rather than just *"signal lost"* — worth two pins on a wearable that a
user puts on themselves.

## Right-leg drive

Datasheet Figure 46 and the *Right Leg Drive Amplifier* section: the inverting
input of A2 is fed internally from the common-mode signal through a 150 kΩ
resistor, so the only external component needed is the integrator capacitor.

*"An integrator can be built by connecting a capacitor between the RLD FB and
RLD terminals. A good starting point is a 1 nF capacitor, which places the
crossover frequency at about 1 kHz... This configuration results in about
26 dB of loop gain available at a frequency range from 50 Hz to 60 Hz for
common-mode line rejection."*

`C17` = **1 nF**, exactly that. 26 dB of mains rejection at 50 Hz is the
single most useful thing this circuit does for a device used near mains
wiring.

---

## Reference / virtual ground

Datasheet Figure 47. `R23`/`R24` = 10 MΩ each from `3V3` and `GND` set `REFIN`
to mid-supply; the internal buffer presents it on `REFOUT`, which is the
analog reference for the whole signal chain.

*"To limit the power consumption of the voltage divider, the use of large
resistors is recommended, such as 10 MΩ... use a capacitor in parallel with
the lower resistor on the divider for additional filtering."*

`C16` = 100 nF does that filtering. The consequence has to be respected:

> Settling time = 5 × (R23 ∥ R24) × C16 = 5 × 5 MΩ × 100 nF = **2.5 seconds**

**Firmware must wait 2.5 s after power-up — and after leaving `SDN` shutdown —
before the first reading means anything.** The datasheet notes that shutdown
does not discharge this capacitor, so a wake from shutdown settles faster in
practice, but 2.5 s is the number to design to.

Total divider current: 3.3 V / 20 MΩ = 165 nA. Negligible even in deep sleep.

---

## High-pass filter — two poles, and the factor of 100

The DC-blocking amplifier is not an ordinary RC. Its corner is *"100 times
higher than is typically expected from a single-pole filter"* because *"the
typical filter cutoff equation is modified by the gain of 100 of the
instrumentation amplifier"*:

```
                 100
    f_-3dB  =  ─────────
               2π · R · C
```

Getting this wrong by 100× is an easy mistake, so both poles are shown
worked out:

**Pole 1** — the DC-blocking integrator (`C18` between `HPDRIVE` and
`HPSENSE`, `R25` between `HPSENSE` and `IAOUT`):

```
    f1 = 100 / (2π × 10 MΩ × 220 nF) = 100 / 13.82 = 7.2 Hz
```

**Pole 2** — passive AC coupling at the in-amp output (`C19` from `IAOUT` to
`SW`, `R26` from `SW` to `REFOUT`). This one is an ordinary RC, no factor of
100:

```
    f2 = 1 / (2π × 1 MΩ × 220 nF) = 0.72 Hz
```

Topology is datasheet Figure 55. Note that `C19`'s far side goes to the **`SW`
pin**, not straight to the filter output: *"Note that the right side of C2
connects to the SW terminal."* `SW` is the fast-restore switch terminal, and
routing the AC-coupling network through it lets the internal 10 kΩ path shunt
`R26` during fast restore, cutting the recovery time.

### Sanity check against the datasheet's own examples

| Datasheet circuit | Stated corner | Components | Check |
|---|---|---|---|
| Fig. 62, single pole | 7 Hz | 10 MΩ, 0.22 µF | 100/(2π·10M·0.22µ) = 7.24 Hz ✓ |
| Fig. 64, two poles | 7 Hz | 10 MΩ + 0.22 µF, 100 kΩ + 0.22 µF | 7.24 Hz and 7.24 Hz ✓ |
| **This design** | **7.2 / 0.72 Hz** | 10 MΩ + 220 nF, 1 MΩ + 220 nF | as above |

The formula reproduces the datasheet's own numbers, which is the point of
checking it.

---

## Low-pass filter and gain — designed, not copied

The datasheet's example circuits use a Sallen-Key here. This design uses two
cascaded single poles instead, for two reasons the datasheet itself raises:

1. A Sallen-Key configured for a gain of 11 has a Q that depends on component
   ratios and can peak or oscillate with real tolerances.
2. *"if this passive network is not buffered, it exhibits higher output
   impedance at the input of a subsequent low-pass filter, such as with
   Sallen-Key filter topologies."* The two-pole HPF ahead of it is exactly
   such an unbuffered network.

The cascade is unconditionally stable and its response is trivially
predictable.

**Pole A** — series `R27` into `OPAMP+`, `C20` to `REFOUT`:

```
    f_A = 1 / (2π × 470 kΩ × 8.2 nF) = 41.3 Hz
```

**Pole B** — `C21` across the feedback resistor `R29`:

```
    f_B = 1 / (2π × 1 MΩ × 3.9 nF) = 40.8 Hz
```

**Gain** — non-inverting, referenced to `REFOUT`:

```
    G = 1 + R29/R28 = 1 + 1 MΩ/100 kΩ = 11
```

**Total system gain = 100 (in-amp) × 11 = 1100.**

### The source-impedance interaction, accounted for

The HPF's output impedance at 20 Hz is roughly `R26` in parallel with `C19`'s
reactance:

```
    X_C19 (20 Hz) = 1/(2π × 20 × 220n) = 36 kΩ
    Z_out ≈ 1 MΩ ∥ 36 kΩ ≈ 35 kΩ
```

That adds to `R27`, moving pole A:

```
    f_A' = 1 / (2π × (470k + 35k) × 8.2n) = 38.4 Hz
```

A 7 % shift, in the harmless direction. `R27` was chosen large (470 kΩ) partly
so this interaction stays small — a 100 kΩ resistor there would have shifted
the pole by 35 %.

---

## Resulting response and dynamic range

| | Value |
|---|---|
| Pass band | ≈ **7 – 40 Hz** |
| Roll-off below 7 Hz | 40 dB/decade to 0.72 Hz, 20 dB/decade below |
| Roll-off above 40 Hz | 40 dB/decade |
| Total gain in band | **1100** |
| Output centre | `REFOUT` = 1.65 V |
| Input 0.1 mV pk-pk (weak abdominal) | 110 mV pk-pk → 1.595 – 1.705 V |
| Input 1.0 mV pk-pk (strong) | 1.1 V pk-pk → 1.10 – 2.20 V |
| ESP32-S3 ADC1, 12 dB attenuation | 0 – 3.1 V |

Both cases sit comfortably inside the ADC range with margin at each rail, so
the signal never clips and the reading stays linear.

Recommended sampling: **250 Hz**. That is 6× the 40 Hz corner, and the
40 dB/decade roll-off puts anything above 125 Hz (the Nyquist limit) more than
20 dB down before `R30`/`C22` add further attenuation.

---

## Why the pass band is narrow — the honest trade-off

7–40 Hz is deliberately narrower than diagnostic ECG (0.05–150 Hz). This is
the central design trade in the whole subsystem, so it is stated plainly.

The datasheet distinguishes its own configurations:

* **Cardiac Monitor (Fig. 66, 0.5 Hz HPF / 40 Hz LPF)** — *"designed for
  monitoring the shape of the ECG waveform. It assumes that the patient
  remains relatively still during the measurement, and therefore, motion
  artifacts are less of an issue."*
* **Exercise / HR at the hands (Fig. 64, 7 Hz HPF / 24 Hz LPF)** — for a
  moving subject, and *"only suitable to determine the heart rate, and not to
  analyze the ECG signal characteristics."*

A belt worn by a walking pregnant woman is the second case, not the first. The
project needs **maternal heart rate and trends**, so motion-artefact rejection
is worth more than waveform fidelity.

**So: this is a heart-rate channel, not a diagnostic ECG.** It will give
reliable beat detection and HR variability on a moving subject. It will *not*
give clinically interpretable ST segments or P-wave morphology, and nothing in
this project should claim otherwise.

### If you want to move toward waveform monitoring

All the filter components are 0805 and reworkable:

| Change | Effect |
|---|---|
| `C18`, `C19` → 2.2 µF | HPF poles to 0.72 Hz and 0.072 Hz — approaches the datasheet's cardiac-monitor response, but needs physically large capacitors at high-impedance nodes, which brings its own leakage problems |
| Better: adopt datasheet **Figure 56** (three extra components, `R_COMP` = 0.14 × R1) | *"allows lower cutoff frequency with lower R and C values"* — the topology ADI themselves use for the 0.5 Hz cardiac monitor |
| `C20` → 2.2 nF, `C21` → 1 nF | LPF to ~150 Hz |
| — | expect to fight motion artefact in firmware instead: adaptive filtering keyed off the LSM6DSOX, which is already on the board and is exactly what the project's own notes propose |

---

## Layout compliance

The datasheet's *Layout Recommendations* section, item by item:

| Requirement | What the board does |
|---|---|
| *"Keep all of the connections between high impedance nodes as short as possible"* | `ECG_HPSENSE`, `ECG_IAOUT`, `ECG_SW`, `ECG_REFIN`, `ECG_REFOUT` all stay inside Zone 3 with their passives placed against `U7`'s fan-out |
| *"keep the input traces symmetrical and length matched"* | `R18` and `R19` are placed symmetrically about the `+IN`/`−IN` axis, same orientation, same distance |
| *"Place safety and input bias resistors in the same position relative to each input"* | `R18`/`R19` (safety) and `R21`/`R22` (bias) are mirror-image pairs |
| *"the use of a ground plane significantly improves the noise rejection"* | Layer 2 is a solid, unbroken GND plane 0.36 mm below the ECG tracks. Not split — see `GROUNDING_NOTES.md` |
| *"Place a 0.1 µF capacitor close to the supply pin. A 1 µF capacitor can be used farther away"* | `C23` = 100 nF adjacent to pin 17, `C24` = 1 µF nearby |

Plus, from the architecture diagram's own note ("keep analog path short /
quiet"):

* `U7` is in the opposite corner of the board from the motor driver
  (Zone 6) and roughly 45 mm from the module antenna;
* the electrode connector `J7` is on the right board edge immediately beside
  `U7`, so the unprotected high-impedance run is about 5 mm;
* ECG nets are pinned to layer 1 wherever the router managed it, so they sit
  directly over the plane with no via discontinuities. Any that had to use
  layer 16 are listed in `DRC_REPORT.md`.

---

## Firmware requirements this circuit imposes

1. **Wait 2.5 s** after power-up, or after releasing `SDN`, before trusting a
   reading. The `REFIN` network needs it.
2. **Sample `IO1` (ADC1_CH0) at 250 Hz.** Use ADC1 — ADC2 is unusable while
   the radio is on.
3. **Read `LOD+` (`IO35`) and `LOD−` (`IO36`) before every measurement.**
   Either high means an electrode is off and the data is meaningless. Report
   *which* one to the user.
4. **Drive `FR` (`IO39`) high for ~100 ms after attaching electrodes**, then
   low. This is what fast restore is for — without it the filters take
   several seconds to settle after the step.
5. **Pull `SDN` (`IO37`) low between measurements** to save ~170 µA. Remember
   the 2.5 s settling on wake.
6. **Do not run the vibration motor while sampling ECG.** The board separates
   them physically and the loop is kept small, but a motor is a motor. Gate
   the two in firmware.
7. **Expect a mains-frequency residual.** RLD gives ~26 dB of rejection at
   50/60 Hz; the 40 Hz low-pass gives more. If it is still visible, a notch in
   firmware is cheaper than a board change.
