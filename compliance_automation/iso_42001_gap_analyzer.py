#!/usr/bin/env python3
"""
VerityAI Showcase - ISO 42001 Gap Analyzer
Comprehensive ISO 42001 compliance gap assessment and implementation roadmap
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum
from datetime import datetime, timedelta
import json


class ComplianceStatus(Enum):
    FULLY_COMPLIANT = "fully_compliant"
    SUBSTANTIALLY_COMPLIANT = "substantially_compliant"
    PARTIALLY_COMPLIANT = "partially_compliant"
    NON_COMPLIANT = "non_compliant"
    NOT_ASSESSED = "not_assessed"


class RequirementCategory(Enum):
    CONTEXT = "organizational_context"
    LEADERSHIP = "leadership_commitment"
    PLANNING = "planning_risk_management"
    SUPPORT = "support_resources"
    OPERATION = "operational_controls"
    EVALUATION = "performance_evaluation"
    IMPROVEMENT = "continual_improvement"


@dataclass
class ComplianceRequirement:
    requirement_id: str
    clause: str
    title: str
    category: RequirementCategory
    description: str
    current_status: ComplianceStatus
    gap_description: str
    implementation_effort: str  # low, medium, high, critical
    dependencies: List[str]
    artifacts_required: List[str]


@dataclass
class GapAnalysisResult:
    overall_compliance_score: float
    readiness_level: str
    category_scores: Dict[str, float]
    critical_gaps: List[str]
    implementation_roadmap: List[Dict[str, Any]]
    estimated_timeline_months: int
    resource_requirements: Dict[str, Any]
    quick_wins: List[str]


class ISO42001GapAnalyzer:
    """ISO 42001 compliance gap analysis and implementation planning"""
    
    def __init__(self):
        self.requirements = self._load_iso_42001_requirements()
        self.assessment_framework = self._load_assessment_framework()
        self.implementation_templates = self._load_implementation_templates()
    
    def _load_iso_42001_requirements(self) -> List[ComplianceRequirement]:
        """Load comprehensive ISO 42001 requirements framework"""
        requirements = [
            # 4. Context of the Organization
            ComplianceRequirement(
                requirement_id="4.1",
                clause="4.1",
                title="Understanding the Organization and its Context",
                category=RequirementCategory.CONTEXT,
                description="Organization must understand internal and external issues relevant to AI management system",
                current_status=ComplianceStatus.NOT_ASSESSED,
                gap_description="",
                implementation_effort="medium",
                dependencies=[],
                artifacts_required=[
                    "Context analysis document",
                    "Stakeholder mapping",
                    "Environmental scan report"
                ]
            ),
            ComplianceRequirement(
                requirement_id="4.2",
                clause="4.2",
                title="Understanding the Needs and Expectations of Interested Parties",
                category=RequirementCategory.CONTEXT,
                description="Identify interested parties and their requirements relevant to AI management system",
                current_status=ComplianceStatus.NOT_ASSESSED,
                gap_description="",
                implementation_effort="medium",
                dependencies=["4.1"],
                artifacts_required=[
                    "Interested parties register",
                    "Requirements analysis",
                    "Stakeholder communication plan"
                ]
            ),
            ComplianceRequirement(
                requirement_id="4.3",
                clause="4.3",
                title="Determining the Scope of the AI Management System",
                category=RequirementCategory.CONTEXT,
                description="Define boundaries and applicability of AI management system",
                current_status=ComplianceStatus.NOT_ASSESSED,
                gap_description="",
                implementation_effort="high",
                dependencies=["4.1", "4.2"],
                artifacts_required=[
                    "Scope statement",
                    "AI system inventory",
                    "Boundary definition document"
                ]
            ),
            
            # 5. Leadership
            ComplianceRequirement(
                requirement_id="5.1",
                clause="5.1",
                title="Leadership and Commitment",
                category=RequirementCategory.LEADERSHIP,
                description="Top management must demonstrate leadership and commitment to AI management system",
                current_status=ComplianceStatus.NOT_ASSESSED,
                gap_description="",
                implementation_effort="critical",
                dependencies=[],
                artifacts_required=[
                    "Leadership commitment statement",
                    "AI governance charter",
                    "Executive sponsorship documentation"
                ]
            ),
            ComplianceRequirement(
                requirement_id="5.2",
                clause="5.2",
                title="AI Policy",
                category=RequirementCategory.LEADERSHIP,
                description="Establish, implement and maintain AI policy appropriate to organization",
                current_status=ComplianceStatus.NOT_ASSESSED,
                gap_description="",
                implementation_effort="high",
                dependencies=["5.1"],
                artifacts_required=[
                    "AI policy document",
                    "Policy communication plan",
                    "Policy review procedures"
                ]
            ),
            
            # 6. Planning
            ComplianceRequirement(
                requirement_id="6.1",
                clause="6.1",
                title="Actions to Address Risks and Opportunities",
                category=RequirementCategory.PLANNING,
                description="Determine risks and opportunities for AI management system effectiveness",
                current_status=ComplianceStatus.NOT_ASSESSED,
                gap_description="",
                implementation_effort="high",
                dependencies=["4.1", "4.2", "4.3"],
                artifacts_required=[
                    "Risk register",
                    "Risk assessment methodology",
                    "Risk treatment plans"
                ]
            ),
            ComplianceRequirement(
                requirement_id="6.2",
                clause="6.2",
                title="AI Objectives and Planning to Achieve Them",
                category=RequirementCategory.PLANNING,
                description="Establish AI objectives consistent with AI policy and plan to achieve them",
                current_status=ComplianceStatus.NOT_ASSESSED,
                gap_description="",
                implementation_effort="medium",
                dependencies=["5.2", "6.1"],
                artifacts_required=[
                    "AI objectives document",
                    "Implementation plans",
                    "Success metrics definition"
                ]
            ),
            
            # 7. Support
            ComplianceRequirement(
                requirement_id="7.1",
                clause="7.1",
                title="Resources",
                category=RequirementCategory.SUPPORT,
                description="Determine and provide resources needed for AI management system",
                current_status=ComplianceStatus.NOT_ASSESSED,
                gap_description="",
                implementation_effort="high",
                dependencies=["6.2"],
                artifacts_required=[
                    "Resource allocation plan",
                    "Competency requirements",
                    "Infrastructure assessment"
                ]
            ),
            ComplianceRequirement(
                requirement_id="7.2",
                clause="7.2",
                title="Competence",
                category=RequirementCategory.SUPPORT,
                description="Ensure persons have necessary competence for effective AI management",
                current_status=ComplianceStatus.NOT_ASSESSED,
                gap_description="",
                implementation_effort="medium",
                dependencies=["7.1"],
                artifacts_required=[
                    "Competency matrix",
                    "Training programs",
                    "Competence evaluation records"
                ]
            ),
            
            # 8. Operation
            ComplianceRequirement(
                requirement_id="8.1",
                clause="8.1",
                title="Operational Planning and Control",
                category=RequirementCategory.OPERATION,
                description="Plan, implement and control processes needed to meet AI management requirements",
                current_status=ComplianceStatus.NOT_ASSESSED,
                gap_description="",
                implementation_effort="critical",
                dependencies=["6.1", "6.2", "7.1"],
                artifacts_required=[
                    "Process documentation",
                    "Operational procedures",
                    "Control mechanisms"
                ]
            ),
            
            # 9. Performance Evaluation
            ComplianceRequirement(
                requirement_id="9.1",
                clause="9.1",
                title="Monitoring, Measurement, Analysis and Evaluation",
                category=RequirementCategory.EVALUATION,
                description="Monitor, measure, analyze and evaluate AI management system performance",
                current_status=ComplianceStatus.NOT_ASSESSED,
                gap_description="",
                implementation_effort="high",
                dependencies=["8.1"],
                artifacts_required=[
                    "Monitoring plan",
                    "KPI definitions",
                    "Performance reports"
                ]
            ),
            ComplianceRequirement(
                requirement_id="9.2",
                clause="9.2",
                title="Internal Audit",
                category=RequirementCategory.EVALUATION,
                description="Conduct internal audits to verify AI management system conformity",
                current_status=ComplianceStatus.NOT_ASSESSED,
                gap_description="",
                implementation_effort="medium",
                dependencies=["9.1"],
                artifacts_required=[
                    "Audit program",
                    "Audit procedures",
                    "Audit reports"
                ]
            ),
            
            # 10. Improvement
            ComplianceRequirement(
                requirement_id="10.1",
                clause="10.1",
                title="Continual Improvement",
                category=RequirementCategory.IMPROVEMENT,
                description="Continually improve suitability, adequacy and effectiveness of AI management system",
                current_status=ComplianceStatus.NOT_ASSESSED,
                gap_description="",
                implementation_effort="medium",
                dependencies=["9.1", "9.2"],
                artifacts_required=[
                    "Improvement plans",
                    "Corrective actions",
                    "Preventive actions"
                ]
            )
        ]
        
        return requirements
    
    def _load_assessment_framework(self) -> Dict[str, Any]:
        """Load assessment scoring framework"""
        return {
            "scoring_criteria": {
                ComplianceStatus.FULLY_COMPLIANT: 5,
                ComplianceStatus.SUBSTANTIALLY_COMPLIANT: 4,
                ComplianceStatus.PARTIALLY_COMPLIANT: 3,
                ComplianceStatus.NON_COMPLIANT: 1,
                ComplianceStatus.NOT_ASSESSED: 0
            },
            "readiness_thresholds": {
                "certification_ready": 4.5,
                "advanced": 3.5,
                "intermediate": 2.5,
                "basic": 1.5,
                "initial": 0.0
            },
            "implementation_effort_weighting": {
                "low": 1,
                "medium": 2,
                "high": 3,
                "critical": 4
            }
        }
    
    def _load_implementation_templates(self) -> Dict[str, Any]:
        """Load implementation guidance templates"""
        return {
            "quick_wins": [
                "Establish AI governance committee",
                "Create AI system inventory",
                "Draft initial AI policy",
                "Conduct stakeholder mapping",
                "Define AI objectives"
            ],
            "resource_templates": {
                "small_organization": {
                    "team_size": "3-5 people",
                    "budget_range": "$50,000-$150,000",
                    "timeline_months": 6
                },
                "medium_organization": {
                    "team_size": "5-10 people",
                    "budget_range": "$150,000-$300,000", 
                    "timeline_months": 9
                },
                "large_organization": {
                    "team_size": "10-20 people",
                    "budget_range": "$300,000-$500,000",
                    "timeline_months": 12
                }
            }
        }
    
    def conduct_gap_analysis(self, organization_profile: Dict[str, Any], 
                           current_state_assessment: Optional[Dict[str, Any]] = None) -> GapAnalysisResult:
        """Conduct comprehensive ISO 42001 gap analysis"""
        
        # Assess current compliance status if assessment provided
        if current_state_assessment:
            self._update_requirements_status(current_state_assessment)
        
        # Calculate compliance scores
        category_scores = self._calculate_category_scores()
        overall_score = self._calculate_overall_compliance_score(category_scores)
        
        # Determine readiness level
        readiness_level = self._determine_readiness_level(overall_score)
        
        # Identify critical gaps
        critical_gaps = self._identify_critical_gaps()
        
        # Generate implementation roadmap
        roadmap = self._generate_implementation_roadmap(organization_profile)
        
        # Estimate timeline and resources
        timeline = self._estimate_implementation_timeline(organization_profile)
        resources = self._estimate_resource_requirements(organization_profile)
        
        # Identify quick wins
        quick_wins = self._identify_quick_wins()
        
        return GapAnalysisResult(
            overall_compliance_score=overall_score,
            readiness_level=readiness_level,
            category_scores=category_scores,
            critical_gaps=critical_gaps,
            implementation_roadmap=roadmap,
            estimated_timeline_months=timeline,
            resource_requirements=resources,
            quick_wins=quick_wins
        )
    
    def _update_requirements_status(self, assessment: Dict[str, Any]):
        """Update requirements status based on assessment"""
        for req in self.requirements:
            if req.requirement_id in assessment:
                req_assessment = assessment[req.requirement_id]
                req.current_status = ComplianceStatus(req_assessment.get('status', 'not_assessed'))
                req.gap_description = req_assessment.get('gap_description', '')
    
    def _calculate_category_scores(self) -> Dict[str, float]:
        """Calculate compliance scores by category"""
        category_scores = {}
        scoring = self.assessment_framework["scoring_criteria"]
        
        for category in RequirementCategory:
            category_requirements = [req for req in self.requirements if req.category == category]
            if category_requirements:
                total_score = sum(scoring[req.current_status] for req in category_requirements)
                max_possible = len(category_requirements) * scoring[ComplianceStatus.FULLY_COMPLIANT]
                category_scores[category.value] = (total_score / max_possible) * 5.0
            else:
                category_scores[category.value] = 0.0
        
        return category_scores
    
    def _calculate_overall_compliance_score(self, category_scores: Dict[str, float]) -> float:
        """Calculate weighted overall compliance score"""
        # Weight categories by criticality
        category_weights = {
            RequirementCategory.LEADERSHIP.value: 0.20,
            RequirementCategory.OPERATION.value: 0.25,
            RequirementCategory.PLANNING.value: 0.15,
            RequirementCategory.CONTEXT.value: 0.10,
            RequirementCategory.SUPPORT.value: 0.15,
            RequirementCategory.EVALUATION.value: 0.10,
            RequirementCategory.IMPROVEMENT.value: 0.05
        }
        
        weighted_score = sum(
            category_scores.get(category, 0) * weight 
            for category, weight in category_weights.items()
        )
        
        return weighted_score
    
    def _determine_readiness_level(self, overall_score: float) -> str:
        """Determine organizational readiness level"""
        thresholds = self.assessment_framework["readiness_thresholds"]
        
        if overall_score >= thresholds["certification_ready"]:
            return "Certification Ready"
        elif overall_score >= thresholds["advanced"]:
            return "Advanced"
        elif overall_score >= thresholds["intermediate"]:
            return "Intermediate" 
        elif overall_score >= thresholds["basic"]:
            return "Basic"
        else:
            return "Initial"
    
    def _identify_critical_gaps(self) -> List[str]:
        """Identify critical compliance gaps requiring immediate attention"""
        critical_gaps = []
        
        for req in self.requirements:
            if (req.current_status in [ComplianceStatus.NON_COMPLIANT, ComplianceStatus.NOT_ASSESSED] and
                req.implementation_effort == "critical"):
                critical_gaps.append(f"{req.clause} - {req.title}")
        
        return critical_gaps
    
    def _generate_implementation_roadmap(self, org_profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate phased implementation roadmap"""
        roadmap = []
        
        # Phase 1: Foundation (Months 1-3)
        phase1 = {
            "phase": "Foundation",
            "duration_months": 3,
            "objectives": [
                "Establish governance structure",
                "Define scope and context",
                "Secure leadership commitment"
            ],
            "requirements": [
                req for req in self.requirements 
                if req.category in [RequirementCategory.CONTEXT, RequirementCategory.LEADERSHIP]
            ],
            "deliverables": [
                "AI governance charter",
                "Organizational context analysis",
                "AI policy framework",
                "Stakeholder engagement plan"
            ]
        }
        roadmap.append(phase1)
        
        # Phase 2: Planning (Months 4-6)
        phase2 = {
            "phase": "Planning",
            "duration_months": 3,
            "objectives": [
                "Develop comprehensive planning framework",
                "Establish risk management processes",
                "Define AI objectives"
            ],
            "requirements": [
                req for req in self.requirements
                if req.category == RequirementCategory.PLANNING
            ],
            "deliverables": [
                "Risk management framework",
                "AI objectives and KPIs",
                "Implementation plans",
                "Resource allocation strategy"
            ]
        }
        roadmap.append(phase2)
        
        # Phase 3: Implementation (Months 7-9)
        phase3 = {
            "phase": "Implementation",
            "duration_months": 3,
            "objectives": [
                "Implement operational controls",
                "Establish support processes",
                "Deploy monitoring systems"
            ],
            "requirements": [
                req for req in self.requirements
                if req.category in [RequirementCategory.SUPPORT, RequirementCategory.OPERATION]
            ],
            "deliverables": [
                "Operational procedures",
                "Training programs",
                "Process documentation",
                "Control mechanisms"
            ]
        }
        roadmap.append(phase3)
        
        # Phase 4: Validation (Months 10-12)
        phase4 = {
            "phase": "Validation",
            "duration_months": 3,
            "objectives": [
                "Establish evaluation processes",
                "Implement continuous improvement",
                "Prepare for certification"
            ],
            "requirements": [
                req for req in self.requirements
                if req.category in [RequirementCategory.EVALUATION, RequirementCategory.IMPROVEMENT]
            ],
            "deliverables": [
                "Monitoring and measurement system",
                "Internal audit program",
                "Improvement processes",
                "Certification readiness assessment"
            ]
        }
        roadmap.append(phase4)
        
        return roadmap
    
    def _estimate_implementation_timeline(self, org_profile: Dict[str, Any]) -> int:
        """Estimate implementation timeline based on organization profile"""
        base_timeline = 12  # months
        
        # Adjust based on organization size
        org_size = org_profile.get('size', 'medium')
        size_multipliers = {
            'small': 0.75,
            'medium': 1.0,
            'large': 1.25,
            'enterprise': 1.5
        }
        
        # Adjust based on AI maturity
        ai_maturity = org_profile.get('ai_maturity', 'intermediate')
        maturity_multipliers = {
            'initial': 1.5,
            'developing': 1.25,
            'intermediate': 1.0,
            'advanced': 0.75
        }
        
        adjusted_timeline = (base_timeline * 
                           size_multipliers.get(org_size, 1.0) *
                           maturity_multipliers.get(ai_maturity, 1.0))
        
        return int(adjusted_timeline)
    
    def _estimate_resource_requirements(self, org_profile: Dict[str, Any]) -> Dict[str, Any]:
        """Estimate resource requirements for implementation"""
        org_size = org_profile.get('size', 'medium')
        templates = self.implementation_templates["resource_templates"]
        
        base_requirements = templates.get(f"{org_size}_organization", templates["medium_organization"])
        
        return {
            "team_composition": {
                "project_manager": 1,
                "ai_governance_specialist": 1,
                "compliance_manager": 1,
                "technical_leads": 2,
                "subject_matter_experts": "2-4"
            },
            "budget_estimate": base_requirements["budget_range"],
            "timeline_estimate": f"{base_requirements['timeline_months']} months",
            "external_support": [
                "ISO 42001 certification consultancy",
                "Legal and regulatory advisory",
                "Technical implementation support"
            ],
            "training_requirements": [
                "ISO 42001 awareness training",
                "AI governance fundamentals",
                "Risk management methodology",
                "Audit and assessment skills"
            ]
        }
    
    def _identify_quick_wins(self) -> List[str]:
        """Identify quick wins for immediate implementation"""
        return [
            "Establish AI governance steering committee",
            "Create comprehensive AI system inventory",
            "Draft organizational AI policy statement",
            "Conduct initial stakeholder analysis",
            "Define preliminary AI objectives and success metrics",
            "Implement basic risk identification process",
            "Establish regular governance review meetings"
        ]
    
    def generate_comprehensive_report(self, analysis_result: GapAnalysisResult, 
                                    org_profile: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comprehensive gap analysis report"""
        
        return {
            "executive_summary": {
                "organization": org_profile.get('name', 'Organization'),
                "assessment_date": datetime.now().isoformat(),
                "overall_compliance_score": f"{analysis_result.overall_compliance_score:.1f}/5.0",
                "readiness_level": analysis_result.readiness_level,
                "critical_gaps_count": len(analysis_result.critical_gaps),
                "estimated_timeline": f"{analysis_result.estimated_timeline_months} months",
                "certification_readiness": "Ready" if analysis_result.overall_compliance_score >= 4.5 else "Requires Implementation"
            },
            "detailed_assessment": {
                "category_scores": {
                    category: f"{score:.1f}/5.0" 
                    for category, score in analysis_result.category_scores.items()
                },
                "strengths": self._identify_strengths(analysis_result.category_scores),
                "improvement_areas": self._identify_improvement_areas(analysis_result.category_scores)
            },
            "implementation_strategy": {
                "roadmap": analysis_result.implementation_roadmap,
                "quick_wins": analysis_result.quick_wins,
                "resource_requirements": analysis_result.resource_requirements,
                "success_factors": [
                    "Strong executive commitment and sponsorship",
                    "Dedicated implementation team with clear roles",
                    "Regular monitoring and progress reviews",
                    "Integration with existing management systems",
                    "Continuous stakeholder engagement"
                ]
            },
            "risk_mitigation": {
                "implementation_risks": [
                    "Insufficient resource allocation",
                    "Lack of stakeholder buy-in",
                    "Competing organizational priorities",
                    "Skills and competency gaps"
                ],
                "mitigation_strategies": [
                    "Secure executive sponsorship and commitment",
                    "Develop comprehensive change management plan",
                    "Invest in team training and development",
                    "Engage external expertise where needed"
                ]
            },
            "professional_services": {
                "recommendation": "Consider VerityAI professional ISO 42001 implementation services",
                "services_offered": [
                    "Gap analysis and readiness assessment",
                    "Implementation planning and project management", 
                    "Training and competency development",
                    "Certification preparation and support"
                ],
                "service_url": "https://verityai.co/landing/ai-compliance-solutions"
            }
        }
    
    def _identify_strengths(self, category_scores: Dict[str, float]) -> List[str]:
        """Identify organizational strengths"""
        strengths = []
        for category, score in category_scores.items():
            if score >= 3.5:
                strengths.append(f"Strong {category.replace('_', ' ').title()} capability")
        
        if not strengths:
            strengths.append("Foundation ready for ISO 42001 implementation")
        
        return strengths
    
    def _identify_improvement_areas(self, category_scores: Dict[str, float]) -> List[str]:
        """Identify areas requiring improvement"""
        improvements = []
        for category, score in category_scores.items():
            if score < 2.0:
                improvements.append(f"Significant improvement needed in {category.replace('_', ' ').title()}")
            elif score < 3.0:
                improvements.append(f"Moderate improvement needed in {category.replace('_', ' ').title()}")
        
        return improvements


def main():
    """Demonstration of ISO 42001 gap analysis"""
    analyzer = ISO42001GapAnalyzer()
    
    print("🛡️ VerityAI Showcase - ISO 42001 Gap Analyzer")
    print("=" * 50)
    
    # Example organization profile
    org_profile = {
        'name': 'TechCorp Industries',
        'size': 'large',
        'ai_maturity': 'intermediate',
        'industry': 'manufacturing',
        'ai_systems_count': 12,
        'regulatory_requirements': ['ISO 9001', 'ISO 27001']
    }
    
    # Example current state assessment
    current_state = {
        '4.1': {'status': 'partially_compliant', 'gap_description': 'Context analysis exists but lacks AI-specific considerations'},
        '5.1': {'status': 'non_compliant', 'gap_description': 'No formal AI governance structure'},
        '5.2': {'status': 'not_assessed', 'gap_description': 'No AI policy exists'},
        '6.1': {'status': 'partially_compliant', 'gap_description': 'General risk management but no AI-specific risks'},
        '8.1': {'status': 'non_compliant', 'gap_description': 'No AI-specific operational controls'}
    }
    
    # Conduct gap analysis
    gap_analysis = analyzer.conduct_gap_analysis(org_profile, current_state)
    
    print(f"\n📊 Gap Analysis Results:")
    print(f"Organization: {org_profile['name']}")
    print(f"Overall Compliance Score: {gap_analysis.overall_compliance_score:.1f}/5.0")
    print(f"Readiness Level: {gap_analysis.readiness_level}")
    print(f"Estimated Implementation Timeline: {gap_analysis.estimated_timeline_months} months")
    
    print(f"\n📈 Category Scores:")
    for category, score in gap_analysis.category_scores.items():
        print(f"  • {category.replace('_', ' ').title()}: {score:.1f}/5.0")
    
    if gap_analysis.critical_gaps:
        print(f"\n⚠️ Critical Gaps ({len(gap_analysis.critical_gaps)}):")
        for gap in gap_analysis.critical_gaps[:3]:  # Show first 3
            print(f"  • {gap}")
    
    print(f"\n🚀 Quick Wins:")
    for win in gap_analysis.quick_wins[:5]:  # Show first 5
        print(f"  • {win}")
    
    # Generate comprehensive report
    comprehensive_report = analyzer.generate_comprehensive_report(gap_analysis, org_profile)
    
    print(f"\n📋 Implementation Phases:")
    for phase in comprehensive_report['implementation_strategy']['roadmap']:
        print(f"  • Phase {comprehensive_report['implementation_strategy']['roadmap'].index(phase) + 1}: {phase['phase']} ({phase['duration_months']} months)")
    
    print(f"\n💼 Professional Services:")
    print(f"  {comprehensive_report['professional_services']['recommendation']}")
    print(f"  Learn more: {comprehensive_report['professional_services']['service_url']}")
    
    print("\n✅ ISO 42001 gap analysis complete!")
    print("Next steps: Begin with quick wins and develop detailed implementation plan")


if __name__ == "__main__":
    main()