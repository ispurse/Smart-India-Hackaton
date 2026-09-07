import React from 'react';
import { projectData } from '../data/projectData';

const Benefits: React.FC = () => {
  return (
    <section id="benefits" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          BENEFITS
        </h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {projectData.benefits.map((benefit) => (
            <div key={benefit.id} className="bg-white p-6 rounded-lg shadow flex flex-col items-center text-center hover:shadow-lg transition-shadow duration-300">
              <div className="w-16 h-16 flex items-center justify-center mb-4">
                <span className="text-2xl">
                  {benefit.id === 1 ? '🦵' :
                   benefit.id === 2 ? '🆘' :
                   benefit.id === 3 ? '👕' :
                   benefit.id === 4 ? '📱' :
                   benefit.id === 5 ? '🧠' :
                   benefit.id === 6 ? '📏' : '⚙️'}
                </span>
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-3">{benefit.title}</h3>
              <p className="text-gray-600 text-center">
                {benefit.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Benefits;