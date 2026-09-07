import React from 'react';

const Preloader: React.FC = () => {
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-white">
      <div className="text-center">
        <div className="flex items-center justify-center mb-4">
          <div className="w-8 h-8 border-4 border-b-primary rounded-full animate-spin"></div>
        </div>
        <div className="space-y-2">
          <span className="font-bold text-xl">ROCKET 🚀</span>
          <span className="font-bold text-2xl">SMART MATERNITY BAND</span>
        </div>
      </div>
    </div>
  );
};

export default Preloader;