import React from 'react';

const SensorExperience: React.FC = () => {
  return (
    <section id="sensor-experience" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          SENSOR EXPERIENCE
        </h2>

        {/* Sensor Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {/* Heart Rate */}
          <div className="bg-gray-50 p-6 rounded-lg flex flex-col items-center text-center">
            <div className="w-16 h-16 bg-red-500/10 flex items-center justify-center mb-4 rounded-lg">
              <span className="text-red-600 text-2xl">❤️</span>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">Heart Rate</h3>
            <p className="text-gray-600 text-sm">
              Monitors heart-rate information as part of the wearable's health-tracking system.
            </p>
          </div>

          {/* SpO2 */}
          <div className="bg-gray-50 p-6 rounded-lg flex flex-col items-center text-center">
            <div className="w-16 h-16 bg-blue-500/10 flex items-center justify-center mb-4 rounded-lg">
              <span className="text-blue-600 text-2xl">💧</span>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">SpO₂</h3>
            <p className="text-gray-600 text-sm">
              Tracks blood oxygen saturation levels for respiratory and cardiac health monitoring.
            </p>
          </div>

          {/* Temperature */}
          <div className="bg-gray-50 p-6 rounded-lg flex flex-col items-center text-center">
            <div className="w-16 h-16 bg-orange-500/10 flex items-center justify-center mb-4 rounded-lg">
              <span className="text-orange-600 text-2xl">🌡️</span>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">Temperature</h3>
            <p className="text-gray-600 text-sm">
              Measures body/skin temperature for fever detection and thermal comfort assessment.
            </p>
          </div>

          {/* Movement */}
          <div className="bg-gray-50 p-6 rounded-lg flex flex-col items-center text-center">
            <div className="w-16 h-16 bg-green-500/10 flex items-center justify-center mb-4 rounded-lg">
              <span className="text-green-600 text-2xl">🏃</span>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">Movement</h3>
            <p className="text-gray-600 text-sm">
              Tracks physical activity and posture through inertial measurement units.
            </p>
          </div>

          {/* Pressure */}
          <div className="bg-gray-50 p-6 rounded-lg flex flex-col items-center text-center">
            <div className="w-16 h-16 bg-purple-500/10 flex items-center justify-center mb-4 rounded-lg">
              <span className="text-purple-600 text-2xl">📏</span>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">Pressure</h3>
            <p className="text-gray-600 text-sm">
              Monitors belt pressure for support optimization and uterine activity monitoring.
            </p>
          </div>

          {/* Fetal Movement */}
          <div className="bg-gray-50 p-6 rounded-lg flex flex-col items-center text-center">
            <div className="w-16 h-16 bg-pink-500/10 flex items-center justify-center mb-4 rounded-lg">
              <span className="text-pink-600 text-2xl">👶</span>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">Fetal Movement</h3>
            <p className="text-gray-600 text-sm">
              Detects fetal movement patterns through piezoelectric film sensors.
            </p>
          </div>
        </div>

        {/* Callout from prototype photo */}
        <div className="mt-16">
          <div className="aspect-w-1 aspect-h-1 w-full rounded-lg overflow-hidden shadow-2xl bg-gray-100">
            <div className="flex h-full items-center justify-center text-gray-400">
              <div className="text-center">
                <div className="w-40 h-40 border-4 border-dashed border-gray-300 rounded-full flex items-center justify-center">
                  <span className="text-gray-500 text-xl">PROTOTYPE</span>
                </div>
                <p className="mt-4 text-sm text-gray-500">Reference Photo - Team Rocket</p>
              </div>
            </div>
          </div>
          <p className="mt-4 text-center text-sm text-gray-500">
            Team Rocket's own reference photos — a person wearing the belt (front cross-section with numbered 1–9 support cells, back view showing electronics pod, lumbar panel, IMU, and counterweight rail) plus a flat belt-layout diagram.
          </p>
        </div>
      </div>
    </section>
  );
};

export default SensorExperience;