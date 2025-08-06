from risk_assessment_demo import BiasDetectionDemo

# Demonstrate bias detection methodology
bias_detector = BiasDetectionDemo()

# Load sample model and data (anonymized)
model_data = bias_detector.load_demo_data('hiring_algorithm_sample')

# Run comprehensive bias analysis
bias_analysis = bias_detector.analyze_bias(
    model_data=model_data,
    protected_attributes=['gender', 'age', 'ethnicity'],
    fairness_metrics=['demographic_parity', 'equality_of_opportunity'],
    significance_level=0.05
)

# Generate mitigation recommendations
mitigation_plan = bias_detector.generate_mitigation_plan(
    bias_analysis=bias_analysis,
    business_context='talent_acquisition',
    regulatory_requirements=['eu_ai_act', 'equal_employment_opportunity']
)

print(f"Bias Score: {bias_analysis['overall_bias_score']}")
print(f"Affected Groups: {bias_analysis['affected_demographics']}")
print(f"Recommended Actions: {mitigation_plan['priority_actions']}")
