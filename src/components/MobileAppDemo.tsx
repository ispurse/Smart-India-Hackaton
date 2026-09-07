import React, { useState } from 'react';

const MobileAppDemo: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'trends' | 'alerts' | 'guidance'>('trends');

  return (
    <section id="mobile-app" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          MOBILE APPLICATION DEMO
        </h2>
        <div className="bg-gray-50 rounded-lg shadow overflow-hidden">
          {/* Tabs */}
          <div className="flex border-b border-gray-200">
            <button
              onClick={() => setActiveTab('trends')}
              className={`flex-1 px-4 py-3 text-left text-sm font-medium ${activeTab === 'trends' ? 'text-navy-800 border-b-2 border-navy-800' : 'text-gray-500 hover:text-gray-700'}`}
            >
              TRENDS
            </button>
            <button
              onClick={() => setActiveTab('alerts')}
              className={`flex-1 px-4 py-3 text-left text-sm font-medium ${activeTab === 'alerts' ? 'text-navy-800 border-b-2 border-navy-800' : 'text-gray-500 hover:text-gray-700'}`}
            >
              ALERTS
            </button>
            <button
              onClick={() => setActiveTab('guidance')}
              className={`flex-1 px-4 py-3 text-left text-sm font-medium ${activeTab === 'guidance' ? 'text-navy-800 border-b-2 border-navy-800' : 'text-gray-500 hover:text-gray-700'}`}
            >
              GUIDANCE
            </button>
          </div>

          {/* Tab Content */}
          <div className="p-6 space-y-4">
            {activeTab === 'trends' && (
              <div className="space-y-6">
                <h3 className="text-lg font-semibold text-gray-900">Trends Tab</h3>
                <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
                  {['Heart Rate', 'SpO2', 'Movement', 'Sleep', 'Kick Counter', 'Shape/Growth Trend'].map((label, index) => (
                    <div key={index} className="bg-white p-4 rounded-lg shadow flex flex-col items-center text-center">
                      <div className="w-10 h-10 flex items-center justify-center mb-3 bg-gray-100 rounded-full">
                        <span className="text-gray-500">{index === 0 ? '❤️' : index === 1 ? '💧' : index === 2 ? '🏃' : index === 3 ? '😴' : index === 4 ? '👶' : '📈'}</span>
                      </div>
                      <p className="text-sm font-medium text-gray-900">{label}</p>
                      <p className="text-xs text-gray-500 mt-1">DEMO DATA</p>
                    </div>
                  ))}
                </div>
              </div>
            )}
            {activeTab === 'alerts' && (
              <div className="space-y-4">
                <h3 className="text-lg font-semibold text-gray-900">Alerts Tab</h3>
                <p className="text-gray-600">No critical alerts</p>
                <div className="mt-4">
                  <div className="flex items-center space-x-3 p-3 bg-white rounded-lg shadow-sm">
                    <div className="w-8 h-8 flex items-center justify-center bg-red-500/10 text-red-600 rounded-full">
                      <span className="text-sm">🚨</span>
                    </div>
                    <div>
                      <p className="font-medium text-gray-900">Demo Alert: Elevated activity detected</p>
                      <p className="text-xs text-gray-500">Just now • Tap to view details</p>
                    </div>
                  </div>
                </div>
              </div>
            )}
            {activeTab === 'guidance' && (
              <div className="space-y-6">
                <h3 className="text-lg font-semibold text-gray-900">Guidance Tab</h3>
                <div className="space-y-4">
                  <div className="bg-white p-4 rounded-lg shadow">
                    <p className="font-medium text-gray-900">Wellness Guidance</p>
                    <p className="text-gray-600 text-sm">Stay hydrated and take short walks to improve circulation.</p>
                  </div>
                  <div className="bg-white p-4 rounded-lg shadow">
                    <p className="font-medium text-gray-900">Health Trends</p>
                    <p className="text-gray-600 text-sm">Your average resting heart rate is stable this week.</p>
                  </div>
                  <div className="bg-white p-4 rounded-lg shadow">
                    <p className="font-medium text-gray-900">Movement</p>
                    <p className="text-gray-600 text-sm">You've been active for 45 minutes today.</p>
                  </div>
                  <div className="bg-white p-4 rounded-lg shadow">
                    <p className="font-medium text-gray-900">Sleep</p>
                    <p className="text-gray-600 text-sm">You slept 7.2 hours last night.</p>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Disclaimer */}
        <div className="mt-6 text-center text-xs text-gray-500">
          Concept demonstration for Smart India Hackathon 2026.
          The website and simulated interfaces are for demonstration purposes and do not
          constitute medical diagnosis or emergency services.
        </div>
      </div>
    </section>
  );
};

export default MobileAppDemo;