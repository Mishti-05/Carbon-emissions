from pydantic import BaseModel
from datetime import datetime


class SensorInput(BaseModel):
    user_id: int
    timestamp: datetime
    temperature: float
    humidity: float
    aqi: float
    occupancy: int


class LifestyleInput(BaseModel):
    """Input schema for user lifestyle carbon footprint calculation"""
    transport_km: float
    electricity_consumption: float
    water_usage: float
    flights_taken: float

    class Config:
        json_schema_extra = {
            "example": {
                "transport_km": 800.0,
                "electricity_consumption": 3.0,
                "water_usage": 1.0,
                "flights_taken": 1.0
            }
        }


class CarbonFootprintResponse(BaseModel):
    """Response schema for carbon footprint predictions"""
    energy_kwh: float
    energy_carbon: float
    activity_carbon: float
    final_carbon_emission: float
    weekly_carbon: float
    recommendations: list