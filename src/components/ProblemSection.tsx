import React from 'react';

const ProblemSection: React.FC = () => {
  return (
    <section id="problem" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          PREGNANCY NEEDS MORE THAN OCCASIONAL CHECK-INS.
        </h2>
        <div className="lg:flex lg:items-center lg:gap-16">
          {/* Text Content */}
          <div className="lg:w-1/2 space-y-8">
            <div className="prose prose-lg max-w-none">
              <p className="text-gray-700 leading-relaxed mb-6">
                Pregnancy is a beautiful journey, but it brings significant physical changes that can impact a woman's daily life and wellbeing. Traditional prenatal care often relies on periodic check-ups, leaving gaps in continuous monitoring that could detect issues earlier.
              </p>
              <p className="text-gray-700 leading-relaxed mb-6">
                Expectant mothers experience increased physical stress on their bodies, particularly in the lumbar region and abdomen. This can lead to discomfort, reduced mobility, and challenges in maintaining an active lifestyle throughout pregnancy.
              </p>
              <p className="text-gray-700 leading-relaxed mb-6">
                There's a growing need for continuous health monitoring that tracks both maternal and fetal wellbeing, providing insights into movement patterns, sleep quality, and potential complications that might otherwise go unnoticed between appointments.
              </p>
              <p className="text-gray-700 leading-relaxed">
                Emergency situations can arise unexpectedly, and having immediate access to alert systems that can notify caregivers or medical professionals could be crucial for timely intervention.
              </p>
            </div>
          </div>

          {/* Visualization */}
          <div className="lg:w-1/2 relative">
            <div className="aspect-w-1 aspect-h-1 w-full rounded-lg overflow-hidden shadow-2xl bg-gray-100">
              {/* Placeholder for animated wearable visualization */}
              <div className="flex h-full items-center justify-center text-gray-400">
                <div className="text-center">
                  <div className="w-24 h-24 border-4 border-dashed border-gray-300 rounded-full flex items-center justify-center">
                    <span className="text-gray-500">WEARABLE</span>
                  </div>
                  <p className="mt-4 text-sm text-gray-500">Smart Maternity Band Concept</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ProblemSection;