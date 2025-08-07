#!/usr/bin/env python3
"""
AI Compliance Checker - Professional Portfolio Demo
Created by Sotirios Spyrou (https://www.linkedin.com/in/sspyrou/)

Demonstrates comprehensive AI compliance assessment across multiple regulatory frameworks.
Essential for Chief Compliance Officers, Risk Managers, and AI Governance Teams.

Target Audience: Compliance Officers, Risk Managers, Legal Teams, C-Suite Executives
Strategic Value: Transforms regulatory complexity into actionable compliance roadmaps

DISCLAIMER: This is demonstration code for portfolio purposes. 
Production implementations require legal consultation and regulatory customization.
Contact: https://verityai.co for enterprise compliance solutions.
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, asdict
from enum import Enum
import uuid


class RegulatoryFramework(Enum):
    """Major AI regulatory and compliance frameworks"""
    EU_AI_ACT = "eu_ai_act"
    GDPR = "gdpr"
    ISO_42001 = "iso_42001"
    NIST_AI_RMF = "nist_ai_rmf"
    IEEE_2859 = "ieee_2859"
    ISO_23053 = "iso_23053"
    CCPA = "ccpa"
    SOX = "sarbanes_oxley"
    HIPAA = "hipaa"
    PCI_DSS = "pci_dss"


class ComplianceStatus(Enum):
    """Compliance assessment status levels"""
    FULLY_COMPLIANT = "fully_compliant"
    SUBSTANTIALLY_COMPLIANT = "substantially_compliant"
    PARTIALLY_COMPLIANT = "partially_compliant"
    NON_COMPLIANT = "non_compliant"
    NOT_ASSESSED = "not_assessed"
    NOT_APPLICABLE = "not_applicable"


class RiskLevel(Enum):
    """Risk level classification for compliance gaps"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NEGLIGIBLE = "negligible"


class ComplianceCategory(Enum):
    """Categories of compliance requirements"""
    TECHNICAL = "technical"
    GOVERNANCE = "governance"
    DOCUMENTATION = "documentation"
    PROCESS = "process"
    TRAINING = "training"
    MONITORING = "monitoring"
    REPORTING = "reporting"


@dataclass
class ComplianceRequirement:
    """Individual compliance requirement definition"""
    requirement_id: str
    framework: RegulatoryFramework
    category: ComplianceCategory
    title: str
    description: str
    mandatory: bool
    weight: float  # Importance weighting 0-1
    validation_criteria: List[str]
    evidence_requirements: List[str]
    implementation_guidance: str


@dataclass
class ComplianceAssessment:
    """Assessment result for specific compliance requirement"""
    requirement_id: str
    status: ComplianceStatus
    score: float  # 0-100 compliance score
    risk_level: RiskLevel
    assessment_date: str
    evidence_provided: List[str]
    gaps_identified: List[str]
    remediation_actions: List[str]
    assessor: str
    next_review_date: str


@dataclass
class SystemComplianceReport:
    """Comprehensive compliance report for AI system"""
    system_id: str
    system_name: str
    assessment_date: str
    frameworks_assessed: List[RegulatoryFramework]
    overall_compliance_score: float
    framework_scores: Dict[str, float]
    compliance_status: ComplianceStatus
    critical_gaps: int
    high_priority_actions: List[Dict[str, Any]]
    certification_ready: bool
    next_assessment_due: str
    assessments: List[ComplianceAssessment]


class AIComplianceChecker:
    """
    Comprehensive AI compliance assessment system
    
    Key Capabilities:
    - Multi-framework compliance assessment
    - Risk-based gap analysis
    - Automated compliance scoring
    - Remediation action planning
    - Certification readiness evaluation
    """
    
    def __init__(self):
        self.compliance_frameworks = self._load_compliance_frameworks()
        self.assessment_history = []
        self.remediation_library = self._load_remediation_library()
        
        print("🔍 AI Compliance Checker Initialized")
        print("🛡️ Ready for comprehensive compliance assessment")
    
    def _load_compliance_frameworks(self) -> Dict[RegulatoryFramework, Dict[str, Any]]:
        """Load comprehensive compliance framework requirements"""
        return {
            RegulatoryFramework.EU_AI_ACT: {
                "name": "EU AI Act",
                "authority": "European Commission",
                "applicability": "AI systems in EU market",
                "key_requirements": [
                    "Risk assessment and classification",
                    "Quality management system",
                    "Data governance and management",
                    "Human oversight requirements",
                    "Accuracy, robustness and cybersecurity",
                    "Transparency and explainability",
                    "Conformity assessment procedures",
                    "Registration and monitoring"
                ],
                "compliance_weight": 0.25,  # High importance
                "penalty_severity": "Very High",
                "implementation_deadline": "2026-08-02"
            },
            RegulatoryFramework.GDPR: {
                "name": "General Data Protection Regulation",
                "authority": "EU Data Protection Authorities",
                "applicability": "Personal data processing",
                "key_requirements": [
                    "Lawful basis for processing",
                    "Data subject rights implementation",
                    "Privacy by design and by default",
                    "Data protection impact assessments",
                    "Data breach notification",
                    "International data transfers",
                    "Consent management",
                    "Data retention and deletion"
                ],
                "compliance_weight": 0.20,
                "penalty_severity": "Very High",
                "implementation_deadline": "Active"
            },
            RegulatoryFramework.ISO_42001: {
                "name": "ISO/IEC 42001 - AI Management Systems",
                "authority": "International Organization for Standardization",
                "applicability": "AI management systems",
                "key_requirements": [
                    "AI management system establishment",
                    "AI policy and objectives",
                    "Risk management processes",
                    "AI system lifecycle management",
                    "Performance monitoring and measurement",
                    "Continuous improvement processes",
                    "Competence and awareness",
                    "Documentation and records management"
                ],
                "compliance_weight": 0.15,
                "penalty_severity": "Medium",
                "implementation_deadline": "Voluntary"
            },
            RegulatoryFramework.NIST_AI_RMF: {
                "name": "NIST AI Risk Management Framework",
                "authority": "National Institute of Standards and Technology",
                "applicability": "AI risk management (US focus)",
                "key_requirements": [
                    "AI risk governance",
                    "AI system mapping and measurement",
                    "AI risk assessment and analysis",
                    "AI risk mitigation and management",
                    "Trustworthy AI characteristics",
                    "Human-AI configuration",
                    "Bias evaluation and mitigation",
                    "Explainability and interpretability"
                ],
                "compliance_weight": 0.15,
                "penalty_severity": "Medium",
                "implementation_deadline": "Guidance"
            },
            RegulatoryFramework.IEEE_2859: {
                "name": "IEEE 2859 - AI Engineering Ethics Framework",
                "authority": "Institute of Electrical and Electronics Engineers",
                "applicability": "AI system engineering ethics",
                "key_requirements": [
                    "Ethical design principles",
                    "Value-sensitive design",
                    "Stakeholder engagement",
                    "Ethics impact assessment",
                    "Moral agency considerations",
                    "Accountability mechanisms",
                    "Transparency requirements",
                    "Fairness evaluation"
                ],
                "compliance_weight": 0.10,
                "penalty_severity": "Low",
                "implementation_deadline": "Best Practice"
            }
        }
    
    def _load_remediation_library(self) -> Dict[str, Dict[str, Any]]:
        """Load remediation action templates for common compliance gaps"""
        return {
            "data_governance": {
                "title": "Implement Data Governance Framework",
                "description": "Establish comprehensive data governance for AI systems",
                "actions": [
                    "Develop data classification scheme",
                    "Implement data quality controls",
                    "Establish data lineage tracking",
                    "Create data retention policies"
                ],
                "timeline": "60-90 days",
                "resources": "Data governance specialist + technical team",
                "cost_estimate": "Medium"
            },
            "bias_monitoring": {
                "title": "Deploy Bias Detection and Monitoring",
                "description": "Implement comprehensive bias detection systems",
                "actions": [
                    "Select bias detection algorithms",
                    "Implement monitoring dashboard",
                    "Establish alert thresholds",
                    "Create bias remediation procedures"
                ],
                "timeline": "45-60 days",
                "resources": "ML engineer + ethics specialist",
                "cost_estimate": "Medium"
            },
            "explainability": {
                "title": "Enhance AI System Explainability",
                "description": "Implement explainable AI capabilities",
                "actions": [
                    "Select appropriate XAI techniques",
                    "Develop explanation interfaces",
                    "Train staff on explanation use",
                    "Validate explanation quality"
                ],
                "timeline": "90-120 days",
                "resources": "Senior ML engineer + UX designer",
                "cost_estimate": "High"
            },
            "documentation": {
                "title": "Complete Regulatory Documentation",
                "description": "Develop comprehensive compliance documentation",
                "actions": [
                    "Create technical documentation",
                    "Develop user guides",
                    "Document risk assessments",
                    "Maintain compliance records"
                ],
                "timeline": "30-45 days",
                "resources": "Technical writer + compliance officer",
                "cost_estimate": "Low"
            },
            "training": {
                "title": "Implement AI Ethics Training Program",
                "description": "Establish comprehensive AI ethics training",
                "actions": [
                    "Develop training curriculum",
                    "Create training materials",
                    "Deploy training program",
                    "Track completion and effectiveness"
                ],
                "timeline": "60-90 days",
                "resources": "Training specialist + ethics expert",
                "cost_estimate": "Medium"
            }
        }
    
    def assess_system_compliance(self, ai_system_config: Dict[str, Any],
                                frameworks: List[RegulatoryFramework] = None) -> SystemComplianceReport:
        """Conduct comprehensive compliance assessment for AI system"""
        
        if frameworks is None:
            frameworks = [RegulatoryFramework.EU_AI_ACT, RegulatoryFramework.GDPR, 
                         RegulatoryFramework.ISO_42001, RegulatoryFramework.NIST_AI_RMF]
        
        system_id = ai_system_config.get("system_id", "unknown")
        system_name = ai_system_config.get("name", "AI System")
        
        print(f"\n🔍 Conducting compliance assessment for: {system_name}")
        print(f"📋 Frameworks: {[f.value.upper() for f in frameworks]}")
        
        # Conduct assessments for each framework
        assessments = []
        framework_scores = {}
        
        for framework in frameworks:
            framework_assessments = self._assess_framework_compliance(framework, ai_system_config)
            assessments.extend(framework_assessments)
            
            # Calculate framework score
            framework_score = sum(a.score for a in framework_assessments) / len(framework_assessments)
            framework_scores[framework.value] = framework_score
            print(f"   {framework.value.upper()}: {framework_score:.1f}%")
        
        # Calculate overall compliance score
        weighted_score = 0
        total_weight = 0
        for framework in frameworks:
            weight = self.compliance_frameworks[framework]["compliance_weight"]
            score = framework_scores[framework.value]
            weighted_score += score * weight
            total_weight += weight
        
        overall_score = weighted_score / total_weight if total_weight > 0 else 0
        
        # Determine overall compliance status
        compliance_status = self._determine_compliance_status(overall_score)
        
        # Count critical gaps
        critical_gaps = len([a for a in assessments if a.risk_level == RiskLevel.CRITICAL])
        
        # Generate high-priority actions
        high_priority_actions = self._generate_priority_actions(assessments)
        
        # Determine certification readiness
        certification_ready = overall_score >= 85 and critical_gaps == 0
        
        # Create comprehensive report
        report = SystemComplianceReport(
            system_id=system_id,
            system_name=system_name,
            assessment_date=datetime.now().isoformat(),
            frameworks_assessed=frameworks,
            overall_compliance_score=overall_score,
            framework_scores=framework_scores,
            compliance_status=compliance_status,
            critical_gaps=critical_gaps,
            high_priority_actions=high_priority_actions,
            certification_ready=certification_ready,
            next_assessment_due=(datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d"),
            assessments=assessments
        )
        
        # Store in assessment history
        self.assessment_history.append(report)
        
        return report
    
    def _assess_framework_compliance(self, framework: RegulatoryFramework, 
                                   ai_config: Dict[str, Any]) -> List[ComplianceAssessment]:
        """Assess compliance with specific regulatory framework"""
        
        assessments = []
        framework_spec = self.compliance_frameworks[framework]
        
        if framework == RegulatoryFramework.EU_AI_ACT:
            assessments = self._assess_eu_ai_act_compliance(ai_config)
        elif framework == RegulatoryFramework.GDPR:
            assessments = self._assess_gdpr_compliance(ai_config)
        elif framework == RegulatoryFramework.ISO_42001:
            assessments = self._assess_iso_42001_compliance(ai_config)
        elif framework == RegulatoryFramework.NIST_AI_RMF:
            assessments = self._assess_nist_ai_rmf_compliance(ai_config)
        elif framework == RegulatoryFramework.IEEE_2859:
            assessments = self._assess_ieee_2859_compliance(ai_config)
        else:
            # Generic assessment for other frameworks
            assessments = self._assess_generic_compliance(framework, ai_config)
        
        return assessments
    
    def _assess_eu_ai_act_compliance(self, ai_config: Dict[str, Any]) -> List[ComplianceAssessment]:
        """Assess EU AI Act specific compliance requirements"""
        assessments = []
        
        # Risk Assessment and Classification
        risk_score = 85 if ai_config.get("risk_assessment_complete") else 25
        assessments.append(ComplianceAssessment(
            requirement_id="eu_ai_act_risk_assessment",
            status=self._score_to_status(risk_score),
            score=risk_score,
            risk_level=self._score_to_risk(risk_score),
            assessment_date=datetime.now().isoformat(),
            evidence_provided=["Risk assessment document"] if risk_score > 50 else [],
            gaps_identified=["Risk assessment incomplete"] if risk_score < 50 else [],
            remediation_actions=["Complete comprehensive risk assessment"] if risk_score < 50 else [],
            assessor="AI Compliance System",
            next_review_date=(datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        ))
        
        # Quality Management System
        qms_score = 80 if ai_config.get("quality_management_system") else 30
        assessments.append(ComplianceAssessment(
            requirement_id="eu_ai_act_qms",
            status=self._score_to_status(qms_score),
            score=qms_score,
            risk_level=self._score_to_risk(qms_score),
            assessment_date=datetime.now().isoformat(),
            evidence_provided=["QMS documentation"] if qms_score > 50 else [],
            gaps_identified=["QMS not established"] if qms_score < 50 else [],
            remediation_actions=["Implement ISO-aligned QMS"] if qms_score < 50 else [],
            assessor="AI Compliance System",
            next_review_date=(datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        ))
        
        # Human Oversight
        oversight_score = 90 if ai_config.get("human_oversight") else 20
        assessments.append(ComplianceAssessment(
            requirement_id="eu_ai_act_human_oversight",
            status=self._score_to_status(oversight_score),
            score=oversight_score,
            risk_level=self._score_to_risk(oversight_score),
            assessment_date=datetime.now().isoformat(),
            evidence_provided=["Human oversight procedures"] if oversight_score > 50 else [],
            gaps_identified=["Human oversight insufficient"] if oversight_score < 50 else [],
            remediation_actions=["Enhance human oversight mechanisms"] if oversight_score < 50 else [],
            assessor="AI Compliance System",
            next_review_date=(datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        ))
        
        # Transparency and Explainability
        transparency_score = 70 if ai_config.get("explainable_ai") else 35
        assessments.append(ComplianceAssessment(
            requirement_id="eu_ai_act_transparency",
            status=self._score_to_status(transparency_score),
            score=transparency_score,
            risk_level=self._score_to_risk(transparency_score),
            assessment_date=datetime.now().isoformat(),
            evidence_provided=["Explainability documentation"] if transparency_score > 50 else [],
            gaps_identified=["Limited explainability"] if transparency_score < 50 else [],
            remediation_actions=["Implement XAI capabilities"] if transparency_score < 50 else [],
            assessor="AI Compliance System",
            next_review_date=(datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        ))
        
        return assessments
    
    def _assess_gdpr_compliance(self, ai_config: Dict[str, Any]) -> List[ComplianceAssessment]:
        """Assess GDPR specific compliance requirements"""
        assessments = []
        
        # Lawful Basis
        legal_basis_score = 90 if ai_config.get("legal_basis_documented") else 15
        assessments.append(ComplianceAssessment(
            requirement_id="gdpr_legal_basis",
            status=self._score_to_status(legal_basis_score),
            score=legal_basis_score,
            risk_level=self._score_to_risk(legal_basis_score),
            assessment_date=datetime.now().isoformat(),
            evidence_provided=["Legal basis documentation"] if legal_basis_score > 50 else [],
            gaps_identified=["Legal basis not documented"] if legal_basis_score < 50 else [],
            remediation_actions=["Document legal basis for processing"] if legal_basis_score < 50 else [],
            assessor="AI Compliance System",
            next_review_date=(datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        ))
        
        # Data Subject Rights
        rights_score = 85 if ai_config.get("data_subject_rights_implemented") else 25
        assessments.append(ComplianceAssessment(
            requirement_id="gdpr_data_subject_rights",
            status=self._score_to_status(rights_score),
            score=rights_score,
            risk_level=self._score_to_risk(rights_score),
            assessment_date=datetime.now().isoformat(),
            evidence_provided=["Rights implementation documentation"] if rights_score > 50 else [],
            gaps_identified=["Data subject rights not fully implemented"] if rights_score < 50 else [],
            remediation_actions=["Implement all data subject rights"] if rights_score < 50 else [],
            assessor="AI Compliance System",
            next_review_date=(datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        ))
        
        # Privacy by Design
        privacy_score = 75 if ai_config.get("privacy_by_design") else 30
        assessments.append(ComplianceAssessment(
            requirement_id="gdpr_privacy_by_design",
            status=self._score_to_status(privacy_score),
            score=privacy_score,
            risk_level=self._score_to_risk(privacy_score),
            assessment_date=datetime.now().isoformat(),
            evidence_provided=["Privacy by design documentation"] if privacy_score > 50 else [],
            gaps_identified=["Privacy by design not implemented"] if privacy_score < 50 else [],
            remediation_actions=["Implement privacy by design principles"] if privacy_score < 50 else [],
            assessor="AI Compliance System",
            next_review_date=(datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        ))
        
        return assessments
    
    def _assess_iso_42001_compliance(self, ai_config: Dict[str, Any]) -> List[ComplianceAssessment]:
        """Assess ISO 42001 specific compliance requirements"""
        assessments = []
        
        # AI Management System
        ams_score = 80 if ai_config.get("ai_management_system") else 40
        assessments.append(ComplianceAssessment(
            requirement_id="iso_42001_ams",
            status=self._score_to_status(ams_score),
            score=ams_score,
            risk_level=self._score_to_risk(ams_score),
            assessment_date=datetime.now().isoformat(),
            evidence_provided=["AMS documentation"] if ams_score > 50 else [],
            gaps_identified=["AI management system incomplete"] if ams_score < 50 else [],
            remediation_actions=["Establish comprehensive AI management system"] if ams_score < 50 else [],
            assessor="AI Compliance System",
            next_review_date=(datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        ))
        
        # Performance Monitoring
        monitoring_score = 85 if ai_config.get("performance_monitoring") else 35
        assessments.append(ComplianceAssessment(
            requirement_id="iso_42001_monitoring",
            status=self._score_to_status(monitoring_score),
            score=monitoring_score,
            risk_level=self._score_to_risk(monitoring_score),
            assessment_date=datetime.now().isoformat(),
            evidence_provided=["Monitoring procedures"] if monitoring_score > 50 else [],
            gaps_identified=["Performance monitoring insufficient"] if monitoring_score < 50 else [],
            remediation_actions=["Implement comprehensive monitoring"] if monitoring_score < 50 else [],
            assessor="AI Compliance System",
            next_review_date=(datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        ))
        
        return assessments
    
    def _assess_nist_ai_rmf_compliance(self, ai_config: Dict[str, Any]) -> List[ComplianceAssessment]:
        """Assess NIST AI RMF specific compliance requirements"""
        assessments = []
        
        # AI Risk Governance
        governance_score = 75 if ai_config.get("ai_governance_framework") else 30
        assessments.append(ComplianceAssessment(
            requirement_id="nist_ai_governance",
            status=self._score_to_status(governance_score),
            score=governance_score,
            risk_level=self._score_to_risk(governance_score),
            assessment_date=datetime.now().isoformat(),
            evidence_provided=["Governance framework documentation"] if governance_score > 50 else [],
            gaps_identified=["AI governance framework incomplete"] if governance_score < 50 else [],
            remediation_actions=["Establish AI governance framework"] if governance_score < 50 else [],
            assessor="AI Compliance System",
            next_review_date=(datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        ))
        
        # Bias Evaluation
        bias_score = 85 if ai_config.get("bias_evaluation") else 25
        assessments.append(ComplianceAssessment(
            requirement_id="nist_bias_evaluation",
            status=self._score_to_status(bias_score),
            score=bias_score,
            risk_level=self._score_to_risk(bias_score),
            assessment_date=datetime.now().isoformat(),
            evidence_provided=["Bias evaluation report"] if bias_score > 50 else [],
            gaps_identified=["Bias evaluation incomplete"] if bias_score < 50 else [],
            remediation_actions=["Conduct comprehensive bias evaluation"] if bias_score < 50 else [],
            assessor="AI Compliance System",
            next_review_date=(datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        ))
        
        return assessments
    
    def _assess_ieee_2859_compliance(self, ai_config: Dict[str, Any]) -> List[ComplianceAssessment]:
        """Assess IEEE 2859 specific compliance requirements"""
        assessments = []
        
        # Ethical Design
        ethics_score = 80 if ai_config.get("ethical_design") else 40
        assessments.append(ComplianceAssessment(
            requirement_id="ieee_2859_ethics",
            status=self._score_to_status(ethics_score),
            score=ethics_score,
            risk_level=self._score_to_risk(ethics_score),
            assessment_date=datetime.now().isoformat(),
            evidence_provided=["Ethical design documentation"] if ethics_score > 50 else [],
            gaps_identified=["Ethical design principles not implemented"] if ethics_score < 50 else [],
            remediation_actions=["Implement ethical design principles"] if ethics_score < 50 else [],
            assessor="AI Compliance System",
            next_review_date=(datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        ))
        
        return assessments
    
    def _assess_generic_compliance(self, framework: RegulatoryFramework, 
                                  ai_config: Dict[str, Any]) -> List[ComplianceAssessment]:
        """Generic compliance assessment for frameworks without specific implementation"""
        base_score = 65 if ai_config.get("general_compliance", False) else 35
        
        return [ComplianceAssessment(
            requirement_id=f"{framework.value}_general",
            status=self._score_to_status(base_score),
            score=base_score,
            risk_level=self._score_to_risk(base_score),
            assessment_date=datetime.now().isoformat(),
            evidence_provided=["General compliance documentation"] if base_score > 50 else [],
            gaps_identified=["Framework-specific assessment needed"] if base_score < 75 else [],
            remediation_actions=["Conduct detailed framework assessment"] if base_score < 75 else [],
            assessor="AI Compliance System",
            next_review_date=(datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        )]
    
    def _score_to_status(self, score: float) -> ComplianceStatus:
        """Convert numeric score to compliance status"""
        if score >= 90:
            return ComplianceStatus.FULLY_COMPLIANT
        elif score >= 75:
            return ComplianceStatus.SUBSTANTIALLY_COMPLIANT
        elif score >= 50:
            return ComplianceStatus.PARTIALLY_COMPLIANT
        else:
            return ComplianceStatus.NON_COMPLIANT
    
    def _score_to_risk(self, score: float) -> RiskLevel:
        """Convert numeric score to risk level"""
        if score >= 90:
            return RiskLevel.NEGLIGIBLE
        elif score >= 75:
            return RiskLevel.LOW
        elif score >= 50:
            return RiskLevel.MEDIUM
        elif score >= 25:
            return RiskLevel.HIGH
        else:
            return RiskLevel.CRITICAL
    
    def _determine_compliance_status(self, overall_score: float) -> ComplianceStatus:
        """Determine overall system compliance status"""
        return self._score_to_status(overall_score)
    
    def _generate_priority_actions(self, assessments: List[ComplianceAssessment]) -> List[Dict[str, Any]]:
        """Generate prioritized remediation actions"""
        actions = []
        
        # Critical risk assessments
        critical_assessments = [a for a in assessments if a.risk_level == RiskLevel.CRITICAL]
        for assessment in critical_assessments:
            actions.append({
                "priority": "CRITICAL",
                "requirement": assessment.requirement_id,
                "action": f"Address critical compliance gap: {assessment.requirement_id}",
                "timeline": "14 days",
                "risk_level": "Critical",
                "estimated_effort": "High"
            })
        
        # High risk assessments
        high_risk_assessments = [a for a in assessments if a.risk_level == RiskLevel.HIGH]
        for assessment in high_risk_assessments:
            actions.append({
                "priority": "HIGH",
                "requirement": assessment.requirement_id,
                "action": f"Improve compliance: {assessment.requirement_id}",
                "timeline": "30 days",
                "risk_level": "High",
                "estimated_effort": "Medium"
            })
        
        # Medium risk assessments (top 3 only)
        medium_risk_assessments = [a for a in assessments if a.risk_level == RiskLevel.MEDIUM][:3]
        for assessment in medium_risk_assessments:
            actions.append({
                "priority": "MEDIUM",
                "requirement": assessment.requirement_id,
                "action": f"Enhance compliance: {assessment.requirement_id}",
                "timeline": "60 days",
                "risk_level": "Medium",
                "estimated_effort": "Medium"
            })
        
        # Sort by priority
        priority_order = {"CRITICAL": 1, "HIGH": 2, "MEDIUM": 3, "LOW": 4}
        return sorted(actions, key=lambda x: priority_order[x["priority"]])
    
    def generate_remediation_plan(self, compliance_report: SystemComplianceReport) -> Dict[str, Any]:
        """Generate comprehensive remediation plan based on compliance assessment"""
        
        # Analyze gaps and generate recommendations
        gap_categories = {}
        for assessment in compliance_report.assessments:
            if assessment.score < 75:  # Needs improvement
                for gap in assessment.gaps_identified:
                    category = self._categorize_gap(gap)
                    if category not in gap_categories:
                        gap_categories[category] = []
                    gap_categories[category].append(gap)
        
        # Generate remediation actions
        remediation_actions = []
        for category, gaps in gap_categories.items():
            if category in self.remediation_library:
                template = self.remediation_library[category]
                remediation_actions.append({
                    "category": category,
                    "title": template["title"],
                    "description": template["description"],
                    "actions": template["actions"],
                    "timeline": template["timeline"],
                    "resources": template["resources"],
                    "cost_estimate": template["cost_estimate"],
                    "gaps_addressed": gaps
                })
        
        return {
            "system_id": compliance_report.system_id,
            "system_name": compliance_report.system_name,
            "plan_date": datetime.now().isoformat(),
            "current_score": compliance_report.overall_compliance_score,
            "target_score": 90.0,
            "critical_gaps": compliance_report.critical_gaps,
            "remediation_timeline": "90-180 days",
            "estimated_investment": self._estimate_remediation_cost(remediation_actions),
            "remediation_actions": remediation_actions,
            "success_metrics": {
                "compliance_score_target": 90.0,
                "critical_gaps_target": 0,
                "certification_ready": True,
                "timeline_target": "6 months"
            }
        }
    
    def _categorize_gap(self, gap: str) -> str:
        """Categorize compliance gap for remediation planning"""
        gap_lower = gap.lower()
        
        if any(keyword in gap_lower for keyword in ["bias", "fairness", "discrimination"]):
            return "bias_monitoring"
        elif any(keyword in gap_lower for keyword in ["explainability", "transparency", "interpretability"]):
            return "explainability"
        elif any(keyword in gap_lower for keyword in ["data", "governance", "quality"]):
            return "data_governance"
        elif any(keyword in gap_lower for keyword in ["documentation", "records", "document"]):
            return "documentation"
        elif any(keyword in gap_lower for keyword in ["training", "competence", "awareness"]):
            return "training"
        else:
            return "documentation"  # Default category
    
    def _estimate_remediation_cost(self, remediation_actions: List[Dict[str, Any]]) -> str:
        """Estimate overall remediation cost based on individual action costs"""
        cost_mapping = {"Low": 1, "Medium": 2, "High": 3}
        total_cost_score = sum(cost_mapping.get(action["cost_estimate"], 2) for action in remediation_actions)
        
        if total_cost_score <= 3:
            return "Low (€50K-100K)"
        elif total_cost_score <= 6:
            return "Medium (€100K-250K)"
        else:
            return "High (€250K+)"
    
    def export_compliance_data(self, format_type: str = "json") -> str:
        """Export compliance assessment data for regulatory submissions"""
        
        export_data = {
            "export_metadata": {
                "generation_timestamp": datetime.now().isoformat(),
                "total_systems_assessed": len(self.assessment_history),
                "frameworks_supported": [f.value for f in RegulatoryFramework],
                "export_format": format_type
            },
            "compliance_reports": []
        }
        
        # Convert reports to exportable format
        for report in self.assessment_history:
            report_dict = asdict(report)
            # Convert enums to strings for JSON serialization
            report_dict["frameworks_assessed"] = [f.value for f in report.frameworks_assessed]
            report_dict["compliance_status"] = report.compliance_status.value
            
            for assessment in report_dict["assessments"]:
                assessment["status"] = assessment["status"].value
                assessment["risk_level"] = assessment["risk_level"].value
            
            export_data["compliance_reports"].append(report_dict)
        
        return json.dumps(export_data, indent=2, sort_keys=True)


def demonstrate_compliance_checking():
    """Portfolio demonstration of AI compliance checking capabilities"""
    print("\n" + "="*75)
    print("🔍 AI COMPLIANCE CHECKER - PORTFOLIO DEMONSTRATION")
    print("🛡️ Showcasing Comprehensive Regulatory Compliance Capabilities")
    print("👨‍💼 Created by Sotirios Spyrou - Technical Marketing Leader")
    print("="*75)
    
    # Initialize compliance checker
    checker = AIComplianceChecker()
    
    # Define sample AI system for assessment
    sample_ai_system = {
        "system_id": "customer_analytics_ai",
        "name": "Customer Analytics and Personalization AI",
        "description": "AI system for customer behavior analysis and personalized recommendations",
        "risk_assessment_complete": True,
        "quality_management_system": True,
        "human_oversight": True,
        "explainable_ai": False,  # Gap for demonstration
        "legal_basis_documented": True,
        "data_subject_rights_implemented": True,
        "privacy_by_design": True,
        "ai_management_system": False,  # Gap for demonstration
        "performance_monitoring": True,
        "ai_governance_framework": True,
        "bias_evaluation": False,  # Gap for demonstration
        "ethical_design": True,
        "general_compliance": True
    }
    
    print(f"\n🔍 1. ASSESSING AI SYSTEM: {sample_ai_system['name']}")
    print(f"📋 System Type: {sample_ai_system['description']}")
    
    # Conduct comprehensive compliance assessment
    compliance_report = checker.assess_system_compliance(
        ai_system_config=sample_ai_system,
        frameworks=[RegulatoryFramework.EU_AI_ACT, RegulatoryFramework.GDPR, 
                   RegulatoryFramework.ISO_42001, RegulatoryFramework.NIST_AI_RMF]
    )
    
    print(f"\n📊 2. COMPLIANCE ASSESSMENT RESULTS")
    print(f"   Overall Compliance Score: {compliance_report.overall_compliance_score:.1f}%")
    print(f"   Compliance Status: {compliance_report.compliance_status.value.replace('_', ' ').title()}")
    print(f"   Critical Gaps: {compliance_report.critical_gaps}")
    print(f"   Certification Ready: {'Yes' if compliance_report.certification_ready else 'No'}")
    
    # Display framework-specific scores
    print(f"\n🎯 3. FRAMEWORK-SPECIFIC SCORES")
    for framework, score in compliance_report.framework_scores.items():
        status_icon = "✅" if score >= 85 else "⚠️" if score >= 60 else "❌"
        print(f"   {status_icon} {framework.upper()}: {score:.1f}%")
    
    # Show critical and high-priority actions
    print(f"\n⚡ 4. PRIORITY ACTIONS ({len(compliance_report.high_priority_actions)})")
    for action in compliance_report.high_priority_actions[:5]:  # Show top 5
        priority_icon = "🔴" if action["priority"] == "CRITICAL" else "🟠" if action["priority"] == "HIGH" else "🟡"
        print(f"   {priority_icon} [{action['priority']}] {action['action']}")
        print(f"      Timeline: {action['timeline']} | Risk: {action['risk_level']}")
    
    # Generate remediation plan
    remediation_plan = checker.generate_remediation_plan(compliance_report)
    
    print(f"\n🛠️ 5. REMEDIATION PLAN")
    print(f"   Current Score: {remediation_plan['current_score']:.1f}%")
    print(f"   Target Score: {remediation_plan['target_score']:.1f}%")
    print(f"   Timeline: {remediation_plan['remediation_timeline']}")
    print(f"   Investment Estimate: {remediation_plan['estimated_investment']}")
    
    # Show top remediation actions
    print(f"\n🔧 6. REMEDIATION ACTIONS")
    for action in remediation_plan["remediation_actions"][:3]:  # Show top 3
        print(f"   • {action['title']}")
        print(f"     Timeline: {action['timeline']} | Cost: {action['cost_estimate']}")
        print(f"     Resources: {action['resources']}")
    
    # Show detailed assessment for one framework
    eu_ai_act_assessments = [a for a in compliance_report.assessments if "eu_ai_act" in a.requirement_id]
    if eu_ai_act_assessments:
        print(f"\n🏛️ 7. EU AI ACT DETAILED ASSESSMENT")
        for assessment in eu_ai_act_assessments:
            status_icon = "✅" if assessment.status == ComplianceStatus.FULLY_COMPLIANT else "⚠️" if assessment.status == ComplianceStatus.PARTIALLY_COMPLIANT else "❌"
            print(f"   {status_icon} {assessment.requirement_id}: {assessment.score:.1f}% ({assessment.status.value.replace('_', ' ').title()})")
            if assessment.gaps_identified:
                print(f"      Gaps: {', '.join(assessment.gaps_identified)}")
    
    print("\n" + "="*75)
    print("🏆 COMPLIANCE ASSESSMENT DEMONSTRATION COMPLETE")
    print("💼 This showcases enterprise-ready regulatory compliance capabilities")
    print("🎯 Perfect for Compliance Officers and Risk Management Teams")
    print("📞 Contact Sotirios Spyrou for compliance consulting")
    print("🔗 LinkedIn: https://www.linkedin.com/in/sspyrou/")
    print("🌐 Enterprise Solutions: https://verityai.co")
    print("="*75)


if __name__ == "__main__":
    demonstrate_compliance_checking()

