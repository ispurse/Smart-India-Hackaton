// Project data for Smart Maternity Band website
// This data is sourced from the project brief and should not contain fabricated information

const projectData = {
  projectInfo: {
    event: "Smart India Hackathon 2026",
    theme: "HealthTech",
    category: "Hardware",
    team: "TEAM ROCKET 🚀",
    project: "SMART MATERNITY BAND",
    problemStatementId: "SIH26113",
    purpose: [
      "Lower physical stress during pregnancy",
      "Help pregnant women move more comfortably",
      "Continuously track mother and baby health"
    ],
    concept: "A dual-layer wearable combining mechanical support (lower lumbar + belly sling), wearable electronics and sensors, ESP32 + BLE connectivity, a mobile/web application, and emergency response features."
  },

  features: [
    "Fetal movement sensing",
    "Blood pressure, metabolism, and musculoskeletal measurement",
    "Sleep cycle and activity measurement (for mental health insight)",
    "Smart health-suggestion app",
    "Daily recommendations (physical exercise, diet, etc.) — frame as general wellness guidance, never as medical prescriptions"
  ],

  softwareFeatures: [
    "Shape trends / growth chart",
    "Kick counter with daily trend",
    "Fall detection → push notification to an emergency contact",
    "Alerts"
  ],

  // Note: Predicted delivery, predicted recovery time, and belly heatmap are NOT FEASIBLE

  sensorSystem: [
    "BLE communication",
    "Sensor fusion",
    "Control loop",
    "IMU (inertial measurement unit)"
  ],

  mechanicalDesign: {
    twoPanelSystem: {
      lowerLumbarPanel: "counterweight rail, IMU, and electronics pod",
      bellySupportSling: "grid of independent fabric cells, lightweight flexible spine, POM (polyoxymethylene) structural elements"
    },
    passiveElasticResistance: true,
    designedToGrowWithPregnancy: true,
    mechanicalConstructionDetails: [
      "Elastic fabric outer layer (carries no structural load — a 'skin')",
      "Flexible TPU/thermoplastic ribs that curve with the belly",
      "Low-friction nylon/UHMWPE sliding channel rails so adjacent panels telescope over one another",
      "Magnetic + hook-and-loop micro-adjustment, fine position lock every 10–15 mm of travel",
      "Thin gel or closed-cell foam load-distributing pads under panel overlaps",
      "Telescropic ribs with spring-loaded joints and detents so ribs self-center"
    ],
    fourZoneSupportMap: [
      { zone: "Front", support: "Soft — gentle upward support" },
      { zone: "Left (medial)", support: "Moderate — inward support" },
      { zone: "Right (medial)", support: "Moderate — inward support" },
      { zone: "Back", support: "Firm — posterior / hip support" }
    ]
  },

  bom: [
    { function: "Main MCU + BLE/Wi-Fi", component: "ESP32-S3 DevKit", qty: 1, cost: "₹650–1,500", status: "Selected" },
    { function: "Maternal HR + SpO₂", component: "MAX30102 module", qty: 1, cost: "₹130–250", status: "Selected for prototype" },
    { function: "Body/skin temperature", component: "TMP117 (or DS18B20 alt.)", qty: 1, cost: "₹150–450", status: "Under evaluation" },
    { function: "Pelvic/torso motion", component: "LSM6DSOX (or MPU6050 alt.)", qty: 1, cost: "₹500–1,200", status: "Under evaluation" },
    { function: "Thigh motion / hip angle", component: "LSM6DSOX", qty: 1, cost: "₹500–1,200", status: "Recommended" },
    { function: "Fetal movement", component: "Piezo-film / flexible piezo sensor", qty: "3–4", cost: "₹100–250", status: "Availability risk noted" },
    { function: "Maternal abdominal shape", component: "Stretch/extension sensor or rotary encoder", qty: 1, cost: "₹100–400", status: "Proposed addition" },
    { function: "Emergency manual SOS", component: "Tactile/push button", qty: 1, cost: "₹10–30", status: "Proposed addition" },
    { function: "Local alert (haptic)", component: "Vibration motor", qty: 1, cost: "₹20–60", status: "Proposed addition" },
    { function: "Local audio alert", component: "Mini buzzer", qty: 1, cost: "₹10–30", status: "Proposed addition" },
    { function: "Battery", component: "3.7V Li-Po, 1500–2000 mAh", qty: 1, cost: "₹250–450", status: "Selected" },
    { function: "Charging", component: "TP4056 protected module", qty: 1, cost: "₹20–50", status: "Selected for prototype" },
    { function: "Battery monitoring", component: "MAX17048 fuel gauge", qty: 1, cost: "₹100–300", status: "Recommended" },
    { function: "Data storage", component: "MicroSD module", qty: 1, cost: "₹80–150", status: "Optional" },
    { function: "Belt pressure", component: "FSR402", qty: 4, cost: "₹155–350", status: "Proposed addition" },
    { function: "Spring force", component: "Load cell", qty: 1, cost: "₹200–700", status: "Proposed addition" },
    { function: "Load-cell amplifier", component: "HX711", qty: 1, cost: "₹100–200", status: "Proposed addition" }
  ],

  estimatedCosts: {
    electronics: "₹3,740–₹9,370 (avg. ~₹6,600)",
    totalProduct: "₹10,000–₹20,000",
    note: "Present these only as internal engineering estimates, explicitly labeled, never as a finished retail price or certified BOM."
  },

  growthStageReference: [
    { stage: "Early pregnancy (Tri 1)", circumference: "~65–75 cm", state: "Compact, ribs fully nested", emphasis: "Posture guidance, light support" },
    { stage: "Mid pregnancy (Tri 2)", circumference: "~75–95 cm", state: "Panel 1 slides out", emphasis: "Load support increases" },
    { stage: "Late pregnancy (Tri 3)", circumference: "~95–120 cm", state: "Panels 2 & 3 slide, max extension", emphasis: "Full load redistribution" },
    { stage: "Postpartum (0–12 wk)", circumference: "~80–95 cm (tightening)", state: "Ribs re-nest, tension increases", emphasis: "Core recovery, gentle compression"
  }],

  knownLimitations: [
    "Blood pressure and heart rate are difficult to measure accurately from a belt form factor; a wrist-worn companion is one option under evaluation.",
    "Predicted delivery date, predicted recovery time, and belly heatmap visualization were explored and marked not currently feasible.",
    "The core mechanical assembly still needs one component fully prototyped for CNC manufacture.",
    "Component and cost figures are internal engineering estimates from the working BOM, not finalized or certified."
  ],

  priorArt: [
    "A wearable brand with heart-rate sensors that sync to an app — noted in source as not yet deployed, still in ideation/prototype stage",
    "A sensor-based adhesive bandage/pad-style device with no mechanical assistance",
    "A sensor-based belt used to predict premature birth, with no mechanical assistance"
  ],

  alternatives: [
    "Adding a wrist-worn companion device that connects over the network for HR/BP sensing.",
    "Making the thigh spring mechanism detachable from the main belt, with a one-pull mechanical release, used only under defined protocols (e.g., sitting/standing transitions only).",
    "Using two IMUs to reduce false alerts, plus a 30-second cancellation window before an SOS/alert is sent, and a dedicated external SOS button.",
    "Rather than having the microcontroller actively operate a fall-prevention/spring mechanism, using a passive cam-based mechanism that does not prevent a fall but reduces the time between the event and an assistance alert.",
    "The sitting-to-standing spring-assist mechanism as the single highlighted, 3-axis-CNC-manufacturable component for demonstration purposes."
  ],

  benefits: [
    { id: 1, title: "ERGONOMIC BACK SUPPORT", description: "Dual-panel system provides lumbar and abdominal support through overlapping flexible panels that grow with pregnancy." },
    { id: 2, title: "AUTOMATED SAFETY", description: "Fall detection with SOS button and 30-second cancellation window for emergency alerts." },
    { id: 3, title: "HYGIENIC & WASHABLE", description: "Elastic fabric outer layer designed to be removable and washable for hygiene." },
    { id: 4, title: "WELLNESS GUIDANCE", description: "Smart health-suggestion app providing daily wellness recommendations for exercise, diet, and lifestyle." },
    { id: 5, title: "MOOD / ACTIVITY TRACKING", description: "Sleep cycle and activity measurement for mental health insight." },
    { id: 6, title: "ADAPTIVE FIT ACROSS TRIMESTERS", description: "Overlapping flexible panels designed to grow with the pregnancy from trimester 1 to postpartum." }
  ],

  technologyStack: [
    { name: "ESP32", description: "Acts as the controller that reads wearable sensor information and communicates with the mobile application." },
    { name: "BLE", description: "Provides the connection between the wearable electronics and the mobile application." },
    { name: "IMU", description: "Tracks movement, posture, and activity levels for health monitoring." },
    { name: "HR/SpO₂", description: "Monitors heart rate and blood oxygen saturation levels." },
    { name: "PRESSURE", description: "Measures belt pressure for support optimization and uterine activity monitoring." },
    { name: "TEMPERATURE", description: "Tracks body/skin temperature for fever detection and thermal comfort." },
    { name: "FETAL-MOVEMENT SENSOR", description: "Detects fetal movement patterns through piezoelectric film sensors." },
    { name: "LOAD CELL", description: "Measures spring force in the mechanical support system for load distribution analysis." }
  ],

  howItWorksSteps: [
    { step: 1, title: "SENSORS COLLECT", description: "Wearable sensors gather maternal and fetal health data including movement, temperature, heart rate, and more." },
    { step: 2, title: "ESP32 PROCESSES", description: "The ESP32 microcontroller processes sensor data and prepares it for transmission." },
    { step: 3, title: "BLE TRANSFERS", description: "Bluetooth Low Energy transmits processed data from the wearable to the mobile application." },
    { step: 4, title: "APP ANALYZES", description: "The mobile application analyzes the data to provide health insights, trends, and personalized guidance." },
    { step: 5, title: "ALERTS & GUIDANCE", description: "Users receive wellness recommendations, activity summaries, and safety alerts based on their data." },
    { step: 6, title: "SAFETY RESPONSE", description: "In case of detected falls or emergencies, the system triggers alerts with a 30-second cancellation window." }
  ],

  impactPoints: [
    { title: "EARLY RISK PREVENTION", description: "Continuous monitoring helps detect potential complications earlier than periodic check-ups alone." },
    { title: "RURAL ACCESSIBILITY", description: "Wearable technology can provide health monitoring in areas with limited access to healthcare facilities." },
    { title: "HEALTHCARE COST REDUCTION", description: "Preventive monitoring may reduce the need for emergency interventions and hospitalizations." },
    { title: "24/7 MONITORING", description: "Around-the-clock health tracking provides a complete picture of maternal and fetal wellbeing." }
  ],

  viabilityPoints: [
    { title: "HIGH-PRECISION SENSING", description: "Advanced sensors provide accurate health data for reliable monitoring." },
    { title: "ADAPTIVE STRUCTURE", description: "Overlapping panel design grows with pregnancy for consistent support throughout trimesters." },
    { title: "PASSIVE MONITORING", description: "Non-intrusive sensing allows for continuous data collection without user intervention." },
    { title: "AVAILABLE ELECTRONICS + LOCAL FABRICS/MATERIALS", description: "Utilizes readily available electronic components and locally sourced materials for scalability." }
  ],

  feasibilityCards: [
    { icon: "👕", title: "COMFORTABILITY & WEARABILITY", description: "Breathable, expandable overlapping-panel construction with magnetic/hook-and-loop micro-adjustment designed to adapt as pregnancy progresses." },
    { icon: "🦵", title: "POSTURE & HEALTH MONITORING", description: "Lower-lumbar IMU sensing for posture, sleep quality, and daily movement/kick-count tracking." },
    { icon: "🆘", title: "EMERGENCY RESPONSE", description: "Dual-IMU fall detection can generate alerts with a 30-second cancellation window before escalation." },
    { icon: "⚙️", title: "COMPONENT-LEVEL ENGINEERING", description: "Built around a defined, costed BOM (ESP32-S3, MAX30102, IMUs, piezo fetal-movement sensors, FSR pressure sensors, load cell) — present as an internal reference, not a finished/certified spec." },
    { icon: "🔒", title: "DATA PRIVACY", description: "User-controlled, phone-based data storage." }
  ],

  privacyInfo: {
    headline: "YOUR HEALTH DATA. YOUR CONTROL.",
    description: "All data stays on the user's phone unless the user chooses to share it.",
    note: "Simulated SHARE DATA interaction animating a user-controlled transfer. Do not claim encryption certifications or compliance standards unless documented."
  },

  teamInfo: {
    headline: "MEET TEAM ROCKET 🚀",
    description: "Building technology for safer and more comfortable maternity care.",
    note: "// ADD REAL TEAM MEMBER INFORMATION HERE IF/WHEN THE TEAM CHOOSES TO PUBLISH IT.\\n// Do not populate with invented or placeholder names."
  },

  finalSection: {
    headline: "REIMAGINING MATERNITY SUPPORT.",
    team: "TEAM ROCKET 🚀",
    project: "SMART MATERNITY BAND",
    event: "SMART INDIA HACKATHON 2026",
    sihId: "SIH26113",
    theme: "HEALTHTECH · HARDWARE"
  }
} as const;

export { projectData };
export type ProjectData = typeof projectData;