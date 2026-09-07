import React from 'react';

const Hero: React.FC = () => {
  return (
    <section id="hero" className="relative pt-20 pb-24 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col-reverse lg:flex-row lg:items-stretch lg:gap-12">
          {/* Hero Content */}
          <div className="lg:w-1/2">
            <h1 className="text-4xl font-bold text-gray-900 lg:text-5xl">
              <span className="block">SMART</span>
              <span className="block">MATERNITY BAND</span>
            </h1>
            <p className="mt-6 text-lg text-gray-600 max-w-xl">
              Technology for safer, smarter and more comfortable maternity care.
            </p>
            <div className="mt-10 flex lg:space-x-8">
              <a href="#solution" className="flex items-center px-8 py-4 bg-navy-800 text-white rounded-lg hover:bg-navy-900 transition-colors font-medium">
                Explore the Solution
                <svg className="ml-2 h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5l7 7-7 7" />
                </svg>
              </a>
              <a href="#team" className="flex items-center px-8 py-4 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors font-medium text-gray-700 hover:text-gray-900">
                Meet Team Rocket
                <svg className="ml-2 h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 10V3L4 14h7v7l9-11h-9z" />
                </svg>
              </a>
            </div>
          </div>

          {/* Hero Product Visual */}
          <div className="lg:w-1/2 relative">
            {/* Placeholder for the actual image - we'll use a div with a background for now */}
            <div className="aspect-w-1 aspect-h-1 w-full rounded-lg overflow-hidden shadow-2xl bg-gray-200">
              {/* In the future, replace this with the actual image from assets */}
              <img src="/assets/hero-placeholder.jpg" alt="Smart Maternity Band" className="object-cover w-full h-full" />
            </div>
          </div>
        </div>
      </div>

      {/* Project Snapshot */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mt-12 flex flex-col items-center lg:flex-row lg:space-x-10">
          <div className="flex flex-col items-center space-y-2 text-center">
            <span className="px-3 py-1 bg-navy-800/10 text-navy-800 text-xs font-medium rounded-full">
              SIH 2026
            </span>
            <span className="px-3 py-1 bg-blue-500/10 text-blue-600 text-xs font-medium rounded-full">
              HEALTHTECH
            </span>
            <span className="px-3 py-1 bg-purple-500/10 text-purple-600 text-xs font-medium rounded-full">
              HARDWARE
            </span>
            <span className="px-3 py-1 bg-green-500/10 text-green-600 text-xs font-medium rounded-full">
              SIH26113
            </span>
            <span className="px-3 py-1 bg-red-500/10 text-red-600 text-xs font-medium rounded-full">
              TEAM ROCKET
            </span>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;