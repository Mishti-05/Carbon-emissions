def recommend(row):
    tips = []

    if row["temperature"] < 24 and row["energy_kwh"] > 3:
        tips.append("Reduce AC usage.")

    if row["occupancy"] == 0 and row["energy_kwh"] > 1:
        tips.append("Turn off unused appliances.")

    return tips


def generate_recommendations(df):
    df["recommendations"] = df.apply(recommend, axis=1)
    return df
