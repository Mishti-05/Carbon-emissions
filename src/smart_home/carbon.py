import numpy as np

def carbon_footprint(energy, aqi, eco_awareness):
    emission_factor = 0.82

    base = energy * emission_factor

    # Pollution-driven purifier usage
    pollution = max(0, (aqi - 100)) * 0.01

    # Eco awareness reduces emissions
    eco_effect = -eco_awareness * 0.1

    return base + pollution + eco_effect + np.random.normal(0, 0.05)
