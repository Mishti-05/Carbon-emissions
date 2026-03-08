import numpy as np

# -----------------------------
# EMISSION FACTORS
# -----------------------------

# Electricity emissions (India average)
EMISSION_FACTOR = 0.82  # kg CO2 per kWh

# Transport emissions (average petrol car)
TRANSPORT_EMISSION_PER_KM = 0.192  # kg CO2 per km

# Flight emissions (average short haul flight)
FLIGHT_EMISSION_PER_FLIGHT = 250  # kg CO2 per flight


# -----------------------------
# NORMALIZATION CONSTANTS
# -----------------------------

TRANSPORT_KM_SCALE = 1283.0
ELECTRICITY_CONSUMPTION_MAX = 24.0
WATER_USAGE_MAX = 2.0
FLIGHTS_TAKEN_MAX = 3.0


# -----------------------------
# EMISSION CALCULATIONS
# -----------------------------

def calculate_energy_carbon(energy_kwh):
    """
    Convert energy consumption to carbon emissions.
    """
    return energy_kwh * EMISSION_FACTOR


def calculate_transport_carbon(transport_km):
    """
    Calculate carbon emissions from vehicle travel.
    """
    return transport_km * TRANSPORT_EMISSION_PER_KM


def calculate_flight_carbon(flights_taken):
    """
    Estimate emissions from flights.
    """
    return flights_taken * FLIGHT_EMISSION_PER_FLIGHT


# -----------------------------
# FEATURE NORMALIZATION
# -----------------------------

def normalize_features(transport_km,
                       electricity_consumption,
                       water_usage,
                       flights_taken):
    """
    Normalize features for ML model prediction.
    """

    normalized_transport = min(transport_km / TRANSPORT_KM_SCALE, 1.0)
    normalized_electricity = min(electricity_consumption / ELECTRICITY_CONSUMPTION_MAX, 1.0)
    normalized_water = min(water_usage / WATER_USAGE_MAX, 1.0)
    normalized_flights = min(flights_taken / FLIGHTS_TAKEN_MAX, 1.0)

    return np.array([[normalized_transport,
                      normalized_electricity,
                      normalized_water,
                      normalized_flights]])


# -----------------------------
# ML PREDICTION
# -----------------------------

def predict_lifestyle_carbon(model,
                             transport_km,
                             electricity_consumption,
                             water_usage,
                             flights_taken):
    """
    Predict lifestyle-related carbon using the ML model.
    """

    normalized_features = normalize_features(
        transport_km,
        electricity_consumption,
        water_usage,
        flights_taken
    )

    prediction = model.predict(normalized_features)[0]

    return prediction


# -----------------------------
# FINAL CARBON CALCULATION
# -----------------------------

def calculate_final_carbon(model,
                           energy_kwh,
                           transport_km,
                           electricity_consumption,
                           water_usage,
                           flights_taken):
    """
    Calculate total carbon footprint.
    """

    energy_carbon = calculate_energy_carbon(energy_kwh)

    transport_carbon = calculate_transport_carbon(transport_km)

    flight_carbon = calculate_flight_carbon(flights_taken)

    lifestyle_carbon = predict_lifestyle_carbon(
        model,
        transport_km,
        electricity_consumption,
        water_usage,
        flights_taken
    )

    final_carbon = (
        energy_carbon
        + transport_carbon
        + flight_carbon
        + lifestyle_carbon
    )

    return final_carbon


# -----------------------------
# SUSTAINABILITY FEEDBACK
# -----------------------------

def generate_feedback(energy_kwh,
                      transport_km,
                      electricity_consumption,
                      water_usage,
                      flights_taken,
                      final_carbon):
    """
    Generate personalized carbon reduction feedback.
    """

    tips = []

    # Energy usage
    if energy_kwh > 3:
        tips.append(
            "Your household electricity consumption is relatively high. Consider reducing AC usage and using energy-efficient appliances."
        )
    elif energy_kwh > 2:
        tips.append(
            "Your electricity usage is moderate. Using LED lighting and smart power strips can help reduce emissions."
        )

    # Transport
    if transport_km > 500:
        tips.append(
            "Your monthly vehicle travel is high. Consider public transport, cycling, or carpooling to reduce emissions."
        )
    elif transport_km > 100:
        tips.append(
            "Reducing short car trips or combining errands can help lower transport emissions."
        )

    # Water usage
    if water_usage > 1.5:
        tips.append(
            "Your water usage is relatively high. Try shorter showers or installing low-flow fixtures."
        )

    # Screen / electricity usage
    if electricity_consumption > 12:
        tips.append(
            "High daily screen time increases electricity consumption. Try reducing TV/PC usage where possible."
        )

    # Flights
    if flights_taken >= 3:
        tips.append(
            "Frequent air travel significantly increases carbon emissions. Consider virtual meetings or carbon offset programs."
        )
    elif flights_taken > 0:
        tips.append(
            "Air travel contributes substantially to carbon emissions. Reducing flights when possible helps."
        )

    # Overall footprint
    if final_carbon > 50:
        tips.append(
            "Your carbon footprint is relatively high. Consider renewable energy sources and lifestyle changes to reduce emissions."
        )
    else:
        tips.append(
            "Great job! You're maintaining a relatively sustainable lifestyle."
        )

    return tips