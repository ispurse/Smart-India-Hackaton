# COMPONENT VERIFICATION — SIH26113 Maternity Assist Belt

Every symbol pinout and every footprint dimension in
`libraries/SIH26113_Maternity_Assist_Belt.lbr` traces back to one of the rows
below. Where a datasheet could not be retrieved, that is stated rather than
papered over.

## Verification levels

| Level | Meaning |
|---|---|
| **V** | Taken from the manufacturer's own datasheet / package-outline / recommended-land-pattern drawing. The document was downloaded and read while producing this design. |
| **I** | Land pattern computed from **IPC-7351B** Nominal (Level B) density, using body and terminal dimensions that are themselves level V. |
| **S** | De-facto standard geometry (2.54 mm pin header, M2 hole, 6 mm tactile switch). Widely interchangeable, but the exact vendor part should still be confirmed. |
| **U** | **Unverified.** Datasheet not retrievable. Not placed on the board. |

## How the datasheets were read

`analog.com`, `mouser.com` and `jst.co.jp` were unreachable or bot-blocked
from this network. Working method:

1. Download the PDF, falling back to manufacturer-authored copies hosted
   elsewhere (`documentation.espressif.com`, `ti.com`, `st.com`,
   `diodes.com`, `jst-mfg.com`, `cdn.sparkfun.com`).
2. Extract text with `pypdf` and read the pin-function and package tables.
3. Where a mechanical drawing is vector-only and its dimensions do not
   extract as text, render the page to a bitmap at 5× with PyMuPDF and read
   the dimensions off the drawing.

Step 3 is how two numbers that appear nowhere in the extracted text were
obtained: the **ESP32-S3-WROOM-1 pin-1 datum (7.49 mm below the antenna
edge)** and the **JST PH PCB hole diameter (ø0.7 +0.1/−0 mm)**. Both matter —
the first sets where all 40 module pads land relative to the antenna
keep-out, the second sets whether the battery connector fits.

---

## A. Main ICs

| Component | Manufacturer | Exact part | Package | Supply | Interface | Pinout | Footprint | Source |
|---|---|---|---|---|---|---|---|---|
| Central MCU | Espressif Systems | **ESP32-S3-WROOM-1-N8R2** | 41-pad castellated module, 25.5 × 18 × 3.1 mm | 3.0–3.6 V | Wi-Fi b/g/n, BLE 5, 2 × I²C, SPI, UART, USB-Serial-JTAG, ADC | **V** — datasheet v1.8 Table 3-1, all 41 pins | **V** — v1.8 Fig. 11-1 land pattern + Fig. 10-1 dimensions | *ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8*, Espressif |
| ECG analog front end | Analog Devices | **AD8232ACPZ-R7** | 20-lead LFCSP_WQ (CP-20-10), 4 × 4 mm, 0.5 mm pitch, 2.50 mm SQ exposed pad | **2.0–3.5 V only** | analog out to ADC; 3 control in, 2 status out | **V** — Rev. A Table 3, all 20 pins + EP | **I** — body/terminal/EP from the Rev. A outline drawing (JEDEC MO-220-WGGD); lands IPC-7351B Nominal 0.80 × 0.28 mm at 1.75 mm from centre | *AD8232 Data Sheet Rev. A*, Analog Devices |

### The AD8232 supply rail is a hard constraint

Absolute maximum supply is **3.5 V**, and the datasheet's *Power Supply
Regulation and Bypassing* section warns that a lithium cell "may exceed the
absolute maximum ratings of the AD8232" during a charge cycle. On this board
the AD8232 sits on the regulated **3V3** rail and never sees `VBAT` (3.0–4.2 V,
and up to 4.2 V while charging).

The architecture diagram does not say which rail feeds it. Getting this wrong
destroys the part on first charge, so it is called out here and in
`DESIGN_ASSUMPTIONS.md`.

### Verified ESP32-S3-WROOM-1 land pattern

Reproduced in the library exactly as Espressif specify it:

| Parameter | Value | Where it comes from |
|---|---|---|
| Module body | 25.5 × 18.0 × 3.1 mm | Fig. 10-1 |
| Land count | 40 signal + 1 EPAD | Table 3-1 |
| Land size | 1.5 mm radial × 0.9 mm tangential | Fig. 11-1 (`40 × 1.5`, `40 × 0.9`) |
| Pitch | 1.27 mm | Fig. 11-1 |
| Column row spacing | 17.5 mm centre-to-centre | Fig. 11-1 |
| Column pad span | 16.51 mm (14 pads/side) | Fig. 10-1 / 11-1 |
| End-row pad span | 13.97 mm (12 pads), 2.015 mm inset each side | Fig. 11-1 |
| **Pin 1 centre** | **7.49 mm below the antenna-end edge** | Fig. 11-1, read from a 5× render |
| Antenna area | 6.0 mm at the pin-1 end, full width | Fig. 11-1 |
| Numbering | 1–14 left column top→bottom, 15–26 end row left→right, 27–40 right column bottom→top, 41 = EPAD | Table 3-1 |

The EPAD is emitted as one 3.4 mm land inside Espressif's 3 × 3 thermal-copper
envelope, plus nine plated 0.3 mm vias **placed at board level, not in the
package**. EAGLE's `<hole>` element is an *unplated* mechanical hole; putting
thermal "vias" in a package that way would drill unplated holes through the
ground land, which is a real manufacturing defect. See `THERMAL_VIAS` in
`scripts/lib_defs.py`.

---

## B. Sensor ICs

| Component | Manufacturer | Exact part | Package | Supply | Interface | Pinout | Footprint | Source |
|---|---|---|---|---|---|---|---|---|
| Temperature | Texas Instruments | **TMP117AIDRVR** | 6-pin WSON (DRV0006B), 2.0 × 2.0 mm, 0.65 mm pitch, 1.0 × 1.6 mm thermal pad | 1.7–5.5 V | I²C, addr **0x48** (ADD0→GND) | **V** — SNOSD82D Table 5-1, WSON column | **V** — TI's own *EXAMPLE BOARD LAYOUT*, SNOSD82D p. 41: lands 0.45 × 0.30 mm, rows 1.95 mm apart | *TMP117 SNOSD82D* rev. Sept 2022, TI |
| 6-axis IMU | STMicroelectronics | **LSM6DSOXTR** | LGA-14L, 2.5 × 3.0 × 0.86 mm, 0.5 mm pitch | VDD 1.71–3.6 V, VDDIO 1.62–3.6 V | I²C, addr **0x6A** (SA0→GND) | **V** — DS12814 Rev. 4 Table 1, all 14 pins | **I** — geometry from DS12814 Rev. 4 Fig. 28 (14 pads 0.475 × 0.25 mm, 1.5/1.0 mm row spans); lands enlarged to 0.50 × 0.28 mm per IPC-7351B. *ST's TN0018 land-pattern note was not retrievable.* | *LSM6DSOX DS12814 Rev. 4*, ST |
| Magnetic angle | ams-OSRAM | **AS5600-ASOM** | SOIC-8; D 4.90, E 6.00, E1 3.90, e 1.27 mm | 3.3 V or 5 V mode | I²C, addr **0x36 — fixed, not configurable** | **V** — DS000365 v1-06 Fig. 4, all 8 pins | **I** — outline from DS000365 v1-06; lands IPC-7351B SOIC127P600X175-8N Nominal | *AS5600 DS000365 v1-06*, ams-OSRAM |
| Bridge / load-cell ADC | Avia Semiconductor | **HX711** | SOP-16L, body 9.90 × 3.90 mm, lead span 6.00 mm, e 1.27 mm | 2.6–5.5 V | 2-wire serial (DOUT + PD_SCK) | **V** — HX711 English datasheet Table 1, all 16 pins | **I** — *Package Dimensions* page of the same datasheet; lands IPC-7351B SOIC127P600X175-16N Nominal | *HX711 datasheet*, Avia Semiconductor |
| Battery fuel gauge | Analog Devices (Maxim) | MAX17048 | WLP-8 (0.9 × 1.7 mm) or TDFN-8 (2 × 2 mm) | 2.5–4.5 V | I²C, addr **0x36 — fixed** | **U — NOT VERIFIED** | **U — NOT VERIFIED, NOT PLACED** | analog.com and every distributor mirror tried were unreachable or bot-blocked |

### Why the MAX17048 is not on the board

Its datasheet could not be retrieved, so neither its pin assignment nor its
land pattern could be checked against primary documentation. Both packages
are also awkward for a hackathon prototype — a 0.9 × 1.7 mm 8-bump WLP is not
hand-assemblable at all.

Rather than invent a footprint, the design does two things:

* **`J4`** — a 5-way 2.54 mm header (`VBAT`, `GND`, `3V3`, `SDA`, `SCL`) for
  an off-the-shelf MAX17048 breakout. Header geometry is standard, so nothing
  is guessed.
* **`R5`/`R6`/`C6`** — a 470 k/470 k divider from `VBAT` to `IO9`
  (ADC1_CH8), giving a battery-voltage reading that works whether or not the
  gauge is fitted. 4.2 V at the cell reads 2.10 V at the pin, comfortably
  inside ADC1's range.

Recorded as an architectural change in `DESIGN_ASSUMPTIONS.md` and as an open
item in `REQUIRES_CONFIRMATION.md`.

---

## C. Power components

| Component | Manufacturer | Exact part | Package | Rating | Pinout | Footprint | Source |
|---|---|---|---|---|---|---|---|
| Li-ion charger | NanJing Top Power ASIC | **TP4056-42-SOP8-PP** | SOP-8 | 4.2 V float ±1.5 %, up to 1 A, programmable | **V** — TP4056 datasheet p. 2, every pin described individually | **I** — SOP-8 per the datasheet's own package/order table; lands IPC-7351B SOIC127P600X175-8N Nominal | *TP4056 datasheet*, NanJing Top Power |
| 3V3 regulator | Diodes Incorporated | **AP2112K-3.3TRG1** | SOT-25 (SOT-23-5) | 600 mA min, 250 mV dropout @ 600 mA, ±1.5 % | **V** — AP2112 DS39724 Rev. 2-2 *Pin Descriptions*, SOT25 column | **I** — JEDEC TO-178; lands IPC-7351B SOT95P280X145-5N Nominal | *AP2112 DS39724 Rev. 2-2*, Diodes |

### TP4056 pins as used

| Pin | Name | This design |
|---|---|---|
| 1 | TEMP | **tied to GND.** The datasheet: "The temperature sense function can be disabled by grounding the TEMP pin." No pack NTC is assumed. |
| 2 | PROG | `R1` = 2.4 kΩ → GND. The datasheet's characteristics table gives **R_PROG = 2.4 k → 500 mA**. 500 mA rather than 1 A halves the linear charger's dissipation, which matters because this SOP-8 footprint carries no thermal land. |
| 3 | GND | plane |
| 4 | VCC | `VBUS` (5 V in) |
| 5 | BAT | `VBAT` — cell positive and system rail |
| 6 | STDBY | open drain → green LED `D2` |
| 7 | CHRG | open drain → red LED `D1` |
| 8 | CE | tied to VCC — enabled whenever 5 V is present |

> **Known limitation, stated because it is real.** The TP4056 has no
> power-path switching. The system load hangs off the same `BAT` node as the
> cell, so load current flows through the charger and disturbs its C/10
> termination detection. This is how essentially every TP4056 prototype is
> wired and it does work, but a production build should use a power-path
> charger (MCP73871, BQ24075 or similar).

---

## D. Discrete semiconductors

| Component | Part | Package | Rating | Pinout | Footprint | Note |
|---|---|---|---|---|---|---|
| Motor / buzzer low-side switch | **AO3400A** (Alpha & Omega), or any pin-compatible logic-level N-FET | SOT-23-3 | 30 V, 5.7 A, V_GS(th) ≤ 1.4 V, R_DS(on) 34 mΩ @ 4.5 V | **S** — 1 = Gate, 2 = Source, 3 = Drain, the universal SOT-23 N-MOSFET assignment | **I** — IPC-7351B SOT95P237X112-3N Nominal | Gate threshold must suit 3.3 V drive — confirm on any substitute |
| Flyback / clamp | **1N5819HW** | SOD-123 | 40 V, 1 A Schottky | 2-pin, pad 1 = cathode (band) | **I** — IPC-7351B DIOM2616X110N Nominal | D5–D8 |
| Indicator LEDs | generic | 0805 | — | pad 1 = cathode | **I** — IPC-7351B | D1–D4 |

---

## E. Passives

| Type | Package | Footprint | Values used |
|---|---|---|---|
| Resistors | 0805 (2012 metric) | **I** — IPC-7351B RESC2012X65N Nominal: lands 1.15 × 1.40 mm, 0.75 mm inner gap | 0R, 100R, 1k, 2k4, 4k7, 10k, 100k, 330k, 470k, 1M, 10M |
| Capacitors | 0805 (2012 metric) | **I** — IPC-7351B CAPC2012X135N Nominal | 1n, 3n9, 8n2, 10n, 100n, 220n, 1u, 10u, 22u |

Voltage ratings: 16 V X7R/X5R is fine on `3V3`; use ≥ 16 V on `VBAT`/`VBUS`;
**`C34` (piezo AC coupling) must be ≥ 50 V**, because a piezo film's
open-circuit transient reaches tens of volts. That requirement is carried in
the BOM value string as `100n/50V` so it cannot be lost.

---

## F. Connectors and electromechanical

| Component | Part | Footprint | Source |
|---|---|---|---|
| Li-Po battery (`J1`), load cell (`J8`) | **JST PH series** — S2B-PH-K-S / S4B-PH-K-S | **V** — JST ePH catalogue, *PC board layout and Assembly layout (Through-hole type)*: pitch 2.00 ±0.05 mm, **PCB hole ø0.7 +0.1/−0 mm**, outline offsets (1.95) × (1.7) mm. Drill specified 0.8 mm — inside JST's tolerance and following their Note 3, "when using PCB made of hard fibreglass material, please consider a larger hole diameter". | `jst-mfg.com/product/pdf/eng/ePH.pdf`, dimensions read from a 5× render because the PDF's fonts do not extract as text |
| All 2.54 mm headers (`J2`–`J7`, `J9`–`J18`) | generic 1×N | **S** — 2.54 mm pitch, 1.0 mm drill, 1.8 mm pad, suiting the 0.64 mm square posts every common header uses. Pad 1 square. | de-facto standard |
| Push-buttons `SW2` RESET, `SW3` BOOT, `SW4` SOS | 6 × 6 mm THT tactile, TL1105 / B3F-10xx family | **S** — 4 leads on a 6.5 × 4.5 mm grid, 1.0 mm drill. Leads 1–2 and 3–4 internally common, mapped with an EAGLE multi-pad connect (`pad="1 2"`). | de-facto standard — **confirm against the chosen vendor part** |
| Mounting holes `H1`–`H4` | M2 | **S** — 2.2 mm drill, 4.4 mm plated annulus tied to GND, 4.6 mm keep-out ring | — |
| Test points `TP1`–`TP19` | — | 1.5 mm round SMD land | — |

---

## G. Off-board transducers

These sit on flying leads; the board carries only their connector and signal
conditioning. **None of their electrical characteristics were verified**,
because no specific part has been selected.

| Function | Connector | On-board conditioning | Status |
|---|---|---|---|
| Belt pressure ×4 | `J9`–`J12` | 10 kΩ divider + 10 nF filter → ADC1 | FSR402 assumed for divider sizing — see `DESIGN_ASSUMPTIONS.md` |
| Load cell | `J8` (JST-PH-4) | HX711 channel A, gain 128, ratiometric to AVDD | bridge resistance and sensitivity **TBD** |
| Abdominal stretch | `J13` | divider + 10 nF filter → ADC1 | **resistance range unknown — `R37` = 10 k is a placeholder** |
| Fetal movement (piezo film) | `J14` | 10 MΩ load, 100 nF/50 V AC coupling, mid-rail bias, 100 kΩ series, Schottky clamps to 3V3 and GND | film capacitance **TBD** |
| Hall / limit switch | `J15` | 10 kΩ pull-up + 100 nF debounce | open-collector or mechanical assumed |
| Vibration motor | `J16` | N-FET low side, flyback diode, optional series ballast `R45` | **voltage / current rating TBD** |
| Buzzer | `J17` | N-FET low side from 3V3, flyback diode | magnetic (inductive) assumed |
| ECG electrodes ×3 | `J7` | 330 kΩ series protection per lead, 10 MΩ bias, driven RLD electrode | standard Ag/AgCl assumed |

---

## Summary

| | Count |
|---|---|
| Placed ICs/modules with a **fully verified** pinout (V) | **8 of 8** |
| Footprints from a **manufacturer land-pattern drawing** (V) | 3 — ESP32-S3-WROOM-1, TMP117 WSON, JST PH |
| Footprints **IPC-7351B-derived** from verified body dimensions (I) | 8 |
| Footprint families on **de-facto standard** geometry (S) | 4 |
| Components **not verified and therefore not placed** (U) | 2 — MAX17048, FS8205A |

No pin mapping in this library was written from memory or inferred from the
architecture diagram.

---

## H. Parts verified but deliberately NOT placed

These were researched after the first pass. Their data is recorded here so the
decision to place them is informed rather than blocked.

### DW01A — one-cell Li-ion/polymer battery protection controller ✅ V

*Primary source: **DW01A Rev. 1.0, DW01A-DS-10_EN, JUN 2009** (FSC), §6 "Pin
Configuration and Package Marking Information".* Package **SOT-23-6**.

| Pin | Symbol | Description (datasheet wording) |
|---|---|---|
| 1 | `OD` | MOSFET gate connection pin for discharge control |
| 2 | `CS` | Input pin for current sense, charger detect |
| 3 | `OC` | MOSFET gate connection pin for charge control |
| 4 | `TD` | Test pin for reduce delay time |
| 5 | `VCC` | Power supply, through a resistor (R1) |
| 6 | `GND` | Ground pin |

Thresholds (§5 Product Name List): overcharge detect **4.300 ±0.050 V**,
release **4.100 ±0.050 V**; overdischarge detect **2.40 ±0.100 V**, release
**3.0 ±0.100 V**; overcurrent detect **150 ±30 mV**. Quiescent current 3 µA at
Vcc = 3.9 V. Delay times are generated internally — **no external capacitors
required**.

Note the datasheet's own footer reads "For Reference Only", which is worth
knowing before designing a safety circuit around it.

### FS8205A — dual N-channel MOSFET (the actual cell-current switch) ❌ U

**Pinout NOT verified.** Only distributor listings and datasheet-aggregator
pages were reachable; **no manufacturer pin-configuration table was
obtained.** Sources disagree on which pins carry S1/S2 and on whether the
drains are internally common. Manufacturer is FuxinSemi, package SOT-23-6L,
document Ver. 2.1 (2018) per one aggregator — the document itself was not
retrieved.

**Consequence:** the DW01A + FS8205A protection circuit **still cannot be
added responsibly**, because the FS8205A is the part carrying the full cell
current. See `REQUIRES_CONFIRMATION.md` **B1**.

### AS5600 3.3 V-mode strapping ✅ confirmed

Not a new part — a confirmation that closes **M5**. *AS5600 Datasheet,
ams-OSRAM, [v1-06] 2018-Jun-20*, page 9: "In 3.3V operation, the VDD5V and
VDD3V3 pins must be tied together. VDD is the voltage level present at the
VDD5V pin." The board does exactly that. Per-pin decoupling (page 3) also
matches: 100 nF on `VDD5V`, 1 µF on `VDD3V3`.
