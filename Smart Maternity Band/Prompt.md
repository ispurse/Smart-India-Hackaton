I am attaching the PCB architecture image to this conversation.

You have access to the project directory and should inspect all existing files before starting.

Create a New Sub folder under the Repo with a similar naming structure and work inside it for this work, nothing should be done outside for this work.

Do not create the deliverables only as explanations in chat. Create the actual files in the project directory.

Use your terminal/file tools extensively. You are expected to generate, inspect, modify and validate the project files yourself.

If a required EDA operation cannot be performed in your environment, create the appropriate source/script/output that can be executed in Autodesk Fusion and explicitly tell me what could not be executed.

Also Create a Readme of what you did and whats happening and everything A to Z for this PCB thing.

MASTER PROMPT — SIH26113 MATERNITY ASSIST BELT
PCB LIBRARY + SCHEMATIC + PCB DESIGN + DOCUMENTATION

You are acting as a senior electronics engineer, PCB designer, embedded hardware engineer, EDA library engineer, and autonomous engineering agent.

I am developing a prototype called:

SIH26113 — Maternity Assist Belt

I have provided an image showing the intended PCB architecture. Treat that architecture image as the starting point, but DO NOT blindly assume that every component, pinout, package, electrical characteristic, or connection shown in the image is technically correct.

Your job is to turn this architecture into a professional, manufacturable prototype PCB design workflow for Autodesk Fusion Electronics / EAGLE-compatible files.

IMPORTANT:
This is an engineering task, not a visual mockup.

The final result must prioritize:
1. Electrical correctness
2. Correct manufacturer pinouts
3. Correct component packages
4. Correct footprints
5. Correct schematic connectivity
6. ERC/DRC compatibility
7. Manufacturability
8. Clear documentation
9. Only then visual quality

DO NOT invent technical information.

============================================================
PART 1 — UNDERSTAND THE PROJECT
============================================================

First carefully analyze the provided architecture image.

The architecture contains the following major blocks:

POWER ENTRY
- Li-Po 3.7 V battery
- JST connector
- TP4056 protected charging module / charger section
- MAX17048 fuel gauge
- 3.3 V regulation

CENTRAL MCU
- ESP32-S3
- BLE
- Wi-Fi
- I2C
- ADC inputs
- GPIO alerts
- Sensor interfaces

ECG
- 3 electrodes
- AD8232
- ECG analog output to ESP32 ADC
- LO+/LO- optional lead-off detection
- Keep analog path short and quiet

MOTION / ANGLE
- LSM6DSOX
- I2C
- AS5600
- I2C
- Optional INT1 / INT2 GPIO
- Potentially one AS5600 per side if the mechanical design requires it

MECHANICAL SENSING
- Load cell
- HX711
- FSR x4
- resistor dividers
- stretch sensor
- signal conditioning
- piezo
- limit/Hall sensor

ALERTS
- GPIO-controlled MOSFET
- vibration motor
- GPIO-controlled MOSFET
- buzzer
- LED + resistor
- flyback diode across vibration motor

USER INPUT / STORAGE
- SOS pushbutton
- GPIO + pull-up
- optional microSD via SPI
- status LED / RGB LED
- firmware debounce and fault handling

I2C BUS
- shared SDA/SCL
- TMP117
- LSM6DSOX
- AS5600
- MAX17048

============================================================
PART 2 — DO NOT ASSUME PART NUMBERS
============================================================

Before creating any final symbol, footprint, schematic or PCB file:

Determine the EXACT component variant and package wherever possible.

For every IC/module/sensor, verify:

- Manufacturer
- Exact part number
- Package
- Package dimensions
- Pin numbering
- Pin names
- Electrical function of every pin
- Power supply requirements
- Absolute maximum ratings where relevant
- Recommended operating voltage
- Required bypass/decoupling capacitors
- Required pull-ups/pull-downs
- Analog/digital characteristics
- Communication interface
- Address configuration
- Interrupt pins
- Enable/shutdown pins
- Ground pins
- Exposed pad if applicable
- Thermal requirements if applicable
- Mechanical dimensions
- Recommended PCB land pattern

Use PRIMARY MANUFACTURER DOCUMENTATION wherever possible.

Preferred sources:
1. Manufacturer datasheet
2. Manufacturer hardware design guide/reference design
3. Manufacturer package/land-pattern documentation
4. Manufacturer application notes
5. Distributor documentation only as secondary verification

DO NOT rely on random online pinout diagrams when an official datasheet exists.

If multiple variants exist, determine the most appropriate one for this prototype.

If the exact part number cannot be determined from the architecture, investigate likely variants and clearly identify the assumption.

If a critical part-number/package ambiguity remains that could make the PCB physically or electrically wrong, STOP that specific component from being finalized and clearly mark it as REQUIRES USER CONFIRMATION rather than inventing a footprint.

============================================================
PART 3 — COMPONENT RESEARCH TABLE
============================================================

Before generating the final library, create:

COMPONENT_VERIFICATION.md

For EVERY component include:

| Component | Manufacturer | Exact Part | Package | Supply | Interface | Pinout Verified | Footprint Verified | Source |
|------------|--------------|------------|---------|--------|-----------|-----------------|--------------------|--------|

Also include:

- What source was used
- Date/version of datasheet if available
- Any uncertainty
- Any design assumption
- Whether the component is an actual IC or a breakout/module
- Whether the footprint is for the IC itself or a prebuilt module

Do not proceed with unverified pin mappings.

============================================================
PART 4 — COMPONENT CLASSIFICATION
============================================================

Separate the components into:

A. MAIN ICs
B. SENSOR ICs
C. MODULES
D. CONNECTORS
E. PASSIVES
F. ELECTROMECHANICAL COMPONENTS
G. PROTECTION COMPONENTS
H. POWER COMPONENTS

Do not confuse a breakout board/module with the underlying IC.

For example:

If the architecture says "TP4056 module", determine whether the PCB should contain:
- a TP4056 IC directly,
OR
- a commercially available TP4056 charging module connected through headers.

Do the same for:
- ESP32-S3
- HX711
- AD8232
- any other module-like component.

For the prototype, prefer direct IC implementation where practical, but do not redesign the architecture unnecessarily.

============================================================
PART 5 — CREATE THE EAGLE/FUSION LIBRARY
============================================================

Create an Autodesk Fusion Electronics / EAGLE-compatible library.

The output should be a real usable library, NOT an image and NOT a text description.

Target deliverables should include, where supported:

SIH26113_Maternity_Assist_Belt.lbr

and/or the appropriate Fusion Electronics library format.

The library must contain:

1. Schematic symbols
2. PCB footprints/packages
3. Device mappings between symbol pins and footprint pads
4. Appropriate 3D/package information where practical

For every symbol:

- Correct pin numbers
- Correct pin names
- Correct pin direction
- Correct electrical type
- Correct power pins
- Correct input/output designation
- Correct bidirectional designation
- Correct passive designation
- Correct open-drain/open-collector designation where applicable
- Correct power-input designation
- Correct no-connect handling where appropriate

Pin electrical types should be chosen correctly.

Examples:
- INPUT
- OUTPUT
- BIDIRECTIONAL
- POWER INPUT
- POWER OUTPUT
- PASSIVE
- OPEN COLLECTOR
- TRI-STATE
- etc.

Do NOT simply mark everything as passive to avoid ERC errors.

The symbol should be readable and logically grouped.

For complex ICs:
- Group power pins logically
- Group analog pins logically
- Group digital communication pins logically
- Group GPIO pins logically
- Clearly identify unused pins
- Clearly identify exposed pads

============================================================
PART 6 — FOOTPRINT CREATION
============================================================

Every footprint must be based on the manufacturer's mechanical drawing / recommended land pattern.

Verify:

- Pad count
- Pad numbering
- Pad dimensions
- Pad pitch
- Row spacing
- Overall package dimensions
- Courtyard
- Silkscreen
- Pin 1 marker
- Assembly outline
- Exposed pad
- Thermal vias if required
- Hole sizes
- Connector dimensions
- Mechanical keepouts

Do not estimate package dimensions from an image.

For connectors and mechanical components, use real dimensions where available.

For modules, use the dimensions of the ACTUAL MODULE rather than the underlying IC.

============================================================
PART 7 — PIN DIRECTION ANNOTATION
============================================================

The user specifically requires annotated pin directions and types.

Make the symbols clearly communicate:

PIN NUMBER
PIN NAME
DIRECTION
ELECTRICAL TYPE

Example:

1 VCC POWER INPUT
2 GND POWER INPUT
3 SDA BIDIRECTIONAL
4 SCL INPUT
5 INT OUTPUT
6 OUT ANALOG OUTPUT

Where the EDA software supports electrical pin types, set the actual EDA pin type accordingly.

Do not merely write "INPUT" as decorative text.

============================================================
PART 8 — POWER ARCHITECTURE
============================================================

Analyze the power architecture before drawing the schematic.

Starting concept:

Li-Po battery
↓
Protection / charging
↓
Power distribution
↓
3.3 V regulator
↓
3.3 V digital + sensor rail

Determine whether the proposed TP4056 arrangement is electrically appropriate.

Check:
- Battery charging
- Battery protection
- Reverse polarity
- USB power entry if applicable
- Charger output
- Battery output
- System load path
- Regulator input range
- Regulator current capability
- ESP32-S3 peak current requirements
- Sensor current requirements
- Motor current
- Buzzer current
- Voltage drops
- Grounding
- Decoupling

DO NOT connect the Li-Po directly to components that cannot tolerate the battery voltage.

If a component requires 3.3 V, ensure it receives the correct regulated rail.

Create clearly named power nets such as:

VBAT
VBUS
3V3
GND
AGND
DGND

Only use separate AGND/DGND if there is a legitimate reason.

============================================================
PART 9 — ESP32-S3
============================================================

Treat ESP32-S3 as the central MCU.

Determine the exact ESP32-S3 implementation.

Prefer an ESP32-S3 module for prototype reliability if appropriate, rather than the bare chip, unless the architecture explicitly requires otherwise.

Verify:

- Exact module
- Pinout
- Antenna location
- Antenna keepout
- Flash/PSRAM configuration if relevant
- Boot pins
- Reset/EN
- USB interface if applicable
- UART
- I2C
- SPI
- ADC
- GPIO availability
- GPIO boot restrictions
- Power requirements

Do not assign GPIOs randomly.

Create a GPIO allocation table:

GPIO
FUNCTION
DIRECTION
DEFAULT STATE
CONNECTED COMPONENT
NOTES

Avoid:
- boot-strapping conflicts
- unavailable ADC channels
- pins reserved for internal functions
- pins that create unexpected boot behavior

============================================================
PART 10 — I2C BUS
============================================================

Create one clearly documented I2C bus.

Suggested logical structure:

3V3
|
+---- TMP117
|
+---- LSM6DSOX
|
+---- AS5600
|
+---- MAX17048
|
ESP32-S3

Use:

I2C_SDA
I2C_SCL

Verify all device addresses.

Check for address conflicts.

Check whether any device has configurable address pins.

Calculate whether pull-ups are appropriate.

Do not blindly add one pull-up pair per device.

Use a sensible common I2C pull-up arrangement based on:
- bus voltage
- bus capacitance
- expected speed
- number of devices

Document the chosen pull-up values.

============================================================
PART 11 — ECG / AD8232
============================================================

Treat ECG as a sensitive analog subsystem.

Do not simply connect:

electrodes → AD8232 → ESP32

without reviewing the complete recommended application circuit.

Verify the official AD8232 reference design/application circuit.

Include required:
- resistors
- capacitors
- gain configuration
- filtering
- reference
- right-leg drive if applicable
- lead-off detection if used
- supply decoupling
- output filtering
- protection appropriate for the intended prototype

Clearly distinguish:

ECG analog ground
digital ground
ADC input

Keep the analog signal path short.

Keep ECG away from:
- vibration motor
- buzzer
- switching regulator
- high-current traces
- noisy digital interfaces
- ESP32 antenna region

Add test points where useful.

IMPORTANT SAFETY NOTE:

This is a wearable human-connected ECG prototype.

Do not claim medical-device safety or clinical suitability.

Clearly document electrical isolation, protection and prototype limitations.

Do not create a design that implies the device is medically certified.

============================================================
PART 12 — LOAD CELL / HX711
============================================================

Verify the exact load cell configuration.

Determine:
- bridge configuration
- excitation voltage
- signal range
- HX711 supply
- gain
- sample rate
- wiring
- connector

Create:

LOADCELL_A+
LOADCELL_A-
LOADCELL_B+
LOADCELL_B-

or appropriate names based on the actual configuration.

Do not assume wire colors.

Use the actual load-cell datasheet if available.

============================================================
PART 13 — FSR SENSORS
============================================================

For each FSR:

Create an appropriate voltage-divider circuit.

Determine suitable resistor values based on:
- FSR resistance range
- desired sensing range
- ADC range
- noise
- current consumption

Do not simply use arbitrary 10k resistors without analysis.

Label:

FSR1_ADC
FSR2_ADC
FSR3_ADC
FSR4_ADC

If filtering is beneficial, include an appropriate RC filter.

Verify ESP32-S3 ADC limitations.

============================================================
PART 14 — STRETCH SENSOR
============================================================

Treat the stretch sensor as a variable-resistance/analog sensor unless the actual device documentation specifies otherwise.

Determine:
- resistance range
- nominal resistance
- measurement configuration
- divider resistor
- filtering
- ADC compatibility

Create:

STRETCH_ADC

Do not invent its resistance range.

============================================================
PART 15 — PIEZO SENSOR
============================================================

Determine whether the piezo is being used as:

- vibration/impact sensor
- pressure sensor
- audio sensor
- alert actuator

If used as a sensor:
- provide suitable protection
- consider the potentially high transient voltage from piezo elements
- use appropriate conditioning before ESP32 ADC

Do not connect a raw piezo directly to an MCU ADC without checking the voltage range and transient behavior.

============================================================
PART 16 — MOTION / ANGLE
============================================================

LSM6DSOX:

Verify:
- VDD
- VDDIO
- SDA
- SCL
- INT1
- INT2
- address selection
- decoupling

AS5600:

Verify:
- supply
- I2C pins
- address
- OUT pin if used
- programming/configuration pins
- magnet/mechanical requirements

If two AS5600 sensors are required, determine how their addresses or bus architecture should work.

If the same fixed I2C address creates a conflict, solve it correctly.

Do not invent a second address.

============================================================
PART 17 — BATTERY FUEL GAUGE
============================================================

MAX17048:

Verify:
- battery connection
- VCC
- GND
- SDA
- SCL
- ALRT
- required capacitors
- battery measurement configuration

Ensure the battery gauge is actually connected to the battery/system rail as recommended by the manufacturer.

============================================================
PART 18 — TEMPERATURE SENSOR
============================================================

TMP117:

Verify:
- VCC
- GND
- SDA
- SCL
- address pins
- ALERT pin if used
- decoupling

Add the device to the shared I2C bus.

============================================================
PART 19 — SOS BUTTON
============================================================

Create:

SOS_BUTTON

with:
- GPIO input
- pull-up or pull-down
- debouncing strategy
- optional RC hardware debounce only if justified
- ESD consideration
- clearly labeled net

Example logical net:

SOS_GPIO

============================================================
PART 20 — VIBRATION MOTOR
============================================================

DO NOT drive the vibration motor directly from ESP32 GPIO.

Use:

ESP32 GPIO
↓
MOSFET gate
↓
MOSFET
↓
Vibration motor
↓
VBAT / appropriate rail

Include:
- appropriate MOSFET
- gate resistor if appropriate
- gate pull-down if appropriate
- flyback diode for inductive motor
- appropriate power routing
- adequate current capability

Verify motor voltage/current before selecting the MOSFET.

Label:

MOTOR_EN

============================================================
PART 21 — BUZZER
============================================================

Determine whether the buzzer is:
- active
- passive
- magnetic
- piezo

Select the appropriate drive circuit.

Do not assume the buzzer can be driven directly from GPIO.

If transistor/MOSFET driving is required, implement it.

Label:

BUZZER_EN

============================================================
PART 22 — LED / RGB LED
============================================================

For each LED:
- calculate current limiting resistor
- verify GPIO current
- determine common anode/common cathode if RGB
- document polarity

Do not omit current limiting resistors.

============================================================
PART 23 — MICROSD
============================================================

If microSD is included:

Use SPI.

Verify:
- VDD
- GND
- CS
- MOSI
- MISO
- SCK
- pull-ups if required
- level compatibility
- connector footprint
- card-detect pin if available/used
- decoupling

Keep SPI routing sensible.

============================================================
PART 24 — PROTECTION
============================================================

Review the complete design for:

- reverse polarity
- ESD
- battery protection
- overcurrent
- short circuit
- motor transients
- piezo transients
- connector protection
- USB protection if USB is included
- GPIO overvoltage
- ADC overvoltage

Do not add unnecessary protection components just to make the BOM larger.

Every protection component should have a reason.

============================================================
PART 25 — SCHEMATIC
============================================================

Generate the complete schematic.

The schematic must show:

- Every component
- Every reference designator
- Every pin
- Every wire
- Every net
- Every power connection
- Every ground
- Every pull-up/pull-down
- Every decoupling capacitor
- Every protection component
- Every connector
- Test points where useful

Use clean hierarchical organization.

Recommended schematic blocks:

PAGE 1:
POWER

PAGE 2:
ESP32-S3 + CORE

PAGE 3:
I2C SENSORS

PAGE 4:
ECG ANALOG FRONT END

PAGE 5:
MECHANICAL SENSORS

PAGE 6:
ALERTS

PAGE 7:
USER INPUT / STORAGE

Use net labels instead of unnecessarily long wires.

Clearly show connections.

============================================================
PART 26 — SCHEMATIC IMAGE
============================================================

Also generate a high-resolution visual schematic/reference image.

It must show:

- Actual components
- Reference designators
- Pin numbers
- Pin names where practical
- Wires
- Net labels
- Power rails
- Ground
- Major subsystem boundaries

The image must be useful while manually inspecting the PCB.

Do not create a decorative block diagram.

It must correspond to the actual generated schematic.

If possible, render/export the actual EDA schematic rather than drawing a separate fake representation.

============================================================
PART 27 — PCB DESIGN
============================================================

After the schematic is validated, create/update the PCB.

Do NOT place components randomly.

Create a logical placement strategy.

Suggested zones:

ZONE 1:
Power / charging

ZONE 2:
ESP32-S3

ZONE 3:
ECG analog

ZONE 4:
I2C sensors

ZONE 5:
Mechanical sensor interfaces

ZONE 6:
Motor / buzzer drivers

ZONE 7:
MicroSD / digital interfaces

Keep high-noise circuits away from ECG.

Keep the ESP32 antenna area clear.

Keep switching/high-current paths short.

Place decoupling capacitors close to their IC power pins.

Place bulk capacitors close to power entry/regulator.

Place connectors according to actual mechanical requirements.

============================================================
PART 28 — PCB GROUNDING
============================================================

Use a proper ground strategy.

Prefer a solid ground plane where appropriate.

For ECG:
- carefully consider analog grounding
- avoid motor return currents through sensitive analog paths
- keep noisy return currents away from ECG input circuitry

Do not create random ground islands.

Explain the grounding strategy in:

GROUNDING_NOTES.md

============================================================
PART 29 — PCB ROUTING
============================================================

Prioritize routing in this order:

1. Critical analog ECG signals
2. Power
3. Ground
4. High-current motor/buzzer paths
5. I2C
6. SPI
7. GPIO
8. Other signals

Use sensible trace widths.

Calculate/justify power trace widths based on expected current.

Keep ECG traces short.

Avoid routing noisy digital traces alongside ECG input traces.

Do not route motor current through sensitive analog ground paths.

============================================================
PART 30 — ERC
============================================================

Run electrical-rule validation.

Identify:
- unconnected pins
- incorrect power pins
- conflicting outputs
- missing power sources
- floating inputs
- missing pull-ups
- invalid GPIO connections
- wrong pin types
- duplicated drivers
- accidental shorts

Do NOT simply suppress ERC warnings.

Every warning should be:

1. Fixed
2. Intentionally marked as no-connect
3. Documented as an intentional exception

Create:

ERC_REPORT.md

============================================================
PART 31 — DRC
============================================================

Run design-rule validation.

Check:
- clearances
- trace widths
- vias
- board edge clearance
- courtyard overlaps
- silkscreen overlaps
- pad issues
- unconnected nets
- antenna keepout
- drill sizes
- manufacturability

Create:

DRC_REPORT.md

Do not claim DRC passed unless you actually checked it.

============================================================
PART 32 — NETLIST
============================================================

Generate a complete:

NETLIST.md

For each net:

NET NAME
SOURCE
DESTINATIONS
SIGNAL TYPE
VOLTAGE
NOTES

Example:

I2C_SDA
ESP32-S3 GPIO
TMP117 SDA
LSM6DSOX SDA
AS5600 SDA
MAX17048 SDA
3V3
Bidirectional

============================================================
PART 33 — GPIO TABLE
============================================================

Generate:

GPIO_ASSIGNMENT.md

with:

GPIO
FUNCTION
INPUT/OUTPUT
BOOT CRITICAL?
ADC?
I2C?
SPI?
INT?
CONNECTED COMPONENT
NOTES

Avoid conflicts.

============================================================
PART 34 — BOM
============================================================

Generate:

BOM.csv

and:

BOM.md

Include:

Reference
Quantity
Manufacturer
Manufacturer Part Number
Description
Package
Value
Supplier if confidently known
Notes
Lifecycle/availability if verified

Do not fabricate supplier SKUs.

If exact supplier information is unavailable, leave it blank rather than inventing it.

============================================================
PART 35 — DESIGN ASSUMPTIONS
============================================================

Generate:

DESIGN_ASSUMPTIONS.md

Document every assumption.

Examples:

- ESP32-S3 module selected because...
- Regulator selected because...
- FSR resistor selected because...
- I2C pull-up selected because...
- Motor MOSFET selected because...
- ECG filtering selected based on...
- AS5600 configuration...
- microSD included/excluded because...

============================================================
PART 36 — USER-CONFIRMATION ITEMS
============================================================

Generate:

REQUIRES_CONFIRMATION.md

Only put genuinely unresolved critical items here.

Examples:

[ ] Exact ESP32-S3 module
[ ] Exact load-cell model
[ ] Exact stretch sensor model
[ ] Exact vibration motor current
[ ] Exact buzzer type
[ ] Exact connector dimensions

Do not stop the whole project unnecessarily.

Proceed with everything that can be verified independently.

For unresolved components, clearly mark placeholders rather than fabricating data.

============================================================
PART 37 — FILE STRUCTURE
============================================================

Organize the final project cleanly.

Suggested structure:

SIH26113_Maternity_Assist_Belt/
│
├── README.md
│
├── libraries/
│ └── SIH26113_Maternity_Assist_Belt.lbr
│
├── schematic/
│ └── SIH26113_Maternity_Assist_Belt.sch
│
├── pcb/
│ └── SIH26113_Maternity_Assist_Belt.brd
│
├── documentation/
│ ├── COMPONENT_VERIFICATION.md
│ ├── GPIO_ASSIGNMENT.md
│ ├── NETLIST.md
│ ├── BOM.md
│ ├── BOM.csv
│ ├── DESIGN_ASSUMPTIONS.md
│ ├── GROUNDING_NOTES.md
│ ├── ERC_REPORT.md
│ ├── DRC_REPORT.md
│ ├── REQUIRES_CONFIRMATION.md
│ └── PCB_BUILD_GUIDE.md
│
├── renders/
│ ├── schematic.png
│ ├── pcb_top.png
│ ├── pcb_bottom.png
│ └── pcb_3d.png
│
└── scripts/
├── generate_library.*
├── generate_schematic.*
└── validation.*

Use the actual file formats supported by the selected Autodesk/Fusion/EAGLE workflow.

============================================================
PART 38 — PCB BUILD GUIDE
============================================================

Create:

PCB_BUILD_GUIDE.md

Give me a beginner-friendly but technically accurate sequence:

STEP 1
Install/open Autodesk Fusion.

STEP 2
Import the library.

STEP 3
Verify library symbols.

STEP 4
Create schematic.

STEP 5
Assign footprints.

STEP 6
Run ERC.

STEP 7
Fix ERC errors.

STEP 8
Generate/update PCB.

STEP 9
Define board outline.

STEP 10
Place components.

STEP 11
Route critical analog signals.

STEP 12
Route power.

STEP 13
Route digital signals.

STEP 14
Add/verify ground plane.

STEP 15
Run DRC.

STEP 16
Fix DRC errors.

STEP 17
Inspect 3D PCB.

STEP 18
Check mechanical clearances.

STEP 19
Generate manufacturing outputs.

STEP 20
Final review.

For every step explain:
- What to click/do
- What to check
- What can go wrong
- How to verify success

============================================================
PART 39 — MANUFACTURING CHECK
============================================================

Before declaring the design complete, check:

- PCB dimensions
- board thickness assumption
- layer count
- copper thickness assumption
- via sizes
- minimum trace width
- minimum clearance
- drill sizes
- component courtyard
- connector accessibility
- antenna keepout
- mounting holes
- assembly feasibility
- component availability
- polarity markings
- pin 1 markings
- silkscreen readability

Do not assume a manufacturer capability unless verified.

============================================================
PART 40 — TEST POINTS
============================================================

Add useful test points for:

VBAT
3V3
GND
I2C_SDA
I2C_SCL
ECG_OUT
MOTOR_EN
BUZZER_EN
SOS_GPIO

Add additional test points if useful.

============================================================
PART 41 — DESIGN FOR DEBUGGING
============================================================

The prototype should be easy to debug.

Include where practical:

- UART/programming access
- reset
- boot
- power test points
- sensor test points
- ECG output test point
- I2C test points
- important GPIO test points

Do not sacrifice PCB quality just to add unnecessary test points.

============================================================
PART 42 — FINAL ENGINEERING REVIEW
============================================================

Before completing the task, perform a second independent review.

Pretend you are reviewing another engineer's PCB before fabrication.

Look specifically for:

1. Wrong pin numbers
2. Wrong footprints
3. Wrong power connections
4. Missing grounds
5. Missing decoupling
6. I2C address conflicts
7. ESP32 boot-pin conflicts
8. ADC limitations
9. Motor current problems
10. Buzzer drive problems
11. ECG noise problems
12. Piezo overvoltage
13. Battery charging problems
14. Regulator capacity problems
15. Connector polarity
16. Missing protection
17. Incorrect MOSFET orientation
18. Incorrect diode orientation
19. Incorrect LED polarity
20. Missing current-limiting resistors
21. Floating inputs
22. Unused pins
23. Antenna keepout
24. PCB mechanical conflicts
25. Unrouted nets
26. ERC issues
27. DRC issues

============================================================
PART 43 — NO FAKE COMPLETION
============================================================

This is extremely important.

NEVER say:

"Done"

merely because files were generated.

Only declare a deliverable complete when:

- file exists
- file is structurally valid
- symbols exist
- footprints exist
- device mappings exist
- pins map correctly
- schematic connections are correct
- required power connections are present
- ERC has been reviewed
- DRC has been reviewed
- unresolved assumptions are documented

If you cannot actually run a particular validation because the required EDA software/tool is unavailable, say:

"NOT EXECUTED — TOOL UNAVAILABLE"

Do NOT falsely claim that ERC/DRC passed.

============================================================
PART 44 — AUTONOMOUS WORKFLOW
============================================================

Work autonomously.

Do not constantly ask me for permission to perform obvious next steps.

Your workflow should be:

ANALYZE
↓
RESEARCH
↓
VERIFY
↓
DESIGN
↓
GENERATE
↓
VALIDATE
↓
FIX
↓
RE-VALIDATE
↓
DOCUMENT
↓
FINAL REVIEW

If one component has an unresolved ambiguity:

- continue designing the rest
- create a clearly marked placeholder only where safe
- document the issue
- do not fabricate the missing technical information

Do not stop after generating the first version.

Iterate until the design is internally consistent.

============================================================
PART 45 — IMPORTANT DISTINCTION
============================================================

There are THREE different levels of completion:

LEVEL 1:
Architecture

LEVEL 2:
Electrical schematic + verified component library

LEVEL 3:
Manufacturable PCB

Do not pretend LEVEL 1 is LEVEL 3.

Clearly state the current level.

============================================================
PART 46 — FINAL OUTPUT
============================================================

At the end, provide a concise final report containing:

1. What was created
2. Exact files generated
3. Exact components used
4. Exact component variants
5. Any unresolved components
6. Important design assumptions
7. ERC status
8. DRC status
9. Number of nets
10. Number of components
11. PCB dimensions
12. Layer count
13. Important risks
14. What I need to verify physically
15. Exact next steps in Autodesk Fusion

Also provide direct links/paths to every generated file.

============================================================
PART 47 — QUALITY STANDARD
============================================================

The result should look like it was prepared by a professional PCB engineer.

Avoid:
- messy schematic wiring
- random component placement
- decorative diagrams
- fake footprints
- guessed pinouts
- arbitrary resistor values
- arbitrary trace widths
- missing power connections
- incorrect pin directions
- incorrect package mappings
- unexplained ERC suppressions
- unexplained DRC suppressions

The design should be:
- clean
- readable
- logical
- maintainable
- debuggable
- manufacturable
- well documented

============================================================
PART 48 — START NOW
============================================================

Start by inspecting the provided SIH26113 Maternity Assist Belt architecture image.

Then:

1. Extract every component and subsystem.
2. Create a preliminary component list.
3. Research and verify exact components.
4. Identify ambiguities.
5. Build the component verification table.
6. Create the library.
7. Create the schematic.
8. Validate the schematic.
9. Create the PCB.
10. Validate the PCB.
11. Generate the schematic reference image.
12. Generate PCB renders.
13. Generate BOM.
14. Generate all engineering documentation.
15. Perform the independent final engineering review.
16. Fix anything you discover.
17. Re-run validation.
18. Give me the final project files and build instructions.

DO NOT optimize for speed.

Optimize for correctness.

DO NOT invent information.

When a manufacturer datasheet exists, use it.

When a package drawing exists, use it.

When a reference design exists, study it.

When you make an engineering assumption, document it.

The final deliverable must be something I can realistically open in Autodesk Fusion Electronics and continue working on.

IMPORTANT:
The attached architecture image is a conceptual starting point. You have permission to improve the architecture where technically necessary, but do not make major changes silently. Document every meaningful architectural change and explain why it was necessary.

