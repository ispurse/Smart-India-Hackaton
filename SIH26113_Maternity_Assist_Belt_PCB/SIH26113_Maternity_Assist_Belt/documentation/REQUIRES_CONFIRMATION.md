# REQUIRES CONFIRMATION — SIH26113 Maternity Assist Belt

Open items only. Everything not listed here was verified against primary
documentation — see `COMPONENT_VERIFICATION.md`.

Ordered by consequence: **BLOCKING** items can damage hardware or a person if
got wrong; **HIGH** items change a component value or a footprint; **MEDIUM**
items affect performance; **LOW** items are cosmetic or convenience.

---

## BLOCKING — resolve before powering the board

### ☐ B1. The Li-Po cell at `J1` must have integrated protection

**There is no battery protection circuit on this board.**

The architecture diagram said "TP4056 **protected** module". A commercial
TP4056 module carries DW01A + FS8205A protection alongside the charger. This
design uses the TP4056 as a bare IC, so that protection is absent.

**Update — the blocker on adding it on-board is now half-cleared:**

| Part | Status |
|---|---|
| **DW01A** protection controller | ✅ **pinout VERIFIED** from the primary datasheet — *DW01A Rev. 1.0, DW01A-DS-10_EN, JUN 2009 (FSC)*, §6 "Pin Configuration": **1 = OD** (MOSFET gate, discharge control), **2 = CS** (current sense input / charger detect), **3 = OC** (MOSFET gate, charge control), **4 = TD** (test pin, reduces delay time), **5 = VCC** (supply, through a resistor R1), **6 = GND**. SOT-23-6. Thresholds: overcharge 4.300 ±0.050 V, release 4.100 ±0.050 V, overdischarge 2.40 ±0.100 V, release 3.0 ±0.100 V, overcurrent 150 ±30 mV. |
| **FS8205A** dual N-FET switch | ❌ **pinout STILL NOT VERIFIED.** Only distributor listings and aggregator pages were reachable; no manufacturer pin table. Sources disagree on whether the drains are internally common and on which pins carry S1/S2. |

**So the circuit still cannot be added responsibly** — half a verified pinout
is not a protection circuit, and the FS8205A is the part that actually carries
the cell current. Guessing on it is not an acceptable risk.

**Note also** that adding this on-board is a **major** change, not a drop-in:
the FS8205A switches the cell's **negative** terminal, so `J1` pin 2 stops
being system `GND` and becomes a separate `BATT−` node. That re-defines the
ground reference at the battery connector and touches the netlist, the plane
connection and the routing. It would be documented as an architecture change
before being done, not slipped in.

**What to confirm:** the cell or pack fitted to `J1` has an integrated
protection circuit module (PCM) providing over-charge, over-discharge and
over-current cut-off. Nearly all 1S Li-Po cells sold for prototyping do; the
tell is a small PCB under the tape at the terminal end. **An unprotected cell
on this board is a fire risk.**

**Also confirm the JST polarity.** `J1` pin 1 = `VBAT` (+), pin 2 = `GND` (−).
JST PH pigtails are not consistently wired between suppliers — check with a
meter before the first connection, not after.

### ☐ B2. ECG electrical safety — this is not a medical device

The ECG channel connects to a human being. What the board does provide:

* 330 kΩ in series with each electrode (LA, RA), limiting fault current to
  < 10 µA at 3.3 V, per the AD8232 datasheet's own rule;
* 330 kΩ in series with the driven RLD electrode;
* a battery-only supply when USB is unplugged.

What it does **not** provide:

* **no galvanic isolation** between the subject and the rest of the circuit;
* **no defibrillation protection** (no gas-discharge tubes, no neon lamps,
  no BAV199-class clamps — the datasheet's own recommendation for that case);
* **no mains isolation while USB is connected.** With `J2` plugged into a
  mains-powered USB supply, the subject is galvanically connected to that
  supply's secondary through 330 kΩ.

**What to confirm:** that use is limited to bench evaluation with informed
participants, that **the board is battery-powered with USB disconnected
whenever electrodes are attached to a person**, and that nobody presents it as
a medical device. No IEC 60601-1 or 60601-2-47 compliance work has been done
and none is claimed.

### ☐ B3. Vibration motor voltage rating vs. `R45`

`R45` is a 0 Ω 0805 in series with the motor's high side, which is on `VBAT`
(3.0 – 4.2 V).

**What to confirm:** the motor's rated and absolute-maximum voltage.

* Motor rated for ≥ 4.2 V → leave `R45` at 0 Ω.
* Motor rated 3.0 V (most coin ERM types) → **populate `R45`** to drop the
  difference at the motor's rated current. For a 3.0 V / 100 mA motor at
  4.2 V that is (4.2 − 3.0)/0.1 = 12 Ω, and check the resistor's power
  rating: 0.1² × 12 = 120 mW, so an 0805 at 125 mW is marginal — use two 24 Ω
  in parallel, or a 1206.

Also confirm stall current: `Q1` (AO3400A, 5.7 A) and the 0.50 mm motor track
(≈ 1.45 A at 10 °C rise, 1 oz copper) both have generous margin over a typical
100 mA coin motor, but a large motor would need checking — coin ERM stall
current can be 3–4× the running figure.

---

## HIGH — resolve before ordering the PCB

### ☐ H1. MAX17048 fuel gauge — not on the board

analog.com and every distributor mirror tried were unreachable or bot-blocked
from this network, so **neither the MAX17048's pinout nor its land pattern
could be verified**. It is therefore not placed. Both of its packages are also
awkward for a hackathon build (an 8-bump 0.9 × 1.7 mm WLP is not
hand-assemblable at all).

**Provided instead:** `J4`, a 5-way header (`VBAT`, `GND`, `3V3`, `SDA`,
`SCL`) on the sensor I²C bus for an off-the-shelf breakout, plus
`R5`/`R6`/`C6` — a 470 k/470 k divider to `IO9` giving battery voltage
regardless.

**What to confirm:** whether you want the gauge at all. If yes, either use a
breakout on `J4` (recommended — SparkFun and Adafruit both make one), or
obtain the datasheet, verify the TDFN-8 land pattern, and add it to the
library. Note the breakout will sit at **0x36 on the sensor bus**, which is
already reserved for it and does not clash there.

### ☐ H2. Abdominal stretch sensor — `R37` is a placeholder

`R37` = 10 kΩ is **a placeholder, not a design value.** The correct value is
roughly the geometric mean of the chosen sensor's useful resistance band, so
that the divider centres its output at mid-rail — the same method used for the
FSRs in `DESIGN_ASSUMPTIONS.md` §7.1.

**What to confirm:** the sensor's part number and its resistance at minimum
and maximum extension. Then set `R37` = √(R_min × R_max) and re-check that
neither extreme clips against a rail. It is a single 0805, so this is a
reworkable change, not a re-spin.

### ☐ H3. Load cell — bridge resistance and sensitivity

The board excites the bridge from `3V3` via `J8` (E+ = pin 1, E− = pin 2,
A+ = pin 3, A− = pin 4) and reads it on HX711 channel A at gain 128 (±20 mV
full scale, ratiometric to AVDD).

**What to confirm:**

* **Bridge resistance** — affects the power budget. 350 Ω draws 9.4 mA (the
  worst case already budgeted); 1 kΩ draws 3.3 mA.
* **Sensitivity in mV/V** — determines whether gain 128 is right. A 1 mV/V
  cell at 3.3 V excitation gives 3.3 mV full scale, comfortably inside ±20 mV.
  A 2 mV/V cell gives 6.6 mV, still fine. Above ~6 mV/V, drop to gain 64.
* **Wire colours.** Do **not** assume the usual red/black/white/green
  convention — it is not universal. Identify E+/E− by measuring the highest
  resistance pair (bridge input) and A+/A− by the remaining pair.

### ☐ H4. Tactile switch footprint (`SW2`, `SW3`, `SW4`)

`TACT-6X6-THT` is the de-facto standard 6 × 6 mm through-hole tactile
geometry: 4 leads on a **6.5 × 4.5 mm grid**, 1.0 mm drill, leads 1–2 and 3–4
internally common (TL1105 / B3F-10xx family).

**What to confirm:** the chosen vendor part actually uses that grid. Some
6 × 6 mm switches use 4.5 × 6.5 (transposed) or are 2-lead. Check the drawing
before ordering the PCB — a transposed switch will not fit.

### ☐ H5. ESP32-S3 module variant — `-N8R2` is not optional

**Fit `ESP32-S3-WROOM-1-N8R2`. Do not substitute N8R8 or N16R8.**

Datasheet v1.8 Table 3-1 note b: on Octal-SPI-PSRAM modules (`R8`, `R16V`),
**IO35/IO36/IO37 are connected to the PSRAM and unavailable**. This design uses
all three for ECG leads-off and shutdown. Fitting an octal-PSRAM part shorts
those signals into the PSRAM bus.

`-N8R2` also keeps VDD_SPI at 3.3 V, so IO47/IO48 (motor and buzzer gate
drives) are 3.3 V logic. On `R16V` parts they are 1.8 V.

### ☐ H6. Fabricator must support 5 mil / 0.127 mm trace and gap

**Measured minimum copper clearance anywhere on the board: 0.130 mm.**
Minimum track: 0.15 mm (fine-pitch escapes only; 0.20 mm signal, 0.50 mm
power elsewhere). Minimum drill: 0.30 mm. Four copper layers.

The tight spots are the fine-pitch fan-outs. A 0.5 mm-pitch QFN cannot be
escaped at 0.15 mm / 0.15 mm - there is not enough room between the pads,
which is also why the escape tracks are 0.15 mm rather than 0.20 mm.
Everywhere else the board keeps 0.154 mm or better track-to-track.

**What to confirm:** the chosen fabricator quotes **5 mil (0.127 mm) trace
and gap on 4 layers**. JLCPCB, PCBWay and most others do, but it is often a
non-default option that has to be selected - the default is frequently 6 mil
(0.152 mm), which this board would fail on those fan-outs. The per-layer
measured minima are printed in `DRC_REPORT.md`; quote the 0.130 mm figure.

---

## MEDIUM — verify before or during bring-up

### ☐ M1. ESP32-S3-WROOM-1 EPAD land position

All 40 signal pads are verified against Espressif's Fig. 11-1 land pattern,
including the pin-1 datum (7.49 mm below the antenna edge), so **the module
will solder correctly**.

The exposed thermal pad is emitted as a single conservative 3.4 mm land at
(−1.25, −2.5) relative to the footprint origin, plus 9 plated 0.3 mm vias.
Espressif's figure sub-divides that region into a 3 × 3 copper array on a
3.7 mm span; the simplification is electrically identical (it is all GND), and
the land was deliberately made **smaller** than the module's actual pad so it
cannot encroach on the signal lands.

**What to confirm:** open the footprint in Fusion against Espressif's
downloadable land-pattern source file (linked from datasheet §11.1) and check
the EPAD land sits within the module's exposed metal. Worst case if it is
offset by ~1 mm: slightly worse thermal contact. It cannot cause a short.

### ☑ M2. USB differential pair impedance — **RESOLVED, no action needed**

**Calculated. See `USB_PAIR_ANALYSIS.md` for the full arithmetic.**

The pair is **≈ 165 Ω differential, not 90 Ω — 83 % high.** The two nets were
routed as ordinary signals, not as a coupled pair: measured closest
edge-to-edge gap is **0.806 mm** (2.24 × the 0.36 mm dielectric height), at
which spacing the coupling term collapses to 5.6 % and you simply have two
independent 87 Ω microstrips.

**It is nevertheless not a functional risk.** The ESP32-S3's built-in
USB-Serial-JTAG is **Full Speed only (12 Mbit/s)**. One-way delay over the
44 mm route is **255 ps**; the conservative critical length at the fastest
edge USB FS permits (4 ns) is **115 mm**. The trace is electrically short by
**2.6×**, so it is a lumped interconnect and the mismatch does not produce
reflections. Length skew is 0.8 mm = **5 ps**.

**If you ever need 90 Ω** (i.e. an external High-Speed PHY): **0.40 mm wide,
0.16 mm gap, both traces on layer 1 for the whole run.** Narrower widths
cannot reach 90 Ω on this stack-up at any buildable gap — you have to *widen*
the traces to lower Z₀ first. Expect it to displace other nets from the left
escape channel.

**One real observation found while measuring this:** both nets change layers,
so their reference plane changes from the `GND` plane (L2) to the `3V3` plane
(L15). At 12 Mbit/s the 0.71 mm interplane capacitance across 70 cm² handles
the return current easily. **It would matter at High Speed.**

### ☐ M3. Buzzer type

The circuit drives `J17` low-side from `3V3` through `Q2`, with `D8` as a
flyback.

**What to confirm:** which type is fitted, because firmware differs.

* **Active magnetic buzzer** (has its own oscillator) — drive `IO48` as a
  simple on/off. `D8` is essential.
* **Passive piezo transducer** — drive `IO48` with LEDC PWM at the
  transducer's resonant frequency (typically 2–4 kHz). `D8` is harmless.

Confirm its current draw too; 30 mA is budgeted.

### ☐ M4. Piezo film capacitance vs. `R38`

`R38` = 10 MΩ across the element sets the low-frequency corner at
1/(2π · 10 M · C_film). At an assumed ~1.5 nF that is ≈ 10 Hz, which suits
fetal movement (roughly 1–10 Hz).

**What to confirm:** the film's capacitance. If it is much larger (a big
element can be 10 nF or more) the corner drops to ~1.6 Hz, which is fine or
even better. If much smaller, the corner rises and low-frequency movement is
attenuated — reduce `R38`, or accept the loss.

`C34` **must be rated ≥ 50 V** (it is specified `100n/50V` in the BOM), because
a piezo film's open-circuit transient reaches tens of volts.

### ☑ M5. AS5600 3.3 V-mode supply strapping — **RESOLVED, design is correct**

**Confirmed from the primary datasheet.** *AS5600 Datasheet, ams-OSRAM,
[v1-06] 2018-Jun-20*, page 9, states verbatim:

> "In 3.3V operation, the VDD5V and VDD3V3 pins must be tied together. VDD is
> the voltage level present at the VDD5V pin."

That is exactly what the board does: `VDD5V` (pin 1) and `VDD3V3` (pin 2) are
both tied to `3V3`. **No change required.**

Decoupling also matches the datasheet's per-pin instructions (page 3): pin 1
"requires 100nF decoupling capacitor" → `C14` = 100 nF; pin 2 "requires an
external 1-μF decoupling capacitor in 5V mode" → `C15` = 1 µF, which is
harmless and beneficial in 3.3 V mode.

**Two useful details found in the same document while confirming this** — see
M6 and L5 below.

### ☐ M6. Magnet for the AS5600

The AS5600 measures the angle of a diametrically-magnetised on-axis magnet.
**No magnet mount exists on this PCB** — it is a mechanical-design item.

**What to confirm:** magnet type (diametric, typically 6 mm × 2.5 mm NdFeB),
its air gap (0.5 – 3 mm), and that it is centred over the IC within about
0.25 mm.

> **How to set the air gap properly** (datasheet [v1-06] page 20). The AS5600
> runs closed-loop Automatic Gain Control, and *"for the most robust
> performance, the gain value should be in the center of its range. The airgap
> of the physical system can be adjusted to achieve this value."*
>
> **In 3.3 V mode the AGC range is 0–128 counts, not 0–255** — so **aim for an
> AGC reading of ≈ 64**, not 128. Read the `AGC` register over I²C and adjust
> the air gap until it centres. Also check the `STATUS` register: `MH` = magnet
> too strong, `ML` = magnet too weak, `MD` = magnet detected. This turns magnet
> mounting from guesswork into a measurement. If the AS5600 needs to be at the belt's rail joint rather than on the
main board, move it to a flying lead on `J6` instead — the angle bus is
already brought out there.

### ☐ M7. TMP117 measures pod temperature, not skin temperature

`U4` is on the main board because that is where the architecture diagram puts
it. **Inside an electronics pod it measures the pod's internal temperature**,
which is influenced by the LDO, the charger and the ESP32.

**What to confirm:** whether skin temperature is actually required. If it is,
relocate the TMP117 to a short flex tail with the sensor against the skin —
the sensor I²C bus is already brought out on `J4`. This is a real measurement
problem, not a layout nicety.

---

## LOW

### ☐ L1. Mounting holes are not at four corners

`H1` (3, 3), `H2` (97, 3), `H4` (97, 67) are corners. **`H3` is at
(2.6, 42)** — mid-left edge, not the top-left corner — because the top-left
corner is inside the module's antenna keep-out and a plated hole there would
detune the antenna.

**What to confirm:** the enclosure design accepts that pattern. If it must be
four true corners, move the antenna to a different edge and re-run
`scripts/generate_board.py`.

### ☐ L2. `J3` on/off switch polarity is inverted

`R4` pulls the LDO's `EN` up to `VBAT`, so **the default state is ON**, and
**closing a switch across `J3` turns the board OFF**. Silkscreened `OFF SW`.

**What to confirm:** whoever wires the enclosure switch knows this. It is
deliberate — it avoids inventing an unverified slide-switch footprint — but it
is the opposite of what most people expect.

### ☐ L3. Silkscreen legibility at 1.0 mm

Reference designators use EAGLE's vector font at 0.8 – 1.1 mm. Most fabs hold
0.8 mm text with a 0.15 mm stroke; some do not.

**What to confirm:** your fab's minimum silkscreen height and line width.
Increase the text sizes in `scripts/lib_defs.py` if needed.

### ☐ L5. AS5600 OTP programming needs a temporary 10 µF at `VDD3V3`

Only relevant **if** you ever permanently program the AS5600's non-volatile
memory (to burn in a start/stop angle range rather than doing that in
firmware).

*AS5600 Datasheet [v1-06]*, page 20: programming can be done in 5 V mode, or
in 3.3 V mode *"using a minimum supply voltage of 3.3V and a 10 μF capacitor
at the VDD3V3 pin to ground. This 10 μF capacitor is needed only during the
programming of the device."*

The board fits `C15` = **1 µF** on `VDD3V3`, which is the datasheet's value
for normal operation. **It is not enough for OTP burning.**

**What to confirm:** whether you need OTP at all. Almost certainly not —
scaling and zeroing the angle in firmware is reversible and OTP is not. If you
do, tack a 10 µF across `C15` temporarily, program, then remove it. No board
change.

### ☐ L4. Supplier part numbers are absent from the BOM

Deliberate. Distributor stock could not be checked from this environment, and
a fabricated SKU is worse than a blank field. Manufacturer part numbers come
from the datasheet ordering guides and are correct.

**What to confirm:** availability and pricing at your distributor,
particularly for the AD8232 (occasionally allocated) and the LSM6DSOX.

---

## Resolved during design — recorded so they are not re-opened

| Item | Resolution |
|---|---|
| I²C address clash: AS5600 and MAX17048 are both fixed at 0x36 | Two physically separate busses. AS5600 on the angle bus (I2C1), fuel-gauge breakout on the sensor bus (I2C0). `DESIGN_ASSUMPTIONS.md` §5 |
| Second AS5600 also clashes | `J6` carries the angle bus plus a fifth pin to `IO3` via `R17` (0 Ω, DNP): use the analog `OUT`, or an external TCA9548A, or a software bus |
| AD8232 supply rail | **3V3 only.** Absolute maximum 3.5 V; `VBAT` reaches 4.2 V while charging |
| ADC2 unusable with the radio on | All 8 analog signals on ADC1 (GPIO1–10) |
| ESP32 boot straps and the LEDs | `IO45`/`IO46` drive LEDs anode-side; at reset the pin is high-Z, the LED cannot conduct, so the internal pull-downs hold both straps at 0 |
| Motor and buzzer flyback polarity | Anode on the switched drain, cathode on the supply. Checked by ERC rule R10 |
| Piezo clamp polarity | `D5` cathode → `3V3`, `D6` anode → `GND`. Checked by ERC rule R10 |
| Thermal vias in packages | Moved to board level as **plated** vias. EAGLE's `<hole>` in a package is an *unplated* hole, which through a thermal land is a defect |
| Two layers were not enough | 4 layers: signal / GND plane / 3V3 plane / signal. Measured evidence in `DESIGN_ASSUMPTIONS.md` §2 |
