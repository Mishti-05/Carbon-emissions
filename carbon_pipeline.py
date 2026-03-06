import numpy as np

EMISSION_FACTOR = 0.82


# These values ensure user inputs are scaled to match the training distribution.
# The dataset already stored `transport_km` as a fraction between 0 and 1.
# To convert raw kilometers into the same domain we divide by an
# estimated upper bound.  Setting the divisor close to the 99th
# percentile of observed values (~1 250 km) keeps typical monthly
# distances well within the model's sensitive region.
TRANSPORT_KM_SCALE = 1283.0  # approximate divisor for kilometers → [0,1]
# coefficient for linear transport term added to ensure monotonicity
TRANSPORT_COEF = 0.35

ELECTRICITY_CONSUMPTION_MAX = 24.0  # Max hours per day (normalize to [0,1])
WATER_USAGE_MAX = 2.0  # Max shower frequency 
FLIGHTS_TAKEN_MAX = 3.0  # Max air travel frequency 



def calculate_energy_carbon(energy_kwh):
    """
    Convert energy consumption to carbon emissions.
    """
    return energy_kwh * EMISSION_FACTOR


def normalize_features(transport_km,
                      electricity_consumption,
                      water_usage,
                      flights_taken):
    """
    Normalize input features to match the training data scale.
    The model was trained on normalized features in range [0, 1].
    """
    
    normalized_transport = min(transport_km / TRANSPORT_KM_SCALE, 1.0)
    normalized_electricity = min(electricity_consumption / ELECTRICITY_CONSUMPTION_MAX, 1.0)
    normalized_water = min(water_usage / WATER_USAGE_MAX, 1.0)
    normalized_flights = min(flights_taken / FLIGHTS_TAKEN_MAX, 1.0)
    
    return np.array([[normalized_transport,
                      normalized_electricity,
                      normalized_water,
                      normalized_flights]])


def predict_activity_carbon(model,
                            transport_km,
                            electricity_consumption,
                            water_usage,
                            flights_taken):

    # normalize everything
    norm_vals = normalize_features(
        transport_km,
        electricity_consumption,
        water_usage,
        flights_taken
    )[0]  # shape (4,)

    normalized_transport = norm_vals[0]
    # prediction without transport influence (set first feature to 0)
    features_no_transport = np.array([[0.0,
                                       norm_vals[1],
                                       norm_vals[2],
                                       norm_vals[3]]])
    base_pred = model.predict(features_no_transport)[0]

    # linear transport component ensures monotonic increase
    transport_contrib = TRANSPORT_COEF * normalized_transport

    return base_pred + transport_contrib


def calculate_final_carbon(energy_carbon, activity_carbon):
    """
    Combine IoT energy carbon + lifestyle carbon
    """
    return energy_carbon + activity_carbon


def generate_feedback(energy_kwh,
                      transport_km,
                      electricity_consumption,
                      water_usage,
                      flights_taken,
                      final_carbon):
    """
    Generate personalized carbon reduction feedback based on user inputs.
    """
    tips = []

    # IoT Energy usage
    if energy_kwh > 3:
        tips.append(
            "Your household electricity consumption is relatively high. Consider reducing AC usage and using energy-efficient devices."
        )
    elif energy_kwh > 2:
        tips.append(
            "Your electricity usage is moderate. Using LED lighting and smart power strips can help."
        )

    # Transport
    if transport_km > 10:
        tips.append(
            "Your monthly vehicle distance is high. Consider public transport, cycling, or carpooling."
        )

    # Water usage
    if water_usage > 1.5:
        tips.append(
            "Your water usage is relatively high. Consider shorter showers or low-flow fixtures."
        )

    # Electricity consumption (TV/PC + Internet)
    if electricity_consumption > 12:
        tips.append(
            "High daily screen time increases electricity consumption. Try to reduce TV/PC and Internet usage."
        )

    # Flights taken
    if flights_taken >= 3:
        tips.append(
            "Frequent air travel significantly increases carbon emissions. Consider carbon offset programs."
        )
    elif flights_taken > 0:
        tips.append(
            "Air travel contributes substantially to carbon emissions. Reduce flight frequency when possible."
        )

    # Overall footprint
    if final_carbon > 5:
        tips.append(
            "Consider renewable energy sources or carbon offset programs to reduce your impact."
        )
    else:
        tips.append(
            "Good work! You're maintaining a relatively sustainable lifestyle."
        )

    return tips