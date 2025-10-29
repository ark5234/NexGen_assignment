# NexGen Logistics — Predictive Delivery Optimizer

![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.50%2B-ff4b4b.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

NexGen Logistics is an AI-powered delivery optimization platform that combines predictive analytics, anomaly detection, and executive-ready reporting inside an interactive Streamlit experience. The prototype ships with synthetic yet realistic logistics data covering orders, routes, carriers, and customer feedback so teams can explore the workflow end-to-end.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Visual Analytics](#visual-analytics)
- [Data Sources](#data-sources)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technical Stack](#technical-stack)
- [Development Notes](#development-notes)
- [Future Enhancements](#future-enhancements)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contact](#contact)

## Overview

- Predict delay risk using machine learning models tuned on historical order, route, and performance data.
- Surface high-risk anomalies with Isolation Forest scoring so operations teams can intervene early.
- Provide decision-ready KPIs, plots, and exports for executives and analysts in a single page app.
- Generate polished PDF reports and CSV extracts in one click for stakeholder handoffs.

## Key Features

### Machine Learning & AI

- RandomForest classifier with 80%+ AUC on the demo data set for on-time delivery prediction.
- Isolation Forest anomaly scoring that ranks orders requiring additional review.
- Feature importance analysis highlighting distance, weather, priority, and other drivers.

### Visual Intelligence

- Delay vs Distance heatmap (default), average-delay column chart, stacked delivery mix, plus 2D and 3D scatter options for deeper dives.
- Carrier benchmarking, cost breakouts, route network visualizations, and trend analysis charts.
- Interactive filters for priority, carrier, warehouse, and time windows that update charts instantly.

### Executive Reporting

- PDF generator built with ReportLab that captures KPIs, route efficiency, carrier insights, and recommendations.
- CSV exports for high-risk orders and filtered datasets to share with downstream tools.

### User Experience

- Wide layout optimized for dashboard consumption with clear sections per workflow.
- Helpful info callouts embedded near visualizations to guide business stakeholders.
- Automatic synthetic data creation when source CSVs are missing, keeping the demo self-contained.

## Visual Analytics

- **Delay vs Distance (Heatmap)**: Aggregates trips into easy-to-read distance and delay bands; ideal for non-technical viewers. Darker cells indicate more orders in that range.
- **Delay vs Distance (Avg Delay Column)**: Shows the average delay per distance band for quick storytelling in executive meetings.
- **Delay vs Distance (Delivery Mix)**: Stacked bars contrasting on-time vs delayed orders to highlight riskier distance buckets.
- **Delay vs Distance (3D Scatter)**: Rotate to relate distance, delay, and a third metric such as order value or delivery cost.
- **Delay vs Distance (2D Scatter)**: Inspect individual orders with hover details and optional bubble sizing.
- **Additional Charts**: Delay distribution histogram, average cost by category, carrier performance comparisons, route network graph, anomaly highlights, and feature importance ranking.

**Need a simpler view?** Stick with the heatmap tab — it was added specifically for normal users who prefer grouped insights over individual scatter points.

## Data Sources

All datasets live in `data/` and are regenerated with realistic values if absent:

- `orders.csv`: Order metadata including customer segment, priority, and value.
- `delivery_performance.csv`: Promised vs actual delivery metrics, delays, and customer ratings.
- `routes_distance.csv`: Route distances, traffic, and weather influence.
- `vehicle_fleet.csv`: Fleet capacity, fuel efficiency, and maintenance context.
- `warehouse_inventory.csv`: Inventory levels per warehouse and product category.
- `customer_feedback.csv`: Ratings, feedback text, and resolution status.
- `cost_breakdown.csv`: Detailed cost components such as fuel, tolls, and labor.

## Installation

### Prerequisites

- Python 3.9 or newer
- `pip`
- (Optional) Git for cloning

### Quick Start

```powershell
# Clone the repository
git clone https://github.com/ark5234/NexGen_assignment.git
cd NexGen_assignment/nexgen_logistics

# Create and activate a virtual environment (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py
```

The dashboard opens at `http://localhost:8501`.

## Usage

1. Launch the app with `streamlit run app.py` from the `nexgen_logistics` folder.
2. Adjust filters on the sidebar (date range, priority, warehouse, carrier, anomaly toggle).
3. Review the KPI cards and scroll through the visualization blocks.
4. Explore the **Analytics**, **AI Predictions**, **Network**, and **Reports** sections using the tabs across the main app.
5. Download CSV risk reports or generate PDF briefs directly from the interface.

### Delay vs Distance Guidance

- **Heatmap tab**: Use when presenting to business stakeholders. It summarizes patterns into distance and delay ranges.
- **Avg Delay tab**: Share in weekly operations reviews to call out distance segments with rising average delays.
- **Delivery Mix tab**: Highlight where delayed orders concentrate so teams can prioritize interventions.
- **3D Scatter tab**: Pick a Z-axis metric and marker sizing for exploratory analysis.
- **2D Scatter tab**: Hover for per-order insights; ideal for operations teams investigating specific outliers.

## Project Structure

```text
nexgen_logistics/
├── app.py                # Streamlit entry point (dashboard UI and controls)
├── utils.py              # Data loading, cleaning, and synthetic data generation
├── report_generator.py   # PDF report builder
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation (this file)
└── data/                 # CSV datasets (auto-generated if missing)
```

## Technical Stack

| Component        | Technology      | Purpose                         |
|------------------|-----------------|---------------------------------|
| Web Framework    | Streamlit 1.50+ | Interactive dashboard UI        |
| Data Handling    | pandas, numpy   | ETL, feature engineering        |
| Machine Learning | scikit-learn    | RandomForest & Isolation Forest |
| Visualization    | Plotly, NetworkX| Charts and network diagrams     |
| Reporting        | ReportLab       | Executive PDF generation        |

## Development Notes

- Code is modular and leverages caching (`st.cache_data`) for rapid reloads.
- Synthetic data generation keeps demo environments reproducible across machines.
- Plotly configuration uses explicit numeric conversions to avoid runtime warnings.

## Future Enhancements

- Real-time ingestion from streaming sources (Kafka or cloud event hubs).
- Additional models (XGBoost, LightGBM) and hyperparameter search automation.
- Mobile-responsive layouts and multi-language localization.
- API endpoints for integration with external TMS/WMS platforms.

## Troubleshooting

- **`No module named streamlit`**: Ensure the virtual environment is activated before installing requirements.
- **`File does not exist: app.py`**: Run commands from `nexgen_logistics/`, not the repository root.
- **Execution policy error (Windows)**: Run PowerShell as Administrator and execute `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` once.
- **Plotly deprecated argument warnings**: Safe to ignore; visuals render correctly.

## License

Released under the MIT License. See the root repository for full text.

## Contact

- Repository: <https://github.com/ark5234/NexGen_assignment>
- Issues & feedback: Please open a GitHub issue.
- Status: Production-ready prototype (last updated October 2025)
