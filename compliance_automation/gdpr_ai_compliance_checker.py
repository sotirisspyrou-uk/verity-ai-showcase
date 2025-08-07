#!/usr/bin/env python3
"""
GDPR AI Compliance Checker - Professional Portfolio Demo
Created by Sotirios Spyrou (https://www.linkedin.com/in/sspyrou/)

Demonstrates comprehensive GDPR compliance assessment for AI systems.
Essential for Data Protection Officers, Legal Teams, and AI Governance.

Target Audience: DPOs, Legal Counsel, Privacy Officers, EU Market Leaders
Strategic Value: Ensures lawful AI deployment across European markets

DISCLAIMER: This is demonstration code for portfolio purposes. 
Production implementations require legal consultation and customization.
Contact: https://verityai.co for enterprise GDPR compliance solutions.
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass
from enum import Enum


class GDPRPrinciple(Enum):
    """GDPR principles applicable to AI systems"""
    LAWFULNESS = "lawfulness"
    FAIRNESS = "fairness" 
    TRANSPARENCY = "transparency"
    PURPOSE_LIMITATION = "purpose_limitation"
    DATA_MINIMISATION = "data_minimisation"
    ACCURACY = "accuracy"
    STORAGE_LIMITATION = "storage_limitation"
    SECURITY = "security"
    ACCOUNTABILITY = "accountability"


class LegalBasis(Enum):
    """Legal bases for AI data processing under GDPR"""
    CONSENT = "consent"
    CONTRACT = "contract"
    LEGAL_OBLIGATION = "legal_obligation"
    VITAL_INTERESTS = "vital_interests"
    PUBLIC_TASK = "public_task"
    LEGITIMATE_INTERESTS = "legitimate_interests"


class DataCategory(Enum):
    """Categories of personal data in AI systems"""
    BASIC_PERSONAL = "basic_personal"
    SPECIAL_CATEGORY = "special_category"
    CRIMINAL_OFFENCE = "criminal_offence"
    PSEUDONYMIZED = "pseudonymized"
    ANONYMOUS = "anonymous"


@dataclass
class GDPRAssessmentResult:
    """GDPR compliance assessment results"""
    overall_score: float
    compliance_status: str
    principle_scores: Dict[str, float]
    legal_basis_status: str
    data_subject_rights_status: Dict[str, str]
    risk_level: str
    recommendations: List[str]
    action_items: List[Dict[str, Any]]


class GDPRAIComplianceChecker:
    """
    Comprehensive GDPR compliance checker for AI systems
    
    Key Capabilities:
    - GDPR principle assessment
    - Legal basis validation  
    - Data subject rights verification
    - Automated compliance scoring
    - Executive-ready recommendations
    """
    
    def __init__(self):
        self.gdpr_principles = self._load_gdpr_principles()
        self.data_subject_rights = self._load_data_subject_rights()
        self.compliance_thresholds = self._load_compliance_thresholds()
        
        print("🛡️ GDPR AI Compliance Checker Initialized")
        print("🇪🇺 Ready for European AI compliance assessment")
    
    def _load_gdpr_principles(self) -> Dict[GDPRPrinciple, Dict[str, Any]]:
        """Load GDPR principles with AI-specific requirements"""
        return {
            GDPRPrinciple.LAWFULNESS: {
                "description": "Processing must have valid legal basis",
                "ai_requirements": [
                    "Clear legal basis identified and documented",
                    "Legal basis communicated to data subjects",
                    "Processing scope matches legal basis"
                ],
                "assessment_criteria": {
                    "legal_basis_identified": 30,
                    "basis_appropriateness": 25,
                    "documentation_quality": 25,
                    "communication_clarity": 20
                }
            },
            GDPRPrinciple.FAIRNESS: {
                "description": "Processing must be fair to data subjects",
                "ai_requirements": [
                    "Bias detection and mitigation implemented",
                    "Fair outcomes across protected groups",
                    "No discriminatory decision-making"
                ],
                "assessment_criteria": {
                    "bias_testing": 35,
                    "fairness_metrics": 30,
                    "discrimination_prevention": 25,
                    "outcome_monitoring": 10
                }
            },
            GDPRPrinciple.TRANSPARENCY: {
                "description": "Clear information about processing activities",
                "ai_requirements": [
                    "Algorithmic transparency provisions",
                    "Clear privacy notices",
                    "Meaningful information about logic involved"
                ],
                "assessment_criteria": {
                    "privacy_notice_quality": 30,
                    "algorithmic_explanations": 35,
                    "decision_logic_clarity": 25,
                    "accessibility": 10
                }
            },
            GDPRPrinciple.PURPOSE_LIMITATION: {
                "description": "Data used only for specified purposes",
                "ai_requirements": [
                    "Clear purpose specification",
                    "Compatible use verification",
                    "Scope limitation controls"
                ],
                "assessment_criteria": {
                    "purpose_specification": 40,
                    "compatibility_assessment": 35,
                    "scope_controls": 25
                }
            },
            GDPRPrinciple.DATA_MINIMISATION: {
                "description": "Only necessary data should be processed",
                "ai_requirements": [
                    "Data minimization assessment",
                    "Feature selection justification", 
                    "Regular data relevance review"
                ],
                "assessment_criteria": {
                    "necessity_assessment": 40,
                    "feature_justification": 35,
                    "regular_review": 25
                }
            },
            GDPRPrinciple.ACCURACY: {
                "description": "Personal data must be accurate and up to date",
                "ai_requirements": [
                    "Data quality controls",
                    "Regular accuracy verification",
                    "Error correction procedures"
                ],
                "assessment_criteria": {
                    "quality_controls": 35,
                    "accuracy_monitoring": 30,
                    "correction_procedures": 25,
                    "update_mechanisms": 10
                }
            }
        }
    
    def _load_data_subject_rights(self) -> Dict[str, Dict[str, Any]]:
        """Load data subject rights with AI implementation requirements"""
        return {
            "access": {
                "name": "Right of Access",
                "ai_requirements": [
                    "Provide copy of personal data used in AI",
                    "Explain automated decision-making logic",
                    "Disclose data sources and recipients"
                ],
                "implementation_score": 0
            },
            "rectification": {
                "name": "Right to Rectification", 
                "ai_requirements": [
                    "Enable data correction in AI systems",
                    "Propagate corrections to model outputs",
                    "Document correction impact"
                ],
                "implementation_score": 0
            },
            "erasure": {
                "name": "Right to Erasure",
                "ai_requirements": [
                    "Enable data deletion from AI systems",
                    "Machine unlearning capabilities",
                    "Complete removal verification"
                ],
                "implementation_score": 0
            },
            "portability": {
                "name": "Right to Data Portability",
                "ai_requirements": [
                    "Structured data export capability",
                    "Machine-readable format provision",
                    "Transfer facilitation"
                ],
                "implementation_score": 0
            },
            "object": {
                "name": "Right to Object",
                "ai_requirements": [
                    "Opt-out from automated decision-making",
                    "Alternative processing methods",
                    "Clear objection mechanisms"
                ],
                "implementation_score": 0
            },
            "automated_decision": {
                "name": "Rights in Automated Decision-Making",
                "ai_requirements": [
                    "Human review of automated decisions",
                    "Explanation of decision logic",
                    "Challenge and correction mechanisms"
                ],
                "implementation_score": 0
            }
        }
    
    def _load_compliance_thresholds(self) -> Dict[str, float]:
        """Load compliance scoring thresholds"""
        return {
            "excellent": 90.0,
            "good": 75.0,
            "acceptable": 60.0,
            "needs_improvement": 40.0,
            "non_compliant": 0.0
        }
    
    def assess_ai_system_compliance(self, ai_system_config: Dict[str, Any]) -> GDPRAssessmentResult:
        """Comprehensive GDPR compliance assessment for AI system"""
        
        print(f"\n🔍 Assessing GDPR compliance for: {ai_system_config.get('name', 'AI System')}")
        
        # Assess GDPR principles
        principle_scores = {}
        total_principle_score = 0
        
        for principle in GDPRPrinciple:
            score = self._assess_principle_compliance(principle, ai_system_config)
            principle_scores[principle.value] = score
            total_principle_score += score
            print(f"   {principle.value.title()}: {score:.1f}%")
        
        overall_score = total_principle_score / len(GDPRPrinciple)
        
        # Assess legal basis
        legal_basis_status = self._assess_legal_basis(ai_system_config)
        
        # Assess data subject rights
        rights_status = self._assess_data_subject_rights(ai_system_config)
        
        # Determine compliance status
        compliance_status = self._determine_compliance_status(overall_score)
        
        # Assess risk level
        risk_level = self._assess_gdpr_risk_level(ai_system_config, overall_score)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(principle_scores, legal_basis_status, rights_status)
        
        # Generate action items
        action_items = self._generate_action_items(principle_scores, rights_status, risk_level)
        
        return GDPRAssessmentResult(
            overall_score=overall_score,
            compliance_status=compliance_status,
            principle_scores=principle_scores,
            legal_basis_status=legal_basis_status,
            data_subject_rights_status=rights_status,
            risk_level=risk_level,
            recommendations=recommendations,
            action_items=action_items
        )
    
    def _assess_principle_compliance(self, principle: GDPRPrinciple, 
                                   ai_config: Dict[str, Any]) -> float:
        """Assess compliance with specific GDPR principle"""
        
        principle_data = self.gdpr_principles[principle]
        criteria = principle_data["assessment_criteria"]
        
        total_score = 0
        total_weight = sum(criteria.values())
        
        # Simulate assessment based on AI system configuration
        # In production: integrate with actual compliance data
        
        if principle == GDPRPrinciple.LAWFULNESS:
            legal_basis_score = 85 if ai_config.get("legal_basis") else 20
            documentation_score = 80 if ai_config.get("legal_documentation") else 30
            communication_score = 75 if ai_config.get("privacy_notice") else 25
            
            total_score = (
                legal_basis_score * criteria["legal_basis_identified"] +
                legal_basis_score * criteria["basis_appropriateness"] +
                documentation_score * criteria["documentation_quality"] +
                communication_score * criteria["communication_clarity"]
            ) / 100
            
        elif principle == GDPRPrinciple.FAIRNESS:
            bias_testing_score = 90 if ai_config.get("bias_testing") else 10
            fairness_metrics_score = 85 if ai_config.get("fairness_monitoring") else 15
            discrimination_score = 80 if ai_config.get("discrimination_controls") else 20
            
            total_score = (
                bias_testing_score * criteria["bias_testing"] +
                fairness_metrics_score * criteria["fairness_metrics"] +
                discrimination_score * criteria["discrimination_prevention"] +
                70 * criteria["outcome_monitoring"]
            ) / 100
            
        elif principle == GDPRPrinciple.TRANSPARENCY:
            privacy_notice_score = 85 if ai_config.get("privacy_notice") else 25
            explanation_score = 70 if ai_config.get("explainable_ai") else 30
            logic_clarity_score = 75 if ai_config.get("decision_logic_docs") else 35
            
            total_score = (
                privacy_notice_score * criteria["privacy_notice_quality"] +
                explanation_score * criteria["algorithmic_explanations"] +
                logic_clarity_score * criteria["decision_logic_clarity"] +
                80 * criteria["accessibility"]
            ) / 100
        
        else:
            # Simplified scoring for other principles
            base_score = 70 if ai_config.get("gdpr_compliant", False) else 45
            total_score = base_score
        
        return min(100.0, max(0.0, total_score))
    
    def _assess_legal_basis(self, ai_config: Dict[str, Any]) -> str:
        """Assess legal basis appropriateness"""
        legal_basis = ai_config.get("legal_basis")
        data_types = ai_config.get("data_types", [])
        
        if not legal_basis:
            return "❌ No legal basis identified"
        
        # Check for special category data
        has_special_data = any(
            cat in data_types for cat in ["health", "biometric", "genetic", "racial", "political"]
        )
        
        if has_special_data and legal_basis == LegalBasis.LEGITIMATE_INTERESTS.value:
            return "⚠️ Legitimate interests insufficient for special category data"
        
        if legal_basis == LegalBasis.CONSENT.value:
            consent_quality = ai_config.get("consent_mechanism", {})
            if not consent_quality.get("freely_given", False):
                return "⚠️ Consent may not meet GDPR requirements"
        
        return f"✅ Legal basis: {legal_basis.title()}"
    
    def _assess_data_subject_rights(self, ai_config: Dict[str, Any]) -> Dict[str, str]:
        """Assess implementation of data subject rights"""
        rights_status = {}
        
        for right_name, right_data in self.data_subject_rights.items():
            # Simulate rights implementation assessment
            implementation_features = ai_config.get("data_subject_rights", {})
            
            if right_name in implementation_features:
                if implementation_features[right_name].get("implemented", False):
                    rights_status[right_name] = "✅ Implemented"
                elif implementation_features[right_name].get("planned", False):
                    rights_status[right_name] = "🔄 Planned"
                else:
                    rights_status[right_name] = "⚠️ Partially implemented"
            else:
                rights_status[right_name] = "❌ Not implemented"
        
        return rights_status
    
    def _determine_compliance_status(self, overall_score: float) -> str:
        """Determine overall compliance status"""
        if overall_score >= self.compliance_thresholds["excellent"]:
            return "🟢 Excellent Compliance"
        elif overall_score >= self.compliance_thresholds["good"]:
            return "🟡 Good Compliance"
        elif overall_score >= self.compliance_thresholds["acceptable"]:
            return "🟠 Acceptable Compliance"
        elif overall_score >= self.compliance_thresholds["needs_improvement"]:
            return "🔴 Needs Improvement"
        else:
            return "⛔ Non-Compliant"
    
    def _assess_gdpr_risk_level(self, ai_config: Dict[str, Any], compliance_score: float) -> str:
        """Assess GDPR-specific risk level"""
        risk_factors = 0
        
        # High-risk factors
        if ai_config.get("automated_decision_making", False):
            risk_factors += 2
        if ai_config.get("special_category_data", False):
            risk_factors += 2
        if ai_config.get("large_scale_processing", False):
            risk_factors += 1
        if ai_config.get("public_access", False):
            risk_factors += 1
        if compliance_score < 60:
            risk_factors += 2
        
        if risk_factors >= 5:
            return "🔴 Very High Risk"
        elif risk_factors >= 3:
            return "🟠 High Risk" 
        elif risk_factors >= 1:
            return "🟡 Medium Risk"
        else:
            return "🟢 Low Risk"
    
    def _generate_recommendations(self, principle_scores: Dict[str, float], 
                                legal_basis_status: str, rights_status: Dict[str, str]) -> List[str]:
        """Generate actionable GDPR compliance recommendations"""
        recommendations = []
        
        # Principle-based recommendations
        for principle, score in principle_scores.items():
            if score < 60:
                if principle == "fairness":
                    recommendations.append("🎯 Implement comprehensive bias testing and fairness monitoring")
                elif principle == "transparency":
                    recommendations.append("📝 Enhance algorithmic transparency and explainability")
                elif principle == "lawfulness":
                    recommendations.append("⚖️ Strengthen legal basis documentation and communication")
                elif principle == "data_minimisation":
                    recommendations.append("🔍 Conduct data minimization review and implement controls")
        
        # Legal basis recommendations
        if "❌" in legal_basis_status or "⚠️" in legal_basis_status:
            recommendations.append("📋 Review and strengthen legal basis for data processing")
        
        # Data subject rights recommendations
        unimplemented_rights = [right for right, status in rights_status.items() if "❌" in status]
        if unimplemented_rights:
            recommendations.append(f"🔧 Implement missing data subject rights: {', '.join(unimplemented_rights)}")
        
        # High-priority recommendations
        if not recommendations:
            recommendations.append("✅ Continue monitoring and maintaining current compliance level")
        
        return recommendations
    
    def _generate_action_items(self, principle_scores: Dict[str, float], 
                             rights_status: Dict[str, str], risk_level: str) -> List[Dict[str, Any]]:
        """Generate specific action items with priorities and timelines"""
        action_items = []
        
        # High priority items for low-scoring principles
        critical_principles = [p for p, score in principle_scores.items() if score < 50]
        
        for principle in critical_principles:
            action_items.append({
                "priority": "HIGH",
                "category": "GDPR Principle Compliance",
                "action": f"Address {principle.replace('_', ' ').title()} compliance gaps",
                "timeline": "30 days",
                "owner": "Data Protection Officer",
                "estimated_effort": "High"
            })
        
        # Data subject rights implementation
        missing_rights = [right for right, status in rights_status.items() if "❌" in status]
        if missing_rights:
            action_items.append({
                "priority": "MEDIUM",
                "category": "Data Subject Rights",
                "action": f"Implement {len(missing_rights)} missing data subject rights",
                "timeline": "60 days", 
                "owner": "Technical Team + Legal",
                "estimated_effort": "Medium"
            })
        
        # Risk-based actions
        if "Very High Risk" in risk_level or "High Risk" in risk_level:
            action_items.append({
                "priority": "CRITICAL",
                "category": "Risk Mitigation",
                "action": "Conduct comprehensive GDPR risk assessment and mitigation",
                "timeline": "14 days",
                "owner": "Chief Privacy Officer",
                "estimated_effort": "High"
            })
        
        return action_items
    
    def generate_dpo_report(self, assessment_result: GDPRAssessmentResult, 
                          ai_system_config: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comprehensive report for Data Protection Officer"""
        
        return {
            "report_metadata": {
                "system_name": ai_system_config.get("name", "AI System"),
                "assessment_date": datetime.now().isoformat(),
                "assessor": "GDPR AI Compliance Checker",
                "report_version": "1.0"
            },
            "executive_summary": {
                "overall_score": f"{assessment_result.overall_score:.1f}%",
                "compliance_status": assessment_result.compliance_status,
                "risk_level": assessment_result.risk_level,
                "critical_actions": len([a for a in assessment_result.action_items if a["priority"] == "CRITICAL"]),
                "key_finding": self._generate_key_finding(assessment_result)
            },
            "detailed_assessment": {
                "gdpr_principles": assessment_result.principle_scores,
                "legal_basis_assessment": assessment_result.legal_basis_status,
                "data_subject_rights": assessment_result.data_subject_rights_status,
                "compliance_gaps": [p for p, score in assessment_result.principle_scores.items() if score < 60]
            },
            "recommendations": assessment_result.recommendations,
            "action_plan": assessment_result.action_items,
            "regulatory_considerations": {
                "supervisory_authority": "Relevant EU Data Protection Authority",
                "potential_fines": self._calculate_potential_fines(assessment_result, ai_system_config),
                "notification_requirements": self._assess_notification_requirements(ai_system_config)
            },
            "next_steps": [
                "Review and approve action plan",
                "Assign resources for implementation",
                "Schedule follow-up assessment in 90 days",
                "Update privacy impact assessment"
            ]
        }
    
    def _generate_key_finding(self, assessment_result: GDPRAssessmentResult) -> str:
        """Generate key finding for executive summary"""
        if assessment_result.overall_score >= 80:
            return "Strong GDPR compliance with minor optimization opportunities"
        elif assessment_result.overall_score >= 60:
            return "Moderate compliance requiring focused improvements in key areas"
        else:
            return "Significant compliance gaps requiring immediate remediation"
    
    def _calculate_potential_fines(self, assessment_result: GDPRAssessmentResult, 
                                 ai_config: Dict[str, Any]) -> str:
        """Calculate potential GDPR fine exposure"""
        if assessment_result.overall_score >= 80:
            return "Low risk - compliance demonstrates good faith efforts"
        elif assessment_result.overall_score >= 60:
            return "Medium risk - up to 2% of annual turnover"
        else:
            return "High risk - up to 4% of annual turnover (€20M maximum)"
    
    def _assess_notification_requirements(self, ai_config: Dict[str, Any]) -> List[str]:
        """Assess regulatory notification requirements"""
        notifications = []
        
        if ai_config.get("high_risk_processing", False):
            notifications.append("Data Protection Impact Assessment required")
        if ai_config.get("international_transfers", False):
            notifications.append("International transfer mechanisms must be documented")
        if ai_config.get("automated_decision_making", False):
            notifications.append("Automated decision-making must be disclosed")
        
        return notifications if notifications else ["No special notification requirements identified"]


def demonstrate_gdpr_compliance():
    """Portfolio demonstration of GDPR compliance checking"""
    print("\n" + "="*65)
    print("🇪🇺 GDPR AI COMPLIANCE CHECKER - PORTFOLIO DEMONSTRATION")
    print("📊 Showcasing European Data Protection Expertise")
    print("👨‍💼 Created by Sotirios Spyrou - Technical Marketing Leader")
    print("="*65)
    
    # Initialize GDPR checker
    checker = GDPRAIComplianceChecker()
    
    # Define sample AI system for assessment
    sample_ai_system = {
        "name": "Customer Risk Assessment AI",
        "description": "AI system for automated customer creditworthiness assessment",
        "legal_basis": "legitimate_interests",
        "legal_documentation": True,
        "privacy_notice": True,
        "data_types": ["financial", "personal", "behavioral"],
        "automated_decision_making": True,
        "special_category_data": False,
        "large_scale_processing": True,
        "public_access": False,
        "bias_testing": True,
        "fairness_monitoring": True,
        "discrimination_controls": True,
        "explainable_ai": False,
        "decision_logic_docs": True,
        "gdpr_compliant": True,
        "data_subject_rights": {
            "access": {"implemented": True},
            "rectification": {"implemented": True},
            "erasure": {"planned": True},
            "portability": {"implemented": False},
            "object": {"implemented": True},
            "automated_decision": {"implemented": False}
        }
    }
    
    print(f"\n🔍 1. ASSESSING AI SYSTEM: {sample_ai_system['name']}")
    print(f"📋 Processing Type: {sample_ai_system['description']}")
    
    # Perform GDPR compliance assessment
    assessment = checker.assess_ai_system_compliance(sample_ai_system)
    
    print(f"\n📊 2. COMPLIANCE ASSESSMENT RESULTS")
    print(f"   Overall Score: {assessment.overall_score:.1f}%")
    print(f"   Status: {assessment.compliance_status}")
    print(f"   Risk Level: {assessment.risk_level}")
    print(f"   Legal Basis: {assessment.legal_basis_status}")
    
    # Display principle scores
    print(f"\n🎯 3. GDPR PRINCIPLES ASSESSMENT")
    for principle, score in assessment.principle_scores.items():
        status = "✅" if score >= 75 else "⚠️" if score >= 60 else "❌"
        print(f"   {status} {principle.replace('_', ' ').title()}: {score:.1f}%")
    
    # Display data subject rights status
    print(f"\n⚖️ 4. DATA SUBJECT RIGHTS STATUS")
    for right, status in assessment.data_subject_rights_status.items():
        print(f"   {status} {right.replace('_', ' ').title()}")
    
    # Show recommendations
    print(f"\n💡 5. KEY RECOMMENDATIONS")
    for i, recommendation in enumerate(assessment.recommendations, 1):
        print(f"   {i}. {recommendation}")
    
    # Generate DPO report
    dpo_report = checker.generate_dpo_report(assessment, sample_ai_system)
    
    print(f"\n📋 6. DATA PROTECTION OFFICER REPORT")
    print(f"   Key Finding: {dpo_report['executive_summary']['key_finding']}")
    print(f"   Critical Actions: {dpo_report['executive_summary']['critical_actions']}")
    print(f"   Potential Fine Risk: {dpo_report['regulatory_considerations']['potential_fines']}")
    
    # Show action items
    if assessment.action_items:
        print(f"\n⚡ 7. PRIORITY ACTION ITEMS")
        for item in assessment.action_items:
            print(f"   🔴 [{item['priority']}] {item['action']}")
            print(f"      Timeline: {item['timeline']} | Owner: {item['owner']}")
    
    print("\n" + "="*65)
    print("🏆 GDPR COMPLIANCE DEMONSTRATION COMPLETE")
    print("💼 This showcases enterprise-ready EU data protection capabilities")
    print("🎯 Perfect for DPOs, Legal Teams, and EU Market Operations")
    print("📞 Contact Sotirios Spyrou for GDPR implementation consulting")
    print("🔗 LinkedIn: https://www.linkedin.com/in/sspyrou/")
    print("🌐 Enterprise Solutions: https://verityai.co")
    print("="*65)


if __name__ == "__main__":
    demonstrate_gdpr_compliance()