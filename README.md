# 🚀 NexGen Logistics AI Platform# NexGen Logistics — Predictive Delivery Optimizer (Prototype)



<div align="center">This repository contains a Streamlit prototype that demonstrates a Predictive Delivery Optimizer for NexGen Logistics.



**Advanced Predictive Intelligence for Modern Logistics**What you get:

- A Streamlit app (`app.py`) that loads the 7 CSVs in `./data/` and builds merged datasets.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)- If the real CSVs are missing, the app creates realistic synthetic data for demo purposes.

[![Streamlit](https://img.shields.io/badge/Streamlit-1.22%2B-FF4B4B)](https://streamlit.io/)- A simple RandomForest model to predict delivery delays and a rule-based recommendation engine for at-risk orders.

[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)- Visualizations (histogram, bar chart, scatter, feature importance) and filters.

- `generate_brief_pdf.py` script to generate a PDF innovation brief from the included markdown.

[Live Demo](#usage) • [Features](#-key-features) • [Installation](#-installation) • [Screenshots](#-screenshots)

How to run (Windows PowerShell):

</div>

1. Create a venv and install requirements

---

```powershell

## 📋 Overviewpython -m venv .venv

.\.venv\Scripts\Activate.ps1

NexGen Logistics AI Platform is a next-generation predictive delivery optimization system built with cutting-edge machine learning and interactive visualizations. This platform transforms logistics operations through:pip install -r requirements.txt

```

- **AI-Powered Predictions**: RandomForest ML models with 80%+ AUC for delay prediction

- **Network Intelligence**: Interactive graph visualization of route networks2. Run the Streamlit app

- **Anomaly Detection**: Automated identification of high-risk orders using Isolation Forest

- **Executive Reporting**: One-click PDF report generation with comprehensive analytics```powershell

- **Real-Time Dashboards**: Dynamic KPIs with custom filtering and drill-down capabilitiesstreamlit run app.py

```

## ✨ Key Features

3. (Optional) Place your CSVs in `./data/` with filenames:

### 🤖 Machine Learning & AI- orders.csv

- **Predictive Modeling**: RandomForest classifier trained on order, route, and performance data- delivery_performance.csv

- **Feature Importance Analysis**: Identifies key delay drivers (distance, traffic, weather, priority)- routes_distance.csv

- **Anomaly Detection**: Isolation Forest algorithm flags outlier orders requiring immediate attention- vehicle_fleet.csv

- **Risk Scoring**: Probability-based risk assessment for proactive intervention- warehouse_inventory.csv

- customer_feedback.csv

### 📊 Advanced Visualizations- cost_breakdown.csv

- **3D Scatter Analysis**: Multi-dimensional delay visualization with customizable axes

- **Network Graphs**: Interactive route network using NetworkX and PlotlyIf any are missing, the app will generate demo data.

- **Trend Analysis**: Time-series performance tracking with animated controls

- **Heatmaps & Charts**: Comprehensive visual analytics across all KPIsNotes & next steps:

- Replace rule-based recommendations with an optimization routine that trades off cost vs delay (e.g., linear programming).

### 📄 Reporting & Export- Add more features (carrier history, vehicle assignment, real GPS traces) to improve predictive power.

- **PDF Report Generation**: Professional executive reports with ReportLab- Build an Innovation Brief PDF using `generate_brief_pdf.py`.

- **CSV Exports**: Download high-risk orders and recommendations

- **Custom Styling**: Gradient headers, branded colors, and polished UILicense: MIT


### 🎨 User Experience
- **Custom CSS Styling**: Modern gradient design with purple/blue theme
- **Responsive Layout**: Wide layout optimized for large datasets
- **Interactive Filters**: Date range, priority, warehouse, carrier, anomaly toggles
- **Tabbed Interface**: Organized navigation (Analytics, AI Predictions, Network, Reports)

## 🛠️ Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Git (for cloning)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/ark5234/NexGen_assignment.git
cd NexGen_assignment

# Create virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The app will automatically launch at `http://localhost:8501`

## 📁 Project Structure

```
nexgen_logistics/
├── app.py                      # Main Streamlit application
├── utils.py                    # Data loading and preprocessing utilities
├── report_generator.py         # PDF report generation module
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore patterns
├── README.md                   # This file
├── Innovation_Brief.md         # Detailed project documentation
├── generate_brief_pdf.py       # PDF generator for innovation brief
└── data/                       # CSV datasets (auto-generated if missing)
    ├── orders.csv              # 200 order records
    ├── delivery_performance.csv # Delivery metrics and ratings
    ├── routes_distance.csv     # Route information and traffic data
    ├── vehicle_fleet.csv       # Fleet capacity and fuel efficiency
    ├── warehouse_inventory.csv # Stock levels by warehouse
    ├── customer_feedback.csv   # Customer ratings and feedback
    └── cost_breakdown.csv      # Detailed cost analysis
```

## 🎯 Usage

### 1. Launch the Application
```bash
streamlit run app.py
```

### 2. Explore the Tabs

**📈 Analytics Tab**
- View real-time KPIs (orders, on-time rate, costs, CO2 emissions)
- Analyze delivery performance trends
- Explore 3D/2D delay vs distance scatter plots
- Compare carrier performance benchmarks

**🤖 AI Predictions Tab**
- Train RandomForest model on historical data
- View model performance metrics (AUC score)
- Analyze feature importance
- Identify high-risk orders with recommended actions
- Export risk reports as CSV

**🗺️ Network Tab**
- Visualize logistics network graph
- See connections between warehouses and destinations
- Analyze top routes by volume
- Color-coded delay rates for quick insights

**📄 Reports Tab**
- Generate comprehensive PDF reports
- Preview key statistics
- Download executive summaries
- Share insights with stakeholders

### 3. Use Filters & Controls
- **Date Range**: Filter orders by date
- **Priority**: Select Express, Standard, or Economy
- **Origin**: Filter by warehouse location
- **Carrier**: Choose specific carriers
- **Anomalies**: Toggle to show only flagged orders
- **3D Controls**: Adjust opacity, size, and axes

## 🔑 Key Technologies

| Technology | Purpose | Version |
|------------|---------|---------|
| **Streamlit** | Web framework for dashboards | 1.22+ |
| **Pandas** | Data manipulation and analysis | 2.0+ |
| **NumPy** | Numerical computing | 1.25+ |
| **scikit-learn** | Machine learning models | 1.2+ |
| **Plotly** | Interactive visualizations | 5.0+ |
| **NetworkX** | Network graph analysis | 3.0+ |
| **ReportLab** | PDF report generation | 3.6+ |

## 🎨 Screenshots

### Dashboard Overview
![Dashboard](https://via.placeholder.com/800x400.png?text=NexGen+Logistics+Dashboard)

### 3D Visualization
![3D Viz](https://via.placeholder.com/800x400.png?text=3D+Delay+Analysis)

### Network Graph
![Network](https://via.placeholder.com/800x400.png?text=Logistics+Network)

## 🚀 Deployment

### Streamlit Cloud
1. Push to GitHub
2. Visit [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your repository
4. Deploy with one click

### Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Vikra**
- GitHub: [@ark5234](https://github.com/ark5234)
- Project: [NexGen Assignment](https://github.com/ark5234/NexGen_assignment)

## 🙏 Acknowledgments

- NexGen Logistics for the case study challenge
- Streamlit community for excellent documentation
- scikit-learn team for robust ML tools
- Plotly for beautiful interactive visualizations

---

<div align="center">
Made with ❤️ and ☕ by Vikra
</div>
