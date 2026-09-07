import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-gray-900 text-gray-200 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div className="flex flex-col items-center space-x-0 space-y-4">
          <div className="flex items-center justify-center space-x-4">
            <span className="text-xl font-bold">ROCKET 🚀 🚀</span>
            <span className="text-xl font-bold">SMART MATERNITY BAND</span>
          </div>
          <div className="text-sm">
            <span>SMART INDIA HACKATHON 2026</span>
            <span className="mx-2">•</span>
            <span>SIH26113</span>
            <span className="mx-2">•</span>
            <span>HEALTHTECH · HARDWARE</span>
          </div>
          <p className="text-xs mt-4">
            © 2026 Team Rocket
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;