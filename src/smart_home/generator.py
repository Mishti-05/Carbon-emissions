import pandas as pd
import numpy as np

np.random.seed(42)

# Time range
timestamps = pd.date_range(
    start="2024-01-01",
    end="2024-03-31",
    freq="H"
)

data = []

for t in timestamps:

    # Base temperature with season + noise
    base_temp = 25 + 5 * np.sin(2*np.pi*t.dayofyear/365)
    temperature = base_temp + np.random.normal(0, 1.5)

    # Humidity with noise
    humidity = 60 + np.random.normal(0, 5)

    # AQI variation
    aqi = 100 + np.random.normal(0, 15)

    # Occupancy randomness
    if 8 <= t.hour <= 18:
        occupancy = np.random.choice([0, 1, 2], p=[0.3, 0.5, 0.2])
    else:
        occupancy = np.random.choice([0, 1], p=[0.6, 0.4])

    # Weekend effect
    if t.weekday() >= 5:
        occupancy += np.random.choice([0, 1], p=[0.7, 0.3])

    # Energy base
    energy = 0.5

    # Temperature effect (AC usage)
    if temperature > 30:
        energy += 2 + np.random.normal(0, 0.5)

    # Occupancy effect
    energy += occupancy * (0.8 + np.random.normal(0, 0.2))

    # Cooking spikes
    if 12 <= t.hour <= 14 or 19 <= t.hour <= 21:
        energy += np.random.normal(1.5, 0.5)

    # Random spikes (guests, events)
    if np.random.rand() < 0.02:
        energy += np.random.uniform(3, 6)

    # Random appliance usage
    energy += np.random.normal(0, 0.3)

    # Sensor faults (missing data)
    if np.random.rand() < 0.005:
        temperature = np.nan

    data.append([
        t, temperature, humidity, aqi,
        occupancy, max(energy, 0.2)
    ])


df = pd.DataFrame(data, columns=[
    "timestamp", "temperature", "humidity",
    "aqi", "occupancy", "energy_kwh"
])

# Save
df.to_csv("smart_home_data.csv", index=False)

print("Realistic synthetic data generated!")
print(df.head())
