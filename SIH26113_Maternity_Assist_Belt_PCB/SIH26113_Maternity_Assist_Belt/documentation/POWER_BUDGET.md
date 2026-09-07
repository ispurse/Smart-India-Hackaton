# POWER BUDGET — SIH26113 Maternity Assist Belt

All figures are from the datasheets cited in `COMPONENT_VERIFICATION.md`,
except where marked *estimate* — those are stated as estimates because the
part has not been selected yet.

## Rails

```
  J2 (5 V in) ──► VBUS ──► TP4056 ──► VBAT ──┬──► AP2112K-3.3 ──► 3V3 (plane, layer 15)
                          (500 mA charge)    │
      J1 (protected Li-Po pack) ─────────────┤
                                             ├──► R45 ──► J16 vibration motor
                                             └──► R5/R6 divider ──► IO9 (VBAT_SENSE)
```

| Rail | Voltage | Source | Distribution |
|---|---|---|---|
| `VBUS` | 5 V | `J2` header | tracks, 0.50 mm |
| `VBAT` | 3.0 – 4.2 V | 1S Li-Po via `J1`, charged by `U1` | tracks, 0.50 mm |
| `3V3` | 3.3 V ±1.5 % | `U2` AP2112K-3.3 | **inner plane, EAGLE layer 15** |
| `GND` | 0 V | — | **inner plane, EAGLE layer 2** |

---

## 3V3 rail — worst case

The point of this table is the total at the bottom, and whether it fits under
the regulator's guaranteed minimum.

| Load | Current | Source of the figure |
|---|---|---|
| ESP32-S3 Wi-Fi TX peak | **355 mA** | ESP32-S3-WROOM-1 datasheet v1.8, current consumption in active mode |
| microSD write peak | **100 mA** *estimate* | typical for an SD card in SPI mode; card-dependent |
| Buzzer (magnetic, while sounding) | **30 mA** *estimate* | typical 3 V magnetic buzzer; part not selected |
| Load-cell bridge excitation | **9.4 mA** | worst case: a 350 Ω bridge at 3.3 V. A 1 kΩ bridge draws 3.3 mA |
| AS5600 | **6.5 mA** | AS5600 DS000365 v1-06 |
| I²C pull-ups, 4 lines pulled low | **2.8 mA** | 4 × 3.3 V / 4.7 kΩ; only while a line is actually low |
| Status + alert LEDs, both on | **2.6 mA** | 2 × (3.3 − 2.0) V / 1 kΩ |
| HX711 | **1.4 mA** | HX711 datasheet |
| FSR dividers ×4, all at full force | **1.1 mA** | 4 × 3.3 V / 12 kΩ, from `DESIGN_ASSUMPTIONS.md` §7.1 |
| LSM6DSOX, both sensors high-performance | **0.55 mA** | LSM6DSOX DS12814 Rev. 4 |
| Stretch-sensor divider | **0.33 mA** *estimate* | depends on the unselected sensor |
| AD8232 | **0.17 mA** | AD8232 Rev. A, supply current |
| VBAT sense divider | **4.5 µA** | 4.2 V / 940 kΩ |
| Piezo bias network | **1.65 µA** | 3.3 V / 2 MΩ |
| TMP117, continuous conversion | **6.3 µA** | TMP117 SNOSD82D |
| **Total, everything simultaneous** | **≈ 510 mA** | |
| **AP2112K-3.3 guaranteed minimum** | **600 mA** | AP2112 DS39724 Rev. 2-2 |
| **Margin** | **≈ 15 %** | |

### Is that margin real?

Yes, and it is more comfortable than 15 % suggests, because the two big items
do not coincide in practice:

* Wi-Fi TX (355 mA) is a burst of a few hundred microseconds. **BLE-only
  operation — the project's actual link — is about 130 mA**, which drops the
  total to ~285 mA.
* microSD writes are buffered by firmware and need not overlap a radio burst.

`C8` (22 µF) plus `C7` (100 nF) at the module's pin 2 supply the radio bursts
locally, which is what those parts are for.

**Realistic steady-state, BLE + all sensors sampling, no motor or buzzer:
≈ 155 mA.** With a 2000 mAh cell that is roughly 13 hours of continuous
operation, before any duty cycling.

---

## The dropout problem — stated because it will bite otherwise

The AP2112K's dropout is **250 mV typical at 600 mA**. So:

| `VBAT` | 3V3 rail output | ESP32-S3 (min 3.0 V) |
|---|---|---|
| 4.2 V (full) | 3.30 V | fine |
| 3.7 V (nominal) | 3.30 V | fine |
| 3.55 V | 3.30 V | at the edge of regulation |
| 3.30 V | ≈ 3.05 V | **marginal** |
| 3.10 V | ≈ 2.85 V | **below minimum — brown-out** |

### Required firmware behaviour

**Implement a low-battery cut-off at 3.5 V using `VBAT_SENSE` on `IO9`.**

The divider is 470 k/470 k, so 3.5 V at the cell reads **1.75 V** at the pin.
Below that, firmware should stop sampling, notify the app, and enter deep
sleep. Without this the board will brown out unpredictably at the bottom of
the discharge curve — and unpredictable behaviour in a device with an SOS
button is worse than a clean shutdown.

This limitation is inherent to an LDO from a single Li-Po cell and is normal
for ESP32 designs. If the extra 15 % of cell capacity matters, the fix is a
buck-boost regulator (see `DESIGN_ASSUMPTIONS.md` §15).

---

## VBAT rail

| Load | Current | Notes |
|---|---|---|
| `3V3` rail input | ≈ 520 mA worst case | LDO input current ≈ output current + 55 µA quiescent |
| Vibration motor | **100 mA** *estimate* | typical coin ERM; part not selected |
| `VBAT_SENSE` divider | 4.5 µA | |
| `J4` fuel-gauge breakout | ≈ 25 µA *estimate* | MAX17048 is a 3 µA part; a breakout adds its own regulator |
| **Total** | **≈ 620 mA peak** | |

`R45` (0 Ω, 0805) is in series with the motor's high side. It exists so the
motor rail can be adapted without cutting tracks — see
`DESIGN_ASSUMPTIONS.md` §8.1. **Confirm the motor's voltage rating before
fitting 0 Ω**; a 3.0 V motor on a full 4.2 V cell will not last.

---

## Charging

| Parameter | Value | Source |
|---|---|---|
| Input | 5 V at `J2` (`VBUS`) | — |
| Charge current | **500 mA** (`R1` = 2.4 kΩ) | TP4056 datasheet characteristics table |
| Float voltage | 4.2 V ±1.5 % | TP4056 datasheet |
| Termination | C/10 = 50 mA | TP4056 datasheet |
| Trickle threshold | 2.9 V | TP4056 datasheet |
| Charger dissipation, worst case | (5 − 3.0) V × 0.5 A ≈ **1.0 W** | at the start of a deeply-discharged charge |
| Time to charge 2000 mAh from empty | ≈ 4.5 h | |

**1.0 W in an SOP-8 with no thermal land will get hot.** The TP4056 has
thermal regulation and folds back the current rather than failing, so this is
safe but slow. It is why 500 mA was chosen over 1 A
(`DESIGN_ASSUMPTIONS.md` §1.2). Give `U1` some copper area on layers 1 and 16
if you re-lay the board, or move to a switching charger.

Note also that the system load flows through `BAT` during charging, so
termination detection is disturbed — §1.3 of `DESIGN_ASSUMPTIONS.md`.

---

## Trace width justification

IPC-2221 external-layer chart, 1 oz (35 µm) copper, 10 °C rise:

| Width | Ampacity | Used for |
|---|---|---|
| 0.20 mm | ≈ 0.74 A | all signals (net classes `default` and `analog_ecg`) |
| 0.50 mm | ≈ 1.45 A | `VBUS`, `VBAT`, motor path (net classes `power` and `motor`) |
| 0.15 mm | ≈ 0.60 A | fine-pitch fan-out escapes only (AD8232, LSM6DSOX, TMP117, HX711), a few millimetres long, carrying signal currents in the microamp range |

Signal and power tracks are narrower than the 0.25 / 0.60 mm this design
started with. They were reduced deliberately: a narrower track needs less
clearance around it, and that bought back the routing density lost when the
clearance model was corrected to measure Euclidean distance. Ampacity was
never the binding constraint — see the margin below.

Highest current on any track is the motor path at ~100 mA and the `VBAT` feed
to the LDO at ~620 mA peak. 0.50 mm carries ≈ 1.45 A, so that is **2.3×
margin** on the worst case.

`3V3` and `GND` are planes, so their ampacity is not a constraint.

Plane vias are 0.3 mm drill / 0.55 mm pad. A 0.3 mm via carries roughly 1 A
comfortably; each plane-net pad has its own, so no via carries more than that
pad's share.

---

## Deep-sleep estimate

| Item | Current |
|---|---|
| ESP32-S3 deep sleep | ≈ 7 µA |
| TMP117 shutdown | 0.25 µA |
| LSM6DSOX power-down | 3 µA |
| AS5600 low-power mode 3 | ≈ 1.5 µA |
| AD8232 in shutdown (`SDN` low) | < 0.2 µA |
| `VBAT_SENSE` divider | 4.5 µA |
| Piezo bias network | 1.65 µA |
| REFIN divider (`R23`/`R24`) | 0.33 µA |
| ECG input bias (`R21`/`R22`) | 0.33 µA |
| AP2112K quiescent | 55 µA |
| HX711 power-down (`PD_SCK` high) | ≈ 0.2 µA |
| **Total** | **≈ 74 µA** |

The AP2112K's own 55 µA quiescent current dominates. That is the price of
choosing an LDO for its noise performance, and it is worth naming: on a
2000 mAh cell, 74 µA is about 3 years of shelf life, so it is not a practical
problem — but if it ever became one, the regulator is where to look, not the
sensors.

**Not measured — all figures are datasheet typicals.** Verify on hardware.
