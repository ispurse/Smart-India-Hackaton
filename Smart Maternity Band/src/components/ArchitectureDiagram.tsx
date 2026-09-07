import React from 'react';

const ArchitectureDiagram: React.FC = () => {
  return (
    <section id="system-architecture" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          SYSTEM ARCHITECTURE
        </h2>

        {/* Architecture Visualization */}
        <div className="relative">
          <div className="aspect-w-1 aspect-h-1 w-full rounded-lg overflow-hidden shadow-2xl bg-gray-100">
            <div className="flex h-full items-center justify-center text-gray-400">
              <div className="text-center space-y-4">
                <div className="flex flex-col items-center">
                  {/* Mechanical System */}
                  <div className="flex items-center space-x-4 mb-4">
                    <div className="w-16 h-16 bg-navy-800/10 flex items-center justify-center rounded-lg">
                      <span className="text-navy-800 text-xl">⚙️</span>
                    </div>
                    <span className="text-gray-600 font-medium">MECHANICAL SYSTEM</span>
                  </div>

                  {/* Connection Line */}
                  <div className="w-px h-8 bg-gray-300"></div>

                  {/* Electronics & Sensors */}
                  <div className="flex items-center space-x-4 mb-4">
                    <div className="w-16 h-16 bg-blue-500/10 flex items-center justify-center rounded-lg">
                      <span className="text-blue-600 text-xl">📡</span>
                    </div>
                    <span className="text-gray-600 font-medium">ELECTRONICS & SENSORS</span>
                  </div>

                  {/* Connection Line */}
                  <div className="w-px h-8 bg-gray-300"></div>

                  {/* BLE */}
                  <div className="flex items-center space-x-4 mb-4">
                    <div className="w-16 h-16 bg-purple-500/10 flex items-center justify-center rounded-lg">
                      <span className="text-purple-600 text-xl">📶</span>
                    </div>
                    <span className="text-gray-600 font-medium">BLE</span>
                  </div>

                  {/* Connection Line */}
                  <div className="w-px h-8 bg-gray-300"></div>

                  {/* Mobile App */}
                  <div className="flex items-center space-x-4">
                    <div className="w-16 h-16 bg-green-500/10 flex items-center justify-center rounded-lg">
                      <span className="text-green-600 text-xl">📱</span>
                    </div>
                    <span className="text-gray-600 font-medium">MOBILE APP</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Detailed Breakdown */}
        <div className="mt-16 grid md:grid-cols-2 gap-8">
          {/* Mechanical System Details */}
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">MECHANICAL SYSTEM</h3>
            <div className="space-y-3">
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-navy-800 rounded-full"></div>
                <span className="text-gray-700">Lower Lumbar Panel</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-navy-800 rounded-full"></div>
                <span className="text-gray-700">Belly Support Sling</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-navy-800 rounded-full"></div>
                <span className="text-gray-700">IMU (LSM6DSOX)</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-navy-800 rounded-full"></div>
                <span className="text-gray-700">Electronics Pod</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-navy-800 rounded-full"></div>
                <span className="text-gray-700">Counterweight Rail</span>
              </div>
            </div>
          </div>

          {/* Electronics & Sensors Details */}
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">ELECTRONICS & SENSORS</h3>
            <div className="space-y-3">
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-blue-600 rounded-full"></div>
                <span className="text-gray-700">ESP32-S3 DevKit</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-blue-600 rounded-full"></div>
                <span className="text-gray-700">IMU (LSM6DSOX)</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-blue-600 rounded-full"></div>
                <span className="text-gray-700">HR/SpO₂ (MAX30102)</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-blue-600 rounded-full"></div>
                <span className="text-gray-700">Temperature (TMP117)</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-blue-600 rounded-full"></div>
                <span className="text-gray-700">Fetal Movement (Piezo)</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-blue-600 rounded-full"></div>
                <span className="text-gray-700">Pressure (FSR402)</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-blue-600 rounded-full"></div>
                <span className="text-gray-700">Load Cell + HX711</span>
              </div>
            </div>
          </div>
        </div>

        {/* Data Flow Animation Description */}
        <div className="mt-16 text-center">
          <h3 className="text-xl font-bold text-gray-900 mb-4">Data Flow Animation</h3>
          <p className="text-gray-600 max-w-xl mx-auto">
            Animate data particles flowing Sensor → ESP32 → BLE → Phone. Hover expands a node and highlights connections while dimming unrelated ones; click opens an info panel.
          </p>
        </div>
      </div>
    </section>
  );
};

export default ArchitectureDiagram;