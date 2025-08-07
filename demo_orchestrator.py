#!/usr/bin/env python3
"""
VerityAI Showcase - Demo Orchestrator
Central demonstration management and execution system
"""

import json
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum


class DemoCategory(Enum):
    RISK_ASSESSMENT = "risk_assessment"
    COMPLIANCE_AUTOMATION = "compliance_automation"
    GOVERNANCE_TEMPLATES = "governance_templates"
    PROFESSIONAL_SERVICES = "professional_services"


@dataclass
class DemoResult:
    demo_id: str
    category: DemoCategory
    success: bool
    output: Dict[str, Any]
    execution_time: float
    error_message: Optional[str] = None


class DemoOrchestrator:
    """Central orchestrator for VerityAI showcase demonstrations"""
    
    def __init__(self):
        self.demos = {}
        self.results = []
        self.logger = self._setup_logging()
    
    def _setup_logging(self) -> logging.Logger:
        """Configure logging for demonstration tracking"""
        logger = logging.getLogger('verity_demo')
        logger.setLevel(logging.INFO)
        
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def register_demo(self, demo_id: str, category: DemoCategory, 
                     demo_class: type, description: str = ""):
        """Register a demonstration for orchestrated execution"""
        self.demos[demo_id] = {
            'category': category,
            'class': demo_class,
            'description': description,
            'registered_at': self._get_timestamp()
        }
        self.logger.info(f"Registered demo: {demo_id} ({category.value})")
    
    def run_demo(self, demo_id: str, **kwargs) -> DemoResult:
        """Execute a specific demonstration"""
        if demo_id not in self.demos:
            raise ValueError(f"Demo '{demo_id}' not registered")
        
        demo_info = self.demos[demo_id]
        self.logger.info(f"Executing demo: {demo_id}")
        
        try:
            import time
            start_time = time.time()
            
            demo_instance = demo_info['class']()
            result = demo_instance.run(**kwargs)
            
            execution_time = time.time() - start_time
            
            demo_result = DemoResult(
                demo_id=demo_id,
                category=demo_info['category'],
                success=True,
                output=result,
                execution_time=execution_time
            )
            
            self.results.append(demo_result)
            self.logger.info(f"Demo '{demo_id}' completed successfully")
            
            return demo_result
            
        except Exception as e:
            execution_time = time.time() - start_time
            
            demo_result = DemoResult(
                demo_id=demo_id,
                category=demo_info['category'],
                success=False,
                output={},
                execution_time=execution_time,
                error_message=str(e)
            )
            
            self.results.append(demo_result)
            self.logger.error(f"Demo '{demo_id}' failed: {str(e)}")
            
            return demo_result
    
    def run_category(self, category: DemoCategory, **kwargs) -> List[DemoResult]:
        """Execute all demonstrations in a category"""
        category_demos = [
            demo_id for demo_id, info in self.demos.items()
            if info['category'] == category
        ]
        
        results = []
        for demo_id in category_demos:
            result = self.run_demo(demo_id, **kwargs)
            results.append(result)
        
        return results
    
    def run_all_demos(self, **kwargs) -> List[DemoResult]:
        """Execute all registered demonstrations"""
        results = []
        for demo_id in self.demos.keys():
            result = self.run_demo(demo_id, **kwargs)
            results.append(result)
        
        return results
    
    def get_demo_summary(self) -> Dict[str, Any]:
        """Generate summary of available demonstrations"""
        summary = {
            'total_demos': len(self.demos),
            'categories': {},
            'recent_results': len(self.results)
        }
        
        for category in DemoCategory:
            category_demos = [
                demo_id for demo_id, info in self.demos.items()
                if info['category'] == category
            ]
            summary['categories'][category.value] = {
                'count': len(category_demos),
                'demos': category_demos
            }
        
        return summary
    
    def generate_executive_report(self, results: List[DemoResult]) -> Dict[str, Any]:
        """Generate executive summary of demonstration results"""
        if not results:
            return {'message': 'No demonstration results available'}
        
        total_demos = len(results)
        successful_demos = sum(1 for r in results if r.success)
        
        report = {
            'executive_summary': {
                'total_demonstrations': total_demos,
                'success_rate': f"{(successful_demos/total_demos)*100:.1f}%",
                'average_execution_time': f"{sum(r.execution_time for r in results)/total_demos:.2f}s"
            },
            'category_breakdown': {},
            'key_insights': [],
            'recommended_actions': []
        }
        
        # Category analysis
        for category in DemoCategory:
            category_results = [r for r in results if r.category == category]
            if category_results:
                success_count = sum(1 for r in category_results if r.success)
                report['category_breakdown'][category.value] = {
                    'total': len(category_results),
                    'successful': success_count,
                    'success_rate': f"{(success_count/len(category_results))*100:.1f}%"
                }
        
        # Generate insights
        if successful_demos == total_demos:
            report['key_insights'].append("All demonstrations executed successfully")
        elif successful_demos > total_demos * 0.8:
            report['key_insights'].append("Strong demonstration performance with minor issues")
        else:
            report['key_insights'].append("Multiple demonstration failures require attention")
        
        return report
    
    def _get_timestamp(self) -> str:
        """Get current timestamp for tracking"""
        from datetime import datetime
        return datetime.now().isoformat()


def main():
    """Demonstration of orchestrator capabilities"""
    orchestrator = DemoOrchestrator()
    
    print("🛡️ VerityAI Showcase - Demo Orchestrator")
    print("=" * 50)
    
    # Display summary
    summary = orchestrator.get_demo_summary()
    print(f"Total Registered Demos: {summary['total_demos']}")
    
    for category, info in summary['categories'].items():
        print(f"  {category.title()}: {info['count']} demos")
    
    print("\nDemo orchestrator ready for showcase execution!")
    print("\nNext steps:")
    print("1. Register demonstrations using orchestrator.register_demo()")
    print("2. Execute demos with orchestrator.run_demo()")
    print("3. Generate reports with orchestrator.generate_executive_report()")


if __name__ == "__main__":
    main()