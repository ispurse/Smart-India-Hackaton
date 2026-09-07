import React from 'react';
import { projectData } from '../data/projectData';

const TeamSection: React.FC = () => {
  return (
    <section id="team" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          {projectData.teamInfo.headline}
        </h2>
        <p className="text-center text-gray-600 mb-16 max-w-xl mx-auto">
          {projectData.teamInfo.description}
        </p>

        {/* Team Member Cards Placeholder */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {/* We'll create generic team cards that can be replaced with real data later */}
          <div className="bg-gray-50 p-8 rounded-lg shadow text-center">
            <div className="w-20 h-20 bg-navy-800/10 flex items-center justify-center mb-4 rounded-full">
              <span className="text-navy-800 text-xl">👥</span>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-3">TEAM ROCKET</h3>
            <p className="text-gray-600">
              Collective team of engineers, designers, and developers working on the Smart Maternity Band project.
              {/* ADD REAL TEAM MEMBER INFORMATION HERE IF/WHEN THE TEAM CHOOSES TO PUBLISH IT. */}
              {/* Do not populate with invented or placeholder names. */}
            </p>
          </div>

          {/* Additional generic cards for future team members */}
          <div className="bg-gray-50 p-8 rounded-lg shadow text-center">
            <div className="w-20 h-20 bg-navy-800/10 flex items-center justify-center mb-4 rounded-full">
              <span className="text-navy-800 text-xl">⚙️</span>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-3">MECHANICAL TEAM</h3>
            <p className="text-gray-600">
              Responsible for the dual-panel support system, expansion mechanisms, and ergonomic design.
            </p>
          </div>

          <div className="bg-gray-50 p-8 rounded-lg shadow text-center">
            <div className="w-20 h-20 bg-navy-800/10 flex items-center justify-center mb-4 rounded-full">
              <span className="text-navy-800 text-xl">📡</span>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-3">ELECTRONICS TEAM</h3>
            <p className="text-gray-600">
              Handling sensor integration, ESP32 programming, BLE connectivity, and power management.
            </p>
          </div>

          <div className="bg-gray-50 p-8 rounded-lg shadow text-center">
            <div className="w-20 h-20 bg-navy-800/10 flex items-center justify-center mb-4 rounded-full">
              <span className="text-navy-800 text-xl">📱</span>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-3">SOFTWARE TEAM</h3>
            <p className="text-gray-600">
              Developing the mobile application, data analytics, and user guidance features.
            </p>
          </div>
        </div>

        {/* Code comment for real team data */}
        <div className="mt-16 bg-gray-50 p-4 rounded-lg font-mono text-sm text-gray-500">
          {/* ADD REAL TEAM MEMBER INFORMATION HERE IF/WHEN THE TEAM CHOOSES TO PUBLISH IT. */}
          {/* Do not populate with invented or placeholder names. */}
        </div>
      </div>
    </section>
  );
};

export default TeamSection;