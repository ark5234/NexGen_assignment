import pandas as pd
import numpy as np
from datetime import datetime
import io
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import plotly.graph_objects as go
import plotly.express as px


def generate_pdf_report(filtered_df, datasets, kpis, model_metrics=None):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=30)
    
    story = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1f77b4'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=8,
        spaceBefore=8,
        fontName='Helvetica-Bold'
    )
    
    story.append(Paragraph("NexGen Logistics", title_style))
    story.append(Paragraph("Comprehensive Delivery Optimization & Risk Analysis Report", styles['Heading2']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
    story.append(Paragraph(f"Report Period: {filtered_df['order_date'].min().strftime('%Y-%m-%d') if not filtered_df.empty else 'N/A'} to {filtered_df['order_date'].max().strftime('%Y-%m-%d') if not filtered_df.empty else 'N/A'}", styles['Normal']))
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("Executive Summary", heading_style))
    
    kpi_data = [
        ['Metric', 'Value', 'Target', 'Status'],
        ['Total Orders', str(kpis.get('total_orders', 0)), 'N/A', 'ℹ'],
        ['On-Time Rate', f"{kpis.get('on_time_rate', 0):.1f}%", '85%', '✓' if kpis.get('on_time_rate', 0) >= 85 else '✗'],
        ['Avg Delivery Cost', f"₹{kpis.get('avg_cost', 0):.2f}", '₹300', '✓' if kpis.get('avg_cost', 0) <= 300 else '✗'],
        ['Total CO2 (kg)', f"{kpis.get('co2_kg', 0):.1f}", 'Reduce 30%', 'ℹ'],
        ['Delayed Orders', str(kpis.get('delayed_orders', 0)), '<15%', '✓' if (kpis.get('delayed_orders', 0) / max(kpis.get('total_orders', 1), 1)) < 0.15 else '✗'],
        ['Revenue at Risk', f"₹{filtered_df[filtered_df['delayed_flag']==1]['order_value'].sum():.2f}" if not filtered_df.empty else '₹0', 'Minimize', 'ℹ'],
    ]
    
    t = Table(kpi_data, colWidths=[2*inch, 1.8*inch, 1.5*inch, 1*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    story.append(t)
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("Carrier Performance Analysis", heading_style))
    
    if not filtered_df.empty and 'carrier' in filtered_df.columns:
        carrier_stats = filtered_df.groupby('carrier').agg({
            'order_id': 'count',
            'delayed_flag': 'mean',
            'delivery_cost': 'mean',
            'customer_rating': 'mean',
            'order_value': 'sum'
        }).reset_index()
        carrier_stats.columns = ['Carrier', 'Orders', 'Delay Rate', 'Avg Cost', 'Avg Rating', 'Total Revenue']
        carrier_stats = carrier_stats.sort_values('Delay Rate')
        
        carrier_data = [['Carrier', 'Orders', 'Delay %', 'Avg Cost', 'Rating', 'Revenue']]
        for _, row in carrier_stats.iterrows():
            carrier_data.append([
                str(row['Carrier']),
                str(int(row['Orders'])),
                f"{row['Delay Rate']*100:.1f}%",
                f"₹{row['Avg Cost']:.0f}",
                f"{row['Avg Rating']:.2f}",
                f"₹{row['Total Revenue']:.0f}"
            ])
        
        t_carrier = Table(carrier_data, colWidths=[1.3*inch, 0.8*inch, 0.9*inch, 1*inch, 0.8*inch, 1.2*inch])
        t_carrier.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e67e22')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        story.append(t_carrier)
        story.append(Spacer(1, 15))
    
    story.append(Paragraph("Route Efficiency & Distance Analysis", heading_style))
    
    if not filtered_df.empty and 'route' in filtered_df.columns:
        route_stats = filtered_df.groupby('route').agg({
            'order_id': 'count',
            'distance_km': 'mean',
            'delayed_flag': 'mean',
            'delivery_cost': 'sum',
            'co2_emissions_kg': 'sum'
        }).reset_index()
        route_stats.columns = ['Route', 'Orders', 'Avg Distance', 'Delay Rate', 'Total Cost', 'CO2 (kg)']
        route_stats = route_stats.sort_values('Total Cost', ascending=False).head(10)
        
        route_data = [['Route', 'Orders', 'Avg Dist (km)', 'Delay %', 'Cost', 'CO2']]
        for _, row in route_stats.iterrows():
            route_data.append([
                str(row['Route'])[:15],
                str(int(row['Orders'])),
                f"{row['Avg Distance']:.0f}",
                f"{row['Delay Rate']*100:.0f}%",
                f"₹{row['Total Cost']:.0f}",
                f"{row['CO2']:.0f}"
            ])
        
        t_route = Table(route_data, colWidths=[1.8*inch, 0.8*inch, 1.1*inch, 0.9*inch, 0.9*inch, 0.8*inch])
        t_route.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#16a085')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        story.append(t_route)
        story.append(Spacer(1, 15))
    
    story.append(Paragraph("Priority-Based Performance Breakdown", heading_style))
    
    if not filtered_df.empty:
        priority_stats = filtered_df.groupby('priority').agg({
            'order_id': 'count',
            'delayed_flag': 'mean',
            'delivery_cost': 'mean',
            'order_value': 'mean',
            'customer_rating': 'mean'
        }).reset_index()
        priority_stats.columns = ['Priority', 'Order Count', 'Delay Rate', 'Avg Cost', 'Avg Value', 'Rating']
        
        priority_data = [['Priority', 'Orders', 'Delay %', 'Avg Cost', 'Avg Order Value', 'Rating']]
        for _, row in priority_stats.iterrows():
            priority_data.append([
                str(row['Priority']),
                str(int(row['Order Count'])),
                f"{row['Delay Rate']*100:.1f}%",
                f"₹{row['Avg Cost']:.2f}",
                f"₹{row['Avg Value']:.2f}",
                f"{row['Rating']:.2f}"
            ])
        
        t2 = Table(priority_data, colWidths=[1.2*inch, 1*inch, 1*inch, 1.2*inch, 1.4*inch, 0.9*inch])
        t2.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2980b9')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        story.append(t2)
        story.append(Spacer(1, 20))
    
    story.append(PageBreak())
    
    story.append(Paragraph("High-Risk Order Analysis", heading_style))
    
    if not filtered_df.empty:
        high_risk = filtered_df[filtered_df['delayed_flag'] == 1].nlargest(15, 'order_value')[
            ['order_id', 'customer_id', 'priority', 'order_value', 'carrier', 'distance_km', 'delivery_cost']
        ]
        
        if len(high_risk) > 0:
            story.append(Paragraph(f"Identified {len(high_risk)} critical high-value delayed orders requiring immediate attention:", subheading_style))
            story.append(Spacer(1, 8))
            
            risk_data = [['Order ID', 'Customer', 'Priority', 'Value', 'Carrier', 'Distance', 'Cost']]
            for _, row in high_risk.iterrows():
                risk_data.append([
                    str(row['order_id'])[:8],
                    str(row['customer_id'])[:8],
                    str(row['priority']),
                    f"₹{row['order_value']:.0f}",
                    str(row['carrier'])[:10],
                    f"{row['distance_km']:.0f}km",
                    f"₹{row['delivery_cost']:.0f}"
                ])
            
            t_risk = Table(risk_data, colWidths=[1*inch, 0.9*inch, 0.8*inch, 0.9*inch, 1*inch, 0.8*inch, 0.8*inch])
            t_risk.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#c0392b')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 7),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                ('BACKGROUND', (0, 1), (-1, -1), colors.Color(1, 0.9, 0.9)),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            story.append(t_risk)
            story.append(Spacer(1, 15))
    
    story.append(Paragraph("Environmental Impact Assessment", heading_style))
    
    if not filtered_df.empty and 'product_category' in filtered_df.columns:
        env_stats = filtered_df.groupby('product_category').agg({
            'co2_emissions_kg': 'sum',
            'order_id': 'count',
            'delivery_cost': 'sum'
        }).reset_index()
        env_stats.columns = ['Category', 'Total CO2 (kg)', 'Orders', 'Total Cost']
        env_stats['CO2 per Order'] = env_stats['Total CO2 (kg)'] / env_stats['Orders']
        env_stats = env_stats.sort_values('Total CO2 (kg)', ascending=False)
        
        env_data = [['Category', 'Total CO2', 'Orders', 'CO2/Order', 'Total Cost']]
        for _, row in env_stats.iterrows():
            env_data.append([
                str(row['Category']),
                f"{row['Total CO2 (kg)']:.1f}kg",
                str(int(row['Orders'])),
                f"{row['CO2 per Order']:.2f}kg",
                f"₹{row['Total Cost']:.0f}"
            ])
        
        t_env = Table(env_data, colWidths=[1.5*inch, 1.2*inch, 1*inch, 1.1*inch, 1.3*inch])
        t_env.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#27ae60')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        story.append(t_env)
        story.append(Spacer(1, 15))
    
    story.append(Paragraph("Cost Breakdown Analysis", heading_style))
    
    if not filtered_df.empty:
        cost_components = {
            'Base Delivery': filtered_df['base_rate'].sum() if 'base_rate' in filtered_df.columns else 0,
            'Fuel Surcharge': filtered_df['fuel_surcharge'].sum() if 'fuel_surcharge' in filtered_df.columns else 0,
            'Toll Charges': filtered_df['toll_charges'].sum() if 'toll_charges' in filtered_df.columns else 0,
            'Labor Cost': filtered_df['labor_cost'].sum() if 'labor_cost' in filtered_df.columns else 0,
            'Vehicle Maintenance': filtered_df['vehicle_maintenance'].sum() if 'vehicle_maintenance' in filtered_df.columns else 0,
            'Insurance': filtered_df['insurance_cost'].sum() if 'insurance_cost' in filtered_df.columns else 0,
        }
        
        total_cost = sum(cost_components.values())
        cost_data = [['Cost Component', 'Total Amount', 'Percentage']]
        for component, amount in sorted(cost_components.items(), key=lambda x: x[1], reverse=True):
            if amount > 0:
                cost_data.append([
                    component,
                    f"₹{amount:.2f}",
                    f"{(amount/total_cost)*100:.1f}%" if total_cost > 0 else "0%"
                ])
        
        t_cost = Table(cost_data, colWidths=[2.5*inch, 2*inch, 1.8*inch])
        t_cost.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8e44ad')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lavender),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        story.append(t_cost)
        story.append(Spacer(1, 20))
    
    story.append(Paragraph("Key Insights & Risk Factors", heading_style))
    
    insights = []
    if kpis.get('on_time_rate', 100) < 80:
        insights.append(f"🔴 CRITICAL: On-time delivery rate is {kpis.get('on_time_rate', 0):.1f}%, significantly below target of 85%")
    elif kpis.get('on_time_rate', 100) < 85:
        insights.append(f"🟡 WARNING: On-time delivery rate is {kpis.get('on_time_rate', 0):.1f}%, marginally below target of 85%")
    else:
        insights.append(f"🟢 POSITIVE: On-time delivery rate is {kpis.get('on_time_rate', 0):.1f}%, meeting or exceeding target")
    
    if kpis.get('avg_cost', 0) > 300:
        insights.append(f"💰 Cost optimization opportunity: Average delivery cost is ₹{kpis.get('avg_cost', 0):.2f}, above target of ₹300")
    
    if not filtered_df.empty:
        high_value_delays = filtered_df[(filtered_df['delayed_flag']==1) & (filtered_df['order_value']>5000)]
        if len(high_value_delays) > 0:
            insights.append(f"⚠️ Risk Alert: {len(high_value_delays)} high-value orders (>₹5000) are delayed, representing ₹{high_value_delays['order_value'].sum():.2f} in revenue at risk")
    
    insights.append(f"🌍 Environmental impact: {kpis.get('co2_kg', 0):.1f} kg CO2 emissions tracked across all deliveries")
    
    if model_metrics and 'auc' in model_metrics:
        reliability = 'Excellent' if model_metrics['auc'] > 0.85 else 'High' if model_metrics['auc'] > 0.8 else 'Moderate'
        insights.append(f"🤖 Predictive model AUC: {model_metrics['auc']:.3f} - Model reliability is {reliability}")
    
    if not filtered_df.empty and 'distance_km' in filtered_df.columns:
        long_distance = filtered_df[filtered_df['distance_km'] > 500]
        if len(long_distance) > 0:
            insights.append(f"📍 Long-haul logistics: {len(long_distance)} orders exceed 500km, requiring special attention for route optimization")
    
    for insight in insights:
        story.append(Paragraph(insight, styles['Normal']))
        story.append(Spacer(1, 6))
    
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("Strategic Recommendations", heading_style))
    
    recommendations = [
        {"priority": "HIGH", "action": "Implement dynamic route optimization algorithms", "impact": "Reduce delivery delays by 15-20% and lower fuel costs by 12%"},
        {"priority": "HIGH", "action": "Establish carrier performance scorecards with penalties", "impact": "Improve on-time delivery rate to 90%+ within 3 months"},
        {"priority": "MEDIUM", "action": "Deploy predictive delay alerts 48-72 hours in advance", "impact": "Enable proactive customer communication, reduce complaints by 25%"},
        {"priority": "MEDIUM", "action": "Invest in electric vehicle fleet for urban routes", "impact": "Reduce CO2 emissions by 30% and operating costs by 18%"},
        {"priority": "MEDIUM", "action": "Consolidate shipments for common routes", "impact": "Decrease per-order delivery costs by ₹45-60"},
        {"priority": "LOW", "action": "Implement IoT sensors for real-time tracking", "impact": "Improve visibility and reduce lost/damaged shipments by 40%"},
    ]
    
    for i, rec in enumerate(recommendations, 1):
        story.append(Paragraph(f"{i}. [{rec['priority']}] {rec['action']}", subheading_style))
        story.append(Paragraph(f"   Expected Impact: {rec['impact']}", styles['Normal']))
        story.append(Spacer(1, 6))
    
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("Immediate Action Items", heading_style))
    action_items = [
        "✓ Review and re-route all high-risk orders identified in this report within 24 hours",
        "✓ Schedule carrier performance meetings with underperforming providers within 1 week",
        "✓ Implement stricter SLA monitoring for Express and Priority orders",
        "✓ Launch pilot program for route optimization software on top 5 routes by volume",
        "✓ Establish weekly executive dashboard reviews to track KPI improvements",
        "✓ Conduct cost-benefit analysis for EV fleet transition within 30 days"
    ]
    
    for item in action_items:
        story.append(Paragraph(item, styles['Normal']))
        story.append(Spacer(1, 5))
    
    story.append(Spacer(1, 20))
    story.append(Paragraph("Report generated by NexGen Logistics AI Platform | Confidential", 
                          ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, textColor=colors.grey, alignment=TA_CENTER)))
    
    doc.build(story)
    buffer.seek(0)
    return buffer
