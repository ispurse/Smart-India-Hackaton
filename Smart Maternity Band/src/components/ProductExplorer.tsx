import React, { useState } from 'react';

const ProductExplorer: React.FC = () => {
  const [activePoint, setActivePoint] = useState<string | null>(null);

  const sensorPoints = [
    { id: 'heart-rate', name: 'Heart Rate', description: 'Monitors heart-rate information as part of the wearable\'s health-tracking system.' },
    { id: 'spo2', name: 'SpO2', description: 'Tracks blood oxygen saturation levels for respiratory and cardiac health monitoring.' },
    { id: 'temperature', name: 'Temperature', description: 'Measures body/skin temperature for fever detection and thermal comfort assessment.' },
    { id: 'movement', name: 'Movement', description: 'Tracks physical activity and posture through inertial measurement units.' },
    { id: 'pressure', name: 'Pressure', description: 'Monitors belt pressure for support optimization and uterine activity monitoring.' },
    { id: 'fetal-movement', name: 'Fetal Movement', description: 'Detects fetal movement patterns through piezoelectric film sensors.' },
    { id: 'fall-detection', name: 'Fall Detection', description: 'Uses dual IMUs to detect falls with a 30-second cancellation window before alert escalation.' },
    { id: 'sos', name: 'SOS', description: 'Emergency manual SOS button for immediate alert triggering.' }
  ];

  const handlePointClick = (id: string) => {
    setActivePoint(id);
  };

  const activeSensor = sensorPoints.find(point => point.id === activePoint);

  return (
    <section id="product-lab" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          PRODUCT LAB
        </h2>
        <div className="relative">
          {/* Product Visualization */}
          <div className="aspect-w-1 aspect-h-1 w-full rounded-lg overflow-hidden shadow-2xl bg-gray-100">
            {/* Product Image */}
            <img src="/assets/product-placeholder.jpg" alt="Smart Maternity Band Prototype" className="object-cover w-full h-full" />
          </div>

          {/* Clickable Points Overlay */}
          <div className="absolute inset-0 pointer-events-none">
            {/* These would be positioned over the actual product image */}
            {/* For now, we'll show them as a list below */}
          </div>
        </div>

        {/* Sensor Information Panel */}
        {activeSensor && (
          <div className="mt-12 bg-gray-50 rounded-lg p-6 shadow">
            <h3 className="text-xl font-bold text-gray-900 mb-4">
              {activeSensor.name}
            </h3>
            <p className="text-gray-700">
              {activeSensor.description}
            </p>
            <div className="mt-6 flex items-center space-x-4">
              <div className="w-3 h-3 bg-blue-500 rounded-full"></div>
              <span className="text-sm text-gray-500">Active component</span>
            </div>
          </div>
        )}

        {/* Sensor Points List */}
        <div className="mt-12 grid md:grid-cols-2 lg:grid-cols-4 gap-4">
          {sensorPoints.map(point => (
            <button
              key={point.id}
              onClick={() => handlePointClick(point.id)}
              className={`flex flex-col items-center p-4 bg-white rounded-lg shadow hover:bg-gray-50 transition-colors
                ${activePoint === point.id ? 'border-2 border-navy-800' : 'border border-gray-200'}`}
            >
              <div className="w-10 h-10 flex items-center justify-center mb-3">
                <span className="text-lg">{point.id === 'heart-rate' ? '❤️' : point.id === 'spo2' ? '💧' : point.id === 'temperature' ? '🌡️' : point.id === 'movement' ? '🏃' : point.id === 'pressure' ? '📏' : point.id === 'fetal-movement' ? '👶' : point.id === 'fall-detection' ? '🚨' : point.id === 'sos' ? '🆘' : '⚙️'}</span>
              </div>
              <p className="text-center text-sm font-medium text-gray-900">{point.name}</p>
            </button>
          ))}
        </div>
      </div>
    </section>
  );
};

export default ProductExplorer;