from fastapi import FastAPI
import joblib
import pandas as pd

from feature_engineering import create_features
from carbon_tracking import compute_carbon
from recommendations import generate_recommendations
from api.schemas import SensorInput


app = FastAPI(title="Smart Home Carbon API")


# ====================
# LOAD MODEL
# ====================
MODEL_PATH = "models/smart_home_model.pkl"
model = joblib.load(MODEL_PATH)


# ====================
# HEALTH CHECK
# ====================
@app.get("/")
def home():
    return {"message": "Smart Home Carbon API running"}


# ====================
# PREDICTION ENDPOINT
# ====================
@app.post("/predict")
def predict(data: SensorInput):

    # Convert to dataframe
    df = pd.DataFrame([data.dict()])

    # Feature engineering
    df = create_features(df)

    # Features used by model
    features = [
        "temperature", "humidity", "aqi", "occupancy",
        "hour_sin", "hour_cos",
        "month_sin", "month_cos",
        "is_weekend",
        "energy_lag1", "energy_lag2", "energy_lag24",
        "rolling_mean_6", "rolling_std_6",
        "is_peak_hour"
    ]

    # Handle missing lag values (single prediction case)
    for col in features:
        if col not in df:
            df[col] = 0

    # Prediction
    energy = model.predict(df[features])[0]
    df["energy_kwh"] = energy

    # Carbon calculation
    df = compute_carbon(df)

    # Recommendations
    df = generate_recommendations(df)

    return {
        "energy_prediction_kwh": float(energy),
        "carbon_kg": float(df["carbon_kg"].iloc[0]),
        "recommendations": df["recommendations"].iloc[0],
    }