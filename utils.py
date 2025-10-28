import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def ensure_data_dir(path="data"):
    os.makedirs(path, exist_ok=True)
    return path


def csv_exists(path, name):
    return os.path.isfile(os.path.join(path, name))


def generate_synthetic_data(path="data"):
    """Generate synthetic datasets matching the problem description and save to CSVs in `path`.
    This allows the prototype app to run even without the real datasets.
    """
    ensure_data_dir(path)
    rng = np.random.default_rng(42)

    # orders.csv (200 records)
    n_orders = 200
    base_date = datetime.today() - timedelta(days=90)
    order_ids = [f"ORD{1000+i}" for i in range(n_orders)]
    dates = [base_date + timedelta(days=int(x)) for x in rng.integers(0, 90, n_orders)]
    customer_segments = rng.choice(["Enterprise", "SMB", "Individual"], size=n_orders, p=[0.2, 0.5, 0.3])
    priorities = rng.choice(["Express", "Standard", "Economy"], size=n_orders, p=[0.2, 0.6, 0.2])
    categories = rng.choice(["Electronics", "Fashion", "Food", "Healthcare", "Industrial", "Books", "Home"], size=n_orders)
    order_values = np.round(rng.uniform(50, 5000, n_orders), 2)
    origins = rng.choice(["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"], size=n_orders)
    destinations = rng.choice(["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Singapore", "Dubai", "Hong Kong", "Bangkok"], size=n_orders)
    special = rng.choice(["None", "Fragile", "Refrigerated", "HighValue"], size=n_orders, p=[0.7, 0.15, 0.1, 0.05])

    orders = pd.DataFrame({
        "order_id": order_ids,
        "order_date": [d.strftime("%Y-%m-%d") for d in dates],
        "customer_segment": customer_segments,
        "priority": priorities,
        "category": categories,
        "order_value": order_values,
        "origin": origins,
        "destination": destinations,
        "special_handling": special,
    })
    orders.to_csv(os.path.join(path, "orders.csv"), index=False)

    # delivery_performance.csv (150 records) - not all orders have delivery info
    n_del = 150
    del_order_ids = rng.choice(order_ids, size=n_del, replace=False)
    carriers = rng.choice([f"Carrier_{i}" for i in range(1, 6)], size=n_del)
    promised_days = np.where(rng.random(n_del) < 0.2, 1, np.where(rng.random(n_del) < 0.7, 3, 7))
    # build a quick map from order_id -> order_date string to avoid chained pandas access
    order_date_map = dict(zip(orders['order_id'], orders['order_date']))
    promised = []
    for oid, d in zip(del_order_ids, promised_days):
        od = order_date_map.get(oid)
        if od is None:
            # fallback to today if order date missing
            base = datetime.today()
        else:
            try:
                base = datetime.strptime(str(od), "%Y-%m-%d")
            except Exception:
                # if parsing fails, use today's date
                base = datetime.today()
        promised.append(base + timedelta(days=int(d)))
    actual_delay = rng.normal(loc=0.5, scale=2.0, size=n_del)  # days; can be negative (early)
    actual = [p + timedelta(days=float(max(-2, min(10, a)))) for p,a in zip(promised, actual_delay)]
    status = ["Delivered" if (datetime.today() - a).days >= 0 else "In Transit" for a in actual]
    quality = rng.choice(["OK", "Damaged", "Wrong Item"], size=n_del, p=[0.9, 0.08, 0.02])
    ratings = rng.choice([1,2,3,4,5], size=n_del, p=[0.02,0.03,0.1,0.3,0.55])
    delivery_costs = np.round(rng.uniform(20, 500, n_del), 2)

    delivery = pd.DataFrame({
        "order_id": del_order_ids,
        "carrier": carriers,
        "promised_date": [d.strftime("%Y-%m-%d") for d in promised],
        "actual_date": [d.strftime("%Y-%m-%d") for d in actual],
        "status": status,
        "quality_issue": quality,
        "customer_rating": ratings,
        "delivery_cost": delivery_costs,
    })
    delivery.to_csv(os.path.join(path, "delivery_performance.csv"), index=False)

    # routes_distance.csv (150 records) - align with delivery rows mostly
    n_routes = n_del
    route_order_ids = del_order_ids
    distances = np.round(rng.uniform(5, 2000, n_routes), 1)
    fuel_consumption = np.round(distances / rng.uniform(8, 15, n_routes), 2)  # liters
    tolls = np.round(rng.uniform(0, 50, n_routes), 2)
    traffic_delay_mins = np.round(np.maximum(0, rng.normal(30, 40, n_routes)), 0)
    weather_impact = rng.choice([0,1], size=n_routes, p=[0.8,0.2])

    routes = pd.DataFrame({
        "order_id": route_order_ids,
        "distance_km": distances,
        "fuel_liters": fuel_consumption,
        "toll_cost": tolls,
        "traffic_delay_mins": traffic_delay_mins,
        "weather_impact_flag": weather_impact,
    })
    routes.to_csv(os.path.join(path, "routes_distance.csv"), index=False)

    # vehicle_fleet.csv (50 records)
    n_veh = 50
    vehicle_ids = [f"VH{200+i}" for i in range(n_veh)]
    types = rng.choice(["Van", "Truck", "Refrigerated", "Bike"], size=n_veh, p=[0.4,0.3,0.15,0.15])
    capacities = np.round(rng.uniform(500, 5000, n_veh), 0)
    fuel_eff = np.round(rng.uniform(5, 18, n_veh), 2)  # km per liter
    locations = rng.choice(["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"], size=n_veh)
    status = rng.choice(["Available", "In Transit", "Maintenance"], size=n_veh, p=[0.6,0.3,0.1])
    age_years = np.round(rng.uniform(0.5, 10, n_veh), 1)
    co2_per_km = np.round(0.27 / fuel_eff * 1000, 3)  # rough g/km proxy

    fleet = pd.DataFrame({
        "vehicle_id": vehicle_ids,
        "type": types,
        "capacity_kg": capacities,
        "fuel_eff_km_per_l": fuel_eff,
        "location": locations,
        "status": status,
        "age_years": age_years,
        "co2_g_per_km": co2_per_km,
    })
    fleet.to_csv(os.path.join(path, "vehicle_fleet.csv"), index=False)

    # warehouse_inventory.csv (35 records)
    warehouses = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"]
    product_cats = ["Electronics", "Fashion", "Food", "Healthcare", "Industrial", "Books", "Home"]
    rows = []
    for w in warehouses:
        for cat in product_cats:
            rows.append({
                "warehouse": w,
                "category": cat,
                "stock_level": int(max(0, rng.normal(500, 300))),
                "reorder_level": int(rng.integers(50, 200)),
                "storage_cost_month": round(rng.uniform(100, 2000),2),
                "last_restocked": (datetime.today() - timedelta(days=int(rng.integers(1,60)))).strftime("%Y-%m-%d")
            })
    inv = pd.DataFrame(rows)
    inv.to_csv(os.path.join(path, "warehouse_inventory.csv"), index=False)

    # customer_feedback.csv (83 records)
    n_fb = 83
    fb_order_ids = rng.choice(del_order_ids, size=n_fb, replace=False)
    ratings = rng.choice([1,2,3,4,5], size=n_fb, p=[0.02,0.03,0.1,0.3,0.55])
    feedback_texts = rng.choice([
        "Delivered on time, good condition",
        "Late delivery, unhappy",
        "Package damaged",
        "Driver was helpful",
        "Wrong item delivered",
        "Excellent service"
    ], size=n_fb)
    rec_likelihood = rng.choice([0,1], size=n_fb, p=[0.2,0.8])
    issue_cat = rng.choice(["None","Delay","Damage","Wrong Item","Other"], size=n_fb, p=[0.5,0.2,0.15,0.1,0.05])
    fb_dates = [datetime.today() - timedelta(days=int(x)) for x in rng.integers(0,90,n_fb)]

    fb = pd.DataFrame({
        "order_id": fb_order_ids,
        "rating": ratings,
        "feedback": feedback_texts,
        "recommendation_likelihood": rec_likelihood,
        "issue_category": issue_cat,
        "feedback_date": [d.strftime("%Y-%m-%d") for d in fb_dates],
    })
    fb.to_csv(os.path.join(path, "customer_feedback.csv"), index=False)

    # cost_breakdown.csv (150 records) - align with route/delivery entries
    n_cost = n_del
    cost_order_ids = del_order_ids
    fuel_costs = np.round(fuel_consumption * rng.uniform(80, 120, n_cost) / 10,2)
    labor = np.round(rng.uniform(50, 200, n_cost),2)
    maintenance = np.round(rng.uniform(0, 30, n_cost),2)
    insurance = np.round(rng.uniform(5, 20, n_cost),2)
    packaging = np.round(rng.uniform(1,10, n_cost),2)
    platform_fee = np.round(rng.uniform(0.5,5, n_cost),2)

    costs = pd.DataFrame({
        "order_id": cost_order_ids,
        "fuel_cost": fuel_costs,
        "labor_cost": labor,
        "maintenance_cost": maintenance,
        "insurance_cost": insurance,
        "packaging_cost": packaging,
        "platform_fee": platform_fee,
    })
    costs.to_csv(os.path.join(path, "cost_breakdown.csv"), index=False)

    return {
        "orders": orders,
        "delivery": delivery,
        "routes": routes,
        "fleet": fleet,
        "inventory": inv,
        "feedback": fb,
        "costs": costs,
    }


def load_datasets(path="data"):
    """Load CSV datasets from provided path. If files missing, generate synthetic data and save.
    Returns a dict of DataFrames.
    """
    ensure_data_dir(path)
    needed = [
        "orders.csv",
        "delivery_performance.csv",
        "routes_distance.csv",
        "vehicle_fleet.csv",
        "warehouse_inventory.csv",
        "customer_feedback.csv",
        "cost_breakdown.csv",
    ]
    missing = [f for f in needed if not csv_exists(path, f)]
    if missing:
        print("Missing files detected, generating synthetic datasets for demo:", missing)
        datasets = generate_synthetic_data(path)
    else:
        datasets = {
            "orders": pd.read_csv(os.path.join(path, "orders.csv")),
            "delivery": pd.read_csv(os.path.join(path, "delivery_performance.csv")),
            "routes": pd.read_csv(os.path.join(path, "routes_distance.csv")),
            "fleet": pd.read_csv(os.path.join(path, "vehicle_fleet.csv")),
            "inventory": pd.read_csv(os.path.join(path, "warehouse_inventory.csv")),
            "feedback": pd.read_csv(os.path.join(path, "customer_feedback.csv")),
            "costs": pd.read_csv(os.path.join(path, "cost_breakdown.csv")),
        }
    return datasets


def preprocess_merge(datasets):
    """Merge datasets into an orders-level table and create derived metrics."""
    orders = datasets["orders"].copy()
    delivery = datasets["delivery"].copy()
    routes = datasets["routes"].copy()
    costs = datasets["costs"].copy()
    fleet = datasets["fleet"].copy()
    feedback = datasets["feedback"].copy()

    # Merge delivery info
    df = orders.merge(delivery, on="order_id", how="left")
    df = df.merge(routes, on="order_id", how="left")
    df = df.merge(costs, on="order_id", how="left")

    # Derived: parse dates
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["promised_date"] = pd.to_datetime(df.get("promised_date"), errors="coerce")
    df["actual_date"] = pd.to_datetime(df.get("actual_date"), errors="coerce")

    # Delay in hours (if available)
    df["delay_days"] = (df["actual_date"] - df["promised_date"]).dt.total_seconds() / (3600*24)
    df["delayed_flag"] = df["delay_days"] > 0.5  # threshold: > 12 hours considered delayed

    # Cost per km
    df["distance_km"] = pd.to_numeric(df.get("distance_km"), errors="coerce")
    df["delivery_cost"] = pd.to_numeric(df.get("delivery_cost"), errors="coerce")
    df["cost_per_km"] = df.apply(lambda r: r.delivery_cost / r.distance_km if pd.notna(r.delivery_cost) and r.distance_km and r.distance_km>0 else np.nan, axis=1)

    # CO2 estimate: join approximate fleet average co2 by vehicle type if available
    # For demo, estimate co2_g_per_km as average across fleet
    fleet_avg_co2 = fleet["co2_g_per_km"].median() if not fleet.empty else 200.0
    df["co2_g_per_km_est"] = df["distance_km"] * fleet_avg_co2

    # Merge feedback aggregated metrics
    fb_agg = feedback.groupby("order_id").agg({"rating": "mean", "recommendation_likelihood": "mean"}).reset_index()
    df = df.merge(fb_agg, on="order_id", how="left")

    # Fill some nulls
    df["priority"] = df["priority"].fillna("Standard")

    return df
