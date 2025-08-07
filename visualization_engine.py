#!/usr/bin/env python3
"""
VerityAI Showcase - Visualization Engine
Interactive demonstrations and reporting visualization
"""

import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


class VisualizationEngine:
    """Generate interactive visualizations for VerityAI demonstrations"""
    
    def __init__(self, style: str = 'professional'):
        self.style = style
        self._setup_styling()
        
    def _setup_styling(self):
        """Configure visualization styling"""
        if self.style == 'professional':
            # VerityAI brand colors
            self.color_palette = ['#1f4e79', '#2e7d32', '#f57c00', '#d32f2f', '#7b1fa2']
            plt.style.use('seaborn-v0_8-whitegrid')
            sns.set_palette(self.color_palette)
        
        # Set default figure parameters
        plt.rcParams.update({
            'figure.figsize': (12, 8),
            'font.size': 11,
            'axes.titlesize': 14,
            'axes.labelsize': 12,
            'xtick.labelsize': 10,
            'ytick.labelsize': 10,
            'legend.fontsize': 10
        })
    
    def create_risk_assessment_dashboard(self, portfolio_data: List[Dict]) -> Dict[str, Any]:
        """Create comprehensive risk assessment dashboard"""
        df = pd.DataFrame(portfolio_data)
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=[
                'Risk Level Distribution',
                'Compliance Status Overview',
                'Industry Risk Breakdown',
                'Business Impact Analysis'
            ],
            specs=[[{'type': 'pie'}, {'type': 'bar'}],
                   [{'type': 'bar'}, {'type': 'scatter'}]]
        )
        
        # Risk level distribution (pie chart)
        risk_counts = df['risk_level'].value_counts()
        fig.add_trace(
            go.Pie(
                labels=risk_counts.index,
                values=risk_counts.values,
                name="Risk Distribution"
            ),
            row=1, col=1
        )
        
        # Compliance status overview (bar chart)
        compliance_counts = df['compliance_status'].value_counts()
        fig.add_trace(
            go.Bar(
                x=compliance_counts.index,
                y=compliance_counts.values,
                name="Compliance Status"
            ),
            row=1, col=2
        )
        
        # Industry risk breakdown
        industry_risk = pd.crosstab(df['industry'], df['risk_level'])
        for risk_level in industry_risk.columns:
            fig.add_trace(
                go.Bar(
                    x=industry_risk.index,
                    y=industry_risk[risk_level],
                    name=risk_level
                ),
                row=2, col=1
            )
        
        # Business impact scatter
        impact_mapping = {'low': 1, 'medium': 2, 'high': 3, 'critical': 4}
        risk_mapping = {'minimal': 1, 'limited': 2, 'high': 3, 'unacceptable': 4}
        
        fig.add_trace(
            go.Scatter(
                x=[risk_mapping.get(r, 0) for r in df['risk_level']],
                y=[impact_mapping.get(i, 0) for i in df['business_impact']],
                mode='markers',
                text=df['name'],
                name="Systems"
            ),
            row=2, col=2
        )
        
        fig.update_layout(
            title_text="VerityAI Risk Assessment Dashboard",
            height=800,
            showlegend=True
        )
        
        return {
            'dashboard': fig,
            'insights': self._generate_risk_insights(df),
            'recommendations': self._generate_risk_recommendations(df)
        }
    
    def create_bias_analysis_report(self, bias_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create comprehensive bias analysis visualization"""
        demographics = bias_data['demographics']
        outcomes = bias_data['outcomes']
        
        # Create bias analysis plots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('VerityAI Bias Detection Analysis', fontsize=16, fontweight='bold')
        
        # Plot 1: Outcome distribution by protected attribute
        for i, (attr, values) in enumerate(demographics.items()):
            if i >= 2:  # Limit to first 2 attributes for space
                break
                
            df_temp = pd.DataFrame({
                attr: values,
                'outcome': outcomes
            })
            
            outcome_rates = df_temp.groupby(attr)['outcome'].mean()
            
            ax = axes[0, i] if i < 2 else axes[1, i-2]
            outcome_rates.plot(kind='bar', ax=ax, color=self.color_palette[i])
            ax.set_title(f'Outcome Rate by {attr.title()}')
            ax.set_ylabel('Positive Outcome Rate')
            ax.tick_params(axis='x', rotation=45)
        
        # Plot 3: Overall bias metrics
        bias_metrics = self._calculate_bias_metrics(demographics, outcomes)
        
        ax = axes[1, 0]
        metrics_df = pd.DataFrame(list(bias_metrics.items()), columns=['Metric', 'Value'])
        bars = ax.bar(metrics_df['Metric'], metrics_df['Value'], color=self.color_palette[:len(metrics_df)])
        ax.set_title('Bias Fairness Metrics')
        ax.set_ylabel('Metric Value')
        ax.tick_params(axis='x', rotation=45)
        
        # Add threshold line for reference
        ax.axhline(y=0.8, color='red', linestyle='--', label='Fairness Threshold')
        ax.legend()
        
        # Plot 4: Bias heat map
        ax = axes[1, 1]
        heatmap_data = self._create_bias_heatmap_data(demographics, outcomes)
        im = ax.imshow(heatmap_data, cmap='RdYlBu_r', aspect='auto')
        ax.set_title('Bias Impact Heatmap')
        
        plt.tight_layout()
        
        return {
            'visualization': fig,
            'bias_metrics': bias_metrics,
            'severity_assessment': self._assess_bias_severity(bias_metrics),
            'mitigation_recommendations': self._generate_bias_mitigations(bias_metrics)
        }
    
    def create_compliance_timeline(self, compliance_data: Dict[str, Any]) -> go.Figure:
        """Create compliance timeline visualization"""
        # Generate sample timeline data
        timeline_data = self._generate_compliance_timeline_data(compliance_data)
        
        fig = go.Figure()
        
        for framework in timeline_data:
            fig.add_trace(go.Scatter(
                x=framework['dates'],
                y=framework['progress'],
                mode='lines+markers',
                name=framework['name'],
                line=dict(width=3),
                marker=dict(size=8)
            ))
        
        fig.update_layout(
            title='VerityAI Compliance Implementation Timeline',
            xaxis_title='Timeline',
            yaxis_title='Compliance Progress (%)',
            yaxis=dict(range=[0, 100]),
            height=600,
            showlegend=True
        )
        
        # Add milestone markers
        fig.add_hline(y=100, line_dash="dash", line_color="green", 
                     annotation_text="Full Compliance")
        fig.add_hline(y=80, line_dash="dash", line_color="orange", 
                     annotation_text="Substantial Compliance")
        
        return fig
    
    def create_executive_summary(self, portfolio_data: List[Dict], 
                                bias_data: Dict[str, Any] = None) -> Dict[str, Any]:
        """Create executive summary visualization"""
        df = pd.DataFrame(portfolio_data)
        
        # Key metrics calculation
        total_systems = len(df)
        high_risk_systems = len(df[df['risk_level'].isin(['high', 'unacceptable'])])
        compliant_systems = len(df[df['compliance_status'] == 'compliant'])
        compliance_rate = (compliant_systems / total_systems) * 100
        
        # Create executive dashboard
        fig = make_subplots(
            rows=2, cols=3,
            subplot_titles=[
                'Risk Overview', 'Compliance Status', 'Industry Distribution',
                'Timeline Progress', 'Key Metrics', 'Action Items'
            ],
            specs=[[{'type': 'indicator'}, {'type': 'pie'}, {'type': 'bar'}],
                   [{'type': 'scatter'}, {'type': 'table'}, {'type': 'bar'}]]
        )
        
        # Risk indicator
        risk_score = (high_risk_systems / total_systems) * 100
        fig.add_trace(
            go.Indicator(
                mode="gauge+number+delta",
                value=100-risk_score,
                title={'text': "Risk Management Score"},
                domain={'x': [0, 1], 'y': [0, 1]},
                gauge={'axis': {'range': [None, 100]},
                       'bar': {'color': "darkblue"},
                       'steps': [{'range': [0, 50], 'color': "lightgray"},
                                {'range': [50, 80], 'color': "gray"}],
                       'threshold': {'line': {'color': "red", 'width': 4},
                                   'thickness': 0.75, 'value': 90}}
            ),
            row=1, col=1
        )
        
        fig.update_layout(
            title_text="VerityAI Executive Dashboard",
            height=800
        )
        
        # Generate insights
        insights = {
            'total_ai_systems': total_systems,
            'high_risk_systems': high_risk_systems,
            'compliance_rate': f"{compliance_rate:.1f}%",
            'risk_score': f"{100-risk_score:.1f}",
            'key_findings': [
                f"{total_systems} AI systems under governance",
                f"{high_risk_systems} systems require enhanced oversight",
                f"{compliance_rate:.1f}% compliance achievement rate",
                f"Risk management score: {100-risk_score:.1f}/100"
            ]
        }
        
        return {
            'dashboard': fig,
            'executive_insights': insights,
            'action_items': self._generate_executive_actions(df)
        }
    
    def _calculate_bias_metrics(self, demographics: Dict, outcomes: List) -> Dict[str, float]:
        """Calculate bias fairness metrics"""
        metrics = {}
        
        for attr, values in demographics.items():
            df_temp = pd.DataFrame({attr: values, 'outcome': outcomes})
            outcome_rates = df_temp.groupby(attr)['outcome'].mean()
            
            if len(outcome_rates) >= 2:
                # Demographic parity (ratio of rates)
                min_rate = outcome_rates.min()
                max_rate = outcome_rates.max()
                parity_ratio = min_rate / max_rate if max_rate > 0 else 0
                metrics[f'{attr}_parity'] = parity_ratio
        
        return metrics
    
    def _create_bias_heatmap_data(self, demographics: Dict, outcomes: List) -> np.ndarray:
        """Create heatmap data for bias visualization"""
        # Simplified heatmap - in practice would be more sophisticated
        return np.random.rand(len(demographics), 5) * 0.3 + 0.7
    
    def _assess_bias_severity(self, bias_metrics: Dict[str, float]) -> str:
        """Assess overall bias severity"""
        if not bias_metrics:
            return "No bias detected"
        
        min_parity = min(bias_metrics.values())
        
        if min_parity >= 0.8:
            return "Low bias risk"
        elif min_parity >= 0.6:
            return "Medium bias risk"
        else:
            return "High bias risk"
    
    def _generate_bias_mitigations(self, bias_metrics: Dict[str, float]) -> List[str]:
        """Generate bias mitigation recommendations"""
        mitigations = []
        
        for metric, value in bias_metrics.items():
            if value < 0.8:
                attribute = metric.replace('_parity', '')
                mitigations.append(f"Address {attribute} disparities through data augmentation")
                mitigations.append(f"Implement fairness constraints for {attribute}")
        
        if not mitigations:
            mitigations.append("Continue monitoring for bias indicators")
        
        return mitigations
    
    def _generate_compliance_timeline_data(self, compliance_data: Dict) -> List[Dict]:
        """Generate sample compliance timeline data"""
        frameworks = ['EU AI Act', 'ISO 42001', 'NIST AI RMF']
        timeline_data = []
        
        base_date = datetime.now() - timedelta(days=365)
        
        for i, framework in enumerate(frameworks):
            dates = [base_date + timedelta(days=30*j) for j in range(13)]
            progress = [min(100, 5 + j*8 + i*10 + np.random.normal(0, 3)) for j in range(13)]
            
            timeline_data.append({
                'name': framework,
                'dates': dates,
                'progress': progress
            })
        
        return timeline_data
    
    def _generate_risk_insights(self, df: pd.DataFrame) -> List[str]:
        """Generate risk assessment insights"""
        insights = []
        
        high_risk_pct = (len(df[df['risk_level'] == 'high']) / len(df)) * 100
        compliant_pct = (len(df[df['compliance_status'] == 'compliant']) / len(df)) * 100
        
        insights.append(f"{high_risk_pct:.1f}% of systems classified as high-risk")
        insights.append(f"{compliant_pct:.1f}% compliance rate across portfolio")
        
        # Industry analysis
        industry_risks = df.groupby('industry')['risk_level'].apply(lambda x: (x == 'high').sum())
        highest_risk_industry = industry_risks.idxmax()
        insights.append(f"{highest_risk_industry} shows highest risk concentration")
        
        return insights
    
    def _generate_risk_recommendations(self, df: pd.DataFrame) -> List[str]:
        """Generate risk mitigation recommendations"""
        recommendations = []
        
        high_risk_systems = df[df['risk_level'] == 'high']
        if len(high_risk_systems) > 0:
            recommendations.append("Prioritize compliance review for high-risk systems")
            recommendations.append("Implement enhanced monitoring for critical business impact systems")
        
        non_compliant = df[df['compliance_status'] != 'compliant']
        if len(non_compliant) > 0:
            recommendations.append("Develop compliance roadmap for non-compliant systems")
        
        return recommendations
    
    def _generate_executive_actions(self, df: pd.DataFrame) -> List[str]:
        """Generate executive action items"""
        actions = []
        
        high_risk_count = len(df[df['risk_level'] == 'high'])
        if high_risk_count > 0:
            actions.append(f"Review {high_risk_count} high-risk AI systems")
        
        non_compliant = len(df[df['compliance_status'] != 'compliant'])
        if non_compliant > 0:
            actions.append(f"Address compliance gaps in {non_compliant} systems")
        
        actions.append("Schedule quarterly AI governance review")
        actions.append("Update board on AI risk management progress")
        
        return actions


def main():
    """Demonstration of visualization capabilities"""
    viz_engine = VisualizationEngine()
    
    print("🛡️ VerityAI Showcase - Visualization Engine")
    print("=" * 50)
    
    # Sample data for demonstration
    sample_portfolio = [
        {'name': 'Credit Risk AI', 'risk_level': 'high', 'compliance_status': 'in_progress', 
         'industry': 'financial', 'business_impact': 'high'},
        {'name': 'Chatbot Assistant', 'risk_level': 'limited', 'compliance_status': 'compliant',
         'industry': 'technology', 'business_impact': 'medium'},
        {'name': 'Fraud Detection', 'risk_level': 'high', 'compliance_status': 'compliant',
         'industry': 'financial', 'business_impact': 'critical'},
    ]
    
    # Create risk dashboard
    dashboard = viz_engine.create_risk_assessment_dashboard(sample_portfolio)
    print(f"Generated risk dashboard with {len(dashboard['insights'])} insights")
    
    # Create executive summary
    exec_summary = viz_engine.create_executive_summary(sample_portfolio)
    print(f"Generated executive summary with {len(exec_summary['action_items'])} action items")
    
    print("\nVisualization engine ready for interactive demonstrations!")
    print("Next steps:")
    print("1. Use create_risk_assessment_dashboard() for portfolio analysis")
    print("2. Use create_bias_analysis_report() for fairness assessment")
    print("3. Use create_executive_summary() for stakeholder reporting")


if __name__ == "__main__":
    main()