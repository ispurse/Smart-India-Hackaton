import React from 'react';

const SolutionSection: React.FC = () => {
  return (
    <section id="solution" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          ONE WEARABLE. MULTIPLE LAYERS OF SUPPORT.
        </h2>
        <p className="text-center text-gray-600 mb-16 max-w-2xl mx-auto">
          MECHANICAL SUPPORT + SMART SENSING + BLE CONNECTIVITY + MOBILE GUIDANCE + SAFETY
        </p>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {/* Mechanical Support */}
          <div className="bg-white p-8 rounded-lg shadow-lg flex flex-col items-center text-center">
            <div className="w-16 h-16 bg-navy-800/10 flex items-center justify-center mb-6 rounded-lg">
              <span className="text-navy-800 text-2xl">⚙️</span>
            </div>
            <h3 className="text-xl font-semibold text-gray-900 mb-4">MECHANICAL SUPPORT</h3>
            <p className="text-gray-600">
              Dual-panel system providing lumbar and abdominal support through overlapping flexible panels that grow with pregnancy.
            </p>
          </div>

          {/* Smart Sensing */}
          <div className="bg-white p-8 rounded-lg shadow-lg flex flex-col items-center text-center">
            <div className="w-16 h-16 bg-blue-500/10 flex items-center justify-center mb-6 rounded-lg">
              <span className="text-blue-600 text-2xl">📡</span>
            </div>
            <h3 className="text-xl font-semibold text-gray-900 mb-4">SMART SENSING</h3>
            <p className="text-gray-600">
              Integrated sensors monitoring vital signs including heart rate, SpO2, temperature, movement, and fetal movement.
            </p>
          </div>

          {/* BLE Connectivity */}
          <div className="bg-white p-8 rounded-lg shadow-lg flex flex-col items-center text-center">
            <div className="w-16 h-16 bg-purple-500/10 flex items-center justify-center mb-6 rounded-lg">
              <span className="text-purple-600 text-2xl">📶</span>
            </div>
            <h3 className="text-xl font-semibold text-gray-900 mb-4">BLE CONNECTIVITY</h3>
            <p className="text-gray-600">
              ESP32-based Bluetooth Low Energy connection for seamless data transmission to mobile applications.
            </p>
          </div>

          {/* Mobile Guidance */}
          <div className="bg-white p-8 rounded-lg shadow-lg flex flex-col items-center text-center">
            <div className="w-16 h-16 bg-green-500/10 flex items-center justify-center mb-6 rounded-lg">
              <span className="text-green-600 text-2xl">📱</span>
            </div>
            <h3 className="text-xl font-semibold text-gray-900 mb-4">MOBILE GUIDANCE</h3>
            <p className="text-gray-600">
              Smart health-suggestion app providing daily wellness recommendations for exercise, diet, and lifestyle.
            </p>
          </div>

          {/* Safety */}
          <div className="bg-white p-8 rounded-lg shadow-lg flex flex-col items-center text-center">
            <div className="w-16 h-16 bg-red-500/10 flex items-center justify-center mb-6 rounded-lg">
              <span className="text-red-600 text-2xl">🆘</span>
            </div>
            <h3 className="text-xl font-semibold text-gray-900 mb-4">SAFETY</h3>
            <p className="text-gray-600">
              Emergency response features including fall detection, SOS button, and 30-second cancellation window for alerts.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default SolutionSection;