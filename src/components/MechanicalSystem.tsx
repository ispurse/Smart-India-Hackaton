import React from 'react';

const MechanicalSystem: React.FC = () => {
  const mechanicalFeatures = [
    { id: 1, name: "Sliding Expansion Panels", description: "Overlapping flexible panels that telescope over one another to accommodate growing belly size." },
    { id: 2, name: "Vector Rail/Leaf Spring", description: "Flexible spring/elastic load-transfer rails that store energy on bending and assist extension on standing." },
    { id: 3, name: "Cam Mechanism", description: "Small cam/rotating linkage that varies the direction of support force with hip angle with hip movement (standing/walking/bending/sitting)." },
    { id: 4, name: "Pulley System", description: "Concept for redistributing tension when one side experiences more load than the other." },
    { id: 5, name: "Overload Clutch", description: "Mechanically self-limiting mechanism in the tensioning system to cap maximum force." },
    { id: 6, name: "Hip Pivot & Torsion Spring", description: "Spring-loaded hip mechanism that loads when sitting and assists upward motion when standing." },
    { id: 7, name: "One-Hand Buckle", description: "Ratcheting/cam buckle closure: pull → click → lock for easy adjustment." }
  ];

  return (
    <section id="mechanical-system" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          ENGINEERED FOR SUPPORT.
        </h2>

        {/* Main Concept Image */}
        <div className="mb-16">
          <div className="aspect-w-1 aspect-h-1 w-full rounded-lg overflow-hidden shadow-2xl bg-gray-100">
            <div className="flex h-full items-center justify-center text-gray-400">
              <div className="text-center">
                <div className="w-40 h-40 border-4 border-dashed border-gray-300 rounded-full flex items-center justify-center">
                  <span className="text-gray-500 text-xl">STRUCTURE A</span>
                </div>
                <p className="mt-4 text-sm text-gray-500">Smart Adaptive Maternity Belt – Concept Sheet</p>
              </div>
            </div>
          </div>
        </div>

        {/* Features Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {mechanicalFeatures.map(feature => (
            <div key={feature.id} className="bg-white p-6 rounded-lg shadow flex flex-col items-center text-center">
              <div className="w-12 h-12 bg-navy-800/10 flex items-center justify-center mb-4 rounded-lg">
                <span className="text-navy-800 text-xl">{feature.id}</span>
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-3">{feature.name}</h3>
              <p className="text-gray-600 text-center">{feature.description}</p>
            </div>
          ))}
        </div>

        {/* Supporting Images */}
        <div className="mt-16 grid md:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="bg-white p-4 rounded-lg shadow">
            <div className="aspect-w-1 aspect-h-1 w-full rounded-lg overflow-hidden shadow bg-gray-100">
              <div className="flex h-full items-center justify-center text-gray-400">
                <span className="text-gray-500">Multi-view</span>
              </div>
            </div>
            <p className="mt-2 text-center text-sm font-medium text-gray-600">Front/Right/Back/Top Views</p>
          </div>

          <div className="bg-white p-4 rounded-lg shadow">
            <div className="aspect-w-1 aspect-h-1 w-full rounded-lg overflow-hidden shadow bg-gray-100">
              <div className="flex h-full items-center justify-center text-gray-400">
                <span className="text-gray-500">Stiffness</span>
              </div>
            </div>
            <p className="mt-2 text-center text-sm font-medium text-gray-600">Variable Zone Map</p>
          </div>

          <div className="bg-white p-4 rounded-lg shadow">
            <div className="aspect-w-1 aspect-h-1 w-full rounded-lg overflow-hidden shadow bg-gray-100">
              <div className="flex h-full items-center justify-center text-gray-400">
                <span className="text-gray-500">Dimensions</span>
              </div>
            </div>
            <p className="mt-2 text-center text-sm font-medium text-gray-600">Key Dimensions Table</p>
          </div>

          <div className="bg-white p-4 rounded-lg shadow">
            <div className="aspect-w-1 aspect-h-1 w-full rounded-lg overflow-hidden shadow bg-gray-100">
              <div className="flex h-full items-center justify-center text-gray-400">
                <span className="text-gray-500">Materials</span>
              </div>
            </div>
            <p className="mt-2 text-center text-sm font-medium text-gray-600">Materials List</p>
          </div>
        </div>

        {/* Exploded View Animation Description */}
        <div className="mt-16 text-center">
          <h3 className="text-xl font-bold text-gray-900 mb-4">Exploded-View Animation Sequence</h3>
          <p className="text-gray-600 max-w-xl mx-auto">
            ASSEMBLED BAND → PANELS SEPARATE → SPRING SYSTEM HIGHLIGHTS → 4 SUPPORT ZONES ACTIVATE → SYSTEM REASSEMBLES
          </p>
        </div>

        {/* Growth Stage Table */}
        <div className="mt-16">
          <h3 className="text-xl font-bold text-gray-900 mb-6">Growth-Stage Reference (Design Target)</h3>
          <p className="text-sm text-gray-500 mb-4">Label as DEMO DATA / DESIGN TARGET, not a clinically validated spec.</p>
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Stage
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Typical Belt Circumference
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Mechanism State
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Support Emphasis
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                <tr>
                  <td className="px-6 py-4 text-sm text-gray-700">Early pregnancy (Tri 1)</td>
                  <td className="px-6 py-4 text-sm text-gray-700">~65–75 cm</td>
                  <td className="px-6 py-4 text-sm text-gray-700">Compact, ribs fully nested</td>
                  <td className="px-6 py-4 text-sm text-gray-700">Posture guidance, light support</td>
                </tr>
                <tr>
                  <td className="px-6 py-4 text-sm text-gray-700">Mid pregnancy (Tri 2)</td>
                  <td className="px-6 py-4 text-sm text-gray-700">~75–95 cm</td>
                  <td className="px-6 py-4 text-sm text-gray-700">Panel 1 slides out</td>
                  <td className="px-6 py-4 text-sm text-gray-700">Load support increases</td>
                </tr>
                <tr>
                  <td className="px-6 py-4 text-sm text-gray-700">Late pregnancy (Tri 3)</td>
                  <td className="px-6 py-4 text-sm text-gray-700">~95–120 cm</td>
                  <td className="px-6 py-4 text-sm text-gray-700">Panels 2 & 3 slide, max extension</td>
                  <td className="px-6 py-4 text-sm text-gray-700">Full load redistribution</td>
                </tr>
                <tr>
                  <td className="px-6 py-4 text-sm text-gray-700">Postpartum (0–12 wk)</td>
                  <td className="px-6 py-4 text-sm text-gray-700">~80–95 cm (tightening)</td>
                  <td className="px-6 py-4 text-sm text-gray-700">Ribs re-nest, tension increases</td>
                  <td className="px-6 py-4 text-sm text-gray-700">Core recovery, gentle compression</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>
  );
};

export default MechanicalSystem;