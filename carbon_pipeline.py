import numpy as np

EMISSION_FACTOR = 0.82


def calculate_energy_carbon(energy_kwh):
    """
    Convert energy consumption to carbon emissions.
    """
    return energy_kwh * EMISSION_FACTOR


def predict_activity_carbon(model,
                            transport_km,
                            electricity_consumption,
                            water_usage,
                            flights_taken):
    """
    Predict lifestyle carbon emissions using the trained model.
    Features: transport_km, electricity_consumption, water_usage, flights_taken
    """
    features = np.array([[transport_km,
                          electricity_consumption,
                          water_usage,
                          flights_taken]])

    prediction = model.predict(features)[0]

    return prediction


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
    if electricity_consumption > 6:
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