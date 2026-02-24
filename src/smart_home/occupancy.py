def occupancy(hour, weekend, family_size):
    if weekend:
        return family_size * 0.8
    if 9 <= hour <= 17:
        return family_size * 0.3
    return family_size * 0.7
