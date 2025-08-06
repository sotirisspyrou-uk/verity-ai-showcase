from risk_assessment_demo import EUAIActClassifier

# Demonstrate AI system classification
classifier = EUAIActClassifier()

# Example: Customer service chatbot classification
ai_system = {
    'name': 'Customer Service Chatbot',
    'purpose': 'Automated customer query resolution',
    'sector': 'financial_services',
    'user_interaction': 'direct_customer_facing',
    'decision_impact': 'service_delivery',
    'data_types': ['personal_data', 'financial_data']
}

# Perform classification
classification_result = classifier.classify_ai_system(ai_system)

print(f"Risk Category: {classification_result['risk_category']}")
print(f"Compliance Requirements: {classification_result['requirements']}")
print(f"Implementation Timeline: {classification_result['timeline']}")

# Output Example:
# Risk Category: High-Risk AI System
# Compliance Requirements: ['risk_management_system', 'data_governance', 'human_oversight']
# Implementation Timeline: 24 months
