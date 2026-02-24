import streamlit as st
import pandas as pd

from data_processing import load_data
from feature_engineering import create_features
from carbon_tracking import (
    compute_carbon,
    weekly_individual_carbon,
    user_behaviour_summary,
    personalised_feedback,
)

# ==============================
# CONFIG
# ==============================
st.set_page_config(page_title="Smart Home Carbon Dashboard", layout="wide")

DATA_PATH = "data/smart_home_data.csv"


# ==============================
# LOAD + PREPROCESS
# ==============================
@st.cache_data
def load_pipeline():
    df = load_data(DATA_PATH)
    df = create_features(df)
    df = compute_carbon(df)

    # ensure at least one user id exists for older datasets
    if "user_id" not in df.columns:
        df["user_id"] = 1

    return df


df = load_pipeline()


# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("Settings")

if "user_id" in df.columns:
    user_ids = df["user_id"].unique()
else:
    user_ids = [1]

selected_user = st.sidebar.selectbox("Select User", user_ids)


# ==============================
# TITLE
# ==============================
st.title("Smart Home Carbon Tracking Dashboard")


# ==============================
# WEEKLY CARBON FOOTPRINT
# ==============================
st.header("Weekly Carbon Footprint")

user_df = df[df["user_id"] == selected_user]
weekly = weekly_individual_carbon(user_df)

# `weekly` contains columns ['user_id','timestamp','carbon_kg']; plot the carbon series
if "timestamp" in weekly.columns and "carbon_kg" in weekly.columns:
    chart_data = weekly.set_index("timestamp")["carbon_kg"]
else:
    chart_data = weekly
st.line_chart(chart_data)

col1, col2 = st.columns(2)

with col1:
    total = weekly["carbon_kg"].sum()
    st.metric("Total Carbon (kg)", round(total, 2))

with col2:
    avg = weekly["carbon_kg"].mean()
    st.metric("Avg Weekly Carbon", round(avg, 2))


# ==============================
# BEHAVIOUR INSIGHTS
# ==============================
st.header("Behaviour Insights")

summary = user_behaviour_summary(df, selected_user)

insight_cols = st.columns(3)

with insight_cols[0]:
    st.metric("Peak Usage %", round(summary.get("peak_usage_ratio", 0) * 100, 2))

with insight_cols[1]:
    st.metric("Weekend Usage %", round(summary.get("weekend_ratio", 0) * 100, 2))

with insight_cols[2]:
    st.metric("High AQI Usage", round(summary.get("high_aqi_usage", 0) * 100, 2))


# ==============================
# PERSONALIZED SUGGESTIONS
# ==============================
st.header("Personalised Suggestions")

feedback = personalised_feedback(summary)

for f in feedback:
    st.success(f)


# ==============================
# RAW DATA
# ==============================
with st.expander("View Raw Data"):
    st.dataframe(user_df.head(100))


# ==============================
# FOOTER
# ==============================
st.markdown("---")
st.caption("AI-powered carbon intelligence for smart homes")
