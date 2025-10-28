# NexGen Logistics AI Platform# NexGen Logistics AI Platform# NexGen Logistics AI Platform# 🚀 NexGen Logistics AI Platform# NexGen Logistics — Predictive Delivery Optimizer (Prototype)



Advanced Predictive Intelligence for Modern Logistics



![Python](https://img.shields.io/badge/python-3.9+-blue.svg)**Advanced Predictive Intelligence for Modern Logistics**

![Streamlit](https://img.shields.io/badge/streamlit-1.22+-red.svg)

![License](https://img.shields.io/badge/license-MIT-green.svg)



This repository contains a Streamlit prototype that demonstrates a Predictive Delivery Optimizer for NexGen Logistics.[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)**Advanced Predictive Intelligence for Modern Logistics**



## Overview[![Streamlit](https://img.shields.io/badge/Streamlit-1.22%2B-FF4B4B)](https://streamlit.io/)



NexGen Logistics AI Platform is a next-generation predictive delivery optimization system built with cutting-edge machine learning and interactive visualizations. This platform transforms logistics operations through:[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)



- **AI-Powered Predictions**: RandomForest ML models with 80%+ AUC for delay prediction

- **Network Intelligence**: Interactive graph visualization of route networks

- **Anomaly Detection**: Automated identification of high-risk orders using Isolation Forest---[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)<div align="center">This repository contains a Streamlit prototype that demonstrates a Predictive Delivery Optimizer for NexGen Logistics.

- **Executive Reporting**: One-click PDF generation with comprehensive analytics

- **Real-time Insights**: Dynamic filtering and what-if scenario analysis



## Features## Overview[![Streamlit](https://img.shields.io/badge/Streamlit-1.22%2B-FF4B4B)](https://streamlit.io/)



### Interactive Filters

- Date range, priority, carrier selection

- Product category and customer segment filteringNexGen Logistics AI Platform is a next-generation predictive delivery optimization system built with cutting-edge machine learning and interactive visualizations. This platform transforms logistics operations through:[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

- Real-time data updates



### 8+ Visualizations

- Delay distribution histograms- **AI-Powered Predictions**: RandomForest ML models with 80%+ AUC for delay prediction

- Priority-based cost analysis

- 3D scatter plots (Distance vs Delay vs Cost)- **Network Intelligence**: Interactive graph visualization of route networks

- Carrier performance bar charts

- Route network graphs- **Anomaly Detection**: Automated identification of high-risk orders using Isolation Forest---**Advanced Predictive Intelligence for Modern Logistics**What you get:

- Time-series trend analysis

- Anomaly detection plots- **Executive Reporting**: One-click PDF report generation with comprehensive analytics



### ML Predictions- **Real-Time Dashboards**: Dynamic KPIs with custom filtering and drill-down capabilities

- RandomForest classifier for delay prediction

- Feature importance analysis

- Model performance metrics (AUC, accuracy)

- Risk probability scoring## Key Features## Overview- A Streamlit app (`app.py`) that loads the 7 CSVs in `./data/` and builds merged datasets.



### Tabbed Interface

- Organized navigation across Analytics, Predictions, Network, and Reporting sections

- Order Inspector for detailed order analysis### Machine Learning & AI

- What-if scenario simulator



### Download Features

- PDF executive reports with KPIs, insights, and recommendations- **Predictive Modeling**: RandomForest classifier trained on order, route, and performance dataNexGen Logistics AI Platform is a next-generation predictive delivery optimization system built with cutting-edge machine learning and interactive visualizations. This platform transforms logistics operations through:[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)- If the real CSVs are missing, the app creates realistic synthetic data for demo purposes.

- CSV export for high-risk orders

- Comprehensive analytics in downloadable format- **Feature Importance Analysis**: Identifies key delay drivers (distance, traffic, weather, priority)



## Installation- **Anomaly Detection**: Isolation Forest algorithm flags outlier orders requiring immediate attention



### Prerequisites- **Risk Scoring**: Probability-based risk assessment for proactive intervention

- Python 3.9 or higher

- pip package manager- **AI-Powered Predictions**: RandomForest ML models with 80%+ AUC for delay prediction[![Streamlit](https://img.shields.io/badge/Streamlit-1.22%2B-FF4B4B)](https://streamlit.io/)- A simple RandomForest model to predict delivery delays and a rule-based recommendation engine for at-risk orders.



### Setup Instructions### Advanced Visualizations



1. Clone the repository:- **Network Intelligence**: Interactive graph visualization of route networks

```bash

git clone https://github.com/ark5234/NexGen_assignment.git- **3D Scatter Analysis**: Multi-dimensional delay visualization with customizable axes

cd NexGen_assignment

```- **Network Graphs**: Interactive route network using NetworkX and Plotly- **Anomaly Detection**: Automated identification of high-risk orders using Isolation Forest[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)- Visualizations (histogram, bar chart, scatter, feature importance) and filters.



2. Create and activate virtual environment:- **Trend Analysis**: Time-series performance tracking with animated controls

```bash

python -m venv .venv- **Heatmaps & Charts**: Comprehensive visual analytics across all KPIs- **Executive Reporting**: One-click PDF report generation with comprehensive analytics

.venv\Scripts\activate  # Windows

source .venv/bin/activate  # Linux/Mac

```

### Reporting & Export- **Real-Time Dashboards**: Dynamic KPIs with custom filtering and drill-down capabilities- `generate_brief_pdf.py` script to generate a PDF innovation brief from the included markdown.

3. Install dependencies:

```bash

pip install -r requirements.txt

```- **PDF Report Generation**: Professional executive reports with ReportLab



4. Run the application:- **CSV Exports**: Download high-risk orders and recommendations

```bash

streamlit run app.py- **Custom Styling**: Gradient headers, branded colors, and polished UI## Key Features[Live Demo](#usage) • [Features](#-key-features) • [Installation](#-installation) • [Screenshots](#-screenshots)

```



The app will automatically launch at `http://localhost:8501`

### User Experience

## Project Structure



```

nexgen_logistics/- **Custom CSS Styling**: Modern gradient design with purple/blue theme### Machine Learning & AIHow to run (Windows PowerShell):

├── app.py                    # Main Streamlit application

├── utils.py                  # Data loading and preprocessing utilities- **Responsive Layout**: Wide layout optimized for large datasets

├── report_generator.py       # PDF report generation module

├── requirements.txt          # Python dependencies- **Interactive Filters**: Date range, priority, warehouse, carrier, anomaly toggles- **Predictive Modeling**: RandomForest classifier trained on order, route, and performance data

├── .gitignore               # Git ignore patterns

├── README.md                # This file- **Tabbed Interface**: Organized navigation (Analytics, AI Predictions, Network, Reports)

└── data/                    # CSV datasets (auto-generated if missing)

    ├── orders.csv           # 200 order records- **Feature Importance Analysis**: Identifies key delay drivers (distance, traffic, weather, priority)</div>

    ├── delivery_performance.csv  # Delivery metrics and ratings

    ├── routes_distance.csv  # Route information and traffic data## Installation

    ├── vehicle_fleet.csv    # Fleet capacity and fuel efficiency

    ├── warehouse_inventory.csv  # Stock levels and turnover- **Anomaly Detection**: Isolation Forest algorithm flags outlier orders requiring immediate attention

    ├── customer_feedback.csv    # Ratings and feedback

    └── cost_breakdown.csv   # Detailed cost components### Prerequisites

```

- **Risk Scoring**: Probability-based risk assessment for proactive intervention1. Create a venv and install requirements

## User Experience

- Python 3.9 or higher

### Custom CSS Styling

- Modern gradient design with purple/blue theme- pip package manager

- Responsive layout with optimized spacing

- Professional typography and color scheme- Git (for cloning)



### Interactive Controls### Advanced Visualizations---

- Date pickers with calendar interface

- Multi-select dropdowns for filters### Quick Start

- Sliders for distance-based filtering

- Toggle buttons for display options- **3D Scatter Analysis**: Multi-dimensional delay visualization with customizable axes



### Performance Metrics```bash

- Cached data loading for faster response

- Efficient data processing with pandas# Clone the repository- **Network Graphs**: Interactive route network using NetworkX and Plotly```powershell

- Optimized visualizations with plotly

git clone https://github.com/ark5234/NexGen_assignment.git

## Technical Stack

cd NexGen_assignment- **Trend Analysis**: Time-series performance tracking with animated controls

- **Frontend**: Streamlit 1.22+

- **Data Processing**: pandas, numpy

- **Machine Learning**: scikit-learn (RandomForest, IsolationForest)

- **Visualization**: plotly, networkx# Create virtual environment (recommended)- **Heatmaps & Charts**: Comprehensive visual analytics across all KPIs## 📋 Overviewpython -m venv .venv

- **Reporting**: reportlab

- **Language**: Python 3.9+python -m venv .venv



## Requirements Compliance



### Dataset Coverage# Activate virtual environment

- Orders: 200 records with customer segments, priorities, categories

- Delivery Performance: On-time rates, delays, quality metrics.venv\Scripts\activate  # Windows### Reporting & Export.\.venv\Scripts\Activate.ps1

- Routes & Distance: Geographic data, traffic patterns, weather impact

- Vehicle Fleet: Capacity, fuel efficiency, maintenance schedulessource .venv/bin/activate  # Linux/Mac

- Warehouse Inventory: Stock levels, turnover rates, availability

- Customer Feedback: Ratings, recommendations, issue categories- **PDF Report Generation**: Professional executive reports with ReportLab

- Cost Breakdown: Multi-component cost analysis (fuel, labor, tolls, etc.)

# Install dependencies

### Visualization Requirements

- 8+ interactive charts and graphspip install -r requirements.txt- **CSV Exports**: Download high-risk orders and recommendationsNexGen Logistics AI Platform is a next-generation predictive delivery optimization system built with cutting-edge machine learning and interactive visualizations. This platform transforms logistics operations through:pip install -r requirements.txt

- 3D scatter plots for multi-dimensional analysis

- Network graphs for route visualization

- Time-series trend analysis

- Custom styling with gradient themes# Run the application- **Custom Styling**: Gradient headers, branded colors, and polished UI



### Predictive Modelsstreamlit run app.py

- RandomForest classifier with hyperparameter tuning

- Isolation Forest for anomaly detection``````

- Feature importance ranking

- Risk scoring and probability estimates



### Download CapabilitiesThe app will automatically launch at `http://localhost:8501`### User Experience

- PDF reports with executive summary, KPIs, carrier analysis, route efficiency, priority breakdowns, high-risk orders, environmental impact, cost analysis, insights, recommendations, and action items

- CSV exports for filtered data

- Comprehensive analytics in portable formats

## Project Structure- **Custom CSS Styling**: Modern gradient design with purple/blue theme- **AI-Powered Predictions**: RandomForest ML models with 80%+ AUC for delay prediction

## Development



### Code Organization

- Modular design with separate utilities```- **Responsive Layout**: Wide layout optimized for large datasets

- Clean separation of concerns

- Type hints and documentationnexgen_logistics/

- Production-ready code without comments

├── app.py                      # Main Streamlit application- **Interactive Filters**: Date range, priority, warehouse, carrier, anomaly toggles- **Network Intelligence**: Interactive graph visualization of route networks2. Run the Streamlit app

### Data Generation

If CSV files are missing, synthetic data is automatically generated with realistic distributions and relationships.├── utils.py                    # Data loading and preprocessing utilities



### Git Integration├── report_generator.py         # PDF report generation module- **Tabbed Interface**: Organized navigation (Analytics, AI Predictions, Network, Reports)

Version controlled with comprehensive commit history documenting all features and fixes.

├── requirements.txt            # Python dependencies

## Future Enhancements

├── .gitignore                  # Git ignore patterns- **Anomaly Detection**: Automated identification of high-risk orders using Isolation Forest

- Real-time data streaming integration

- Advanced ML models (XGBoost, Neural Networks)├── README.md                   # This file

- Mobile-responsive design

- Multi-language support└── data/                       # CSV datasets (auto-generated if missing)## Installation

- API endpoints for external integration

- Cloud deployment (AWS/GCP/Azure)    ├── orders.csv              # 200 order records



## License    ├── delivery_performance.csv # Delivery metrics and ratings- **Executive Reporting**: One-click PDF report generation with comprehensive analytics```powershell



MIT License - See LICENSE file for details    ├── routes_distance.csv     # Route information and traffic data



## Contact    ├── vehicle_fleet.csv       # Fleet capacity and fuel efficiency### Prerequisites



For questions or feedback, please open an issue on the GitHub repository.    ├── warehouse_inventory.csv # Stock levels by warehouse



---    ├── customer_feedback.csv   # Customer ratings and feedback- Python 3.9 or higher- **Real-Time Dashboards**: Dynamic KPIs with custom filtering and drill-down capabilitiesstreamlit run app.py



**Repository**: https://github.com/ark5234/NexGen_assignment.git    └── cost_breakdown.csv      # Detailed cost analysis



**Status**: Production-ready prototype```- pip package manager



**Last Updated**: October 2025


## Usage- Git (for cloning)```



### 1. Launch the Application



```bash### Quick Start## ✨ Key Features

streamlit run app.py

```



### 2. Explore the Tabs```bash3. (Optional) Place your CSVs in `./data/` with filenames:



**Analytics Tab**# Clone the repository

- View real-time KPIs (orders, on-time rate, costs, CO2 emissions)

- Analyze delivery performance trendsgit clone https://github.com/ark5234/NexGen_assignment.git### 🤖 Machine Learning & AI- orders.csv

- Explore 3D/2D delay vs distance scatter plots

- Compare carrier performance benchmarkscd NexGen_assignment



**AI Predictions Tab**- **Predictive Modeling**: RandomForest classifier trained on order, route, and performance data- delivery_performance.csv

- Train RandomForest model on historical data

- View model performance metrics (AUC score)# Create virtual environment (recommended)

- Analyze feature importance

- Identify high-risk orders with recommended actionspython -m venv .venv- **Feature Importance Analysis**: Identifies key delay drivers (distance, traffic, weather, priority)- routes_distance.csv

- Export risk reports as CSV



**Network Tab**

- Visualize logistics network graph# Activate virtual environment- **Anomaly Detection**: Isolation Forest algorithm flags outlier orders requiring immediate attention- vehicle_fleet.csv

- See connections between warehouses and destinations

- Analyze top routes by volume.venv\Scripts\activate  # Windows

- Color-coded delay rates for quick insights

source .venv/bin/activate  # Linux/Mac- **Risk Scoring**: Probability-based risk assessment for proactive intervention- warehouse_inventory.csv

**Reports Tab**

- Generate comprehensive PDF reports

- Preview key statistics

- Download executive summaries# Install dependencies- customer_feedback.csv

- Share insights with stakeholders

pip install -r requirements.txt

### 3. Use Filters & Controls

### 📊 Advanced Visualizations- cost_breakdown.csv

- **Date Range**: Filter orders by date

- **Priority**: Select Express, Standard, or Economy# Run the application

- **Origin**: Filter by warehouse location

- **Carrier**: Choose specific carriersstreamlit run app.py- **3D Scatter Analysis**: Multi-dimensional delay visualization with customizable axes

- **Anomalies**: Toggle to show only flagged orders

- **3D Controls**: Adjust opacity, size, and axes```



## Key Technologies- **Network Graphs**: Interactive route network using NetworkX and PlotlyIf any are missing, the app will generate demo data.



| Technology | Purpose | Version |The app will automatically launch at `http://localhost:8501`

|------------|---------|---------|

| **Streamlit** | Web framework for dashboards | 1.22+ |- **Trend Analysis**: Time-series performance tracking with animated controls

| **Pandas** | Data manipulation and analysis | 2.0+ |

| **NumPy** | Numerical computing | 1.25+ |## Project Structure

| **scikit-learn** | Machine learning models | 1.2+ |

| **Plotly** | Interactive visualizations | 5.0+ |- **Heatmaps & Charts**: Comprehensive visual analytics across all KPIsNotes & next steps:

| **NetworkX** | Network graph analysis | 3.0+ |

| **ReportLab** | PDF report generation | 3.6+ |```



## Requirements Compliancenexgen_logistics/- Replace rule-based recommendations with an optimization routine that trades off cost vs delay (e.g., linear programming).



### Python and Streamlit├── app.py                      # Main Streamlit application

- All data processing and analysis uses Python

- Interactive web application built using Streamlit├── utils.py                    # Data loading and preprocessing utilities### 📄 Reporting & Export- Add more features (carrier history, vehicle assignment, real GPS traces) to improve predictive power.

- Application runs locally with: `streamlit run app.py`

├── report_generator.py         # PDF report generation module

### Data Analysis

- Loads and analyzes 7 different datasets├── requirements.txt            # Python dependencies- **PDF Report Generation**: Professional executive reports with ReportLab- Build an Innovation Brief PDF using `generate_brief_pdf.py`.

- Performs meaningful calculations (delay metrics, cost per km, CO2 estimates)

- Handles missing data with appropriate fallbacks and synthetic generation├── .gitignore                  # Git ignore patterns

- Creates derived metrics (delay_days, cost_per_km, co2_g_per_km_est, delay_flag)

├── README.md                   # This file- **CSV Exports**: Download high-risk orders and recommendations

### Visualization

- Includes 8+ different chart types:├── generate_brief_pdf.py       # PDF generator for innovation brief

  1. Delivery Performance Trend (Line chart with fill)

  2. Cost Distribution by Category (Bar chart)└── data/                       # CSV datasets (auto-generated if missing)- **Custom Styling**: Gradient headers, branded colors, and polished UILicense: MIT

  3. 3D Scatter Plot (Distance vs Delay vs Custom Z-axis)

  4. 2D Scatter Plot (Distance vs Delay with size)    ├── orders.csv              # 200 order records

  5. Carrier Performance Benchmark (Horizontal bar chart)

  6. Network Graph (Interactive node-edge visualization)    ├── delivery_performance.csv # Delivery metrics and ratings

  7. Top Routes by Volume (Horizontal bar with color scale)

  8. Feature Importance (Bar chart)    ├── routes_distance.csv     # Route information and traffic data### 🎨 User Experience

- All visualizations are interactive using Plotly

- Appropriate chart types for each data presentation    ├── vehicle_fleet.csv       # Fleet capacity and fuel efficiency- **Custom CSS Styling**: Modern gradient design with purple/blue theme



### Interactivity    ├── warehouse_inventory.csv # Stock levels by warehouse- **Responsive Layout**: Wide layout optimized for large datasets

- Filters: Date range, priority, warehouse, carrier, anomaly toggle

- Dashboard responds dynamically to all user choices    ├── customer_feedback.csv   # Customer ratings and feedback- **Interactive Filters**: Date range, priority, warehouse, carrier, anomaly toggles

- Download functionality:

  - CSV export for high-risk orders (in AI Predictions tab)    └── cost_breakdown.csv      # Detailed cost analysis- **Tabbed Interface**: Organized navigation (Analytics, AI Predictions, Network, Reports)

  - PDF report generation with download button (in Reports tab)

```

### Code Quality

- Well-organized modular structure (app.py, utils.py, report_generator.py)## 🛠️ Installation

- Readable code with clear function names

- Documentation in README and inline where needed## Usage

- Error handling for missing files, parsing errors, edge cases

- Efficient processing with caching (@st.cache_data)### Prerequisites



## Download Features### Launch the Application- Python 3.9 or higher



### CSV Export (AI Predictions Tab)```bash- pip package manager

- Located in the **AI Predictions** tab

- After model training, view high-risk orders tablestreamlit run app.py- Git (for cloning)

- Click "Download Risk Report (CSV)" button to export the analysis

```

### PDF Report (Reports Tab)

- Navigate to the **Reports** tab### Quick Start

- Click "Generate PDF Report" button

- A success message will appear### Explore the Tabs

- Click "Download Report (PDF)" button to save the executive report

- Report includes: KPIs, insights, recommendations, and priority statistics```bash



## Deployment#### Analytics Tab# Clone the repository



### Streamlit Cloud- View real-time KPIs (orders, on-time rate, costs, CO2 emissions)git clone https://github.com/ark5234/NexGen_assignment.git

1. Push to GitHub

2. Visit [streamlit.io/cloud](https://streamlit.io/cloud)- Analyze delivery performance trendscd NexGen_assignment

3. Connect your repository

4. Deploy with one click- Explore 3D/2D delay vs distance scatter plots



### Docker- Compare carrier performance benchmarks# Create virtual environment (recommended)



```dockerfilepython -m venv .venv

FROM python:3.9-slim

WORKDIR /app#### AI Predictions Tab.venv\Scripts\activate  # Windows

COPY requirements.txt .

RUN pip install -r requirements.txt- Train RandomForest model on historical datasource .venv/bin/activate  # Linux/Mac

COPY . .

CMD ["streamlit", "run", "app.py"]- View model performance metrics (AUC score)

```

- Analyze feature importance# Install dependencies

## Contributing

- Identify high-risk orders with recommended actionspip install -r requirements.txt

Contributions are welcome! Please feel free to submit a Pull Request.

- Export risk reports as CSV

1. Fork the repository

2. Create your feature branch (`git checkout -b feature/AmazingFeature`)# Run the application

3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)

4. Push to the branch (`git push origin feature/AmazingFeature`)#### Network Tabstreamlit run app.py

5. Open a Pull Request

- Visualize logistics network graph```

## License

- See connections between warehouses and destinations

This project is licensed under the MIT License - see the LICENSE file for details.

- Analyze top routes by volumeThe app will automatically launch at `http://localhost:8501`

## Author

- Color-coded delay rates for quick insights

**Vikra**

- GitHub: [@ark5234](https://github.com/ark5234)## 📁 Project Structure

- Project: [NexGen Assignment](https://github.com/ark5234/NexGen_assignment)

#### Reports Tab

## Acknowledgments

- Generate comprehensive PDF reports```

- NexGen Logistics for the case study challenge

- Streamlit community for excellent documentation- Preview key statisticsnexgen_logistics/

- scikit-learn team for robust ML tools

- Plotly for beautiful interactive visualizations- Download executive summaries├── app.py                      # Main Streamlit application



---- Share insights with stakeholders├── utils.py                    # Data loading and preprocessing utilities



Made with dedication by Vikra├── report_generator.py         # PDF report generation module


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
