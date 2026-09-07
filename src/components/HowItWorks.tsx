import React from 'react';
import { projectData } from '../data/projectData';

const HowItWorks: React.FC = () => {
  return (
    <section id="how-it-works" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          HOW IT WORKS
        </h2>
        <div className="relative">
          {/* Timeline Container */}
          <div className="relative">
            {/* Vertical Line */}
            <div className="absolute inset-y-0 left-1/2 -ml-px w-px bg-gray-200"></div>

            {/* Steps */}
            <div className="relative pt-12 pb-20 md:flex md:items-start md:justify-between md:space-x-12">
              {projectData.howItWorksSteps.map((step, index) => (
                <div
                  key={step.step}
                  className={`flex-1 md:w-1/6 text-center px-4 md:pt-8 ${index === 0 ? 'pb-12' : ''}`}
                >
                  {/* Step Circle */}
                  <div className="relative">
                    <div className="w-12 h-12 flex items-center justify-center rounded-full bg-navy-800/10 text-navy-800 font-bold mx-auto mb-4">
                      {step.step < 10 ? `0${step.step}` : step.step}
                    </div>
                    {/* Connecting Line (except for last step) */}
                    {index < projectData.howItWorksSteps.length - 1 && (
                      <div className="absolute -left-1/2 -ml-[6px] -mt-[6px] w-2 h-2 rounded-full bg-navy-800"></div>
                    )}
                  </div>

                  {/* Step Title */}
                  <h3 className="text-lg font-semibold text-gray-900 mb-3">
                    {step.title}
                  </h3>

                  {/* Step Description */}
                  <p className="text-gray-600 text-sm">
                    {step.description}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HowItWorks;