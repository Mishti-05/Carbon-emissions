import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # make sure there's a user_id column for downstream logic
    if "user_id" not in df.columns:
        # dataset appears to be single‑user; assign a dummy id of 1
        df["user_id"] = 1

    return df
