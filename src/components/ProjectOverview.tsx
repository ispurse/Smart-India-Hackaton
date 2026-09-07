import React from 'react';

const ProjectOverview: React.FC = () => {
  return (
    <section id="project-overview" className="py-16 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          Project Overview
        </h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 text-center">
          <div className="bg-white p-6 rounded-lg shadow">
            <div className="flex items-center justify-center h-12 mb-4">
              <span className="text-navy-800 text-xl font-bold">SIH 2026</span>
            </div>
            <p className="text-gray-600">Event</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <div className="flex items-center justify-center h-12 mb-4">
              <span className="text-blue-600 text-xl font-bold">HEALTHTECH</span>
            </div>
            <p className="text-gray-600">Theme</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <div className="flex items-center justify-center h-12 mb-4">
              <span className="text-purple-600 text-xl font-bold">HARDWARE</span>
            </div>
            <p className="text-gray-600">Category</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <div className="flex items-center justify-center h-12 mb-4">
              <span className="text-red-600 text-xl font-bold">SIH26113</span>
            </div>
            <p className="text-gray-600">Problem Statement ID</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ProjectOverview;