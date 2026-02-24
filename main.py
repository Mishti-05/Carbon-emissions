from data_processing import load_data
from feature_engineering import create_features
from train_model import train_model, evaluate, save_model
from carbon_tracking import (
    compute_carbon,
    weekly_individual_carbon,
    user_behaviour_summary,
    personalised_feedback,
    simulate_reduction,
)
from recommendations import generate_recommendations
from explainability import plot_feature_importance

from sklearn.model_selection import train_test_split

DATA_PATH = "data/smart_home_data.csv"
MODEL_PATH = "models/smart_home_model.pkl"


# =====================
# 1. LOAD DATA
# =====================
df = load_data(DATA_PATH)


# =====================
# 2. FEATURE ENGINEERING
# =====================
df = create_features(df)


# =====================
# 3. MODEL TRAINING
# =====================
features = [
    "temperature", "humidity", "aqi", "occupancy",
    "hour_sin", "hour_cos",
    "month_sin", "month_cos",
    "is_weekend",
    "energy_lag1", "energy_lag2", "energy_lag24",
    "rolling_mean_6", "rolling_std_6",
    "is_peak_hour"
]

X = df[features]
y = df["energy_kwh"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

model = train_model(X_train, y_train)
evaluate(model, X_test, y_test)
save_model(model, MODEL_PATH)


# =====================
# 4. CARBON EMISSIONS
# =====================
df = compute_carbon(df)

weekly = weekly_individual_carbon(df)
print("\nWeekly Carbon Footprint:")
print(weekly.head())


# =====================
# 5. USER BEHAVIOUR ANALYSIS
# =====================
user_id = df["user_id"].iloc[0]  # demo user

summary = user_behaviour_summary(df, user_id)
print("\nUser Behaviour Summary:")
print(summary)


# =====================
# 6. PERSONALISED FEEDBACK
# =====================
feedback = personalised_feedback(summary)

print("\nPersonalised Suggestions:")
for f in feedback:
    print("-", f)


# =====================
# 7. REDUCTION SIMULATION
# =====================
impact = simulate_reduction(df, user_id)

print("\nEstimated Carbon Reduction:")
print(impact)


# =====================
# 8. AUTOMATED RECOMMENDATIONS
# =====================
df = generate_recommendations(df)

print("\nSample Recommendations:")
print(df[["timestamp", "recommendations"]].head())



