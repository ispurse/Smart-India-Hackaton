import React from 'react';
import { projectData } from '../data/projectData';

const Feasibility: React.FC = () => {
  return (
    <section id="feasibility" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          FEASIBILITY
        </h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {projectData.feasibilityCards.map((card, index) => (
            <div key={index} className="bg-white p-6 rounded-lg shadow flex flex-col items-center text-center">
              <div className="w-16 h-16 flex items-center justify-center mb-4">
                <span className="text-2xl">{card.icon}</span>
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-3">{card.title}</h3>
              <p className="text-gray-600 text-center">
                {card.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Feasibility;