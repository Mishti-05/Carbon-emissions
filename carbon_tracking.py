BASE_EMISSION_FACTOR = 0.82


def dynamic_emission_factor(row):
    factor = BASE_EMISSION_FACTOR

    if row.get("is_peak_hour", 0) == 1:
        factor *= 1.15

    if row.get("aqi", 0) > 150:
        factor *= 1.10

    if row.get("temperature", 0) > 30:
        factor *= 1.05

    return factor


def compute_carbon(df):
    df = df.copy()
    # if the dataset was missing a user_id we already added one in load_data,
    # but ensure here as well for safety
    if "user_id" not in df.columns:
        df["user_id"] = 1

    df["emission_factor"] = df.apply(dynamic_emission_factor, axis=1)
    df["carbon_kg"] = df["energy_kwh"] * df["emission_factor"]
    return df

def weekly_individual_carbon(df):
    # guard against missing user_id by promoting a default single user
    if "user_id" not in df.columns:
        df = df.copy()
        df["user_id"] = 1

    # make sure timestamps are sorted for resampling
    df = df.sort_values("timestamp")

    # use set_index then groupby to avoid pandas grouping/resample bug
    result = (
        df.set_index("timestamp")
          .groupby("user_id")["carbon_kg"]
          .resample("W")
          .sum()
          .reset_index()
    )
    return result

def user_behaviour_summary(df, user_id):
    if "user_id" not in df.columns:
        # single‑user fallback
        user_df = df
    else:
        user_df = df[df["user_id"] == user_id]

    summary = {
        "total_carbon": user_df["carbon_kg"].sum(),
        "peak_hour_carbon": user_df[user_df.get("is_peak_hour", 0) == 1]["carbon_kg"].sum(),
        "weekend_carbon": user_df[user_df.get("is_weekend", 0) == 1]["carbon_kg"].sum(),
        "high_temp_usage": user_df[user_df.get("temperature", 0) > 30]["carbon_kg"].sum(),
    }

    return summary

def personalised_feedback(summary):
    feedback = []

    if summary["peak_hour_carbon"] > 0.4 * summary["total_carbon"]:
        feedback.append(
            "You use a lot of energy during peak hours. Shifting usage to non-peak times can reduce both cost and emissions."
        )

    if summary["weekend_carbon"] > 0.3 * summary["total_carbon"]:
        feedback.append(
            "Your weekend consumption is high. Consider automating appliances or using smart scheduling."
        )

    if summary["high_temp_usage"] > 0.25 * summary["total_carbon"]:
        feedback.append(
            "Cooling systems contribute heavily to your footprint. Try energy-efficient cooling or better insulation."
        )

    if not feedback:
        feedback.append("Great job! Your energy usage is already efficient.")

    return feedback

def simulate_reduction(df, user_id, shift_peak=0.2):
    user_df = df[df["user_id"] == user_id].copy()

    peak_mask = user_df["is_peak_hour"] == 1
    reduction = user_df.loc[peak_mask, "carbon_kg"].sum() * shift_peak

    return {
        "estimated_reduction_kg": reduction
    }
