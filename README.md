# NexGen Logistics — Predictive Delivery Optimizer (Prototype)

This repository contains a Streamlit prototype that demonstrates a Predictive Delivery Optimizer for NexGen Logistics.

What you get:
- A Streamlit app (`app.py`) that loads the 7 CSVs in `./data/` and builds merged datasets.
- If the real CSVs are missing, the app creates realistic synthetic data for demo purposes.
- A simple RandomForest model to predict delivery delays and a rule-based recommendation engine for at-risk orders.
- Visualizations (histogram, bar chart, scatter, feature importance) and filters.
- `generate_brief_pdf.py` script to generate a PDF innovation brief from the included markdown.

How to run (Windows PowerShell):

1. Create a venv and install requirements

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run the Streamlit app

```powershell
streamlit run app.py
```

3. (Optional) Place your CSVs in `./data/` with filenames:
- orders.csv
- delivery_performance.csv
- routes_distance.csv
- vehicle_fleet.csv
- warehouse_inventory.csv
- customer_feedback.csv
- cost_breakdown.csv

If any are missing, the app will generate demo data.

Notes & next steps:
- Replace rule-based recommendations with an optimization routine that trades off cost vs delay (e.g., linear programming).
- Add more features (carrier history, vehicle assignment, real GPS traces) to improve predictive power.
- Build an Innovation Brief PDF using `generate_brief_pdf.py`.

License: MIT
