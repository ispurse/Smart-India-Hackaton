import React from 'react';
import { projectData } from '../data/projectData';

const PrivacySection: React.FC = () => {
  return (
    <section id="privacy" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          {projectData.privacyInfo.headline}
        </h2>
        <div className="relative">
          {/* Smartphone Illustration Placeholder */}
          <div className="aspect-w-1 aspect-h-1 w-full max-w-md mx-auto rounded-lg overflow-hidden shadow-2xl bg-gray-100 mb-12">
            <div className="flex h-full items-center justify-center relative">
              {/* Phone Outline */}
              <div className="w-11/12 h-11/12 bg-white/20 border-2 border-gray-200 rounded-xl relative">
                {/* Data Particles */}
                <div className="absolute inset-0 pointer-events-none">
                  {/* These would be animated data particles in a real implementation */}
                  <div className="absolute inset-0"></div>
                </div>
                {/* Shield Overlay */}
                <div className="absolute inset-0 bg-black/5 rounded-xl pointer-events-none"></div>
              </div>
            </div>
          </div>

          <p className="text-center text-gray-600 mb-8 max-w-xl mx-auto">
            {projectData.privacyInfo.description}
          </p>

          {/* Simulated SHARE DATA interaction description */}
          <div className="mt-8 text-center text-xs text-gray-500">
            {projectData.privacyInfo.note}
          </div>
        </div>
      </div>
    </section>
  );
};

export default PrivacySection;