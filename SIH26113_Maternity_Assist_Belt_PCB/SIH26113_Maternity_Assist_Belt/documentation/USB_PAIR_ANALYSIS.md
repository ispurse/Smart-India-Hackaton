# USB DIFFERENTIAL PAIR — IMPEDANCE ANALYSIS

Closes item **M2** in `REQUIRES_CONFIRMATION.md`, which previously read
"**NOT CALCULATED**".

**Result up front: the pair is ≈ 165 Ω differential, not 90 Ω — 83 % high. It
is nevertheless not a functional risk at Full Speed, because the trace is
electrically short by a factor of ~2.6 against the fastest edge USB 2.0 FS
permits.** The arithmetic for both halves of that statement is below, along
with the geometry that *would* give 90 Ω if you want it.

---

## 1. What the board actually contains

Measured by re-parsing the emitted `.brd`, not assumed:

| Property | `USB_DM` (`IO19`) | `USB_DP` (`IO20`) |
|---|---|---|
| Track width | 0.20 mm | 0.20 mm (one 0.25 mm segment) |
| Segments | 8 | 17 |
| Layers used | **1 and 16** | **1 and 16** |
| Total length | **43.9 mm** | **43.1 mm** |

| Pair geometry | Value |
|---|---|
| Closest centre-to-centre distance | **1.031 mm** (layer 1) |
| Closest **edge-to-edge gap** | **0.806 mm** |
| Gap as a multiple of dielectric height | **2.24 × h** |

> **The two nets are not routed as a coupled pair at all.** They were treated
> as two ordinary signals by the router: independent paths, independent layer
> changes, and a closest approach of 0.806 mm — which is more than twice the
> 0.36 mm dielectric height, i.e. far enough apart that the coupling between
> them is negligible.

## 2. Stack-up used for the calculation

| Parameter | Value | Source |
|---|---|---|
| `h` — dielectric to the reference plane | **0.360 mm** | the `.brd` design rules (L1 → L2) |
| `t` — copper thickness | **0.035 mm** | 1 oz, manufacturing check item 4 |
| `εr` | **4.3** | FR-4 nominal — **an assumption**, see §6 |

## 3. Single-ended impedance

IPC-2141A microstrip (valid for 0.1 < w/h < 3.0, 1 < εr < 15; here
w/h = 0.56 ✅):

$$Z_0 = \frac{87}{\sqrt{\varepsilon_r + 1.41}} \ln\!\left(\frac{5.98h}{0.8w + t}\right)$$

$$Z_0 = \frac{87}{\sqrt{5.71}} \ln\!\left(\frac{5.98 \times 0.36}{0.8 \times 0.20 + 0.035}\right) = \mathbf{87.4\ \Omega}$$

## 4. Differential impedance as routed

IPC-2141A edge-coupled differential microstrip:

$$Z_{diff} = 2 Z_0 \left(1 - 0.48\, e^{-0.96 s / h}\right)$$

With `s` = 0.806 mm and `h` = 0.36 mm:

$$Z_{diff} = 2 \times 87.4 \times \left(1 - 0.48\, e^{-2.149}\right) = 2 \times 87.4 \times 0.944 = \mathbf{165.1\ \Omega}$$

| | |
|---|---|
| USB 2.0 target | **90 Ω ± 15 %** → 76.5 – 103.5 Ω |
| As routed | **165 Ω** |
| Deviation | **+83 %** |

The coupling term has collapsed to 5.6 % because the traces are 2.24 × h
apart. At that spacing you effectively have two independent 87 Ω
single-ended microstrips, and 2 × 87 ≈ 165 Ω is exactly what an uncoupled
pair gives.

## 5. Why it is not a functional problem

The ESP32-S3's built-in USB-Serial-JTAG is **Full Speed only — 12 Mbit/s**.
Transmission-line behaviour only matters when the propagation delay is a
significant fraction of the signal's rise time.

**Effective permittivity** (microstrip, w = 0.20 mm, h = 0.36 mm):

$$\varepsilon_{eff} = \frac{\varepsilon_r + 1}{2} + \frac{\varepsilon_r - 1}{2}\cdot\frac{1}{\sqrt{1 + 10h/w}} = 3.03$$

**Propagation velocity and delay:**

$$v = \frac{c}{\sqrt{\varepsilon_{eff}}} = \frac{299.8}{\sqrt{3.03}} = 172\ \text{mm/ns} \qquad t_{pd} = 5.80\ \text{ps/mm}$$

**One-way delay over the 44 mm route: 255 ps.**

USB 2.0 specifies Full-Speed rise/fall time as **4 – 20 ns**. Taking the
worst case (fastest permitted edge, 4 ns):

| Criterion | Critical length | 44 mm verdict |
|---|---|---|
| Conservative, `tr·v/6` | **115 mm** | ✅ **electrically short** (2.6× margin) |
| Common, `tr·v/2` | 345 mm | ✅ electrically short (7.8× margin) |

At the slowest permitted edge (20 ns) the conservative critical length is
574 mm — 13× margin.

**The trace is a lumped interconnect, not a transmission line, at this speed.
An impedance mismatch on a lumped interconnect does not produce the
reflections that a mismatch on a transmission line does.**

**Length skew:** 43.9 mm − 43.1 mm = 0.8 mm = **5 ps**. USB FS allows far
more than that. Irrelevant.

### One real observation while measuring this

**Both nets change layers**, so their reference plane changes from the `GND`
plane (layer 2, referencing layer 1) to the `3V3` plane (layer 15,
referencing layer 16). The return current has to transfer between the two
planes through their interplane capacitance.

The 0.71 mm core between L2 and L15 across a 70 cm² board is a large
distributed capacitor, so at 12 Mbit/s this is not a problem. **It would be a
problem at High Speed (480 Mbit/s)**, and it is the sort of thing that is
invisible unless you measure it. Noted rather than hidden.

## 6. Honest limits of this analysis

| Limitation | Effect |
|---|---|
| **Closed-form IPC-2141A, not a 2D field solver** | typically ±10 % on `Z0`. Does not change any conclusion here. |
| **εr = 4.3 is nominal.** Real FR-4 panels run 4.0 – 4.6 and are frequency- and glass-weave-dependent | shifts `Z0` a few ohms and `v` a few percent. 44 mm ≪ 115 mm survives it comfortably. |
| **Dielectric heights are the declared stack-up**, not a fab's actual press-out | ask your fab for their real 4-layer stack if you ever need controlled impedance |
| **Not measured** | ❌ no TDR, no prototype. This is calculation, like every other figure in this project. |

## 7. If you want 90 Ω anyway

Solved from the same formulas, for this stack-up:

| Track width | Edge-to-edge gap for 90 Ω | Practical? |
|---|---|---|
| 0.20 mm | 0.010 mm | ❌ impossible |
| 0.25 mm | 0.031 mm | ❌ impossible |
| 0.30 mm | 0.069 mm | ❌ below the 0.127 mm rule |
| 0.35 mm | 0.111 mm | ❌ below the 0.127 mm rule |
| **0.40 mm** | **0.159 mm** | ✅ **buildable** |

**So: 0.40 mm wide, 0.16 mm gap, both traces on layer 1 for the whole run,
no layer changes.**

Note *why* the narrow widths are impossible: on a 0.36 mm dielectric a
0.20 mm trace is already 87 Ω single-ended, so an uncoupled pair is 175 Ω and
you would need the traces almost touching to pull it down to 90 Ω. Getting to
90 Ω requires **widening** the traces to lower `Z0` first. That is the
opposite of what most people try.

### What it would cost

`USB_DM` and `USB_DP` run from module pins 13/14 to `J2`, straight through the
**left escape channel** — one of the three corridors that exist because the
ESP32-S3 has 40 lands on 1.27 mm pitch and nowhere to put them. Widening two
tracks from 0.20 mm to 0.40 mm and forcing both onto layer 1 for the full
44 mm will displace other nets from the most congested region of the board.

**Expect the unrouted-net count to rise.** Do this only if you have a reason.

### The recommendation

**Leave it.** The pair is electrically short by 2.6× at the fastest edge USB
FS permits, the skew is 5 ps, and `J5` (UART) is a fully-wired fallback
programming path if USB ever proves unreliable.

**Revisit only if** you move to an external High-Speed USB PHY, in which case
this becomes a genuine 90 Ω controlled-impedance problem *and* the layer
changes in §5 become a real return-path discontinuity — and at that point the
right answer is to re-plan the route, not to widen the existing one.

## 8. Verdict

| | |
|---|---|
| M2 status | ✅ **CALCULATED** (was ❌ NOT CALCULATED) |
| Differential impedance, as routed | **≈ 165 Ω** |
| Meets USB 2.0's 90 Ω ± 15 % | ❌ **No** |
| Functional risk at Full Speed (12 Mbit/s) | ✅ **None** — electrically short, 2.6× margin |
| Action required | **None.** Documented, quantified, and left as designed. |
| Action if High Speed is ever needed | re-plan the route: 0.40 mm / 0.16 mm, single layer |
