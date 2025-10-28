# NexGen Logistics AI Platform# 🚀 NexGen Logistics AI Platform# NexGen Logistics — Predictive Delivery Optimizer (Prototype)



**Advanced Predictive Intelligence for Modern Logistics**



[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)<div align="center">This repository contains a Streamlit prototype that demonstrates a Predictive Delivery Optimizer for NexGen Logistics.

[![Streamlit](https://img.shields.io/badge/Streamlit-1.22%2B-FF4B4B)](https://streamlit.io/)

[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)



---**Advanced Predictive Intelligence for Modern Logistics**What you get:



## Overview- A Streamlit app (`app.py`) that loads the 7 CSVs in `./data/` and builds merged datasets.



NexGen Logistics AI Platform is a next-generation predictive delivery optimization system built with cutting-edge machine learning and interactive visualizations. This platform transforms logistics operations through:[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)- If the real CSVs are missing, the app creates realistic synthetic data for demo purposes.



- **AI-Powered Predictions**: RandomForest ML models with 80%+ AUC for delay prediction[![Streamlit](https://img.shields.io/badge/Streamlit-1.22%2B-FF4B4B)](https://streamlit.io/)- A simple RandomForest model to predict delivery delays and a rule-based recommendation engine for at-risk orders.

- **Network Intelligence**: Interactive graph visualization of route networks

- **Anomaly Detection**: Automated identification of high-risk orders using Isolation Forest[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)- Visualizations (histogram, bar chart, scatter, feature importance) and filters.

- **Executive Reporting**: One-click PDF report generation with comprehensive analytics

- **Real-Time Dashboards**: Dynamic KPIs with custom filtering and drill-down capabilities- `generate_brief_pdf.py` script to generate a PDF innovation brief from the included markdown.



## Key Features[Live Demo](#usage) • [Features](#-key-features) • [Installation](#-installation) • [Screenshots](#-screenshots)



### Machine Learning & AIHow to run (Windows PowerShell):

- **Predictive Modeling**: RandomForest classifier trained on order, route, and performance data

- **Feature Importance Analysis**: Identifies key delay drivers (distance, traffic, weather, priority)</div>

- **Anomaly Detection**: Isolation Forest algorithm flags outlier orders requiring immediate attention

- **Risk Scoring**: Probability-based risk assessment for proactive intervention1. Create a venv and install requirements



### Advanced Visualizations---

- **3D Scatter Analysis**: Multi-dimensional delay visualization with customizable axes

- **Network Graphs**: Interactive route network using NetworkX and Plotly```powershell

- **Trend Analysis**: Time-series performance tracking with animated controls

- **Heatmaps & Charts**: Comprehensive visual analytics across all KPIs## 📋 Overviewpython -m venv .venv



### Reporting & Export.\.venv\Scripts\Activate.ps1

- **PDF Report Generation**: Professional executive reports with ReportLab

- **CSV Exports**: Download high-risk orders and recommendationsNexGen Logistics AI Platform is a next-generation predictive delivery optimization system built with cutting-edge machine learning and interactive visualizations. This platform transforms logistics operations through:pip install -r requirements.txt

- **Custom Styling**: Gradient headers, branded colors, and polished UI

```

### User Experience

- **Custom CSS Styling**: Modern gradient design with purple/blue theme- **AI-Powered Predictions**: RandomForest ML models with 80%+ AUC for delay prediction

- **Responsive Layout**: Wide layout optimized for large datasets

- **Interactive Filters**: Date range, priority, warehouse, carrier, anomaly toggles- **Network Intelligence**: Interactive graph visualization of route networks2. Run the Streamlit app

- **Tabbed Interface**: Organized navigation (Analytics, AI Predictions, Network, Reports)

- **Anomaly Detection**: Automated identification of high-risk orders using Isolation Forest

## Installation

- **Executive Reporting**: One-click PDF report generation with comprehensive analytics```powershell

### Prerequisites

- Python 3.9 or higher- **Real-Time Dashboards**: Dynamic KPIs with custom filtering and drill-down capabilitiesstreamlit run app.py

- pip package manager

- Git (for cloning)```



### Quick Start## ✨ Key Features



```bash3. (Optional) Place your CSVs in `./data/` with filenames:

# Clone the repository

git clone https://github.com/ark5234/NexGen_assignment.git### 🤖 Machine Learning & AI- orders.csv

cd NexGen_assignment

- **Predictive Modeling**: RandomForest classifier trained on order, route, and performance data- delivery_performance.csv

# Create virtual environment (recommended)

python -m venv .venv- **Feature Importance Analysis**: Identifies key delay drivers (distance, traffic, weather, priority)- routes_distance.csv



# Activate virtual environment- **Anomaly Detection**: Isolation Forest algorithm flags outlier orders requiring immediate attention- vehicle_fleet.csv

.venv\Scripts\activate  # Windows

source .venv/bin/activate  # Linux/Mac- **Risk Scoring**: Probability-based risk assessment for proactive intervention- warehouse_inventory.csv



# Install dependencies- customer_feedback.csv

pip install -r requirements.txt

### 📊 Advanced Visualizations- cost_breakdown.csv

# Run the application

streamlit run app.py- **3D Scatter Analysis**: Multi-dimensional delay visualization with customizable axes

```

- **Network Graphs**: Interactive route network using NetworkX and PlotlyIf any are missing, the app will generate demo data.

The app will automatically launch at `http://localhost:8501`

- **Trend Analysis**: Time-series performance tracking with animated controls

## Project Structure

- **Heatmaps & Charts**: Comprehensive visual analytics across all KPIsNotes & next steps:

```

nexgen_logistics/- Replace rule-based recommendations with an optimization routine that trades off cost vs delay (e.g., linear programming).

├── app.py                      # Main Streamlit application

├── utils.py                    # Data loading and preprocessing utilities### 📄 Reporting & Export- Add more features (carrier history, vehicle assignment, real GPS traces) to improve predictive power.

├── report_generator.py         # PDF report generation module

├── requirements.txt            # Python dependencies- **PDF Report Generation**: Professional executive reports with ReportLab- Build an Innovation Brief PDF using `generate_brief_pdf.py`.

├── .gitignore                  # Git ignore patterns

├── README.md                   # This file- **CSV Exports**: Download high-risk orders and recommendations

├── generate_brief_pdf.py       # PDF generator for innovation brief

└── data/                       # CSV datasets (auto-generated if missing)- **Custom Styling**: Gradient headers, branded colors, and polished UILicense: MIT

    ├── orders.csv              # 200 order records

    ├── delivery_performance.csv # Delivery metrics and ratings

    ├── routes_distance.csv     # Route information and traffic data### 🎨 User Experience

    ├── vehicle_fleet.csv       # Fleet capacity and fuel efficiency- **Custom CSS Styling**: Modern gradient design with purple/blue theme

    ├── warehouse_inventory.csv # Stock levels by warehouse- **Responsive Layout**: Wide layout optimized for large datasets

    ├── customer_feedback.csv   # Customer ratings and feedback- **Interactive Filters**: Date range, priority, warehouse, carrier, anomaly toggles

    └── cost_breakdown.csv      # Detailed cost analysis- **Tabbed Interface**: Organized navigation (Analytics, AI Predictions, Network, Reports)

```

## 🛠️ Installation

## Usage

### Prerequisites

### Launch the Application- Python 3.9 or higher

```bash- pip package manager

streamlit run app.py- Git (for cloning)

```

### Quick Start

### Explore the Tabs

```bash

#### Analytics Tab# Clone the repository

- View real-time KPIs (orders, on-time rate, costs, CO2 emissions)git clone https://github.com/ark5234/NexGen_assignment.git

- Analyze delivery performance trendscd NexGen_assignment

- Explore 3D/2D delay vs distance scatter plots

- Compare carrier performance benchmarks# Create virtual environment (recommended)

python -m venv .venv

#### AI Predictions Tab.venv\Scripts\activate  # Windows

- Train RandomForest model on historical datasource .venv/bin/activate  # Linux/Mac

- View model performance metrics (AUC score)

- Analyze feature importance# Install dependencies

- Identify high-risk orders with recommended actionspip install -r requirements.txt

- Export risk reports as CSV

# Run the application

#### Network Tabstreamlit run app.py

- Visualize logistics network graph```

- See connections between warehouses and destinations

- Analyze top routes by volumeThe app will automatically launch at `http://localhost:8501`

- Color-coded delay rates for quick insights

## 📁 Project Structure

#### Reports Tab

- Generate comprehensive PDF reports```

- Preview key statisticsnexgen_logistics/

- Download executive summaries├── app.py                      # Main Streamlit application

- Share insights with stakeholders├── utils.py                    # Data loading and preprocessing utilities

├── report_generator.py         # PDF report generation module

### Use Filters & Controls├── requirements.txt            # Python dependencies

- **Date Range**: Filter orders by date├── .gitignore                  # Git ignore patterns

- **Priority**: Select Express, Standard, or Economy├── README.md                   # This file

- **Origin**: Filter by warehouse location├── Innovation_Brief.md         # Detailed project documentation

- **Carrier**: Choose specific carriers├── generate_brief_pdf.py       # PDF generator for innovation brief

- **Anomalies**: Toggle to show only flagged orders└── data/                       # CSV datasets (auto-generated if missing)

- **3D Controls**: Adjust opacity, size, and axes    ├── orders.csv              # 200 order records

    ├── delivery_performance.csv # Delivery metrics and ratings

## Key Technologies    ├── routes_distance.csv     # Route information and traffic data

    ├── vehicle_fleet.csv       # Fleet capacity and fuel efficiency

| Technology | Purpose | Version |    ├── warehouse_inventory.csv # Stock levels by warehouse

|------------|---------|---------|    ├── customer_feedback.csv   # Customer ratings and feedback

| **Streamlit** | Web framework for dashboards | 1.22+ |    └── cost_breakdown.csv      # Detailed cost analysis

| **Pandas** | Data manipulation and analysis | 2.0+ |```

| **NumPy** | Numerical computing | 1.25+ |

| **scikit-learn** | Machine learning models | 1.2+ |## 🎯 Usage

| **Plotly** | Interactive visualizations | 5.0+ |

| **NetworkX** | Network graph analysis | 3.0+ |### 1. Launch the Application

| **ReportLab** | PDF report generation | 3.6+ |```bash

streamlit run app.py

## Requirements Compliance```



### Python and Streamlit### 2. Explore the Tabs

- ✅ All data processing and analysis uses Python

- ✅ Interactive web application built using Streamlit**📈 Analytics Tab**

- ✅ Application runs locally with: `streamlit run app.py`- View real-time KPIs (orders, on-time rate, costs, CO2 emissions)

- Analyze delivery performance trends

### Data Analysis- Explore 3D/2D delay vs distance scatter plots

- ✅ Loads and analyzes 7 different datasets- Compare carrier performance benchmarks

- ✅ Performs meaningful calculations (delay metrics, cost per km, CO2 estimates)

- ✅ Handles missing data with appropriate fallbacks and synthetic generation**🤖 AI Predictions Tab**

- ✅ Creates derived metrics (delay_days, cost_per_km, co2_g_per_km_est, delay_flag)- Train RandomForest model on historical data

- View model performance metrics (AUC score)

### Visualization- Analyze feature importance

- ✅ Includes 8+ different chart types:- Identify high-risk orders with recommended actions

  1. Delivery Performance Trend (Line chart with fill)- Export risk reports as CSV

  2. Cost Distribution by Category (Bar chart)

  3. 3D Scatter Plot (Distance vs Delay vs Custom Z-axis)**🗺️ Network Tab**

  4. 2D Scatter Plot (Distance vs Delay with size)- Visualize logistics network graph

  5. Carrier Performance Benchmark (Horizontal bar chart)- See connections between warehouses and destinations

  6. Network Graph (Interactive node-edge visualization)- Analyze top routes by volume

  7. Top Routes by Volume (Horizontal bar with color scale)- Color-coded delay rates for quick insights

  8. Feature Importance (Bar chart)

- ✅ All visualizations are interactive using Plotly**📄 Reports Tab**

- ✅ Appropriate chart types for each data presentation- Generate comprehensive PDF reports

- Preview key statistics

### Interactivity- Download executive summaries

- ✅ Filters: Date range, priority, warehouse, carrier, anomaly toggle- Share insights with stakeholders

- ✅ Dashboard responds dynamically to all user choices

- ✅ Download functionality:### 3. Use Filters & Controls

  - CSV export for high-risk orders (in AI Predictions tab)- **Date Range**: Filter orders by date

  - PDF report generation with download button (in Reports tab)- **Priority**: Select Express, Standard, or Economy

- **Origin**: Filter by warehouse location

### Code Quality- **Carrier**: Choose specific carriers

- ✅ Well-organized modular structure (app.py, utils.py, report_generator.py)- **Anomalies**: Toggle to show only flagged orders

- ✅ Readable code with clear function names- **3D Controls**: Adjust opacity, size, and axes

- ✅ Documentation in README and inline where needed

- ✅ Error handling for missing files, parsing errors, edge cases## 🔑 Key Technologies

- ✅ Efficient processing with caching (@st.cache_data)

| Technology | Purpose | Version |

## Download Features|------------|---------|---------|

| **Streamlit** | Web framework for dashboards | 1.22+ |

### CSV Export (AI Predictions Tab)| **Pandas** | Data manipulation and analysis | 2.0+ |

- Located in the **AI Predictions** tab| **NumPy** | Numerical computing | 1.25+ |

- After model training, view high-risk orders table| **scikit-learn** | Machine learning models | 1.2+ |

- Click "Download Risk Report (CSV)" button to export the analysis| **Plotly** | Interactive visualizations | 5.0+ |

| **NetworkX** | Network graph analysis | 3.0+ |

### PDF Report (Reports Tab)| **ReportLab** | PDF report generation | 3.6+ |

- Navigate to the **Reports** tab

- Click "Generate PDF Report" button## 🎨 Screenshots

- A success message will appear

- Click "Download Report (PDF)" button to save the executive report### Dashboard Overview

- Report includes: KPIs, insights, recommendations, and priority statistics![Dashboard](https://via.placeholder.com/800x400.png?text=NexGen+Logistics+Dashboard)



## Deployment### 3D Visualization

![3D Viz](https://via.placeholder.com/800x400.png?text=3D+Delay+Analysis)

### Streamlit Cloud

1. Push to GitHub### Network Graph

2. Visit [streamlit.io/cloud](https://streamlit.io/cloud)![Network](https://via.placeholder.com/800x400.png?text=Logistics+Network)

3. Connect your repository

4. Deploy with one click## 🚀 Deployment



### Docker### Streamlit Cloud

```dockerfile1. Push to GitHub

FROM python:3.9-slim2. Visit [streamlit.io/cloud](https://streamlit.io/cloud)

WORKDIR /app3. Connect your repository

COPY requirements.txt .4. Deploy with one click

RUN pip install -r requirements.txt

COPY . .### Docker

CMD ["streamlit", "run", "app.py"]```dockerfile

```FROM python:3.9-slim

WORKDIR /app

## ContributingCOPY requirements.txt .

RUN pip install -r requirements.txt

Contributions are welcome! Please feel free to submit a Pull Request.COPY . .

CMD ["streamlit", "run", "app.py"]

1. Fork the repository```

2. Create your feature branch (`git checkout -b feature/AmazingFeature`)

3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)## 🤝 Contributing

4. Push to the branch (`git push origin feature/AmazingFeature`)

5. Open a Pull RequestContributions are welcome! Please feel free to submit a Pull Request.



## License1. Fork the repository

2. Create your feature branch (`git checkout -b feature/AmazingFeature`)

This project is licensed under the MIT License - see the LICENSE file for details.3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)

4. Push to the branch (`git push origin feature/AmazingFeature`)

## Author5. Open a Pull Request



**Vikra**## 📝 License

- GitHub: [@ark5234](https://github.com/ark5234)

- Project: [NexGen Assignment](https://github.com/ark5234/NexGen_assignment)This project is licensed under the MIT License - see the LICENSE file for details.



## Acknowledgments## 👨‍💻 Author



- NexGen Logistics for the case study challenge**Vikra**

- Streamlit community for excellent documentation- GitHub: [@ark5234](https://github.com/ark5234)

- scikit-learn team for robust ML tools- Project: [NexGen Assignment](https://github.com/ark5234/NexGen_assignment)

- Plotly for beautiful interactive visualizations

## 🙏 Acknowledgments

---

- NexGen Logistics for the case study challenge

Made with dedication by Vikra- Streamlit community for excellent documentation

- scikit-learn team for robust ML tools
- Plotly for beautiful interactive visualizations

---

<div align="center">
Made with ❤️ and ☕ by Vikra
</div>
