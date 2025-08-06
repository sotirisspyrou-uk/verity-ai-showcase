from governance_templates import GovernanceDashboard

# Demonstrate real-time governance monitoring
dashboard = GovernanceDashboard()

# Configure enterprise AI portfolio monitoring
portfolio_config = dashboard.configure_monitoring([
    {'system_id': 'customer_service_ai', 'risk_level': 'high', 'compliance_status': 'in_progress'},
    {'system_id': 'fraud_detection_ai', 'risk_level': 'high', 'compliance_status': 'compliant'},
    {'system_id': 'recommendation_engine', 'risk_level': 'limited', 'compliance_status': 'compliant'},
    {'system_id': 'chatbot_assistant', 'risk_level': 'minimal', 'compliance_status': 'compliant'}
])

# Generate executive summary
executive_summary = dashboard.generate_executive_report(
    portfolio_data=portfolio_config,
    reporting_period='Q4_2024',
    stakeholder_level='board_of_directors'
)

print(f"AI Systems Monitored: {executive_summary['total_systems']}")
print(f"Compliance Rate: {executive_summary['compliance_percentage']:.1%}")
print(f"High-Risk Systems: {executive_summary['high_risk_count']}")
