import streamlit as stimport streamlit as st

import pandas as pdimport pandas as pd

import numpy as npimport numpy as np

import osimport os

from utils import load_datasets, preprocess_mergefrom utils import load_datasets, preprocess_merge

from datetime import datetime, datefrom datetime import datetime, date

from sklearn.ensemble import RandomForestClassifier, IsolationForest

from sklearn.model_selection import train_test_split# ML

from sklearn.metrics import roc_auc_scorefrom sklearn.ensemble import RandomForestClassifier

import plotly.express as pxfrom sklearn.model_selection import train_test_split

import plotly.graph_objects as gofrom sklearn.metrics import roc_auc_score, classification_report

from report_generator import generate_pdf_report

import networkx as nxst.set_page_config(page_title="NexGen Logistics — Predictive Delivery Optimizer", layout="wide")



st.set_page_config(st.title("NexGen Logistics — Predictive Delivery Optimizer")

    page_title="NexGen Logistics AI Platform",st.markdown("""

    layout="wide",This prototype predicts delivery delays and suggests corrective actions for at-risk orders.

    initial_sidebar_state="expanded"- Upload your CSVs into the `data/` folder (orders.csv, delivery_performance.csv, routes_distance.csv, vehicle_fleet.csv, warehouse_inventory.csv, customer_feedback.csv, cost_breakdown.csv)

)- If files are missing, the app generates synthetic demo data.

""")

st.markdown("""

<style>DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

    .main-header {

        font-size: 3rem;@st.cache_data

        font-weight: bold;def load_and_prepare():

        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);    datasets = load_datasets(DATA_DIR)

        -webkit-background-clip: text;    df = preprocess_merge(datasets)

        -webkit-text-fill-color: transparent;    return datasets, df

        text-align: center;

        padding: 1rem 0;datasets, df = load_and_prepare()

    }

    .metric-card {# Sidebar filters

        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);st.sidebar.header("Filters")

        padding: 1.5rem;min_date = df["order_date"].min()

        border-radius: 10px;max_date = df["order_date"].max()

        box-shadow: 0 4px 6px rgba(0,0,0,0.1);date_range = st.sidebar.date_input(

        color: white;    "Order date range",

        text-align: center;    value=(min_date.date() if pd.notna(min_date) else datetime.today().date(),

    }           max_date.date() if pd.notna(max_date) else datetime.today().date()),

    .insight-box {)

        background: #f8f9fa;priority = st.sidebar.multiselect("Priority", options=df["priority"].unique(), default=list(df["priority"].unique()))

        border-left: 4px solid #667eea;warehouse = st.sidebar.multiselect("Origin Warehouse", options=df["origin"].unique(), default=list(df["origin"].unique()))

        padding: 1rem;carrier = st.sidebar.multiselect("Carrier", options=df["carrier"].dropna().unique() if "carrier" in df.columns else [], default=None)

        margin: 1rem 0;

        border-radius: 4px;# Apply filters

    }filtered = df.copy()

    .stButton>button {if isinstance(date_range, (list, tuple)) and len(date_range) == 2:

        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);    start, end = date_range

        color: white;    filtered = filtered[(filtered["order_date"] >= pd.to_datetime(start)) & (filtered["order_date"] <= pd.to_datetime(end))]

        font-weight: bold;else:

        border-radius: 8px;    # single date selected -> filter for that day

        padding: 0.5rem 2rem;    try:

        border: none;        # convert single date to pandas Timestamp safely

    }        if isinstance(date_range, (datetime, date)):

</style>            single = pd.Timestamp(date_range)

""", unsafe_allow_html=True)        else:

            single = pd.Timestamp(str(date_range))

st.markdown('<p class="main-header">🚀 NexGen Logistics AI Platform</p>', unsafe_allow_html=True)        filtered = filtered[filtered["order_date"] == single]

st.markdown('<p style="text-align:center;color:#666;font-size:1.2rem;">Predictive Intelligence for Modern Logistics</p>', unsafe_allow_html=True)    except Exception:

        # if parsing fails, leave unfiltered

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")        pass

if priority:

@st.cache_data    filtered = filtered[filtered["priority"].isin(priority)]

def load_and_prepare():if warehouse:

    datasets = load_datasets(DATA_DIR)    filtered = filtered[filtered["origin"].isin(warehouse)]

    df = preprocess_merge(datasets)if carrier:

    return datasets, df    filtered = filtered[filtered["carrier"].isin(carrier)]



@st.cache_datast.subheader("High-level KPIs")

def detect_anomalies(data):col1, col2, col3, col4 = st.columns(4)

    features = ['distance_km', 'delivery_cost', 'delay_days', 'traffic_delay_mins']col1.metric("Orders (filtered)", int(filtered.shape[0]))

    valid_data = data[features].dropna()col2.metric("On-time rate", f"{100*(1 - filtered['delayed_flag'].mean() if filtered['delayed_flag'].count()>0 else 0):.1f}%")

    col3.metric("Avg delivery cost", f"₹{filtered['delivery_cost'].mean():.2f}")

    if len(valid_data) < 10:col4.metric("Estimated CO2 (kg)", f"{(filtered['co2_g_per_km_est'].sum()/1000):.1f} kg")

        return pd.Series([False] * len(data), index=data.index)

    st.markdown("---")

    iso_forest = IsolationForest(contamination=0.1, random_state=42)

    predictions = iso_forest.fit_predict(valid_data)# Visualizations

    anomalies = pd.Series([False] * len(data), index=data.index)st.header("Visualizations")

    anomalies.loc[valid_data.index] = predictions == -1

    return anomaliesimport plotly.express as px



datasets, df = load_and_prepare()# 1) Delay distribution

df['is_anomaly'] = detect_anomalies(df)st.subheader("Delay distribution")

fig1 = px.histogram(filtered, x="delay_days", nbins=40, title="Delay (days) distribution")

st.sidebar.markdown("## 🎛️ Control Panel")st.plotly_chart(fig1, use_container_width=True)

st.sidebar.markdown("---")

# 2) Cost breakdown (average by category)

min_date = df["order_date"].min()st.subheader("Average delivery cost by category")

max_date = df["order_date"].max()cost_by_cat = filtered.groupby("category")["delivery_cost"].mean().reset_index()

date_range = st.sidebar.date_input(fig2 = px.bar(cost_by_cat, x="category", y="delivery_cost", title="Avg delivery cost by product category")

    "📅 Date Range",st.plotly_chart(fig2, use_container_width=True)

    value=(min_date.date() if pd.notna(min_date) else datetime.today().date(),

           max_date.date() if pd.notna(max_date) else datetime.today().date()),# 3) Delay vs distance (2D / 3D scatter)

)st.subheader("Delay vs Distance")



priority = st.sidebar.multiselect("⚡ Priority", options=df["priority"].unique(), default=list(df["priority"].unique()))# Sidebar controls for the scatter

warehouse = st.sidebar.multiselect("🏭 Origin", options=df["origin"].unique(), default=list(df["origin"].unique()))st.sidebar.markdown("---")

carrier = st.sidebar.multiselect("🚛 Carrier", options=df["carrier"].dropna().unique() if "carrier" in df.columns else [], default=None)st.sidebar.subheader("Scatter controls")

view_mode = st.sidebar.selectbox("View", ["3D", "2D"], index=0)

show_anomalies = st.sidebar.checkbox("🔍 Show Anomalies Only", value=False)z_field = st.sidebar.selectbox("Z-axis (for 3D)", ["order_value", "delivery_cost", "traffic_delay_mins"], index=0)

size_field = st.sidebar.selectbox("Marker size field", ["delivery_cost", "order_value", "distance_km", "None"], index=0)

filtered = df.copy()opacity = st.sidebar.slider("Marker opacity", 0.1, 1.0, 0.8, 0.05)

if isinstance(date_range, (list, tuple)) and len(date_range) == 2:max_marker = st.sidebar.slider("Max marker size", 2, 30, 10)

    start, end = date_range

    filtered = filtered[(filtered["order_date"] >= pd.to_datetime(start)) & (filtered["order_date"] <= pd.to_datetime(end))]plot_df = filtered.copy()

else:# Use explicit column checks and Series access so the type-checker understands we're passing a Series to to_numeric

    try:if "distance_km" in plot_df.columns:

        if isinstance(date_range, (datetime, date)):    plot_df["distance_km"] = pd.to_numeric(plot_df["distance_km"], errors="coerce")

            single = pd.Timestamp(date_range)else:

        else:    plot_df["distance_km"] = pd.Series([None] * len(plot_df), dtype=float)

            single = pd.Timestamp(str(date_range))

        filtered = filtered[filtered["order_date"] == single]if "delay_days" in plot_df.columns:

    except Exception:    plot_df["delay_days"] = pd.to_numeric(plot_df["delay_days"], errors="coerce")

        passelse:

    plot_df["delay_days"] = pd.Series([None] * len(plot_df), dtype=float)

if priority:

    filtered = filtered[filtered["priority"].isin(priority)]if "order_value" in plot_df.columns:

if warehouse:    plot_df["order_value"] = pd.to_numeric(plot_df["order_value"], errors="coerce")

    filtered = filtered[filtered["origin"].isin(warehouse)]else:

if carrier:    plot_df["order_value"] = pd.Series([None] * len(plot_df), dtype=float)

    filtered = filtered[filtered["carrier"].isin(carrier)]

if show_anomalies:if "delivery_cost" in plot_df.columns:

    filtered = filtered[filtered['is_anomaly'] == True]    plot_df["delivery_cost"] = pd.to_numeric(plot_df["delivery_cost"], errors="coerce")

else:

st.markdown("### 📊 Real-Time KPIs")    plot_df["delivery_cost"] = pd.Series([None] * len(plot_df), dtype=float)

col1, col2, col3, col4, col5 = st.columns(5)

# Build kwargs for scatter_3d and avoid passing size if it's all NaN (Plotly errors on NaN sizes)

with col1:scatter_kwargs = dict(

    st.metric("📦 Orders", int(filtered.shape[0]), delta=f"+{int(filtered.shape[0]*0.12)}")    data_frame=plot_df,

with col2:    x="distance_km",

    on_time_rate = 100*(1 - filtered['delayed_flag'].mean() if filtered['delayed_flag'].count()>0 else 0)    y="delay_days",

    st.metric("✅ On-Time", f"{on_time_rate:.1f}%", delta=f"{on_time_rate-85:.1f}%")    z="order_value",

with col3:    hover_data=["order_id", "origin", "destination"],

    avg_cost = filtered['delivery_cost'].mean()    title="Delay vs Distance vs Order Value (3D)",

    st.metric("💰 Avg Cost", f"₹{avg_cost:.0f}", delta="-8%"))

with col4:if "priority" in plot_df.columns:

    co2_kg = filtered['co2_g_per_km_est'].sum()/1000    scatter_kwargs["color"] = "priority"

    st.metric("🌱 CO2 (kg)", f"{co2_kg:.0f}", delta="-12%")

with col5:if size_field != "None" and size_field in plot_df.columns:

    anomaly_count = filtered['is_anomaly'].sum()    if plot_df[size_field].notna().any():

    st.metric("⚠️ Anomalies", int(anomaly_count), delta=f"{int(anomaly_count)}")        plot_df["_size_field"] = plot_df[size_field].fillna(plot_df[size_field].median() or 1.0)

        # normalize size to [2, max_marker]

st.markdown("---")        s = plot_df["_size_field"].astype(float)

        if s.max() > s.min():

tab1, tab2, tab3, tab4 = st.tabs(["📈 Analytics", "🤖 AI Predictions", "🗺️ Network", "📄 Reports"])            s_scaled = 2 + (s - s.min()) / (s.max() - s.min()) * (max_marker - 2)

        else:

with tab1:            s_scaled = pd.Series([max_marker] * len(s))

    col_left, col_right = st.columns(2)        plot_df["_size_scaled"] = s_scaled

    

    with col_left:if view_mode == "3D":

        st.markdown("#### Delivery Performance Trend")    # build z axis from selection

            if z_field in plot_df.columns:

        trend_df = filtered.groupby(filtered['order_date'].dt.to_period('D')).agg({        z_col = z_field

            'delayed_flag': 'mean',    else:

            'order_id': 'count'        z_col = "order_value"

        }).reset_index()    if size_field != "None" and "_size_scaled" in plot_df.columns:

        trend_df['order_date'] = trend_df['order_date'].dt.to_timestamp()        scatter_kwargs["size"] = "_size_scaled"

            # add opacity via marker dict

        fig_trend = go.Figure()    fig3 = px.scatter_3d(

        fig_trend.add_trace(go.Scatter(        plot_df,

            x=trend_df['order_date'],        x="distance_km",

            y=trend_df['delayed_flag']*100,        y="delay_days",

            mode='lines+markers',        z=z_col,

            name='Delay Rate',        color="priority" if "priority" in plot_df.columns else None,

            line=dict(color='#e74c3c', width=3),        hover_data=["order_id", "origin", "destination"],

            fill='tozeroy'        title=f"Delay vs Distance vs {z_col} (3D)",

        ))    )

        fig_trend.update_layout(    # update marker opacity and size

            xaxis_title="Date",    fig3.update_traces(marker=dict(symbol='circle', opacity=opacity))

            yaxis_title="Delay Rate (%)",    st.plotly_chart(fig3, use_container_width=True)

            hovermode='x unified',else:

            template='plotly_white',    # 2D scatter: x distance, y delay, color by priority, size by scaled marker

            height=400    if "_size_scaled" in plot_df.columns:

        )        fig2d = px.scatter(plot_df, x="distance_km", y="delay_days", color="priority", size="_size_scaled", hover_data=["order_id","origin","destination"], title="Delay vs Distance (2D)")

        st.plotly_chart(fig_trend, use_container_width=True)    else:

                fig2d = px.scatter(plot_df, x="distance_km", y="delay_days", color="priority", hover_data=["order_id","origin","destination"], title="Delay vs Distance (2D)")

        st.markdown("#### Cost Distribution by Category")    fig2d.update_traces(marker=dict(opacity=opacity))

        cost_cat = filtered.groupby('category')['delivery_cost'].mean().sort_values(ascending=False).reset_index()    st.plotly_chart(fig2d, use_container_width=True)

        fig_cat = px.bar(

            cost_cat,# Selection table: show selected points if any via Plotly selection is not trivial in Streamlit; provide a filter instead

            x='category',st.markdown("---")

            y='delivery_cost',st.subheader("Scatter filter & selection")

            color='delivery_cost',min_dist = int(plot_df["distance_km"].min() or 0)

            color_continuous_scale='Viridis'max_dist = int(plot_df["distance_km"].max() or 0)

        )if min_dist == max_dist:

        fig_cat.update_layout(template='plotly_white', height=400, showlegend=False)    min_dist, max_dist = 0, max_dist

        st.plotly_chart(fig_cat, use_container_width=True)min_dist, max_dist = st.slider("Distance range (km)", min_dist, max_dist, (min_dist, max_dist))

    filtered_scatter = plot_df[(plot_df["distance_km"] >= min_dist) & (plot_df["distance_km"] <= max_dist)]

    with col_right:st.write(f"Showing {len(filtered_scatter)} points after distance filter")

        st.markdown("#### Dynamic Delay Analysis")st.dataframe(filtered_scatter[["order_id","origin","destination","priority","order_value","distance_km","delay_days"]].head(200))

        

        st.sidebar.markdown("---")# 4) On-time rate by carrier

        st.sidebar.markdown("### 🎨 Visualization Controls")st.subheader("On-time rate by carrier")

        view_mode = st.sidebar.selectbox("View Mode", ["3D", "2D"], index=0)if "carrier" in filtered.columns:

        z_field = st.sidebar.selectbox("Z-Axis", ["order_value", "delivery_cost", "traffic_delay_mins"], index=0)    # select the delayed_flag column explicitly to avoid the pandas future deprecation

        opacity = st.sidebar.slider("Opacity", 0.1, 1.0, 0.7, 0.05)    carrier_perf = (

                filtered.groupby("carrier")["delayed_flag"]

        plot_df = filtered.copy()        .apply(lambda s: 1 - s.mean() if s.count() > 0 else np.nan)

                .reset_index(name="on_time_rate")

        for col in ["distance_km", "delay_days", "order_value", "delivery_cost"]:    )

            if col in plot_df.columns:    fig4 = px.bar(carrier_perf.sort_values(by="on_time_rate", ascending=False), x="carrier", y="on_time_rate", title="Carrier on-time rate")

                plot_df[col] = pd.to_numeric(plot_df[col], errors="coerce")    st.plotly_chart(fig4, use_container_width=True)

            else:else:

                plot_df[col] = pd.Series([None] * len(plot_df), dtype=float)    st.info("No carrier data available in the current dataset.")

        

        if view_mode == "3D":st.markdown("---")

            fig3d = px.scatter_3d(

                plot_df,# Predictive model

                x="distance_km",st.header("Predictive Delay Model")

                y="delay_days",st.markdown("This section trains a simple RandomForest to predict whether a delivery will be delayed (binary). Model is retrained when data/filter selection changes.")

                z=z_field,

                color="priority",model_cols = ["priority","order_value","distance_km","traffic_delay_mins","toll_cost","weather_impact_flag"]

                hover_data=["order_id", "origin", "destination"],train_df = filtered.copy()

                title=f"Multi-Dimensional Delivery Analysis"train_df = train_df[train_df["delayed_flag"].notna()]

            )

            fig3d.update_traces(marker=dict(size=5, opacity=opacity))if train_df.shape[0] < 30:

            fig3d.update_layout(height=500)    st.warning("Not enough labeled delivery history in the filtered data to train a reliable model. Show demo metrics only.")

            st.plotly_chart(fig3d, use_container_width=True)else:

        else:    X = train_df[model_cols].copy()

            fig2d = px.scatter(    # simple encoding

                plot_df,    X = pd.get_dummies(X, columns=["priority"], drop_first=True)

                x="distance_km",    y = train_df["delayed_flag"].astype(int)

                y="delay_days",

                color="priority",    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

                size="order_value",    clf = RandomForestClassifier(n_estimators=100, random_state=42)

                hover_data=["order_id"],    clf.fit(X_train.fillna(0), y_train)

                title="Delay vs Distance Analysis"    y_pred = clf.predict_proba(X_test.fillna(0))[:,1]

            )    auc = roc_auc_score(y_test, y_pred)

            fig2d.update_traces(marker=dict(opacity=opacity))    st.write(f"AUC (test): {auc:.3f}")

            fig2d.update_layout(template='plotly_white', height=500)

            st.plotly_chart(fig2d, use_container_width=True)    # Feature importance

            importances = pd.Series(clf.feature_importances_, index=X_train.columns).sort_values(ascending=False)

        st.markdown("#### Carrier Performance Benchmark")    st.subheader("Feature importance")

        if "carrier" in filtered.columns:    imp_df = importances.reset_index().rename(columns={"index": "feature", 0: "importance"})

            carrier_perf = (    # ensure consistent column name for plotly

                filtered.groupby("carrier")["delayed_flag"]    if "importance" not in imp_df.columns and imp_df.shape[1] >= 2:

                .apply(lambda s: 1 - s.mean() if s.count() > 0 else np.nan)        imp_df.columns = ["feature", "importance"]

                .reset_index(name="on_time_rate")    fig_imp = px.bar(imp_df, x="feature", y="importance", title="Feature importance")

            )    st.plotly_chart(fig_imp, use_container_width=True)

            fig_carrier = px.bar(

                carrier_perf.sort_values(by="on_time_rate", ascending=False),    # Predict on current filtered unlabeled orders

                x="carrier",    unlabeled = filtered[filtered["delayed_flag"].isna()].copy()

                y="on_time_rate",    if not unlabeled.empty:

                color="on_time_rate",        X_unl = unlabeled[model_cols]

                color_continuous_scale='RdYlGn'        X_unl = pd.get_dummies(X_unl, columns=["priority"], drop_first=True)

            )        # align columns

            fig_carrier.update_layout(template='plotly_white', height=400, showlegend=False)        for c in X_train.columns:

            st.plotly_chart(fig_carrier, use_container_width=True)            if c not in X_unl.columns:

                X_unl[c] = 0

with tab2:        X_unl = X_unl[X_train.columns]

    st.markdown("### 🤖 Machine Learning Predictions")        unlabeled["delay_risk_prob"] = clf.predict_proba(X_unl.fillna(0))[:,1]

            st.subheader("At-risk upcoming orders")

    model_cols = ["priority","order_value","distance_km","traffic_delay_mins","toll_cost","weather_impact_flag"]        top_risk = unlabeled.sort_values(by=["delay_risk_prob"], ascending=False).head(20)

    train_df = filtered.copy()        st.dataframe(top_risk[["order_id","origin","destination","priority","order_value","distance_km","delay_risk_prob"]])

    train_df = train_df[train_df["delayed_flag"].notna()]

            # Recommendation engine: simple rules

    if train_df.shape[0] >= 30:        def recommend_action(row):

        X = train_df[model_cols].copy()            actions = []

        X = pd.get_dummies(X, columns=["priority"], drop_first=True)            if row["priority"] == "Express":

        y = train_df["delayed_flag"].astype(int)                actions.append("Use fastest vehicle (truck/van) or priority lane")

                    if row.get("distance_km",0) > 200 and row.get("delay_risk_prob",0) > 0.5:

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)                actions.append("Consider air/partner carrier")

        clf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)            if row.get("weather_impact_flag",0) == 1:

        clf.fit(X_train.fillna(0), y_train)                actions.append("Re-route to avoid affected region or delay dispatch until weather clears")

        y_pred_proba = clf.predict_proba(X_test.fillna(0))[:,1]            if not actions:

        auc = roc_auc_score(y_test, y_pred_proba)                actions = ["Monitor closely; notify carrier"]

                    return "; ".join(actions)

        col1, col2 = st.columns([1, 2])

                top_risk["recommended_action"] = top_risk.apply(recommend_action, axis=1)

        with col1:        st.download_button("Download recommendations (CSV)", top_risk.to_csv(index=False), file_name="recommendations.csv")

            st.markdown('<div class="insight-box">', unsafe_allow_html=True)

            st.markdown(f"**Model Performance**")# Order inspector

            st.metric("AUC Score", f"{auc:.3f}", delta="High Accuracy" if auc > 0.8 else "Moderate")st.header("Order inspector & what-if")

            st.markdown(f"**Training Size:** {len(X_train)} orders")order_sel = st.selectbox("Select order to inspect (from filtered set)", options=filtered["order_id"].tolist()[:200])

            st.markdown(f"**Test Size:** {len(X_test)} orders")ord = filtered[filtered["order_id"]==order_sel].iloc[0]

            st.markdown('</div>', unsafe_allow_html=True)st.write(ord.to_dict())

            

            feature_imp = pd.DataFrame({st.markdown("---")

                'feature': X_train.columns,st.markdown("### Notes & next steps")

                'importance': clf.feature_importances_st.markdown("- This is a prototype. With the real datasets we can improve model features (carrier history, vehicle assignment, route-level telemetry), run cross-validation, and produce costed action plans that trade-off delay reduction vs cost.")

            }).sort_values('importance', ascending=False).head(10)

            st.sidebar.markdown("---")

            fig_imp = px.bar(st.sidebar.write("Data files located at: ")

                feature_imp,st.sidebar.write(DATA_DIR)

                x='importance',
                y='feature',
                orientation='h',
                color='importance',
                color_continuous_scale='Blues'
            )
            fig_imp.update_layout(height=400, showlegend=False, template='plotly_white')
            st.plotly_chart(fig_imp, use_container_width=True)
        
        with col2:
            unlabeled = filtered[filtered["delayed_flag"].isna()].copy()
            
            if not unlabeled.empty:
                X_unl = unlabeled[model_cols]
                X_unl = pd.get_dummies(X_unl, columns=["priority"], drop_first=True)
                
                for c in X_train.columns:
                    if c not in X_unl.columns:
                        X_unl[c] = 0
                X_unl = X_unl[X_train.columns]
                
                unlabeled["delay_risk_prob"] = clf.predict_proba(X_unl.fillna(0))[:,1]
                
                st.markdown("#### 🎯 High-Risk Orders Identified")
                top_risk = unlabeled.sort_values(by=["delay_risk_prob"], ascending=False).head(15)
                
                def get_action(row):
                    actions = []
                    if row["priority"] == "Express":
                        actions.append("🚨 Fast-track processing")
                    if row.get("distance_km",0) > 200 and row.get("delay_risk_prob",0) > 0.5:
                        actions.append("✈️ Consider air freight")
                    if row.get("weather_impact_flag",0) == 1:
                        actions.append("🌧️ Weather contingency")
                    if not actions:
                        actions = ["👁️ Monitor"]
                    return " | ".join(actions)
                
                top_risk["action"] = top_risk.apply(get_action, axis=1)
                
                display_cols = ["order_id", "origin", "destination", "priority", "delay_risk_prob", "action"]
                display_df = top_risk[display_cols].copy()
                display_df["delay_risk_prob"] = display_df["delay_risk_prob"].apply(lambda x: f"{x*100:.1f}%")
                
                st.dataframe(
                    display_df,
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "delay_risk_prob": st.column_config.TextColumn("Risk %", width="small"),
                        "action": st.column_config.TextColumn("Recommended Action", width="large")
                    }
                )
                
                csv_export = top_risk.to_csv(index=False)
                st.download_button(
                    label="📥 Download Risk Report (CSV)",
                    data=csv_export,
                    file_name=f"high_risk_orders_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv"
                )
            else:
                st.info("No unlabeled orders to predict.")
    else:
        st.warning("Insufficient data for model training. Need at least 30 labeled records.")

with tab3:
    st.markdown("### 🗺️ Logistics Network Visualization")
    
    route_data = filtered.groupby(['origin', 'destination']).agg({
        'order_id': 'count',
        'delivery_cost': 'mean',
        'delayed_flag': 'mean'
    }).reset_index()
    route_data.columns = ['origin', 'destination', 'volume', 'avg_cost', 'delay_rate']
    
    G = nx.DiGraph()
    
    for _, row in route_data.iterrows():
        G.add_edge(row['origin'], row['destination'], weight=row['volume'])
    
    pos = nx.spring_layout(G, k=2, iterations=50)
    
    edge_trace = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace.append(go.Scatter(
            x=[x0, x1, None],
            y=[y0, y1, None],
            mode='lines',
            line=dict(width=2, color='#888'),
            hoverinfo='none'
        ))
    
    node_x = []
    node_y = []
    node_text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(f"{node}<br>Connections: {G.degree(node)}")
    
    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers+text',
        text=[node for node in G.nodes()],
        textposition="top center",
        hovertext=node_text,
        marker=dict(
            size=30,
            color='#667eea',
            line=dict(width=2, color='white')
        )
    )
    
    fig_network = go.Figure(data=edge_trace + [node_trace])
    fig_network.update_layout(
        showlegend=False,
        hovermode='closest',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=600,
        plot_bgcolor='#f8f9fa'
    )
    st.plotly_chart(fig_network, use_container_width=True)
    
    st.markdown("#### 📊 Top Routes by Volume")
    top_routes = route_data.sort_values('volume', ascending=False).head(10)
    
    fig_routes = px.bar(
        top_routes,
        x='volume',
        y=top_routes['origin'] + ' → ' + top_routes['destination'],
        orientation='h',
        color='delay_rate',
        color_continuous_scale='RdYlGn_r',
        labels={'color': 'Delay Rate'}
    )
    fig_routes.update_layout(height=400, template='plotly_white')
    st.plotly_chart(fig_routes, use_container_width=True)

with tab4:
    st.markdown("### 📄 Executive Report Generator")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Generate a comprehensive PDF report with:
        - Executive summary and KPIs
        - Detailed performance analytics
        - Priority-wise breakdown
        - Actionable recommendations
        - Next steps for optimization
        """)
    
    with col2:
        if st.button("🚀 Generate PDF Report", use_container_width=True):
            kpis = {
                'total_orders': int(filtered.shape[0]),
                'on_time_rate': 100*(1 - filtered['delayed_flag'].mean() if filtered['delayed_flag'].count()>0 else 0),
                'avg_cost': filtered['delivery_cost'].mean(),
                'co2_kg': filtered['co2_g_per_km_est'].sum()/1000,
                'delayed_orders': int(filtered['delayed_flag'].sum() if 'delayed_flag' in filtered.columns else 0)
            }
            
            model_metrics = None
            if train_df.shape[0] >= 30:
                model_metrics = {'auc': auc}
            
            pdf_buffer = generate_pdf_report(filtered, datasets, kpis, model_metrics)
            
            st.download_button(
                label="📥 Download Report (PDF)",
                data=pdf_buffer,
                file_name=f"NexGen_Logistics_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                mime="application/pdf"
            )
            st.success("✅ Report generated successfully!")
    
    st.markdown("---")
    st.markdown("#### 📊 Quick Stats Preview")
    
    quick_stats = pd.DataFrame({
        'Metric': ['Total Orders', 'On-Time Rate', 'Avg Cost', 'CO2 Emissions', 'Anomalies'],
        'Value': [
            int(filtered.shape[0]),
            f"{100*(1 - filtered['delayed_flag'].mean() if filtered['delayed_flag'].count()>0 else 0):.1f}%",
            f"₹{filtered['delivery_cost'].mean():.2f}",
            f"{filtered['co2_g_per_km_est'].sum()/1000:.1f} kg",
            int(filtered['is_anomaly'].sum())
        ]
    })
    
    st.dataframe(quick_stats, use_container_width=True, hide_index=True)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 About")
st.sidebar.info("""
**NexGen Logistics AI Platform**

Advanced predictive analytics for logistics optimization using machine learning, network analysis, and real-time insights.

Built with Streamlit, Plotly, and scikit-learn.
""")
