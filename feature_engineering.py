import numpy as np

def create_features(df):

    # Handle missing values first (important for noisy data)
    df.fillna(method="ffill", inplace=True)

    # Time features
    df["hour"] = df["timestamp"].dt.hour
    df["day"] = df["timestamp"].dt.dayofweek
    df["month"] = df["timestamp"].dt.month

    df["is_weekend"] = (df["day"] >= 5).astype(int)

    # Cyclical encoding
    df["hour_sin"] = np.sin(2*np.pi*df["hour"]/24)
    df["hour_cos"] = np.cos(2*np.pi*df["hour"]/24)

    df["month_sin"] = np.sin(2*np.pi*df["month"]/12)
    df["month_cos"] = np.cos(2*np.pi*df["month"]/12)

    # ⭐ IMPORTANT: Lag features
    df["energy_lag1"] = df["energy_kwh"].shift(1)
    df["energy_lag2"] = df["energy_kwh"].shift(2)
    df["energy_lag24"] = df["energy_kwh"].shift(24)
    df["rolling_mean_24"] = df["energy_kwh"].rolling(24).mean()


    # Rolling trends
    df["rolling_mean_6"] = df["energy_kwh"].rolling(6).mean()
    df["rolling_std_6"] = df["energy_kwh"].rolling(6).std()
    df["rolling_std_24"] = df["energy_kwh"].rolling(24).std()

    # Peak hour indicator
    df["is_peak_hour"] = df["hour"].isin([12,13,14,19,20,21]).astype(int)

    return df.dropna()
