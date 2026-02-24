import numpy as np

def create_households(n=50):
    households = []
    for i in range(n):
        profile = {
            "house_id": i,
            "family_size": np.random.randint(1, 6),
            "income_level": np.random.choice(["low", "medium", "high"]),
            "eco_awareness": np.random.uniform(0.2, 1.0),
            "has_ac": np.random.choice([0, 1], p=[0.3, 0.7]),
            "has_purifier": np.random.choice([0, 1], p=[0.5, 0.5])
        }
        households.append(profile)
    return households
