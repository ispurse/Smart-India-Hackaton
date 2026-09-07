import React from 'react';
import { projectData } from '../data/projectData';

const LimitationsSection: React.FC = () => {
  return (
    <section id="limitations" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          KNOWN LIMITATIONS & OPEN ENGINEERING QUESTIONS
        </h2>
        <p className="text-center text-gray-600 mb-12 max-w-xl mx-auto">
          Presenting transparent engineering challenges as a sign of maturity and rigor.
        </p>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {projectData.knownLimitations.map((limitation, index) => (
            <div key={index} className="bg-white p-6 rounded-lg shadow border-l-4 border-navy-800">
              <div className="flex items-start space-x-4">
                <div className="flex-shrink-0">
                  <div className="w-8 h-8 flex items-center justify-center bg-navy-800/10 text-navy-800 rounded-full">
                    <span className="text-sm">{index + 1}</span>
                  </div>
                </div>
                <div className="flex-1">
                  <p className="text-gray-700">
                    {limitation}
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Alternatives under consideration */}
        <div className="mt-16">
          <h3 className="text-xl font-bold text-gray-900 mb-6">Alternatives Under Consideration</h3>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {projectData.alternatives.map((alternative, index) => (
              <div key={index} className="bg-white p-4 rounded-lg shadow border-l-2 border-blue-500">
                <p className="text-gray-600 text-sm">
                  • {alternative}
                </p>
              </div>
            ))}
          </div>
        </div>

        {/* Prior Art */}
        <div className="mt-16">
          <h3 className="text-xl font-bold text-gray-900 mb-6">Prior Art / Competitive Landscape</h3>
          <div className="space-y-4">
            {projectData.priorArt.map((art, index) => (
              <div key={index} className="bg-white p-4 rounded-lg shadow border-l-2 border-gray-500">
                <p className="text-gray-600 text-sm">
                  • {art}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default LimitationsSection;