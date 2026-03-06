import pandas as pd
import joblib

from data_processing import load_data
from feature_engineering import create_features
from train_model import train_model, evaluate, save_model
from carbon_pipeline import (
    calculate_energy_carbon,
    predict_activity_carbon,
    calculate_final_carbon,
    generate_feedback
)
from recommendations import generate_recommendations
from sklearn.model_selection import train_test_split

DATA_PATH = "data/smart_home_data.csv"
MODEL_PATH = "models/smart_home_model.pkl"


# =====================
# 1. LOAD DATA
# =====================
df = load_data(DATA_PATH)


# =====================
# 2. FEATURE ENGINEERING
# =====================
df = create_features(df)


# =====================
# 3. MODEL TRAINING
# =====================
features = [
    "temperature", "humidity", "aqi", "occupancy",
    "hour_sin", "hour_cos",
    "month_sin", "month_cos",
    "is_weekend",
    "energy_lag1", "energy_lag2", "energy_lag24",
    "rolling_mean_6", "rolling_std_6",
    "is_peak_hour"
]

X = df[features]
y = df["energy_kwh"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

model = train_model(X_train, y_train)
evaluate(model, X_test, y_test)
save_model(model, MODEL_PATH)

energy_pred = model.predict(X_test)
latest_energy = energy_pred[-1]

iot_output = pd.DataFrame({"energy_kwh":[latest_energy]})
iot_output.to_csv("iot_output.csv", index=False)


# =====================
# 4. CARBON EMISSIONS
# =====================

# load activity model
model = joblib.load("models/carbon_emission_model.pkl")

# IoT energy prediction (example output)
energy_kwh = 3.061892273847997

# User inputs (4-feature lifestyle model)
transport_km = 800                  # Monthly vehicle distance in km
electricity_consumption = 3.0       # TV/PC + Internet hours per day
water_usage = 1.0                   # Shower frequency (0=never, 0.5=less, 1=daily, 1.5=more, 2=twice/day)
flights_taken = 1.0                 # Air travel frequency (0=never, 1=rarely, 2=frequently, 3=very frequently)


energy_carbon = calculate_energy_carbon(energy_kwh)

# Predict activity carbon from lifestyle inputs
activity_carbon = predict_activity_carbon(
    model,
    transport_km,
    electricity_consumption,
    water_usage,
    flights_taken
)

# Calculate final carbon (energy + activity)
final_carbon = calculate_final_carbon(
    energy_carbon,
    activity_carbon
)

# Generate personalized feedback
tips = generate_feedback(
    energy_kwh,
    transport_km,
    electricity_consumption,
    water_usage,
    flights_taken,
    final_carbon
)

# Calculate weekly emissions
weekly_carbon = final_carbon * 7

# Display results
print("=" * 60)
print("DAILY CARBON FOOTPRINT ANALYSIS")
print("=" * 60)
print(f"Energy from IoT:            {energy_kwh:.4f} kWh")
print(f"Energy Carbon:              {energy_carbon:.4f} kg CO2")
print(f"Activity Carbon:            {activity_carbon:.4f} kg CO2")
print(f"Final Carbon Emission:      {final_carbon:.4f} kg CO2")
print()
print("=" * 60)
print("WEEKLY CARBON PROJECTION")
print("=" * 60)
print(f"Weekly Total Carbon:        {weekly_carbon:.4f} kg CO2")
print(f"Annual Projection:          {weekly_carbon * 52:.1f} kg CO2/year")
print()
print("=" * 60)
print("PERSONALIZED RECOMMENDATIONS")
print("=" * 60)
for tip in tips:
    print("-", tip)


# =====================
# 8. AUTOMATED RECOMMENDATIONS
# =====================
df = generate_recommendations(df)

print("\nSample Recommendations:")
print(df[["timestamp", "recommendations"]].head())



