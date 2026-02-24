import numpy as np

def appliance_energy(temp, occupancy, household):
    energy = 0.2  # fridge baseline

    # Lights
    energy += 0.05 * occupancy

    # Cooking peak
    if occupancy > 1:
        energy += np.random.uniform(0.3, 0.7)

    # AC usage
    if household["has_ac"] and temp > 26:
        energy += (temp - 26) * 0.15 * occupancy

    # Purifier
    if household["has_purifier"]:
        energy += max(0, 0.01 * (household["eco_awareness"]))

    return energy
