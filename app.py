import streamlit as st
import pandas as pd
import numpy as np
import os
from utils import load_datasets, preprocess_merge
from datetime import datetime, date
from report_generator import generate_pdf_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report

st.set_page_config(page_title="NexGen Logistics — Predictive Delivery Optimizer", layout="wide")

st.title("NexGen Logistics — Predictive Delivery Optimizer")
st.markdown("""
This prototype predicts delivery delays and suggests corrective actions for at-risk orders.
- Upload your CSVs into the `data/` folder (orders.csv, delivery_performance.csv, routes_distance.csv, vehicle_fleet.csv, warehouse_inventory.csv, customer_feedback.csv, cost_breakdown.csv)
- If files are missing, the app generates synthetic demo data.
""")

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

@st.cache_data
def load_and_prepare():
    datasets = load_datasets(DATA_DIR)
    df = preprocess_merge(datasets)
    return datasets, df

datasets, df = load_and_prepare()

st.sidebar.header("Filters")
min_date = df["order_date"].min()
max_date = df["order_date"].max()
date_range = st.sidebar.date_input(
    "Order date range",
    value=(min_date.date() if pd.notna(min_date) else datetime.today().date(),
           max_date.date() if pd.notna(max_date) else datetime.today().date()),
)
priority = st.sidebar.multiselect("Priority", options=df["priority"].unique(), default=list(df["priority"].unique()))
warehouse = st.sidebar.multiselect("Origin Warehouse", options=df["origin"].unique(), default=list(df["origin"].unique()))
carrier = st.sidebar.multiselect("Carrier", options=df["carrier"].dropna().unique() if "carrier" in df.columns else [], default=None)

filtered = df.copy()
if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
    start, end = date_range
    filtered = filtered[(filtered["order_date"] >= pd.to_datetime(start)) & (filtered["order_date"] <= pd.to_datetime(end))]
else:
    try:
        if isinstance(date_range, (datetime, date)):
            single = pd.Timestamp(date_range)
        else:
            single = pd.Timestamp(str(date_range))
        filtered = filtered[filtered["order_date"] == single]
    except Exception:
        pass
if priority:
    filtered = filtered[filtered["priority"].isin(priority)]
if warehouse:
    filtered = filtered[filtered["origin"].isin(warehouse)]
if carrier:
    filtered = filtered[filtered["carrier"].isin(carrier)]

st.subheader("High-level KPIs")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Orders (filtered)", int(filtered.shape[0]))
col2.metric("On-time rate", f"{100*(1 - filtered['delayed_flag'].mean() if filtered['delayed_flag'].count()>0 else 0):.1f}%")
col3.metric("Avg delivery cost", f"₹{filtered['delivery_cost'].mean():.2f}")
col4.metric("Estimated CO2 (kg)", f"{(filtered['co2_g_per_km_est'].sum()/1000):.1f} kg")

st.markdown("---")

st.header("Visualizations")

import plotly.express as px

st.subheader("Delay distribution")
fig1 = px.histogram(filtered, x="delay_days", nbins=40, title="Delay (days) distribution")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Average delivery cost by category")
cost_by_cat = filtered.groupby("category")["delivery_cost"].mean().reset_index()
fig2 = px.bar(cost_by_cat, x="category", y="delivery_cost", title="Avg delivery cost by product category")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Delay vs Distance Analysis")

tab1, tab2, tab3 = st.tabs(["Heatmap (Recommended)", "3D Scatter", "2D Scatter"])

with tab1:
    st.markdown("**Intuitive visualization showing delay patterns across distance ranges**")
    
    heatmap_data = filtered.copy()
    heatmap_data['distance_bin'] = pd.cut(heatmap_data['distance_km'], bins=10, labels=[f"{int(i*20)}-{int((i+1)*20)}km" for i in range(10)])
    heatmap_data['delay_bin'] = pd.cut(heatmap_data['delay_days'], bins=8, labels=[f"{int(i*2)}-{int((i+1)*2)}d" for i in range(8)])
    
    heatmap_pivot = heatmap_data.groupby(['distance_bin', 'delay_bin'], observed=True).size().reset_index(name='count')
    heatmap_pivot_wide = heatmap_pivot.pivot(index='delay_bin', columns='distance_bin', values='count').fillna(0)
    
    fig_heatmap = px.imshow(
        heatmap_pivot_wide,
        labels=dict(x="Distance Range", y="Delay Range", color="Order Count"),
        title="Delay Patterns by Distance Range (Darker = More Orders)",
        color_continuous_scale="RdYlGn_r",
        aspect="auto"
    )
    fig_heatmap.update_xaxes(side="bottom")
    st.plotly_chart(fig_heatmap, use_container_width=True)
    
    st.info("💡 **How to read this**: Dark red areas show distance-delay combinations with many orders. Ideally, we want to see dark colors only in the low-delay rows (bottom).")

with tab2:
    st.markdown("**3D visualization for detailed multi-dimensional analysis**")

st.sidebar.markdown("---")
st.sidebar.subheader("Scatter controls")
view_mode = st.sidebar.selectbox("View", ["3D", "2D"], index=0)
z_field = st.sidebar.selectbox("Z-axis (for 3D)", ["order_value", "delivery_cost", "traffic_delay_mins"], index=0)
size_field = st.sidebar.selectbox("Marker size field", ["delivery_cost", "order_value", "distance_km", "None"], index=0)
opacity = st.sidebar.slider("Marker opacity", 0.1, 1.0, 0.8, 0.05)
max_marker = st.sidebar.slider("Max marker size", 2, 30, 10)

plot_df = filtered.copy()
# Use explicit column checks and Series access so the type-checker understands we're passing a Series to to_numeric
if "distance_km" in plot_df.columns:
    plot_df["distance_km"] = pd.to_numeric(plot_df["distance_km"], errors="coerce")
else:
    plot_df["distance_km"] = pd.Series([None] * len(plot_df), dtype=float)

if "delay_days" in plot_df.columns:
    plot_df["delay_days"] = pd.to_numeric(plot_df["delay_days"], errors="coerce")
else:
    plot_df["delay_days"] = pd.Series([None] * len(plot_df), dtype=float)

if "order_value" in plot_df.columns:
    plot_df["order_value"] = pd.to_numeric(plot_df["order_value"], errors="coerce")
else:
    plot_df["order_value"] = pd.Series([None] * len(plot_df), dtype=float)

if "delivery_cost" in plot_df.columns:
    plot_df["delivery_cost"] = pd.to_numeric(plot_df["delivery_cost"], errors="coerce")
else:
    plot_df["delivery_cost"] = pd.Series([None] * len(plot_df), dtype=float)

# Build kwargs for scatter_3d and avoid passing size if it's all NaN (Plotly errors on NaN sizes)
scatter_kwargs = dict(
    data_frame=plot_df,
    x="distance_km",
    y="delay_days",
    z="order_value",
    hover_data=["order_id", "origin", "destination"],
    title="Delay vs Distance vs Order Value (3D)",
)
if "priority" in plot_df.columns:
    scatter_kwargs["color"] = "priority"

if size_field != "None" and size_field in plot_df.columns:
    if plot_df[size_field].notna().any():
        plot_df["_size_field"] = plot_df[size_field].fillna(plot_df[size_field].median() or 1.0)
        s = plot_df["_size_field"].astype(float)
        if s.max() > s.min():
            s_scaled = 2 + (s - s.min()) / (s.max() - s.min()) * (max_marker - 2)
        else:
            s_scaled = pd.Series([max_marker] * len(s))
        plot_df["_size_scaled"] = s_scaled

if view_mode == "3D":
    if z_field in plot_df.columns:
        z_col = z_field
    else:
        z_col = "order_value"
    if size_field != "None" and "_size_scaled" in plot_df.columns:
        scatter_kwargs["size"] = "_size_scaled"
    fig3 = px.scatter_3d(
        plot_df,
        x="distance_km",
        y="delay_days",
        z=z_col,
        color="priority" if "priority" in plot_df.columns else None,
        hover_data=["order_id", "origin", "destination"],
        title=f"Delay vs Distance vs {z_col} (3D)",
    )
    fig3.update_traces(marker=dict(symbol='circle', opacity=opacity))
    st.plotly_chart(fig3, use_container_width=True)
    st.info("💡 **For analysts**: Rotate the 3D plot to explore relationships between distance, delay, and cost/value.")

with tab3:
    st.markdown("**2D visualization for detailed order inspection**")
    if "_size_scaled" in plot_df.columns:
        fig2d = px.scatter(plot_df, x="distance_km", y="delay_days", color="priority", size="_size_scaled", hover_data=["order_id","origin","destination"], title="Delay vs Distance (2D)")
    else:
        fig2d = px.scatter(plot_df, x="distance_km", y="delay_days", color="priority", hover_data=["order_id","origin","destination"], title="Delay vs Distance (2D)")
    fig2d.update_traces(marker=dict(opacity=opacity))
    st.plotly_chart(fig2d, use_container_width=True)
    st.info("💡 **For detailed analysis**: Hover over points to see order details. Color indicates priority level.")

st.markdown("---")
st.subheader("🎯 Scatter Filter & Selection")
st.markdown("Filter and analyze orders by distance range")

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    min_dist = int(plot_df["distance_km"].min() or 0)
    max_dist = int(plot_df["distance_km"].max() or 0)
    if min_dist == max_dist:
        min_dist, max_dist = 0, max_dist
    selected_range = st.slider("📏 Distance range (km)", min_dist, max_dist, (min_dist, max_dist), key="distance_slider")
    min_dist, max_dist = selected_range

with col2:
    filtered_scatter = plot_df[(plot_df["distance_km"] >= min_dist) & (plot_df["distance_km"] <= max_dist)]
    st.metric("Orders in Range", len(filtered_scatter))
    st.metric("Avg Distance", f"{filtered_scatter['distance_km'].mean():.1f} km")

with col3:
    delayed_in_range = filtered_scatter[filtered_scatter["delayed_flag"] == True].shape[0] if "delayed_flag" in filtered_scatter.columns else 0
    st.metric("Delayed Orders", delayed_in_range)
    if len(filtered_scatter) > 0:
        st.metric("Delay Rate", f"{(delayed_in_range/len(filtered_scatter)*100):.1f}%")

st.markdown("### 📋 Filtered Orders")
display_cols = ["order_id","origin","destination","priority","order_value","distance_km","delay_days"]
available_cols = [col for col in display_cols if col in filtered_scatter.columns]

st.dataframe(
    filtered_scatter[available_cols].head(200),
    use_container_width=True,
    height=400,
    column_config={
        "order_id": st.column_config.TextColumn("Order ID", width="small"),
        "origin": st.column_config.TextColumn("Origin", width="medium"),
        "destination": st.column_config.TextColumn("Destination", width="medium"),
        "priority": st.column_config.TextColumn("Priority", width="small"),
        "order_value": st.column_config.NumberColumn("Order Value (₹)", format="₹%.2f"),
        "distance_km": st.column_config.NumberColumn("Distance (km)", format="%.1f"),
        "delay_days": st.column_config.NumberColumn("Delay (days)", format="%.1f")
    }
)

st.subheader("On-time rate by carrier")
if "carrier" in filtered.columns:
    carrier_perf = (
        filtered.groupby("carrier")["delayed_flag"]
        .apply(lambda s: 1 - s.mean() if s.count() > 0 else np.nan)
        .reset_index(name="on_time_rate")
    )
    fig4 = px.bar(carrier_perf.sort_values(by="on_time_rate", ascending=False), x="carrier", y="on_time_rate", title="Carrier on-time rate")
    st.plotly_chart(fig4, use_container_width=True)
else:
    st.info("No carrier data available in the current dataset.")

st.markdown("---")

st.header("Predictive Delay Model")
st.markdown("This section trains a simple RandomForest to predict whether a delivery will be delayed (binary). Model is retrained when data/filter selection changes.")

model_cols = ["priority","order_value","distance_km","traffic_delay_mins","toll_cost","weather_impact_flag"]
train_df = filtered.copy()
train_df = train_df[train_df["delayed_flag"].notna()]
auc = None

if train_df.shape[0] < 30:
    st.warning("Not enough labeled delivery history in the filtered data to train a reliable model. Show demo metrics only.")
else:
    X = train_df[model_cols].copy()
    X = pd.get_dummies(X, columns=["priority"], drop_first=True)
    y = train_df["delayed_flag"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train.fillna(0), y_train)
    y_pred = clf.predict_proba(X_test.fillna(0))[:,1]
    auc = roc_auc_score(y_test, y_pred)
    st.write(f"AUC (test): {auc:.3f}")

    importances = pd.Series(clf.feature_importances_, index=X_train.columns).sort_values(ascending=False)
    st.subheader("Feature importance")
    imp_df = importances.reset_index().rename(columns={"index": "feature", 0: "importance"})
    if "importance" not in imp_df.columns and imp_df.shape[1] >= 2:
        imp_df.columns = ["feature", "importance"]
    fig_imp = px.bar(imp_df, x="feature", y="importance", title="Feature importance")
    st.plotly_chart(fig_imp, use_container_width=True)

    unlabeled = filtered[filtered["delayed_flag"].isna()].copy()
    if not unlabeled.empty:
        X_unl = unlabeled[model_cols]
        X_unl = pd.get_dummies(X_unl, columns=["priority"], drop_first=True)
        for c in X_train.columns:
            if c not in X_unl.columns:
                X_unl[c] = 0
        X_unl = X_unl[X_train.columns]
        unlabeled["delay_risk_prob"] = clf.predict_proba(X_unl.fillna(0))[:,1]
        st.subheader("At-risk upcoming orders")
        top_risk = unlabeled.sort_values(by=["delay_risk_prob"], ascending=False).head(20)
        st.dataframe(top_risk[["order_id","origin","destination","priority","order_value","distance_km","delay_risk_prob"]])

        def recommend_action(row):
            actions = []
            if row["priority"] == "Express":
                actions.append("Use fastest vehicle (truck/van) or priority lane")
            if row.get("distance_km",0) > 200 and row.get("delay_risk_prob",0) > 0.5:
                actions.append("Consider air/partner carrier")
            if row.get("weather_impact_flag",0) == 1:
                actions.append("Re-route to avoid affected region or delay dispatch until weather clears")
            if not actions:
                actions = ["Monitor closely; notify carrier"]
            return "; ".join(actions)

        top_risk["recommended_action"] = top_risk.apply(recommend_action, axis=1)
        st.download_button("Download recommendations (CSV)", top_risk.to_csv(index=False), file_name="recommendations.csv")

st.header("Executive PDF Report")
st.markdown("""
Generate a comprehensive PDF report with:
- Executive summary and KPIs
- Detailed performance analytics
- Priority-wise breakdown
- Actionable recommendations
- Next steps for optimization
""")

col1, col2 = st.columns([2, 1])

with col1:
    quick_stats = pd.DataFrame({
        'Metric': ['Total Orders', 'On-Time Rate', 'Avg Cost', 'CO2 Emissions', 'Delayed Orders'],
        'Value': [
            str(int(filtered.shape[0])),
            f"{100*(1 - filtered['delayed_flag'].mean() if filtered['delayed_flag'].count()>0 else 0):.1f}%",
            f"₹{filtered['delivery_cost'].mean():.2f}",
            f"{filtered['co2_g_per_km_est'].sum()/1000:.1f} kg",
            str(int(filtered['delayed_flag'].sum() if 'delayed_flag' in filtered.columns else 0))
        ]
    })
    st.dataframe(quick_stats, use_container_width=True, hide_index=True)

with col2:
    if st.button("Generate PDF Report", use_container_width=True):
        kpis = {
            'total_orders': int(filtered.shape[0]),
            'on_time_rate': 100*(1 - filtered['delayed_flag'].mean() if filtered['delayed_flag'].count()>0 else 0),
            'avg_cost': filtered['delivery_cost'].mean(),
            'co2_kg': filtered['co2_g_per_km_est'].sum()/1000,
            'delayed_orders': int(filtered['delayed_flag'].sum() if 'delayed_flag' in filtered.columns else 0)
        }
        
        model_metrics = None
        if train_df.shape[0] >= 30:
            try:
                model_metrics = {'auc': auc}
            except:
                pass
        
        pdf_buffer = generate_pdf_report(filtered, datasets, kpis, model_metrics)
        
        st.download_button(
            label="Download Report (PDF)",
            data=pdf_buffer,
            file_name=f"NexGen_Logistics_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
            mime="application/pdf"
        )
        st.success("✅ Report generated successfully!")

st.header("🔍 Order Inspector & What-If Analysis")
st.markdown("Inspect individual orders and simulate delivery scenarios")

order_sel = st.selectbox("Select order to inspect (from filtered set)", options=filtered["order_id"].tolist()[:200], key="order_inspector")
ord = filtered[filtered["order_id"]==order_sel].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Order Details")
    order_info = {
        "Order ID": ord.get("order_id", "N/A"),
        "Order Date": ord.get("order_date", "N/A"),
        "Customer Segment": ord.get("customer_segment", "N/A"),
        "Priority": ord.get("priority", "N/A"),
        "Category": ord.get("category", "N/A"),
        "Order Value": f"₹{ord.get('order_value', 0):.2f}",
        "Special Handling": ord.get("special_handling", "N/A")
    }
    
    for key, value in order_info.items():
        st.markdown(f"**{key}:** {value}")
    
    st.markdown("### Route Information")
    route_info = {
        "Origin": ord.get("origin", "N/A"),
        "Destination": ord.get("destination", "N/A"),
        "Distance": f"{ord.get('distance_km', 0):.1f} km",
        "Fuel Consumption": f"{ord.get('fuel_liters', 0):.2f} L",
        "Toll Cost": f"₹{ord.get('toll_cost', 0):.2f}",
        "Traffic Delay": f"{ord.get('traffic_delay_mins', 0):.0f} mins",
        "Weather Impact": "Yes" if ord.get("weather_impact_flag", 0) == 1 else "No"
    }
    
    for key, value in route_info.items():
        st.markdown(f"**{key}:** {value}")

with col2:
    st.markdown("### Delivery Performance")
    delivery_info = {
        "Carrier": ord.get("carrier", "N/A"),
        "Promised Date": ord.get("promised_date", "N/A"),
        "Actual Date": ord.get("actual_date", "N/A"),
        "Status": ord.get("status", "N/A"),
        "Delay (days)": f"{ord.get('delay_days', 0):.1f}",
        "Delayed?": "WARNING: Yes" if ord.get("delayed_flag", False) else "OK: No",
        "Quality Issue": ord.get("quality_issue", "N/A"),
        "Customer Rating": f"{ord.get('customer_rating', 0):.1f}/5.0" if pd.notna(ord.get("customer_rating")) else "N/A"
    }
    
    for key, value in delivery_info.items():
        st.markdown(f"**{key}:** {value}")
    
    st.markdown("### Cost Breakdown")
    cost_info = {
        "Delivery Cost": f"₹{ord.get('delivery_cost', 0):.2f}",
        "Fuel Cost": f"₹{ord.get('fuel_cost', 0):.2f}",
        "Labor Cost": f"₹{ord.get('labor_cost', 0):.2f}",
        "Maintenance": f"₹{ord.get('maintenance_cost', 0):.2f}",
        "Insurance": f"₹{ord.get('insurance_cost', 0):.2f}",
        "Packaging": f"₹{ord.get('packaging_cost', 0):.2f}",
        "Platform Fee": f"₹{ord.get('platform_fee', 0):.2f}",
        "Cost per KM": f"₹{ord.get('cost_per_km', 0):.3f}",
        "CO2 Estimate": f"{ord.get('co2_g_per_km_est', 0):.1f} g"
    }
    
    for key, value in cost_info.items():
        st.markdown(f"**{key}:** {value}")

st.markdown("---")
st.markdown("### 📝 Notes & Next Steps")
st.info("💡 This prototype can be enhanced with carrier history analysis, vehicle assignment optimization, real-time GPS tracking, cross-validation, and cost-benefit trade-off models for delay reduction strategies.")

st.sidebar.markdown("---")
st.sidebar.write("Data files located at: ")
st.sidebar.write(DATA_DIR)
