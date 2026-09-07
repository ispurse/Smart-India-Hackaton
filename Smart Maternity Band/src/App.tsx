import { useEffect, useMemo, useState } from 'react';
import type { CSSProperties } from 'react';
import { AnimatePresence, motion, useReducedMotion } from 'framer-motion';
import {
  Activity,
  AlertTriangle,
  ArrowUpRight,
  Bluetooth,
  Check,
  ChevronRight,
  CircleAlert,
  Cpu,
  HeartPulse,
  LockKeyhole,
  Menu,
  Move,
  Radio,
  RotateCcw,
  ShieldCheck,
  Smartphone,
  Sparkles,
  Thermometer,
  X,
} from 'lucide-react';
import { projectData } from './data/projectData';

type PhoneTab = 'trends' | 'alerts' | 'guidance';
type SosState = 'idle' | 'countdown' | 'cancelled' | 'sent';

const sensorItems = [
  { id: 'heart-rate', label: 'Heart rhythm', short: 'HR / SpO₂', icon: HeartPulse, detail: 'Maternal HR + SpO₂ is represented by the MAX30102 module selected for the prototype.', status: 'Concept sensor' },
  { id: 'temperature', label: 'Temperature', short: 'Skin temp.', icon: Thermometer, detail: 'Body/skin temperature sensing is under evaluation using a TMP117 or DS18B20 alternative.', status: 'Under evaluation' },
  { id: 'movement', label: 'Movement', short: 'Dual IMU', icon: Move, detail: 'IMU inputs support posture, activity and the fall-alert concept with a cancellable response window.', status: 'Concept sensor' },
  { id: 'pressure', label: 'Support pressure', short: 'FSR402', icon: Activity, detail: 'Belt-pressure sensing is a proposed addition for support optimisation and uterine activity monitoring.', status: 'Proposed addition' },
  { id: 'fetal-movement', label: 'Movement pattern', short: 'Piezo film', icon: Radio, detail: 'Piezo-film or flexible piezo sensing is included as a fetal-movement concept; availability risk is noted.', status: 'Concept sensor' },
  { id: 'sos', label: 'Safety control', short: 'Manual SOS', icon: AlertTriangle, detail: 'A dedicated external SOS button is a proposed addition for user-controlled assistance alerts.', status: 'Proposed addition' },
] as const;

const navItems = [
  ['Concept', 'concept'],
  ['Product lab', 'product-lab'],
  ['Engineering', 'engineering'],
  ['System', 'system'],
  ['Safety', 'safety'],
] as const;

function scrollToSection(id: string) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function SectionIntro({ eyebrow, title, copy, center = false }: { eyebrow: string; title: string; copy?: string; center?: boolean }) {
  return (
    <div className={`section-intro${center ? ' section-intro--center' : ''}`}>
      <p className="eyebrow"><span />{eyebrow}</p>
      <h2>{title}</h2>
      {copy && <p className="section-copy">{copy}</p>}
    </div>
  );
}

function BandIllustration({ activeSensor }: { activeSensor: string }) {
  return (
    <div className="band-stage" aria-label="Conceptual Smart Maternity Band illustration">
      <div className="stage-orbit stage-orbit--one" />
      <div className="stage-orbit stage-orbit--two" />
      <div className="band-shadow" />
      <div className="band-body">
        <div className="band-body__top" />
        <div className="band-body__center">
          <div className="band-grid" />
          <div className="band-sling" />
        </div>
        <div className="band-body__base">
          <i /><i /><i /><i /><i />
        </div>
        <div className="band-pod"><span /><span /><span /></div>
        <div className="band-clasp"><span /></div>
      </div>
      <div className={`band-hotspot band-hotspot--heart${activeSensor === 'heart-rate' ? ' is-active' : ''}`}><span /></div>
      <div className={`band-hotspot band-hotspot--temperature${activeSensor === 'temperature' ? ' is-active' : ''}`}><span /></div>
      <div className={`band-hotspot band-hotspot--movement${activeSensor === 'movement' ? ' is-active' : ''}`}><span /></div>
      <div className={`band-hotspot band-hotspot--pressure${activeSensor === 'pressure' ? ' is-active' : ''}`}><span /></div>
      <div className={`band-hotspot band-hotspot--fetal${activeSensor === 'fetal-movement' ? ' is-active' : ''}`}><span /></div>
      <div className={`band-hotspot band-hotspot--sos${activeSensor === 'sos' ? ' is-active' : ''}`}><span /></div>
      <p className="concept-label">Conceptual system illustration</p>
    </div>
  );
}

function PhoneDemo() {
  const [tab, setTab] = useState<PhoneTab>('trends');
  const tabs: { id: PhoneTab; label: string }[] = [
    { id: 'trends', label: 'Trends' },
    { id: 'alerts', label: 'Alerts' },
    { id: 'guidance', label: 'Guidance' },
  ];

  return (
    <div className="phone-shell">
      <div className="phone-hardware"><span /></div>
      <div className="phone-screen">
        <div className="phone-status"><span>9:41</span><span>● ● ●</span></div>
        <div className="phone-head"><div><p>Tuesday, 14 May</p><strong>Today</strong></div><span className="phone-avatar">R</span></div>
        <div className="demo-chip"><Sparkles size={12} /> DEMO DATA</div>
        <div className="phone-tabs" role="tablist" aria-label="Mobile app demo">
          {tabs.map((item) => (
            <button key={item.id} role="tab" aria-selected={tab === item.id} className={tab === item.id ? 'is-selected' : ''} onClick={() => setTab(item.id)}>{item.label}</button>
          ))}
        </div>
        <AnimatePresence mode="wait">
          {tab === 'trends' && (
            <motion.div className="phone-panel" key="trends" initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -8 }}>
              <div className="phone-card phone-card--hero"><p>Daily movement</p><div className="phone-stat"><strong>Balanced</strong><span>Concept trend</span></div><div className="mini-wave"><i /><i /><i /><i /><i /><i /><i /><i /><i /><i /><i /><i /></div></div>
              <div className="phone-metrics"><div><span className="metric-dot metric-dot--coral" /><p>Support fit</p><strong>Reviewed</strong></div><div><span className="metric-dot metric-dot--blue" /><p>Kick count</p><strong>Tracked</strong></div></div>
              <p className="phone-note">Interface states are illustrative—not clinical measurements.</p>
            </motion.div>
          )}
          {tab === 'alerts' && (
            <motion.div className="phone-panel" key="alerts" initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -8 }}>
              <div className="alert-card"><span className="alert-card__icon"><ShieldCheck size={18} /></span><div><strong>Safety controls ready</strong><p>Alert concepts include a 30-second cancellation window.</p></div></div>
              <div className="phone-row"><span>Movement check</span><strong>Review</strong></div><div className="phone-row"><span>Support reminder</span><strong>Today</strong></div>
              <p className="phone-note">Alerts shown here are interface concepts, not active notifications.</p>
            </motion.div>
          )}
          {tab === 'guidance' && (
            <motion.div className="phone-panel" key="guidance" initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -8 }}>
              <div className="guidance-card"><span><HeartPulse size={19} /></span><p>Wellness guidance</p><strong>Build an activity rhythm that feels comfortable.</strong><small>General wellness guidance only—not medical advice or a prescription.</small></div>
              <div className="phone-row"><span>Posture reflection</span><ChevronRight size={16} /></div><div className="phone-row"><span>Daily routine</span><ChevronRight size={16} /></div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}

function App() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [activeSensor, setActiveSensor] = useState<(typeof sensorItems)[number]['id']>('heart-rate');
  const [activeArchitecture, setActiveArchitecture] = useState(0);
  const [sosState, setSosState] = useState<SosState>('idle');
  const [countdown, setCountdown] = useState(30);
  const reducedMotion = useReducedMotion();

  const activeSensorDetail = useMemo(() => sensorItems.find((sensor) => sensor.id === activeSensor) ?? sensorItems[0], [activeSensor]);
  const architecture = [
    { title: 'Support system', description: 'Lower lumbar counterweight rail and belly-support sling create the mechanical foundation.', icon: Move },
    { title: 'Sensors + ESP32', description: 'Wearable inputs and an ESP32-S3 controller are organised as the electronics concept.', icon: Cpu },
    { title: 'BLE transfer', description: 'Bluetooth Low Energy is the stated link between the wearable and the mobile application.', icon: Bluetooth },
    { title: 'Mobile experience', description: 'A companion experience presents trends, general wellness guidance and user-controlled safety flows.', icon: Smartphone },
  ];

  useEffect(() => {
    if (sosState !== 'countdown') return;
    const timer = window.setInterval(() => {
      setCountdown((remaining) => {
        if (remaining <= 1) {
          window.clearInterval(timer);
          setSosState('sent');
          return 0;
        }
        return remaining - 1;
      });
    }, 1000);
    return () => window.clearInterval(timer);
  }, [sosState]);

  const startSos = () => { setCountdown(30); setSosState('countdown'); };
  const resetSos = () => { setCountdown(30); setSosState('idle'); };
  const selectNav = (id: string) => { setMenuOpen(false); scrollToSection(id); };

  return (
    <div className="site-shell">
      <a className="skip-link" href="#concept">Skip to content</a>
      <header className="site-header">
        <button className="brand" onClick={() => scrollToSection('top')} aria-label="Go to Smart Maternity Band home"><span className="brand-mark">R</span><span>ROCKET <em>LABS</em></span></button>
        <nav className="desktop-nav" aria-label="Main navigation">
          {navItems.map(([label, id]) => <button key={id} onClick={() => selectNav(id)}>{label}</button>)}
        </nav>
        <button className="nav-cta" onClick={() => selectNav('product-lab')}>Explore the system <ArrowUpRight size={15} /></button>
        <button className="menu-toggle" onClick={() => setMenuOpen((open) => !open)} aria-label={menuOpen ? 'Close navigation menu' : 'Open navigation menu'} aria-expanded={menuOpen}>{menuOpen ? <X /> : <Menu />}</button>
      </header>
      <AnimatePresence>
        {menuOpen && <motion.nav className="mobile-nav" initial={{ opacity: 0, y: -16 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -16 }} aria-label="Mobile navigation">{navItems.map(([label, id]) => <button key={id} onClick={() => selectNav(id)}>{label}<ChevronRight size={16} /></button>)}</motion.nav>}
      </AnimatePresence>

      <main id="top">
        <section className="hero" id="concept" style={{ minHeight: '100vh', position: 'relative', overflow: 'hidden' }}>
          <div className="hero-background" aria-hidden="true">
            <div className="hero-grid-pattern" aria-hidden="true"></div>
            <div className="hero-gradient-overlay" aria-hidden="true"></div>
          </div>
          <div className="hero-content">
            <div className="hero-brand-section">
              <div className="hero-eyebrow">
                <span className="hero-team-label">TEAM ROCKET 🚀</span>
                <span className="hero-divider">·</span>
                <span className="hero-event-label">SIH 2026</span>
              </div>
              <h1 className="hero-title">
                <span className="hero-title-part">SMART</span>
                <span className="hero-title-part">MATERNITY</span>
                <span className="hero-title-part">BAND</span>
              </h1>
              <p className="hero-subtitle">
                Technology for safer, smarter and more comfortable maternity care.
              </p>
              <div className="hero-metadata">
                <span className="hero-chip">HEALTHTECH</span>
                <span className="hero-chip">HARDWARE</span>
                <span className="hero-chip">SIH26113</span>
              </div>
              <div className="hero-actions-primary">
                <button className="hero-button hero-button--primary" onClick={() => scrollToSection('product-lab')}>
                  EXPLORE THE SYSTEM
                </button>
                <button className="hero-button hero-button--secondary" onClick={() => scrollToSection('engineering')}>
                  VIEW ENGINEERING
                </button>
              </div>
            </div>
            <div className="hero-product-section">
              <motion.div
                className="hero-product-visual"
                initial={reducedMotion ? false : { opacity: 0, y: 20, scale: 0.95 }}
                animate={{ opacity: 1, y: 0, scale: 1 }}
                transition={{ duration: 0.8, delay: 0.2 }}
              >
                <BandIllustration activeSensor="" />
                <div className="hero-product-overlay">
                  <div className="hero-sensor-pulses" aria-hidden="true">
                    {/* Animated sensor pulses will be added here */}
                  </div>
                </div>
              </motion.div>
            </div>
          </div>
        </section>

        <section className="context-strip">
          <div><span className="context-number">01</span><p>Lower physical stress during pregnancy</p></div><div><span className="context-number">02</span><p>Help pregnant women move more comfortably</p></div><div><span className="context-number">03</span><p>Bring support, sensing and response together</p></div>
        </section>

        <section className="section section--soft solution-section">
          <SectionIntro eyebrow="The concept" title="One wearable. Multiple layers of support." copy={projectData.projectInfo.concept} />
          <div className="layer-path">
            {[
              ['01', 'Mechanical support', 'Lower-lumbar support and a belly sling designed to adapt.'],
              ['02', 'Wearable sensing', 'A proposed mix of movement, temperature and support inputs.'],
              ['03', 'Thoughtful connection', 'ESP32 processing with BLE transfer to a companion experience.'],
              ['04', 'User control', 'Guidance and safety flows built around clear, visible choices.'],
            ].map(([number, title, copy], index) => <motion.article className="layer-card" key={title} initial={reducedMotion ? false : { opacity: 0, y: 18 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true, amount: 0.25 }} transition={{ delay: index * 0.08 }}><span>{number}</span><h3>{title}</h3><p>{copy}</p><i /></motion.article>)}
          </div>
        </section>

        <section className="section product-section" id="product-lab">
          <SectionIntro eyebrow="Product lab" title="Explore the wearable system." copy="Select an element to see how it fits into the current concept. These are engineering directions—not live measurements or a clinical device." />
          <div className="product-lab-grid">
            <div className="sensor-list" role="tablist" aria-label="Concept sensor and control elements">
              {sensorItems.map((sensor, index) => { const Icon = sensor.icon; const selected = sensor.id === activeSensor; return <button role="tab" aria-selected={selected} key={sensor.id} className={`sensor-button${selected ? ' is-selected' : ''}`} onClick={() => setActiveSensor(sensor.id)}><span className="sensor-index">0{index + 1}</span><span className="sensor-icon"><Icon size={18} /></span><span><strong>{sensor.label}</strong><small>{sensor.short}</small></span><ChevronRight size={17} /></button>; })}
            </div>
            <BandIllustration activeSensor={activeSensor} />
            <AnimatePresence mode="wait"><motion.article className="sensor-detail" key={activeSensorDetail.id} initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -12 }}><span className="data-label">{activeSensorDetail.status}</span><activeSensorDetail.icon size={28} strokeWidth={1.5} /><h3>{activeSensorDetail.label}</h3><p>{activeSensorDetail.detail}</p><div className="sensor-detail__line" /><small>Conceptual interaction · no live reading</small></motion.article></AnimatePresence>
          </div>
        </section>

        <section className="section engineering-section" id="engineering">
          <div className="engineering-heading"><SectionIntro eyebrow="Mechanical language" title="Built around a changing body." copy="The mechanical direction uses a two-panel system: a lower lumbar panel with a counterweight rail and electronics pod, plus a belly-support sling with independent fabric cells and a flexible spine." /><span className="data-label">Concept / prototype</span></div>
          <div className="teardown">
            <div className="teardown-visual"><span className="teardown-label teardown-label--one">Elastic outer skin</span><span className="teardown-label teardown-label--two">Telescoping ribs</span><span className="teardown-label teardown-label--three">Load-distributing pads</span><div className="exploded-layer exploded-layer--one"><i /><i /><i /><i /><i /></div><div className="exploded-layer exploded-layer--two"><i /><i /><i /><i /><i /></div><div className="exploded-layer exploded-layer--three"><i /><i /><i /><i /><i /></div><div className="teardown-core"><div /><div /><div /></div></div>
            <div className="teardown-copy"><p className="eyebrow"><span />Construction studies</p><h3>Expand. Align. Support.</h3><ul>{projectData.mechanicalDesign.mechanicalConstructionDetails.slice(0, 4).map((detail) => <li key={detail}><Check size={16} /><span>{detail}</span></li>)}</ul><p className="fine-print">Mechanical layers are conceptual engineering studies. The core mechanical assembly still requires a fully prototyped CNC-manufacturable component.</p></div>
          </div>
          <div className="support-map"><div className="support-map__diagram"><span className="support-zone support-zone--front">Front <b>Soft</b></span><span className="support-zone support-zone--left">Left <b>Moderate</b></span><span className="support-zone support-zone--right">Right <b>Moderate</b></span><span className="support-zone support-zone--back">Back <b>Firm</b></span><div className="support-body" /></div><div><p className="eyebrow"><span />Four-zone support map</p><h3>Support is placed with intention.</h3><p>The proposed zoning separates gentle front support from more structured posterior and hip support.</p><div className="zone-key">{projectData.mechanicalDesign.fourZoneSupportMap.map((zone) => <span key={zone.zone}><i />{zone.zone}: {zone.support}</span>)}</div></div></div>
        </section>

        <section className="section section--ink system-section" id="system">
          <SectionIntro eyebrow="System architecture" title="A clear route from support to insight." copy="A connected concept, deliberately shown as a simple and user-readable flow—not a claim of autonomous clinical monitoring." center />
          <div className="architecture-flow">
            {architecture.map((item, index) => { const Icon = item.icon; const selected = index === activeArchitecture; return <div className="architecture-wrap" key={item.title}><button onClick={() => setActiveArchitecture(index)} className={`architecture-node${selected ? ' is-selected' : ''}`} aria-pressed={selected}><span><Icon size={22} /></span><small>0{index + 1}</small><strong>{item.title}</strong></button>{index < architecture.length - 1 && <div className="architecture-link"><i /></div>}</div>; })}
          </div>
          <AnimatePresence mode="wait"><motion.div key={activeArchitecture} className="architecture-detail" initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -10 }}><span>Selected route</span><strong>{architecture[activeArchitecture].title}</strong><p>{architecture[activeArchitecture].description}</p></motion.div></AnimatePresence>
        </section>

        <section className="section mobile-section">
          <div className="mobile-copy"><SectionIntro eyebrow="Companion experience" title="Health data that feels human." copy="A calm, intentional mobile experience for checking concept trends, safety states and general wellness guidance." /><div className="mobile-copy__points"><div><span><Activity size={17} /></span><p><strong>Designed for clarity</strong><small>Readable states before dense dashboards.</small></p></div><div><span><LockKeyhole size={17} /></span><p><strong>User-controlled data</strong><small>{projectData.privacyInfo.description}</small></p></div></div><p className="disclaimer"><CircleAlert size={15} />All shown metrics and interface states are DEMO DATA. Wellness guidance is not medical advice, diagnosis or prescription.</p></div><PhoneDemo />
        </section>

        <section className="section safety-section" id="safety">
          <div className="safety-intro"><SectionIntro eyebrow="Safety, with control" title="A response window designed around a human decision." copy="Dual-IMU false-alert reduction and a manual SOS control are concepts that keep the cancellation step visible—not hidden behind automation." /><div className="safety-attributes"><span><ShieldCheck size={16} /> Dual-IMU concept</span><span><RotateCcw size={16} /> 30-second cancellation</span><span><AlertTriangle size={16} /> Manual SOS control</span></div></div>
          <div className={`sos-card sos-card--${sosState}`}>
            <div className="sos-card__top"><span className="data-label">Website demonstration only</span><span aria-live="polite">{sosState === 'countdown' ? 'Alert countdown active' : sosState === 'sent' ? 'Demo alert sent' : sosState === 'cancelled' ? 'Alert cancelled' : 'Ready'}</span></div>
            {sosState === 'idle' && <><div className="sos-orb"><AlertTriangle size={31} /></div><h3>Need assistance?</h3><p>Start a simulated SOS flow with an always-visible 30-second cancellation window.</p><button className="sos-button" onClick={startSos}>Trigger SOS demo <ArrowUpRight size={17} /></button></>}
            {sosState === 'countdown' && <><div className="countdown-ring" style={{ '--progress': `${(countdown / 30) * 360}deg` } as CSSProperties}><strong>{countdown}</strong><span>seconds</span></div><h3>Alert countdown started</h3><p>Cancel before the demonstration reaches zero.</p><button className="sos-button sos-button--cancel" onClick={() => setSosState('cancelled')}>Cancel alert <X size={17} /></button></>}
            {sosState === 'cancelled' && <><div className="sos-orb sos-orb--success"><Check size={31} /></div><h3>Alert cancelled</h3><p>No notification was sent. This was a website-only simulation.</p><button className="reset-button" onClick={resetSos}><RotateCcw size={15} /> Reset demonstration</button></>}
            {sosState === 'sent' && <><div className="sos-orb sos-orb--sent"><Radio size={31} /></div><h3>Demo alert sent</h3><p>This website demonstration does not contact emergency services or any emergency contact.</p><button className="reset-button" onClick={resetSos}><RotateCcw size={15} /> Reset demonstration</button></>}
          </div>
        </section>

        <section className="section build-section">
          <SectionIntro eyebrow="Built deliberately" title="Transparent about what is being explored." copy="The project stays clear about what is selected for a prototype, what is under evaluation and what remains a proposed addition." center />
          <div className="build-grid"><article className="estimate-card"><span className="data-label">Internal engineering estimate</span><h3>Working BOM range</h3><p className="estimate-number">{projectData.estimatedCosts.totalProduct}</p><p>{projectData.estimatedCosts.note}</p><button onClick={() => scrollToSection('notes')}>Read engineering notes <ChevronRight size={15} /></button></article><article className="bom-card"><div><p>Reference electronics range</p><strong>{projectData.estimatedCosts.electronics}</strong></div><ul>{projectData.bom.slice(0, 4).map((item) => <li key={item.component}><span>{item.component}</span><small>{item.status}</small></li>)}</ul></article></div>
        </section>

        <section className="section notes-section" id="notes">
          <div><SectionIntro eyebrow="Transparent engineering notes" title="Known limitations stay in view." copy="Important constraints are part of the concept—not fine print to be hidden after a polished interaction." /></div><div className="notes-list">{projectData.knownLimitations.map((note, index) => <article key={note}><span>0{index + 1}</span><p>{note}</p></article>)}</div>
        </section>

        <section className="closing-section"><div className="closing-orb closing-orb--one" /><div className="closing-orb closing-orb--two" /><p className="eyebrow"><span />TEAM ROCKET 🚀</p><h2>Reimagining<br /><i>maternity support.</i></h2><p>Smart Maternity Band · Smart India Hackathon 2026</p><div className="closing-meta"><span>SIH26113</span><span>HealthTech · Hardware</span><span>Concept experience</span></div></section>
      </main>
      <footer><span className="brand-mark">R</span><p>TEAM ROCKET 🚀 · SMART MATERNITY BAND</p><span>SIH 2026</span></footer>
    </div>
  );
}

export default App;
