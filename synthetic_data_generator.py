#!/usr/bin/env python3
"""
VerityAI Showcase - Synthetic Data Generator
Realistic but synthetic data generation for demonstrations
"""

import random
import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum


class IndustryType(Enum):
    FINANCIAL_SERVICES = "financial_services"
    HEALTHCARE = "healthcare"
    MANUFACTURING = "manufacturing"
    RETAIL = "retail"
    TECHNOLOGY = "technology"
    GOVERNMENT = "government"


class RiskLevel(Enum):
    MINIMAL = "minimal"
    LIMITED = "limited"
    HIGH = "high"
    UNACCEPTABLE = "unacceptable"


@dataclass
class SyntheticAISystem:
    system_id: str
    name: str
    purpose: str
    industry: IndustryType
    risk_level: RiskLevel
    deployment_status: str
    compliance_status: str
    data_types: List[str]
    user_groups: List[str]
    business_impact: str


class SyntheticDataGenerator:
    """Generate realistic synthetic data for VerityAI demonstrations"""
    
    def __init__(self, seed: Optional[int] = None):
        if seed:
            random.seed(seed)
        
        self.ai_system_templates = self._load_ai_system_templates()
        self.company_profiles = self._load_company_profiles()
        
    def _load_ai_system_templates(self) -> Dict[str, Any]:
        """Load AI system templates for different industries"""
        return {
            IndustryType.FINANCIAL_SERVICES: [
                {
                    'names': ['Credit Risk Engine', 'Fraud Detection System', 'Robo Advisor', 'Customer Service Chatbot'],
                    'purposes': ['Credit assessment', 'Fraud prevention', 'Investment advice', 'Customer support'],
                    'data_types': ['financial_data', 'personal_data', 'transaction_history', 'credit_scores'],
                    'user_groups': ['customers', 'loan_officers', 'compliance_team', 'executives']
                }
            ],
            IndustryType.HEALTHCARE: [
                {
                    'names': ['Diagnostic AI', 'Drug Discovery Platform', 'Patient Monitoring System', 'Clinical Decision Support'],
                    'purposes': ['Medical diagnosis', 'Drug research', 'Patient care', 'Clinical guidance'],
                    'data_types': ['medical_records', 'diagnostic_images', 'lab_results', 'genetic_data'],
                    'user_groups': ['physicians', 'nurses', 'researchers', 'patients']
                }
            ],
            IndustryType.MANUFACTURING: [
                {
                    'names': ['Predictive Maintenance', 'Quality Control AI', 'Supply Chain Optimizer', 'Safety Monitor'],
                    'purposes': ['Equipment maintenance', 'Quality assurance', 'Logistics optimization', 'Workplace safety'],
                    'data_types': ['sensor_data', 'production_metrics', 'supply_chain_data', 'safety_records'],
                    'user_groups': ['operators', 'engineers', 'quality_inspectors', 'managers']
                }
            ],
            IndustryType.RETAIL: [
                {
                    'names': ['Recommendation Engine', 'Price Optimization', 'Inventory Forecasting', 'Customer Analytics'],
                    'purposes': ['Product recommendations', 'Dynamic pricing', 'Stock management', 'Customer insights'],
                    'data_types': ['customer_behavior', 'purchase_history', 'inventory_data', 'market_trends'],
                    'user_groups': ['customers', 'marketing_team', 'merchandisers', 'executives']
                }
            ],
            IndustryType.TECHNOLOGY: [
                {
                    'names': ['Code Review Assistant', 'Security Scanner', 'Performance Optimizer', 'User Experience Analyzer'],
                    'purposes': ['Code quality', 'Security analysis', 'Performance tuning', 'UX improvement'],
                    'data_types': ['source_code', 'security_logs', 'performance_metrics', 'user_interactions'],
                    'user_groups': ['developers', 'security_team', 'product_managers', 'designers']
                }
            ],
            IndustryType.GOVERNMENT: [
                {
                    'names': ['Document Classifier', 'Benefit Eligibility System', 'Traffic Management', 'Public Safety AI'],
                    'purposes': ['Document processing', 'Benefits administration', 'Traffic optimization', 'Emergency response'],
                    'data_types': ['government_documents', 'citizen_data', 'traffic_data', 'emergency_records'],
                    'user_groups': ['civil_servants', 'citizens', 'traffic_controllers', 'emergency_responders']
                }
            ]
        }
    
    def _load_company_profiles(self) -> List[Dict[str, Any]]:
        """Load synthetic company profiles"""
        return [
            {
                'name': 'Global Financial Corp',
                'industry': IndustryType.FINANCIAL_SERVICES,
                'size': 'fortune_500',
                'ai_maturity': 'advanced',
                'compliance_focus': ['eu_ai_act', 'basel_iii', 'mifid_ii']
            },
            {
                'name': 'Healthcare Innovation Ltd',
                'industry': IndustryType.HEALTHCARE,
                'size': 'large_enterprise',
                'ai_maturity': 'intermediate',
                'compliance_focus': ['fda_regulations', 'hipaa', 'gdpr']
            },
            {
                'name': 'Manufacturing Solutions Inc',
                'industry': IndustryType.MANUFACTURING,
                'size': 'mid_market',
                'ai_maturity': 'emerging',
                'compliance_focus': ['iso_45001', 'osha_standards', 'environmental_regulations']
            },
            {
                'name': 'Retail Tech Ventures',
                'industry': IndustryType.RETAIL,
                'size': 'growth_company',
                'ai_maturity': 'advanced',
                'compliance_focus': ['gdpr', 'ccpa', 'consumer_protection']
            }
        ]
    
    def generate_ai_system(self, industry: IndustryType = None, 
                          risk_level: RiskLevel = None) -> SyntheticAISystem:
        """Generate a synthetic AI system"""
        if not industry:
            industry = random.choice(list(IndustryType))
        
        if not risk_level:
            risk_level = random.choice(list(RiskLevel))
        
        templates = self.ai_system_templates.get(industry, [])
        if not templates:
            templates = list(self.ai_system_templates.values())[0]
        
        template = templates[0]  # Use first template for simplicity
        
        system_id = f"{industry.value}_{random.randint(1000, 9999)}"
        name = random.choice(template['names'])
        purpose = random.choice(template['purposes'])
        
        # Select random subset of data types and user groups
        data_types = random.sample(
            template['data_types'], 
            random.randint(1, len(template['data_types']))
        )
        user_groups = random.sample(
            template['user_groups'], 
            random.randint(1, len(template['user_groups']))
        )
        
        # Generate status based on risk level
        deployment_status = self._get_deployment_status(risk_level)
        compliance_status = self._get_compliance_status(risk_level)
        business_impact = self._get_business_impact(risk_level)
        
        return SyntheticAISystem(
            system_id=system_id,
            name=name,
            purpose=purpose,
            industry=industry,
            risk_level=risk_level,
            deployment_status=deployment_status,
            compliance_status=compliance_status,
            data_types=data_types,
            user_groups=user_groups,
            business_impact=business_impact
        )
    
    def generate_ai_portfolio(self, size: int = 5) -> List[SyntheticAISystem]:
        """Generate a portfolio of AI systems"""
        portfolio = []
        
        # Ensure diverse risk levels
        risk_distribution = {
            RiskLevel.MINIMAL: max(1, size // 4),
            RiskLevel.LIMITED: max(1, size // 3),
            RiskLevel.HIGH: max(1, size // 3),
            RiskLevel.UNACCEPTABLE: max(0, size // 10)
        }
        
        for risk_level, count in risk_distribution.items():
            for _ in range(count):
                system = self.generate_ai_system(risk_level=risk_level)
                portfolio.append(system)
        
        # Fill remaining slots with random systems
        while len(portfolio) < size:
            system = self.generate_ai_system()
            portfolio.append(system)
        
        return portfolio[:size]
    
    def generate_bias_dataset(self, protected_attributes: List[str] = None) -> Dict[str, Any]:
        """Generate synthetic dataset for bias analysis"""
        if not protected_attributes:
            protected_attributes = ['gender', 'age_group', 'ethnicity']
        
        sample_size = random.randint(1000, 5000)
        
        # Generate synthetic demographic data
        demographics = {}
        for attr in protected_attributes:
            if attr == 'gender':
                demographics[attr] = [random.choice(['male', 'female', 'other']) for _ in range(sample_size)]
            elif attr == 'age_group':
                demographics[attr] = [random.choice(['18-25', '26-35', '36-45', '46-55', '56-65', '65+']) for _ in range(sample_size)]
            elif attr == 'ethnicity':
                demographics[attr] = [random.choice(['white', 'black', 'hispanic', 'asian', 'other']) for _ in range(sample_size)]
            else:
                demographics[attr] = [random.choice(['group_a', 'group_b', 'group_c']) for _ in range(sample_size)]
        
        # Generate synthetic outcomes with potential bias
        outcomes = []
        for i in range(sample_size):
            # Introduce subtle bias for demonstration
            base_probability = 0.5
            
            # Gender bias example
            if 'gender' in demographics and demographics['gender'][i] == 'female':
                base_probability *= 0.9
            
            # Age bias example
            if 'age_group' in demographics and demographics['age_group'][i] in ['18-25', '65+']:
                base_probability *= 0.8
            
            outcome = random.random() < base_probability
            outcomes.append(outcome)
        
        return {
            'sample_size': sample_size,
            'demographics': demographics,
            'outcomes': outcomes,
            'protected_attributes': protected_attributes,
            'bias_injected': True,
            'generation_timestamp': datetime.now().isoformat()
        }
    
    def _get_deployment_status(self, risk_level: RiskLevel) -> str:
        """Generate appropriate deployment status based on risk level"""
        status_options = {
            RiskLevel.MINIMAL: ['production', 'production', 'production', 'testing'],
            RiskLevel.LIMITED: ['production', 'production', 'testing', 'development'],
            RiskLevel.HIGH: ['testing', 'compliance_review', 'development', 'production'],
            RiskLevel.UNACCEPTABLE: ['suspended', 'compliance_review', 'development']
        }
        return random.choice(status_options[risk_level])
    
    def _get_compliance_status(self, risk_level: RiskLevel) -> str:
        """Generate appropriate compliance status based on risk level"""
        status_options = {
            RiskLevel.MINIMAL: ['compliant', 'compliant', 'compliant', 'monitoring'],
            RiskLevel.LIMITED: ['compliant', 'compliant', 'monitoring', 'in_progress'],
            RiskLevel.HIGH: ['in_progress', 'in_progress', 'compliant', 'gap_identified'],
            RiskLevel.UNACCEPTABLE: ['gap_identified', 'suspended', 'major_remediation']
        }
        return random.choice(status_options[risk_level])
    
    def _get_business_impact(self, risk_level: RiskLevel) -> str:
        """Generate appropriate business impact based on risk level"""
        impact_options = {
            RiskLevel.MINIMAL: ['low', 'low', 'medium'],
            RiskLevel.LIMITED: ['medium', 'medium', 'high'],
            RiskLevel.HIGH: ['high', 'high', 'critical'],
            RiskLevel.UNACCEPTABLE: ['critical', 'critical']
        }
        return random.choice(impact_options[risk_level])


def main():
    """Demonstration of synthetic data generation"""
    generator = SyntheticDataGenerator(seed=42)
    
    print("🛡️ VerityAI Showcase - Synthetic Data Generator")
    print("=" * 50)
    
    # Generate sample AI system
    ai_system = generator.generate_ai_system()
    print(f"Sample AI System: {ai_system.name}")
    print(f"Industry: {ai_system.industry.value}")
    print(f"Risk Level: {ai_system.risk_level.value}")
    print(f"Compliance Status: {ai_system.compliance_status}")
    
    # Generate portfolio
    portfolio = generator.generate_ai_portfolio(size=8)
    print(f"\nGenerated Portfolio: {len(portfolio)} AI systems")
    
    risk_summary = {}
    for system in portfolio:
        risk_level = system.risk_level.value
        risk_summary[risk_level] = risk_summary.get(risk_level, 0) + 1
    
    print("Risk Distribution:")
    for risk, count in risk_summary.items():
        print(f"  {risk.title()}: {count} systems")
    
    # Generate bias dataset
    bias_data = generator.generate_bias_dataset()
    print(f"\nBias Analysis Dataset: {bias_data['sample_size']} samples")
    print(f"Protected Attributes: {bias_data['protected_attributes']}")
    
    print("\nSynthetic data ready for demonstration use!")


if __name__ == "__main__":
    main()