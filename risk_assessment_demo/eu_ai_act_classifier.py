#!/usr/bin/env python3
"""
VerityAI Showcase - EU AI Act Classifier
Systematic AI system classification according to EU AI Act requirements
"""

import json
from typing import Dict, List, Any, Optional
from enum import Enum
from dataclasses import dataclass
from datetime import datetime, timedelta


class RiskCategory(Enum):
    UNACCEPTABLE = "unacceptable"
    HIGH_RISK = "high_risk"
    LIMITED_RISK = "limited_risk" 
    MINIMAL_RISK = "minimal_risk"


class AISystemSector(Enum):
    BIOMETRIC = "biometric_identification"
    CRITICAL_INFRASTRUCTURE = "critical_infrastructure"
    EDUCATION = "education_vocational_training"
    EMPLOYMENT = "employment_workers_management"
    ESSENTIAL_SERVICES = "essential_private_public_services"
    LAW_ENFORCEMENT = "law_enforcement"
    MIGRATION = "migration_asylum_border"
    JUSTICE = "administration_of_justice"
    DEMOCRATIC = "democratic_processes"
    GENERAL = "general_purpose"


@dataclass
class ClassificationResult:
    risk_category: RiskCategory
    sector: AISystemSector
    requirements: List[str]
    timeline_months: int
    compliance_deadline: str
    prohibited_practices: List[str]
    mitigation_measures: List[str]
    documentation_required: List[str]


class EUAIActClassifier:
    """Comprehensive EU AI Act system classifier and compliance assessor"""
    
    def __init__(self):
        self.prohibited_practices = self._load_prohibited_practices()
        self.high_risk_criteria = self._load_high_risk_criteria()
        self.sector_mappings = self._load_sector_mappings()
        self.compliance_requirements = self._load_compliance_requirements()
    
    def _load_prohibited_practices(self) -> List[str]:
        """Load AI practices prohibited under EU AI Act"""
        return [
            "social_scoring_citizens",
            "subliminal_manipulation",
            "exploitation_vulnerabilities",
            "real_time_biometric_public",
            "emotion_recognition_workplace_education",
            "biometric_categorization_sensitive_attributes",
            "indiscriminate_surveillance"
        ]
    
    def _load_high_risk_criteria(self) -> Dict[str, List[str]]:
        """Load criteria for high-risk AI system identification"""
        return {
            "safety_component": [
                "machinery_safety",
                "aviation_safety", 
                "automotive_safety",
                "medical_devices",
                "rail_safety"
            ],
            "regulated_domain": [
                "biometric_identification",
                "critical_infrastructure",
                "education_training",
                "employment_hr",
                "essential_services",
                "law_enforcement",
                "migration_border",
                "justice_democracy"
            ],
            "impact_criteria": [
                "fundamental_rights",
                "health_safety", 
                "democratic_processes",
                "legal_consequences",
                "access_to_services"
            ]
        }
    
    def _load_sector_mappings(self) -> Dict[str, AISystemSector]:
        """Map business sectors to AI Act regulated domains"""
        return {
            "financial_services": AISystemSector.ESSENTIAL_SERVICES,
            "healthcare": AISystemSector.ESSENTIAL_SERVICES,
            "education": AISystemSector.EDUCATION,
            "employment": AISystemSector.EMPLOYMENT,
            "law_enforcement": AISystemSector.LAW_ENFORCEMENT,
            "transportation": AISystemSector.CRITICAL_INFRASTRUCTURE,
            "energy": AISystemSector.CRITICAL_INFRASTRUCTURE,
            "telecommunications": AISystemSector.CRITICAL_INFRASTRUCTURE,
            "government": AISystemSector.DEMOCRATIC,
            "general": AISystemSector.GENERAL
        }
    
    def _load_compliance_requirements(self) -> Dict[RiskCategory, List[str]]:
        """Load compliance requirements by risk category"""
        return {
            RiskCategory.UNACCEPTABLE: [
                "immediate_prohibition",
                "system_decommission",
                "legal_review_required"
            ],
            RiskCategory.HIGH_RISK: [
                "risk_management_system",
                "data_governance_measures",
                "technical_documentation",
                "record_keeping_system",
                "transparency_obligations",
                "human_oversight_measures",
                "accuracy_robustness_cybersecurity",
                "quality_management_system",
                "conformity_assessment",
                "ce_marking",
                "registration_eu_database",
                "post_market_monitoring"
            ],
            RiskCategory.LIMITED_RISK: [
                "transparency_obligations",
                "user_information_requirements",
                "human_interaction_disclosure"
            ],
            RiskCategory.MINIMAL_RISK: [
                "voluntary_codes_conduct",
                "best_practices_adherence"
            ]
        }
    
    def classify_ai_system(self, ai_system: Dict[str, Any]) -> ClassificationResult:
        """Perform comprehensive EU AI Act classification"""
        
        # Check for prohibited practices first
        prohibited = self._check_prohibited_practices(ai_system)
        if prohibited:
            return self._create_unacceptable_result(ai_system, prohibited)
        
        # Determine sector
        sector = self._determine_sector(ai_system)
        
        # Assess risk level
        risk_category = self._assess_risk_level(ai_system, sector)
        
        # Generate compliance requirements
        requirements = self.compliance_requirements[risk_category]
        
        # Calculate timeline
        timeline = self._calculate_compliance_timeline(risk_category, sector)
        
        # Generate mitigation measures
        mitigations = self._generate_mitigation_measures(ai_system, risk_category)
        
        # Required documentation
        documentation = self._determine_documentation_requirements(risk_category)
        
        return ClassificationResult(
            risk_category=risk_category,
            sector=sector,
            requirements=requirements,
            timeline_months=timeline,
            compliance_deadline=self._calculate_deadline(timeline),
            prohibited_practices=prohibited,
            mitigation_measures=mitigations,
            documentation_required=documentation
        )
    
    def _check_prohibited_practices(self, ai_system: Dict[str, Any]) -> List[str]:
        """Check if AI system involves prohibited practices"""
        violations = []
        
        purpose = ai_system.get('purpose', '').lower()
        use_cases = ai_system.get('use_cases', [])
        data_types = ai_system.get('data_types', [])
        
        # Check for social scoring
        if 'social_scoring' in purpose or 'citizen_scoring' in purpose:
            violations.append('social_scoring_citizens')
        
        # Check for subliminal manipulation
        if 'subliminal' in purpose or 'manipulation' in purpose:
            violations.append('subliminal_manipulation')
        
        # Check for real-time biometric identification in public
        if ('biometric' in data_types and 
            ai_system.get('deployment_context') == 'public_space' and
            ai_system.get('real_time', False)):
            violations.append('real_time_biometric_public')
        
        # Check for emotion recognition in workplace/education
        if ('emotion_recognition' in use_cases and 
            ai_system.get('context') in ['workplace', 'education']):
            violations.append('emotion_recognition_workplace_education')
        
        return violations
    
    def _determine_sector(self, ai_system: Dict[str, Any]) -> AISystemSector:
        """Determine the regulated sector for the AI system"""
        sector_hint = ai_system.get('sector', 'general')
        return self.sector_mappings.get(sector_hint, AISystemSector.GENERAL)
    
    def _assess_risk_level(self, ai_system: Dict[str, Any], sector: AISystemSector) -> RiskCategory:
        """Assess the risk level of the AI system"""
        
        # High-risk sectors
        high_risk_sectors = [
            AISystemSector.BIOMETRIC,
            AISystemSector.CRITICAL_INFRASTRUCTURE,
            AISystemSector.EDUCATION,
            AISystemSector.EMPLOYMENT,
            AISystemSector.ESSENTIAL_SERVICES,
            AISystemSector.LAW_ENFORCEMENT,
            AISystemSector.MIGRATION,
            AISystemSector.JUSTICE
        ]
        
        if sector in high_risk_sectors:
            return RiskCategory.HIGH_RISK
        
        # Check for high-risk characteristics
        decision_impact = ai_system.get('decision_impact', '')
        user_interaction = ai_system.get('user_interaction', '')
        
        if decision_impact in ['automated_decision', 'significant_impact', 'legal_consequences']:
            return RiskCategory.HIGH_RISK
        
        # Check for limited risk (transparency required)
        if (user_interaction == 'direct_user_facing' or 
            'chatbot' in ai_system.get('name', '').lower() or
            'recommendation' in ai_system.get('purpose', '').lower()):
            return RiskCategory.LIMITED_RISK
        
        return RiskCategory.MINIMAL_RISK
    
    def _calculate_compliance_timeline(self, risk_category: RiskCategory, sector: AISystemSector) -> int:
        """Calculate compliance timeline in months"""
        base_timelines = {
            RiskCategory.UNACCEPTABLE: 0,  # Immediate
            RiskCategory.HIGH_RISK: 24,   # 2 years
            RiskCategory.LIMITED_RISK: 12, # 1 year
            RiskCategory.MINIMAL_RISK: 6   # 6 months
        }
        
        timeline = base_timelines[risk_category]
        
        # Adjust for sector complexity
        if sector in [AISystemSector.LAW_ENFORCEMENT, AISystemSector.JUSTICE]:
            timeline += 6  # Additional 6 months for sensitive sectors
        
        return timeline
    
    def _calculate_deadline(self, months: int) -> str:
        """Calculate compliance deadline date"""
        deadline = datetime.now() + timedelta(days=30 * months)
        return deadline.strftime('%Y-%m-%d')
    
    def _create_unacceptable_result(self, ai_system: Dict[str, Any], 
                                   violations: List[str]) -> ClassificationResult:
        """Create result for unacceptable risk systems"""
        return ClassificationResult(
            risk_category=RiskCategory.UNACCEPTABLE,
            sector=self._determine_sector(ai_system),
            requirements=self.compliance_requirements[RiskCategory.UNACCEPTABLE],
            timeline_months=0,
            compliance_deadline='Immediate',
            prohibited_practices=violations,
            mitigation_measures=['System must be prohibited and decommissioned'],
            documentation_required=['Legal review documentation', 'Decommission plan']
        )
    
    def _generate_mitigation_measures(self, ai_system: Dict[str, Any], 
                                    risk_category: RiskCategory) -> List[str]:
        """Generate specific mitigation measures"""
        measures = []
        
        if risk_category == RiskCategory.HIGH_RISK:
            measures.extend([
                'Implement comprehensive risk management system',
                'Establish human oversight protocols',
                'Deploy bias monitoring and mitigation',
                'Create incident response procedures',
                'Implement data governance framework'
            ])
        
        elif risk_category == RiskCategory.LIMITED_RISK:
            measures.extend([
                'Implement user disclosure mechanisms', 
                'Create transparency reporting',
                'Establish user feedback channels'
            ])
        
        return measures
    
    def _determine_documentation_requirements(self, risk_category: RiskCategory) -> List[str]:
        """Determine required documentation"""
        base_docs = ['System description', 'Risk assessment']
        
        if risk_category == RiskCategory.HIGH_RISK:
            base_docs.extend([
                'Technical documentation',
                'Quality management documentation',
                'Risk management documentation',
                'Data governance documentation',
                'Human oversight procedures',
                'Post-market monitoring plan',
                'Incident response plan'
            ])
        
        elif risk_category == RiskCategory.LIMITED_RISK:
            base_docs.extend([
                'User information documentation',
                'Transparency measures documentation'
            ])
        
        return base_docs
    
    def generate_compliance_report(self, classification: ClassificationResult, 
                                 ai_system: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comprehensive compliance report"""
        return {
            'system_overview': {
                'name': ai_system.get('name'),
                'purpose': ai_system.get('purpose'),
                'sector': classification.sector.value,
                'classification_date': datetime.now().isoformat()
            },
            'risk_assessment': {
                'risk_category': classification.risk_category.value,
                'risk_justification': f"Classified as {classification.risk_category.value} based on sector and impact assessment",
                'prohibited_practices': classification.prohibited_practices
            },
            'compliance_roadmap': {
                'requirements': classification.requirements,
                'timeline_months': classification.timeline_months,
                'compliance_deadline': classification.compliance_deadline,
                'mitigation_measures': classification.mitigation_measures
            },
            'documentation_requirements': classification.documentation_required,
            'next_steps': self._generate_next_steps(classification),
            'professional_services': {
                'recommendation': 'Contact VerityAI for comprehensive EU AI Act compliance implementation',
                'service_url': 'https://verityai.co/landing/ai-compliance-solutions'
            }
        }
    
    def _generate_next_steps(self, classification: ClassificationResult) -> List[str]:
        """Generate actionable next steps"""
        steps = ['Conduct detailed risk assessment']
        
        if classification.risk_category == RiskCategory.HIGH_RISK:
            steps.extend([
                'Establish AI governance committee',
                'Develop risk management framework',
                'Implement data governance measures',
                'Design human oversight procedures',
                'Plan conformity assessment process'
            ])
        elif classification.risk_category == RiskCategory.LIMITED_RISK:
            steps.extend([
                'Implement user disclosure mechanisms',
                'Create transparency documentation',
                'Establish monitoring procedures'
            ])
        
        return steps


def main():
    """Demonstration of EU AI Act classification"""
    classifier = EUAIActClassifier()
    
    print("🛡️ VerityAI Showcase - EU AI Act Classifier")
    print("=" * 50)
    
    # Example: Customer service chatbot classification
    ai_system = {
        'name': 'Customer Service Chatbot',
        'purpose': 'Automated customer query resolution with recommendation engine',
        'sector': 'financial_services',
        'user_interaction': 'direct_customer_facing',
        'decision_impact': 'service_delivery',
        'data_types': ['personal_data', 'financial_data'],
        'deployment_context': 'private_platform',
        'real_time': True,
        'use_cases': ['customer_support', 'product_recommendation']
    }
    
    # Perform classification
    classification_result = classifier.classify_ai_system(ai_system)
    
    print(f"\n📊 Classification Results:")
    print(f"System: {ai_system['name']}")
    print(f"Risk Category: {classification_result.risk_category.value.title().replace('_', ' ')}")
    print(f"Regulated Sector: {classification_result.sector.value.title().replace('_', ' ')}")
    print(f"Compliance Timeline: {classification_result.timeline_months} months")
    print(f"Compliance Deadline: {classification_result.compliance_deadline}")
    
    print(f"\n📋 Compliance Requirements ({len(classification_result.requirements)}):")
    for req in classification_result.requirements[:5]:  # Show first 5
        print(f"  • {req.replace('_', ' ').title()}")
    if len(classification_result.requirements) > 5:
        print(f"  • ... and {len(classification_result.requirements) - 5} more")
    
    print(f"\n🛠️ Recommended Mitigation Measures:")
    for measure in classification_result.mitigation_measures:
        print(f"  • {measure}")
    
    # Generate compliance report
    compliance_report = classifier.generate_compliance_report(classification_result, ai_system)
    
    print(f"\n🎯 Next Steps:")
    for step in compliance_report['next_steps']:
        print(f"  • {step}")
    
    print(f"\n💼 Professional Services:")
    print(f"  {compliance_report['professional_services']['recommendation']}")
    print(f"  Learn more: {compliance_report['professional_services']['service_url']}")
    
    print("\n✅ EU AI Act classification complete!")


if __name__ == "__main__":
    main()
