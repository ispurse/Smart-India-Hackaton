import React from 'react';
import { projectData } from '../data/projectData';

const TechnologyStack: React.FC = () => {
  return (
    <section id="technology" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          TECHNOLOGY / COMPONENT REFERENCE
        </h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {projectData.technologyStack.map((tech, index) => (
            <div
              key={tech.name}
              className={`flex flex-col items-center p-4 bg-white rounded-lg shadow hover:shadow-lg transition-shadow
                ${index % 2 === 0 ? 'border-l-2 border-navy-800' : ''}`}
            >
              <div className="w-12 h-12 flex items-center justify-center mb-4">
                <span className="text-lg">{tech.name === 'ESP32' ? '💾' :
                                 tech.name === 'BLE' ? '📶' :
                                 tech.name === 'IMU' ? '📊' :
                                 tech.name === 'HR/SpO₂' ? '❤️' :
                                 tech.name === 'PRESSURE' ? '📏' :
                                 tech.name === 'TEMPERATURE' ? '🌡️' :
                                 tech.name === 'FETAL-MOVEMENT SENSOR' ? '👶' :
                                 tech.name === 'LOAD CELL' ? '⚖️' : '⚙️'}</span>
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">{tech.name}</h3>
              <p className="text-gray-600 text-center text-sm">{tech.description}</p>
            </div>
          ))}
        </div>

        {/* Optional: Engineering BOM Detail View */}
        <div className="mt-16 bg-white rounded-lg shadow overflow-hidden">
          <div className="bg-navy-50 px-6 py-4 border-b border-gray-200">
            <h3 className="text-lg font-semibold text-navy-800">Engineering BOM (Internal Reference)</h3>
            <p className="text-sm text-gray-500 mt-1">
              Estimated electronics cost: ₹3,740–₹9,370 (avg. ~₹6,600) → estimated total product cost ₹10,000–₹20,000.
              Present these only as internal engineering estimates, explicitly labeled, never as a finished retail price or certified BOM.
            </p>
          </div>
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead>
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Function
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Candidate Component
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Qty
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Approx. Cost/Unit (₹)
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Status
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {projectData.bom.map((item, index) => (
                  <tr key={index} className={index % 2 === 0 ? 'bg-gray-50' : ''}>
                    <td className="px-6 py-4 text-sm text-gray-700">{item.function}</td>
                    <td className="px-6 py-4 text-sm text-gray-700">{item.component}</td>
                    <td className="px-6 py-4 text-sm text-gray-700">{item.qty}</td>
                    <td className="px-6 py-4 text-sm text-gray-700">{item.cost}</td>
                    <td className="px-6 py-4 text-sm text-gray-700">{item.status}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>
  );
};

export default TechnologyStack;