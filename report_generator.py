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
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
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
    
    story.append(Paragraph("NexGen Logistics", title_style))
    story.append(Paragraph("Predictive Delivery Optimization Report", styles['Heading2']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("Executive Summary", heading_style))
    
    kpi_data = [
        ['Metric', 'Value'],
        ['Total Orders', str(kpis.get('total_orders', 0))],
        ['On-Time Rate', f"{kpis.get('on_time_rate', 0):.1f}%"],
        ['Avg Delivery Cost', f"₹{kpis.get('avg_cost', 0):.2f}"],
        ['Total CO2 (kg)', f"{kpis.get('co2_kg', 0):.1f}"],
        ['Delayed Orders', str(kpis.get('delayed_orders', 0))],
    ]
    
    t = Table(kpi_data, colWidths=[3*inch, 3*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    story.append(t)
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("Key Insights", heading_style))
    
    insights = []
    if kpis.get('on_time_rate', 100) < 80:
        insights.append(f"• Critical: On-time delivery rate is {kpis.get('on_time_rate', 0):.1f}%, below target of 85%")
    
    if kpis.get('avg_cost', 0) > 300:
        insights.append(f"• Cost optimization opportunity: Average delivery cost is ₹{kpis.get('avg_cost', 0):.2f}")
    
    insights.append(f"• Environmental impact: {kpis.get('co2_kg', 0):.1f} kg CO2 emissions tracked")
    
    if model_metrics and 'auc' in model_metrics:
        insights.append(f"• Predictive model AUC: {model_metrics['auc']:.3f} - Model reliability is {'High' if model_metrics['auc'] > 0.8 else 'Moderate'}")
    
    for insight in insights:
        story.append(Paragraph(insight, styles['Normal']))
        story.append(Spacer(1, 6))
    
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("Recommendations", heading_style))
    
    recommendations = [
        "1. Implement dynamic route optimization to reduce delivery delays by 15-20%",
        "2. Prioritize carrier partnerships with proven on-time performance",
        "3. Deploy predictive alerts 48 hours before estimated delays",
        "4. Invest in electric vehicle fleet to reduce CO2 emissions by 30%",
        "5. Establish real-time monitoring dashboards for warehouse managers",
    ]
    
    for rec in recommendations:
        story.append(Paragraph(rec, styles['Normal']))
        story.append(Spacer(1, 6))
    
    story.append(PageBreak())
    
    story.append(Paragraph("Detailed Statistics", heading_style))
    
    if not filtered_df.empty:
        priority_stats = filtered_df.groupby('priority').agg({
            'order_id': 'count',
            'delayed_flag': 'mean',
            'delivery_cost': 'mean'
        }).reset_index()
        priority_stats.columns = ['Priority', 'Order Count', 'Delay Rate', 'Avg Cost']
        
        if len(priority_stats) > 0:
            priority_data = [['Priority', 'Orders', 'Delay Rate', 'Avg Cost']]
            for _, row in priority_stats.iterrows():
                priority_data.append([
                    str(row['Priority']),
                    str(int(row['Order Count'])),
                    f"{row['Delay Rate']*100:.1f}%",
                    f"₹{row['Avg Cost']:.2f}"
                ])
            
            t2 = Table(priority_data, colWidths=[1.5*inch, 1.5*inch, 1.5*inch, 1.5*inch])
            t2.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2980b9')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            story.append(t2)
            story.append(Spacer(1, 20))
    
    story.append(Paragraph("Next Steps", heading_style))
    next_steps_text = """
    Based on this analysis, we recommend immediate action on:
    - High-risk orders identified by the predictive model
    - Route optimization for long-distance deliveries
    - Carrier performance review and contract renegotiation
    - Investment in sustainable logistics infrastructure
    """
    story.append(Paragraph(next_steps_text, styles['Normal']))
    
    doc.build(story)
    buffer.seek(0)
    return buffer
