#!/usr/bin/env python3
"""
VerityAI Showcase - Executive Dashboard
Real-time AI governance monitoring and executive reporting
"""

import json
import pandas as pd
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum


class RiskLevel(Enum):
    MINIMAL = "minimal"
    LIMITED = "limited"
    HIGH = "high"
    UNACCEPTABLE = "unacceptable"


class ComplianceStatus(Enum):
    COMPLIANT = "compliant"
    IN_PROGRESS = "in_progress"
    GAP_IDENTIFIED = "gap_identified"
    NON_COMPLIANT = "non_compliant"


@dataclass
class AISystemStatus:
    system_id: str
    name: str
    risk_level: RiskLevel
    compliance_status: ComplianceStatus
    business_impact: str
    deployment_status: str
    last_assessment: str
    performance_score: float
    incidents_count: int


class GovernanceDashboard:
    """Executive dashboard for AI governance monitoring and reporting"""
    
    def __init__(self):
        self.portfolio_data = []
        self.metrics_history = []
        self.risk_thresholds = self._load_risk_thresholds()
        
    def _load_risk_thresholds(self) -> Dict[str, float]:
        """Load risk management thresholds"""
        return {
            "high_risk_systems_max": 0.20,  # Max 20% high-risk systems
            "compliance_rate_min": 0.85,    # Min 85% compliance rate
            "incident_rate_max": 0.05,      # Max 5% systems with incidents
            "performance_score_min": 0.80   # Min 80% average performance
        }
    
    def configure_monitoring(self, systems_config: List[Dict[str, Any]]) -> List[AISystemStatus]:
        """Configure monitoring for AI system portfolio"""
        portfolio = []
        
        for config in systems_config:
            system_status = AISystemStatus(
                system_id=config['system_id'],
                name=config.get('name', config['system_id'].replace('_', ' ').title()),
                risk_level=RiskLevel(config['risk_level']),
                compliance_status=ComplianceStatus(config['compliance_status']),
                business_impact=config.get('business_impact', 'medium'),
                deployment_status=config.get('deployment_status', 'production'),
                last_assessment=config.get('last_assessment', datetime.now().strftime('%Y-%m-%d')),
                performance_score=config.get('performance_score', 0.85),
                incidents_count=config.get('incidents_count', 0)
            )
            portfolio.append(system_status)
        
        self.portfolio_data = portfolio
        return portfolio
    
    def generate_executive_report(self, portfolio_data: List[AISystemStatus], 
                                reporting_period: str = "Q4_2024",
                                stakeholder_level: str = "board_of_directors") -> Dict[str, Any]:
        """Generate comprehensive executive summary report"""
        
        total_systems = len(portfolio_data)
        if total_systems == 0:
            return {"error": "No systems configured for monitoring"}
        
        # Calculate key metrics
        compliant_systems = len([s for s in portfolio_data if s.compliance_status == ComplianceStatus.COMPLIANT])
        high_risk_systems = len([s for s in portfolio_data if s.risk_level == RiskLevel.HIGH])
        systems_with_incidents = len([s for s in portfolio_data if s.incidents_count > 0])
        
        compliance_percentage = compliant_systems / total_systems
        high_risk_percentage = high_risk_systems / total_systems
        incident_rate = systems_with_incidents / total_systems
        average_performance = sum(s.performance_score for s in portfolio_data) / total_systems
        
        # Risk assessment
        risk_status = self._assess_portfolio_risk(
            compliance_percentage, high_risk_percentage, incident_rate, average_performance
        )
        
        # Generate insights
        insights = self._generate_executive_insights(portfolio_data, risk_status)
        
        # Action items
        action_items = self._generate_action_items(portfolio_data, risk_status)
        
        return {
            "reporting_period": reporting_period,
            "generation_date": datetime.now().isoformat(),
            "stakeholder_level": stakeholder_level,
            "portfolio_overview": {
                "total_systems": total_systems,
                "compliance_percentage": compliance_percentage,
                "high_risk_count": high_risk_systems,
                "systems_with_incidents": systems_with_incidents,
                "average_performance_score": average_performance
            },
            "risk_assessment": {
                "overall_risk_level": risk_status["overall_risk"],
                "risk_factors": risk_status["risk_factors"],
                "threshold_status": risk_status["threshold_compliance"]
            },
            "key_insights": insights,
            "priority_actions": action_items,
            "detailed_metrics": self._generate_detailed_metrics(portfolio_data),
            "trend_analysis": self._generate_trend_analysis(portfolio_data)
        }
    
    def _assess_portfolio_risk(self, compliance_rate: float, high_risk_rate: float, 
                              incident_rate: float, performance_score: float) -> Dict[str, Any]:
        """Assess overall portfolio risk level"""
        
        risk_factors = []
        threshold_compliance = {}
        
        # Check against thresholds
        if compliance_rate < self.risk_thresholds["compliance_rate_min"]:
            risk_factors.append(f"Compliance rate below threshold: {compliance_rate:.1%}")
            threshold_compliance["compliance"] = "BREACH"
        else:
            threshold_compliance["compliance"] = "OK"
            
        if high_risk_rate > self.risk_thresholds["high_risk_systems_max"]:
            risk_factors.append(f"High-risk systems exceed threshold: {high_risk_rate:.1%}")
            threshold_compliance["high_risk_systems"] = "BREACH"
        else:
            threshold_compliance["high_risk_systems"] = "OK"
            
        if incident_rate > self.risk_thresholds["incident_rate_max"]:
            risk_factors.append(f"Incident rate exceeds threshold: {incident_rate:.1%}")
            threshold_compliance["incidents"] = "BREACH"
        else:
            threshold_compliance["incidents"] = "OK"
            
        if performance_score < self.risk_thresholds["performance_score_min"]:
            risk_factors.append(f"Performance below threshold: {performance_score:.1%}")
            threshold_compliance["performance"] = "BREACH"
        else:
            threshold_compliance["performance"] = "OK"
        
        # Overall risk determination
        breach_count = sum(1 for status in threshold_compliance.values() if status == "BREACH")
        
        if breach_count >= 3:
            overall_risk = "CRITICAL"
        elif breach_count >= 2:
            overall_risk = "HIGH"
        elif breach_count >= 1:
            overall_risk = "MEDIUM"
        else:
            overall_risk = "LOW"
        
        return {
            "overall_risk": overall_risk,
            "risk_factors": risk_factors,
            "threshold_compliance": threshold_compliance
        }
    
    def _generate_executive_insights(self, portfolio_data: List[AISystemStatus], 
                                   risk_status: Dict[str, Any]) -> List[str]:
        """Generate key insights for executive stakeholders"""
        insights = []
        
        total_systems = len(portfolio_data)
        compliant_systems = len([s for s in portfolio_data if s.compliance_status == ComplianceStatus.COMPLIANT])
        
        # Compliance insight
        if compliant_systems == total_systems:
            insights.append("🟢 Full portfolio compliance achieved across all AI systems")
        elif compliant_systems / total_systems >= 0.8:
            insights.append(f"🟡 Strong compliance progress: {compliant_systems}/{total_systems} systems compliant")
        else:
            insights.append(f"🔴 Compliance gap requires attention: {compliant_systems}/{total_systems} systems compliant")
        
        # Risk distribution insight
        high_risk_count = len([s for s in portfolio_data if s.risk_level == RiskLevel.HIGH])
        if high_risk_count > 0:
            insights.append(f"⚠️ {high_risk_count} high-risk systems require enhanced oversight and monitoring")
        
        # Performance insight
        avg_performance = sum(s.performance_score for s in portfolio_data) / total_systems
        if avg_performance >= 0.9:
            insights.append(f"📈 Excellent system performance: {avg_performance:.1%} average score")
        elif avg_performance >= 0.8:
            insights.append(f"📊 Good system performance: {avg_performance:.1%} average score")
        else:
            insights.append(f"📉 Performance improvement needed: {avg_performance:.1%} average score")
        
        # Business impact insight
        critical_systems = [s for s in portfolio_data if s.business_impact == 'critical']
        if critical_systems:
            insights.append(f"🎯 {len(critical_systems)} mission-critical systems require priority attention")
        
        return insights
    
    def _generate_action_items(self, portfolio_data: List[AISystemStatus], 
                              risk_status: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate priority action items for executive decision-making"""
        actions = []
        
        # Compliance actions
        non_compliant = [s for s in portfolio_data if s.compliance_status != ComplianceStatus.COMPLIANT]
        if non_compliant:
            actions.append({
                "priority": "HIGH",
                "category": "Compliance",
                "action": f"Accelerate compliance efforts for {len(non_compliant)} non-compliant systems",
                "timeline": "30 days",
                "owner": "Chief Compliance Officer",
                "systems_affected": [s.system_id for s in non_compliant]
            })
        
        # High-risk system actions
        high_risk_systems = [s for s in portfolio_data if s.risk_level == RiskLevel.HIGH]
        if high_risk_systems:
            actions.append({
                "priority": "HIGH",
                "category": "Risk Management",
                "action": f"Implement enhanced monitoring for {len(high_risk_systems)} high-risk systems",
                "timeline": "14 days",
                "owner": "Chief Risk Officer",
                "systems_affected": [s.system_id for s in high_risk_systems]
            })
        
        # Performance improvement actions
        poor_performers = [s for s in portfolio_data if s.performance_score < 0.75]
        if poor_performers:
            actions.append({
                "priority": "MEDIUM",
                "category": "Performance",
                "action": f"Performance optimization required for {len(poor_performers)} underperforming systems",
                "timeline": "60 days",
                "owner": "Chief Technology Officer",
                "systems_affected": [s.system_id for s in poor_performers]
            })
        
        # Governance actions based on overall risk
        if risk_status["overall_risk"] in ["CRITICAL", "HIGH"]:
            actions.append({
                "priority": "CRITICAL",
                "category": "Governance",
                "action": "Emergency AI governance review and risk mitigation planning",
                "timeline": "7 days",
                "owner": "AI Ethics Committee",
                "systems_affected": "All systems"
            })
        
        return sorted(actions, key=lambda x: {"CRITICAL": 1, "HIGH": 2, "MEDIUM": 3, "LOW": 4}[x["priority"]])
    
    def _generate_detailed_metrics(self, portfolio_data: List[AISystemStatus]) -> Dict[str, Any]:
        """Generate detailed metrics breakdown"""
        
        # Risk distribution
        risk_distribution = {}
        for risk_level in RiskLevel:
            count = len([s for s in portfolio_data if s.risk_level == risk_level])
            risk_distribution[risk_level.value] = count
        
        # Compliance distribution
        compliance_distribution = {}
        for status in ComplianceStatus:
            count = len([s for s in portfolio_data if s.compliance_status == status])
            compliance_distribution[status.value] = count
        
        # Business impact analysis
        business_impact_distribution = {}
        for system in portfolio_data:
            impact = system.business_impact
            business_impact_distribution[impact] = business_impact_distribution.get(impact, 0) + 1
        
        return {
            "risk_distribution": risk_distribution,
            "compliance_distribution": compliance_distribution,
            "business_impact_distribution": business_impact_distribution,
            "performance_statistics": {
                "average_score": sum(s.performance_score for s in portfolio_data) / len(portfolio_data),
                "highest_score": max(s.performance_score for s in portfolio_data),
                "lowest_score": min(s.performance_score for s in portfolio_data)
            },
            "incident_statistics": {
                "total_incidents": sum(s.incidents_count for s in portfolio_data),
                "systems_with_incidents": len([s for s in portfolio_data if s.incidents_count > 0]),
                "incident_rate": len([s for s in portfolio_data if s.incidents_count > 0]) / len(portfolio_data)
            }
        }
    
    def _generate_trend_analysis(self, portfolio_data: List[AISystemStatus]) -> Dict[str, Any]:
        """Generate trend analysis (simulated for demonstration)"""
        
        # Simulated historical trends
        current_compliance = len([s for s in portfolio_data if s.compliance_status == ComplianceStatus.COMPLIANT]) / len(portfolio_data)
        
        return {
            "compliance_trend": {
                "current": f"{current_compliance:.1%}",
                "previous_quarter": "78%",
                "trend_direction": "↗️" if current_compliance > 0.78 else "↘️",
                "quarterly_change": f"{(current_compliance - 0.78) * 100:+.1f}%"
            },
            "risk_trend": {
                "high_risk_systems": len([s for s in portfolio_data if s.risk_level == RiskLevel.HIGH]),
                "previous_quarter": 3,
                "trend_direction": "↗️" if len([s for s in portfolio_data if s.risk_level == RiskLevel.HIGH]) > 3 else "↘️"
            },
            "performance_trend": {
                "current_avg": f"{sum(s.performance_score for s in portfolio_data) / len(portfolio_data):.1%}",
                "previous_quarter": "82%",
                "trend_direction": "↗️"
            }
        }
    
    def export_dashboard_data(self, format_type: str = "json") -> str:
        """Export dashboard data for external systems"""
        if not self.portfolio_data:
            return json.dumps({"error": "No data to export"})
        
        export_data = {
            "export_timestamp": datetime.now().isoformat(),
            "portfolio_summary": {
                "total_systems": len(self.portfolio_data),
                "systems": [
                    {
                        "system_id": s.system_id,
                        "name": s.name,
                        "risk_level": s.risk_level.value,
                        "compliance_status": s.compliance_status.value,
                        "performance_score": s.performance_score,
                        "incidents_count": s.incidents_count
                    } for s in self.portfolio_data
                ]
            }
        }
        
        if format_type == "json":
            return json.dumps(export_data, indent=2)
        else:
            return str(export_data)


def main():
    """Demonstration of executive dashboard capabilities"""
    print("🛡️ VerityAI Showcase - Executive Dashboard")
    print("=" * 50)
    
    # Initialize dashboard
    dashboard = GovernanceDashboard()
    
    # Configure sample AI portfolio
    sample_portfolio = [
        {
            'system_id': 'customer_service_ai', 
            'name': 'Customer Service AI Assistant',
            'risk_level': 'high', 
            'compliance_status': 'in_progress',
            'business_impact': 'critical',
            'performance_score': 0.87,
            'incidents_count': 0
        },
        {
            'system_id': 'fraud_detection_ai', 
            'name': 'Fraud Detection System',
            'risk_level': 'high', 
            'compliance_status': 'compliant',
            'business_impact': 'critical',
            'performance_score': 0.92,
            'incidents_count': 0
        },
        {
            'system_id': 'recommendation_engine', 
            'name': 'Product Recommendation Engine',
            'risk_level': 'limited', 
            'compliance_status': 'compliant',
            'business_impact': 'high',
            'performance_score': 0.88,
            'incidents_count': 0
        },
        {
            'system_id': 'chatbot_assistant', 
            'name': 'General Purpose Chatbot',
            'risk_level': 'minimal', 
            'compliance_status': 'compliant',
            'business_impact': 'medium',
            'performance_score': 0.83,
            'incidents_count': 1
        },
        {
            'system_id': 'inventory_optimizer',
            'name': 'Inventory Optimization AI',
            'risk_level': 'limited',
            'compliance_status': 'gap_identified',
            'business_impact': 'high',
            'performance_score': 0.79,
            'incidents_count': 0
        }
    ]
    
    # Configure monitoring
    portfolio_status = dashboard.configure_monitoring(sample_portfolio)
    
    # Generate executive report
    executive_summary = dashboard.generate_executive_report(
        portfolio_data=portfolio_status,
        reporting_period='Q1_2025',
        stakeholder_level='board_of_directors'
    )
    
    # Display key metrics
    print(f"\n📊 Portfolio Overview:")
    print(f"AI Systems Monitored: {executive_summary['portfolio_overview']['total_systems']}")
    print(f"Compliance Rate: {executive_summary['portfolio_overview']['compliance_percentage']:.1%}")
    print(f"High-Risk Systems: {executive_summary['portfolio_overview']['high_risk_count']}")
    print(f"Average Performance: {executive_summary['portfolio_overview']['average_performance_score']:.1%}")
    print(f"Overall Risk Level: {executive_summary['risk_assessment']['overall_risk_level']}")
    
    # Display insights
    print(f"\n🎯 Key Insights:")
    for insight in executive_summary['key_insights']:
        print(f"  {insight}")
    
    # Display priority actions
    print(f"\n📋 Priority Actions ({len(executive_summary['priority_actions'])}):")
    for action in executive_summary['priority_actions'][:3]:  # Show top 3
        print(f"  🔴 [{action['priority']}] {action['action']}")
        print(f"      Timeline: {action['timeline']} | Owner: {action['owner']}")
    
    print(f"\n✅ Executive dashboard ready for stakeholder review!")
    print("Dashboard provides real-time AI governance monitoring and actionable insights")
    
    # Professional services mention
    print(f"\n💼 Professional Services:")
    print("For customized executive dashboards and AI governance consulting:")
    print("Contact VerityAI at hello@verityai.co or visit verityai.co/services/ai-governance")


if __name__ == "__main__":
    main()