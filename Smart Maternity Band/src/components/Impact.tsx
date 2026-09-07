import React from 'react';
import { projectData } from '../data/projectData';

const Impact: React.FC = () => {
  return (
    <section id="impact" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          DESIGNED FOR IMPACT.
        </h2>
        <div className="relative">
          {/* Central Illustration Placeholder */}
          <div className="aspect-w-1 aspect-h-1 w-full rounded-lg overflow-hidden shadow-2xl bg-gray-100 mb-12">
            <div className="flex h-full items-center justify-center text-gray-400">
              <div className="text-center">
                <div className="w-24 h-24 border-4 border-dashed border-gray-300 rounded-full flex items-center justify-center">
                  <span className="text-gray-500 text-xl">🤰</span>
                </div>
                <p className="mt-4 text-sm text-gray-500">Impact Illustration</p>
              </div>
            </div>
          </div>

          {/* Impact Cards */}
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 text-center">
            {projectData.impactPoints.map((point, index) => (
              <div key={index} className="bg-white p-6 rounded-lg shadow">
                <h3 className="text-lg font-semibold text-gray-900 mb-3">{point.title}</h3>
                <p className="text-gray-600">
                  {point.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Impact;