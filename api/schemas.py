from pydantic import BaseModel
from datetime import datetime


class SensorInput(BaseModel):
    user_id: int
    timestamp: datetime
    temperature: float
    humidity: float
    aqi: float
    occupancy: int