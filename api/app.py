from fastapi import FastAPI
from pydantic import BaseModel
import joblib

from carbon_pipeline import (
    calculate_energy_carbon,
    predict_activity_carbon,
    calculate_final_carbon,
    generate_feedback
)

app = FastAPI(title="Smart Carbon Footprint API")

model = joblib.load("models/carbon_emission_model.pkl")


# -----------------------------
# Input schema
# -----------------------------
class UserInput(BaseModel):

    # IoT model output
    energy_kwh: float

    # lifestyle inputs (4 model features)
    transport_km: float
    electricity_consumption: float  # TV/PC + Internet hours per day
    water_usage: float              # shower frequency (0=never, 0.5=less freq, 1=daily, 1.5=more freq, 2=twice/day)
    flights_taken: float            # air travel frequency (0=never, 1=rarely, 2=frequently, 3=very frequently)


# -----------------------------
# Root endpoint
# -----------------------------
@app.get("/")
def home():
    return {"message": "Smart Carbon Emission API running"}


# -----------------------------
# Prediction endpoint
# -----------------------------
@app.post("/predict-carbon")
def predict_carbon(data: UserInput):

    # Carbon from energy
    energy_carbon = calculate_energy_carbon(data.energy_kwh)

    # Lifestyle carbon prediction
    activity_carbon = predict_activity_carbon(
        model,
        data.transport_km,
        data.electricity_consumption,
        data.water_usage,
        data.flights_taken
    )

    # Final carbon
    final_carbon = calculate_final_carbon(
        energy_carbon,
        activity_carbon
    )

    # Feedback
    tips = generate_feedback(
        data.energy_kwh,
        data.transport_km,
        data.electricity_consumption,
        data.water_usage,
        data.flights_taken,
        final_carbon
    )

    return {
        "energy_kwh": data.energy_kwh,
        "energy_carbon": round(energy_carbon, 3),
        "activity_carbon": round(activity_carbon, 3),
        "final_carbon_emission": round(final_carbon, 3),
        "weekly_carbon_estimate": round(final_carbon * 7, 3),
        "recommendations": tips
    }
