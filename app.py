import streamlit as st
import pandas as pd
import numpy as np
import os
from utils import load_datasets, preprocess_merge
from datetime import datetime, date
from report_generator import generate_pdf_report

# ML
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

# Sidebar filters
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

# Apply filters
filtered = df.copy()
if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
    start, end = date_range
    filtered = filtered[(filtered["order_date"] >= pd.to_datetime(start)) & (filtered["order_date"] <= pd.to_datetime(end))]
else:
    # single date selected -> filter for that day
    try:
        # convert single date to pandas Timestamp safely
        if isinstance(date_range, (datetime, date)):
            single = pd.Timestamp(date_range)
        else:
            single = pd.Timestamp(str(date_range))
        filtered = filtered[filtered["order_date"] == single]
    except Exception:
        # if parsing fails, leave unfiltered
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

# Visualizations
st.header("Visualizations")

import plotly.express as px

# 1) Delay distribution
st.subheader("Delay distribution")
fig1 = px.histogram(filtered, x="delay_days", nbins=40, title="Delay (days) distribution")
st.plotly_chart(fig1, use_container_width=True)

# 2) Cost breakdown (average by category)
st.subheader("Average delivery cost by category")
cost_by_cat = filtered.groupby("category")["delivery_cost"].mean().reset_index()
fig2 = px.bar(cost_by_cat, x="category", y="delivery_cost", title="Avg delivery cost by product category")
st.plotly_chart(fig2, use_container_width=True)

# 3) Delay vs distance (2D / 3D scatter)
st.subheader("Delay vs Distance")

# Sidebar controls for the scatter
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
        # normalize size to [2, max_marker]
        s = plot_df["_size_field"].astype(float)
        if s.max() > s.min():
            s_scaled = 2 + (s - s.min()) / (s.max() - s.min()) * (max_marker - 2)
        else:
            s_scaled = pd.Series([max_marker] * len(s))
        plot_df["_size_scaled"] = s_scaled

if view_mode == "3D":
    # build z axis from selection
    if z_field in plot_df.columns:
        z_col = z_field
    else:
        z_col = "order_value"
    if size_field != "None" and "_size_scaled" in plot_df.columns:
        scatter_kwargs["size"] = "_size_scaled"
    # add opacity via marker dict
    fig3 = px.scatter_3d(
        plot_df,
        x="distance_km",
        y="delay_days",
        z=z_col,
        color="priority" if "priority" in plot_df.columns else None,
        hover_data=["order_id", "origin", "destination"],
        title=f"Delay vs Distance vs {z_col} (3D)",
    )
    # update marker opacity and size
    fig3.update_traces(marker=dict(symbol='circle', opacity=opacity))
    st.plotly_chart(fig3, use_container_width=True)
else:
    # 2D scatter: x distance, y delay, color by priority, size by scaled marker
    if "_size_scaled" in plot_df.columns:
        fig2d = px.scatter(plot_df, x="distance_km", y="delay_days", color="priority", size="_size_scaled", hover_data=["order_id","origin","destination"], title="Delay vs Distance (2D)")
    else:
        fig2d = px.scatter(plot_df, x="distance_km", y="delay_days", color="priority", hover_data=["order_id","origin","destination"], title="Delay vs Distance (2D)")
    fig2d.update_traces(marker=dict(opacity=opacity))
    st.plotly_chart(fig2d, use_container_width=True)

# Selection table: show selected points if any via Plotly selection is not trivial in Streamlit; provide a filter instead
st.markdown("---")
st.subheader("Scatter filter & selection")
min_dist = int(plot_df["distance_km"].min() or 0)
max_dist = int(plot_df["distance_km"].max() or 0)
if min_dist == max_dist:
    min_dist, max_dist = 0, max_dist
min_dist, max_dist = st.slider("Distance range (km)", min_dist, max_dist, (min_dist, max_dist))
filtered_scatter = plot_df[(plot_df["distance_km"] >= min_dist) & (plot_df["distance_km"] <= max_dist)]
st.write(f"Showing {len(filtered_scatter)} points after distance filter")
st.dataframe(filtered_scatter[["order_id","origin","destination","priority","order_value","distance_km","delay_days"]].head(200))

# 4) On-time rate by carrier
st.subheader("On-time rate by carrier")
if "carrier" in filtered.columns:
    # select the delayed_flag column explicitly to avoid the pandas future deprecation
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

# Predictive model
st.header("Predictive Delay Model")
st.markdown("This section trains a simple RandomForest to predict whether a delivery will be delayed (binary). Model is retrained when data/filter selection changes.")

model_cols = ["priority","order_value","distance_km","traffic_delay_mins","toll_cost","weather_impact_flag"]
train_df = filtered.copy()
train_df = train_df[train_df["delayed_flag"].notna()]

if train_df.shape[0] < 30:
    st.warning("Not enough labeled delivery history in the filtered data to train a reliable model. Show demo metrics only.")
else:
    X = train_df[model_cols].copy()
    # simple encoding
    X = pd.get_dummies(X, columns=["priority"], drop_first=True)
    y = train_df["delayed_flag"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train.fillna(0), y_train)
    y_pred = clf.predict_proba(X_test.fillna(0))[:,1]
    auc = roc_auc_score(y_test, y_pred)
    st.write(f"AUC (test): {auc:.3f}")

    # Feature importance
    importances = pd.Series(clf.feature_importances_, index=X_train.columns).sort_values(ascending=False)
    st.subheader("Feature importance")
    imp_df = importances.reset_index().rename(columns={"index": "feature", 0: "importance"})
    # ensure consistent column name for plotly
    if "importance" not in imp_df.columns and imp_df.shape[1] >= 2:
        imp_df.columns = ["feature", "importance"]
    fig_imp = px.bar(imp_df, x="feature", y="importance", title="Feature importance")
    st.plotly_chart(fig_imp, use_container_width=True)

    # Predict on current filtered unlabeled orders
    unlabeled = filtered[filtered["delayed_flag"].isna()].copy()
    if not unlabeled.empty:
        X_unl = unlabeled[model_cols]
        X_unl = pd.get_dummies(X_unl, columns=["priority"], drop_first=True)
        # align columns
        for c in X_train.columns:
            if c not in X_unl.columns:
                X_unl[c] = 0
        X_unl = X_unl[X_train.columns]
        unlabeled["delay_risk_prob"] = clf.predict_proba(X_unl.fillna(0))[:,1]
        st.subheader("At-risk upcoming orders")
        top_risk = unlabeled.sort_values(by=["delay_risk_prob"], ascending=False).head(20)
        st.dataframe(top_risk[["order_id","origin","destination","priority","order_value","distance_km","delay_risk_prob"]])

        # Recommendation engine: simple rules
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

# PDF Report Generation
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
    # Quick stats preview
    quick_stats = pd.DataFrame({
        'Metric': ['Total Orders', 'On-Time Rate', 'Avg Cost', 'CO2 Emissions', 'Delayed Orders'],
        'Value': [
            int(filtered.shape[0]),
            f"{100*(1 - filtered['delayed_flag'].mean() if filtered['delayed_flag'].count()>0 else 0):.1f}%",
            f"₹{filtered['delivery_cost'].mean():.2f}",
            f"{filtered['co2_g_per_km_est'].sum()/1000:.1f} kg",
            int(filtered['delayed_flag'].sum() if 'delayed_flag' in filtered.columns else 0)
        ]
    })
    st.dataframe(quick_stats, use_container_width=True, hide_index=True)

with col2:
    if st.button("Generate PDF Report", use_container_width=True):
        # Prepare KPIs
        kpis = {
            'total_orders': int(filtered.shape[0]),
            'on_time_rate': 100*(1 - filtered['delayed_flag'].mean() if filtered['delayed_flag'].count()>0 else 0),
            'avg_cost': filtered['delivery_cost'].mean(),
            'co2_kg': filtered['co2_g_per_km_est'].sum()/1000,
            'delayed_orders': int(filtered['delayed_flag'].sum() if 'delayed_flag' in filtered.columns else 0)
        }
        
        # Add model metrics if model was trained
        model_metrics = None
        if train_df.shape[0] >= 30:
            try:
                model_metrics = {'auc': auc}
            except:
                pass
        
        # Generate PDF
        pdf_buffer = generate_pdf_report(filtered, datasets, kpis, model_metrics)
        
        st.download_button(
            label="Download Report (PDF)",
            data=pdf_buffer,
            file_name=f"NexGen_Logistics_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
            mime="application/pdf"
        )
        st.success("✅ Report generated successfully!")

# Order inspector
st.header("Order inspector & what-if")
order_sel = st.selectbox("Select order to inspect (from filtered set)", options=filtered["order_id"].tolist()[:200])
ord = filtered[filtered["order_id"]==order_sel].iloc[0]
st.write(ord.to_dict())

st.markdown("---")
st.markdown("### Notes & next steps")
st.markdown("- This is a prototype. With the real datasets we can improve model features (carrier history, vehicle assignment, route-level telemetry), run cross-validation, and produce costed action plans that trade-off delay reduction vs cost.")

st.sidebar.markdown("---")
st.sidebar.write("Data files located at: ")
st.sidebar.write(DATA_DIR)
