#!/usr/bin/env python3
"""
AI Audit Trail Builder - Professional Portfolio Demo
Created by Sotirios Spyrou (https://www.linkedin.com/in/sspyrou/)

Demonstrates comprehensive audit trail generation for AI systems compliance.
Essential for regulatory reporting, governance oversight, and risk management.

Target Audience: Chief Risk Officers, Compliance Teams, Auditors, Board Directors
Strategic Value: Transforms compliance from cost center to competitive advantage

DISCLAIMER: This is demonstration code for portfolio purposes. 
Production implementations require professional consultation and customization.
Contact: https://verityai.co for enterprise solutions.
"""

import json
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum
import uuid


class EventType(Enum):
    """AI system event classification for audit tracking"""
    MODEL_TRAINING = "model_training"
    MODEL_DEPLOYMENT = "model_deployment"
    DATA_PROCESSING = "data_processing"
    PREDICTION_MADE = "prediction_made"
    BIAS_DETECTION = "bias_detection"
    PERFORMANCE_MONITORING = "performance_monitoring"
    INCIDENT_LOGGED = "incident_logged"
    ACCESS_GRANTED = "access_granted"
    CONFIG_CHANGED = "configuration_changed"
    COMPLIANCE_REVIEW = "compliance_review"


class ComplianceFramework(Enum):
    """Regulatory frameworks requiring audit trails"""
    GDPR = "gdpr"
    EU_AI_ACT = "eu_ai_act"
    ISO_42001 = "iso_42001"
    NIST_AI_RMF = "nist_ai_rmf"
    SOX = "sarbanes_oxley"
    BASEL_III = "basel_iii"


@dataclass
class AuditEvent:
    """Immutable audit event record"""
    event_id: str
    timestamp: str
    event_type: EventType
    system_id: str
    user_id: str
    action_description: str
    data_hash: str
    compliance_frameworks: List[ComplianceFramework]
    risk_level: str
    business_impact: str
    metadata: Dict[str, Any]
    verification_signature: str


class AIAuditTrailBuilder:
    """
    Enterprise-grade audit trail system for AI governance
    
    Key Benefits:
    - Regulatory compliance automation
    - Immutable audit records
    - Real-time compliance monitoring
    - Executive-ready reporting
    """
    
    def __init__(self):
        self.audit_events = []
        self.system_registry = {}
        self.compliance_rules = self._load_compliance_rules()
        self.encryption_key = self._generate_encryption_key()
        
        print("🛡️ AI Audit Trail Builder Initialized")
        print("📊 Ready for enterprise compliance tracking")
    
    def _load_compliance_rules(self) -> Dict[ComplianceFramework, Dict[str, Any]]:
        """Define compliance-specific audit requirements"""
        return {
            ComplianceFramework.GDPR: {
                "retention_days": 2190,  # 6 years
                "required_events": [EventType.DATA_PROCESSING, EventType.ACCESS_GRANTED],
                "anonymization_required": True,
                "consent_tracking": True
            },
            ComplianceFramework.EU_AI_ACT: {
                "retention_days": 2555,  # 7 years
                "required_events": [EventType.MODEL_TRAINING, EventType.BIAS_DETECTION, 
                                  EventType.PERFORMANCE_MONITORING],
                "risk_assessment_required": True,
                "human_oversight_tracking": True
            },
            ComplianceFramework.ISO_42001: {
                "retention_days": 2190,
                "required_events": [EventType.COMPLIANCE_REVIEW, EventType.INCIDENT_LOGGED],
                "continuous_monitoring": True,
                "process_documentation": True
            }
        }
    
    def _generate_encryption_key(self) -> str:
        """Generate unique encryption key for audit integrity"""
        return hashlib.sha256(f"audit_key_{datetime.now().isoformat()}".encode()).hexdigest()
    
    def register_ai_system(self, system_id: str, system_name: str, 
                          risk_level: str, compliance_frameworks: List[ComplianceFramework]):
        """Register AI system for audit tracking"""
        self.system_registry[system_id] = {
            "name": system_name,
            "risk_level": risk_level,
            "compliance_frameworks": compliance_frameworks,
            "registration_date": datetime.now().isoformat(),
            "audit_events_count": 0
        }
        
        # Log system registration as audit event
        self.log_event(
            event_type=EventType.CONFIG_CHANGED,
            system_id=system_id,
            user_id="system_admin",
            action_description=f"AI system '{system_name}' registered for audit tracking",
            compliance_frameworks=compliance_frameworks,
            risk_level=risk_level,
            business_impact="high",
            metadata={"registration": True, "system_name": system_name}
        )
    
    def log_event(self, event_type: EventType, system_id: str, user_id: str,
                  action_description: str, compliance_frameworks: List[ComplianceFramework],
                  risk_level: str, business_impact: str, metadata: Dict[str, Any] = None):
        """Log immutable audit event with compliance verification"""
        
        if metadata is None:
            metadata = {}
        
        # Create unique event ID
        event_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        
        # Create data hash for integrity verification
        data_string = f"{event_id}{timestamp}{event_type.value}{system_id}{action_description}"
        data_hash = hashlib.sha256(data_string.encode()).hexdigest()
        
        # Generate verification signature
        verification_data = f"{data_hash}{self.encryption_key}"
        verification_signature = hashlib.sha256(verification_data.encode()).hexdigest()
        
        # Create audit event
        audit_event = AuditEvent(
            event_id=event_id,
            timestamp=timestamp,
            event_type=event_type,
            system_id=system_id,
            user_id=user_id,
            action_description=action_description,
            data_hash=data_hash,
            compliance_frameworks=compliance_frameworks,
            risk_level=risk_level,
            business_impact=business_impact,
            metadata=metadata,
            verification_signature=verification_signature
        )
        
        # Store event (in production: encrypted database)
        self.audit_events.append(audit_event)
        
        # Update system registry
        if system_id in self.system_registry:
            self.system_registry[system_id]["audit_events_count"] += 1
        
        print(f"✅ Audit Event Logged: {event_type.value} for system {system_id}")
        return event_id
    
    def verify_audit_integrity(self, event_id: str) -> Dict[str, Any]:
        """Verify audit event integrity and authenticity"""
        event = next((e for e in self.audit_events if e.event_id == event_id), None)
        
        if not event:
            return {"verified": False, "error": "Event not found"}
        
        # Recreate data hash
        data_string = f"{event.event_id}{event.timestamp}{event.event_type.value}{event.system_id}{event.action_description}"
        expected_hash = hashlib.sha256(data_string.encode()).hexdigest()
        
        # Verify hash integrity
        hash_verified = event.data_hash == expected_hash
        
        # Verify signature
        verification_data = f"{event.data_hash}{self.encryption_key}"
        expected_signature = hashlib.sha256(verification_data.encode()).hexdigest()
        signature_verified = event.verification_signature == expected_signature
        
        return {
            "verified": hash_verified and signature_verified,
            "hash_verified": hash_verified,
            "signature_verified": signature_verified,
            "event_timestamp": event.timestamp,
            "verification_timestamp": datetime.now().isoformat()
        }
    
    def generate_compliance_report(self, framework: ComplianceFramework, 
                                  start_date: str = None, end_date: str = None) -> Dict[str, Any]:
        """Generate framework-specific compliance audit report"""
        
        if not start_date:
            start_date = (datetime.now() - timedelta(days=90)).isoformat()
        if not end_date:
            end_date = datetime.now().isoformat()
        
        # Filter events for framework and date range
        filtered_events = [
            e for e in self.audit_events
            if framework in e.compliance_frameworks
            and start_date <= e.timestamp <= end_date
        ]
        
        # Analyze compliance requirements
        rules = self.compliance_rules.get(framework, {})
        required_events = rules.get("required_events", [])
        
        # Check event type coverage
        logged_event_types = set(e.event_type for e in filtered_events)
        missing_events = set(required_events) - logged_event_types
        
        # Generate metrics
        total_events = len(filtered_events)
        high_risk_events = len([e for e in filtered_events if e.risk_level == "high"])
        systems_covered = len(set(e.system_id for e in filtered_events))
        
        report = {
            "framework": framework.value.upper(),
            "report_period": {"start": start_date, "end": end_date},
            "generation_timestamp": datetime.now().isoformat(),
            "compliance_summary": {
                "total_audit_events": total_events,
                "high_risk_events": high_risk_events,
                "systems_audited": systems_covered,
                "required_events_covered": len(required_events) - len(missing_events),
                "compliance_score": self._calculate_compliance_score(filtered_events, rules)
            },
            "event_breakdown": {
                event_type.value: len([e for e in filtered_events if e.event_type == event_type])
                for event_type in EventType
            },
            "missing_requirements": [event.value for event in missing_events],
            "recommendations": self._generate_compliance_recommendations(framework, filtered_events, rules),
            "executive_summary": self._generate_executive_summary(framework, filtered_events, rules)
        }
        
        return report
    
    def _calculate_compliance_score(self, events: List[AuditEvent], rules: Dict[str, Any]) -> float:
        """Calculate compliance score (0-100) based on audit completeness"""
        required_events = rules.get("required_events", [])
        if not required_events:
            return 100.0
        
        logged_types = set(e.event_type for e in events)
        coverage = len(set(required_events) & logged_types) / len(required_events)
        
        # Adjust for event frequency and recency
        frequency_score = min(len(events) / 100, 1.0)  # Normalize by expected volume
        
        return (coverage * 0.7 + frequency_score * 0.3) * 100
    
    def _generate_compliance_recommendations(self, framework: ComplianceFramework, 
                                           events: List[AuditEvent], rules: Dict[str, Any]) -> List[str]:
        """Generate actionable compliance recommendations"""
        recommendations = []
        
        required_events = rules.get("required_events", [])
        logged_types = set(e.event_type for e in events)
        missing_events = set(required_events) - logged_types
        
        if missing_events:
            recommendations.append(f"Implement logging for missing event types: {[e.value for e in missing_events]}")
        
        high_risk_events = [e for e in events if e.risk_level == "high"]
        if len(high_risk_events) > len(events) * 0.1:  # More than 10% high risk
            recommendations.append("High proportion of high-risk events requires enhanced monitoring")
        
        if framework == ComplianceFramework.GDPR and rules.get("anonymization_required"):
            recommendations.append("Ensure personal data anonymization in audit logs")
        
        if framework == ComplianceFramework.EU_AI_ACT and rules.get("risk_assessment_required"):
            recommendations.append("Conduct regular AI risk assessments and document findings")
        
        return recommendations
    
    def _generate_executive_summary(self, framework: ComplianceFramework, 
                                  events: List[AuditEvent], rules: Dict[str, Any]) -> str:
        """Generate executive-level summary"""
        compliance_score = self._calculate_compliance_score(events, rules)
        
        if compliance_score >= 90:
            status = "Excellent compliance posture"
        elif compliance_score >= 75:
            status = "Strong compliance with minor gaps"
        elif compliance_score >= 60:
            status = "Moderate compliance requiring attention"
        else:
            status = "Significant compliance gaps requiring immediate action"
        
        return f"{framework.value.upper()} Compliance: {compliance_score:.1f}% - {status}. " \
               f"{len(events)} audit events tracked across {len(set(e.system_id for e in events))} AI systems."
    
    def export_audit_trail(self, format_type: str = "json", include_metadata: bool = True) -> str:
        """Export complete audit trail for regulatory submissions"""
        
        export_data = {
            "export_metadata": {
                "generation_timestamp": datetime.now().isoformat(),
                "total_events": len(self.audit_events),
                "systems_registered": len(self.system_registry),
                "export_format": format_type,
                "verification_key_hash": hashlib.sha256(self.encryption_key.encode()).hexdigest()[:16]
            },
            "system_registry": self.system_registry,
            "audit_events": []
        }
        
        # Convert events to exportable format
        for event in self.audit_events:
            event_dict = asdict(event)
            event_dict["event_type"] = event.event_type.value
            event_dict["compliance_frameworks"] = [f.value for f in event.compliance_frameworks]
            
            if not include_metadata:
                event_dict.pop("metadata", None)
            
            export_data["audit_events"].append(event_dict)
        
        return json.dumps(export_data, indent=2, sort_keys=True)
    
    def get_audit_statistics(self) -> Dict[str, Any]:
        """Generate comprehensive audit trail statistics"""
        if not self.audit_events:
            return {"message": "No audit events recorded"}
        
        # Event type distribution
        event_distribution = {}
        for event_type in EventType:
            count = len([e for e in self.audit_events if e.event_type == event_type])
            event_distribution[event_type.value] = count
        
        # Risk level distribution
        risk_distribution = {}
        for risk in ["low", "medium", "high", "critical"]:
            count = len([e for e in self.audit_events if e.risk_level == risk])
            risk_distribution[risk] = count
        
        # Compliance framework coverage
        framework_coverage = {}
        for framework in ComplianceFramework:
            count = len([e for e in self.audit_events if framework in e.compliance_frameworks])
            framework_coverage[framework.value] = count
        
        return {
            "total_events": len(self.audit_events),
            "date_range": {
                "earliest": min(e.timestamp for e in self.audit_events),
                "latest": max(e.timestamp for e in self.audit_events)
            },
            "event_type_distribution": event_distribution,
            "risk_level_distribution": risk_distribution,
            "compliance_framework_coverage": framework_coverage,
            "systems_tracked": len(self.system_registry),
            "integrity_verified": all(
                self.verify_audit_integrity(e.event_id)["verified"] 
                for e in self.audit_events[-10:]  # Sample verification
            )
        }


def demonstrate_audit_capabilities():
    """Portfolio demonstration of audit trail capabilities"""
    print("\n" + "="*60)
    print("🎯 AI AUDIT TRAIL BUILDER - PORTFOLIO DEMONSTRATION")
    print("📊 Showcasing Enterprise AI Governance Capabilities")
    print("👨‍💼 Created by Sotirios Spyrou - Technical Marketing Leader")
    print("="*60)
    
    # Initialize audit system
    audit_system = AIAuditTrailBuilder()
    
    # Register demo AI systems
    print("\n📋 1. REGISTERING AI SYSTEMS FOR AUDIT TRACKING")
    
    audit_system.register_ai_system(
        system_id="fraud_detection_v2",
        system_name="Advanced Fraud Detection AI",
        risk_level="high",
        compliance_frameworks=[ComplianceFramework.GDPR, ComplianceFramework.EU_AI_ACT]
    )
    
    audit_system.register_ai_system(
        system_id="recommendation_engine",
        system_name="Product Recommendation System",
        risk_level="medium",
        compliance_frameworks=[ComplianceFramework.GDPR]
    )
    
    # Simulate AI system activities
    print("\n⚡ 2. LOGGING AI SYSTEM ACTIVITIES")
    
    # Fraud detection training event
    audit_system.log_event(
        event_type=EventType.MODEL_TRAINING,
        system_id="fraud_detection_v2",
        user_id="data_scientist_001",
        action_description="Model retrained with 50K new fraud cases",
        compliance_frameworks=[ComplianceFramework.EU_AI_ACT],
        risk_level="high",
        business_impact="critical",
        metadata={"training_samples": 50000, "accuracy_improvement": 0.03}
    )
    
    # Bias detection check
    audit_system.log_event(
        event_type=EventType.BIAS_DETECTION,
        system_id="fraud_detection_v2",
        user_id="ai_ethics_officer",
        action_description="Automated bias detection scan completed - no significant bias detected",
        compliance_frameworks=[ComplianceFramework.EU_AI_ACT, ComplianceFramework.GDPR],
        risk_level="medium",
        business_impact="high",
        metadata={"bias_score": 0.02, "protected_attributes": ["age", "gender", "location"]}
    )
    
    # Data processing event
    audit_system.log_event(
        event_type=EventType.DATA_PROCESSING,
        system_id="recommendation_engine",
        user_id="system_automated",
        action_description="Daily user preference data processing completed",
        compliance_frameworks=[ComplianceFramework.GDPR],
        risk_level="low",
        business_impact="medium",
        metadata={"records_processed": 125000, "anonymized": True}
    )
    
    # Generate compliance reports
    print("\n📊 3. GENERATING COMPLIANCE REPORTS")
    
    gdpr_report = audit_system.generate_compliance_report(ComplianceFramework.GDPR)
    eu_ai_act_report = audit_system.generate_compliance_report(ComplianceFramework.EU_AI_ACT)
    
    print(f"📈 GDPR Compliance Score: {gdpr_report['compliance_summary']['compliance_score']:.1f}%")
    print(f"📈 EU AI Act Compliance Score: {eu_ai_act_report['compliance_summary']['compliance_score']:.1f}%")
    
    print(f"\n💡 GDPR Executive Summary:")
    print(f"   {gdpr_report['executive_summary']}")
    
    # Display audit statistics
    print("\n📊 4. AUDIT TRAIL STATISTICS")
    stats = audit_system.get_audit_statistics()
    print(f"   Total Events Logged: {stats['total_events']}")
    print(f"   Systems Under Audit: {stats['systems_tracked']}")
    print(f"   Integrity Verified: {'✅ PASSED' if stats['integrity_verified'] else '❌ FAILED'}")
    
    # Demonstrate event verification
    print("\n🔐 5. AUDIT INTEGRITY VERIFICATION")
    if audit_system.audit_events:
        sample_event = audit_system.audit_events[0]
        verification = audit_system.verify_audit_integrity(sample_event.event_id)
        print(f"   Event Verification: {'✅ VERIFIED' if verification['verified'] else '❌ COMPROMISED'}")
    
    print("\n" + "="*60)
    print("🏆 DEMONSTRATION COMPLETE")
    print("💼 This showcases enterprise-ready AI audit capabilities")
    print("🎯 Perfect for Chief Risk Officers and Compliance Teams")
    print("📞 Contact Sotirios Spyrou for implementation consulting")
    print("🔗 LinkedIn: https://www.linkedin.com/in/sspyrou/")
    print("🌐 Enterprise Solutions: https://verityai.co")
    print("="*60)


if __name__ == "__main__":
    demonstrate_audit_capabilities()