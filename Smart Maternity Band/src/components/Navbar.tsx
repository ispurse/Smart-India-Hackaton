import React from 'react';

const Navbar: React.FC = () => {
  return (
    <nav className="fixed top-0 left-0 right-0 z-40 bg-white/80 backdrop-blur-lg border-b border-gray-100">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <span className="text-2xl font-bold text-navy-800">ROCKET 🚀</span>
            </div>
            <div className="hidden md:block">
              <div className="flex space-x-8">
                <a href="#home" className="text-gray-600 hover:text-gray-900 transition-colors">Home</a>
                <a href="#problem" className="text-gray-600 hover:text-gray-900 transition-colors">Problem</a>
                <a href="#solution" className="text-gray-600 hover:text-gray-900 transition-colors">Solution</a>
                <a href="#technology" className="text-gray-600 hover:text-gray-900 transition-colors">Technology</a>
                <a href="#safety" className="text-gray-600 hover:text-gray-900 transition-colors">Safety</a>
                <a href="#impact" className="text-gray-600 hover:text-gray-900 transition-colors">Impact</a>
                <a href="#team" className="text-gray-600 hover:text-gray-900 transition-colors">Team</a>
              </div>
            </div>
          </div>
          <div className="flex items-center">
            <span className="badge bg-gradient-to-r from-blue-500 to-purple-600 text-white text-xs font-medium px-3 py-1 rounded-full">
              SIH 2026
            </span>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;