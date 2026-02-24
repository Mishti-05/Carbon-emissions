## 🔹 deployment branch → Production API

Includes only:

• FastAPI backend
• Trained ML model
• Feature pipeline
• Carbon engine
• Recommendation system

This branch is designed for:

• Cloud deployment
• Integration with frontend
• Real‑time IoT systems

---

# 🚀 Features

## ✅ Machine Learning

• Time‑series inspired energy forecasting
• Lag features and rolling statistics
• Robust feature engineering
• Performance evaluation

## ✅ Carbon Tracking

• Energy → carbon conversion
• Weekly footprint tracking
• Behavioural analysis

## ✅ Personalised Recommendations

• Peak hour optimisation
• Appliance usage insights
• Behavioural nudges

## ✅ Explainability

• Feature importance

## ✅ Dashboard

• Interactive carbon monitoring

## ✅ Production API

• Real‑time prediction
• Scalable backend

---

# ⚙️ Setup Instructions (Main Branch)

## 1️⃣ Clone repository

```
 git clone <repo_url>
 cd <repo_name>
```

## 2️⃣ Create environment

```
 python -m venv venv
 source venv/bin/activate
```

(Windows)

```
 venv\Scripts\activate
```

## 3️⃣ Install dependencies

```
 pip install -r requirements.txt
```

## 4️⃣ Train model

```
 python main.py
```

## 5️⃣ Run dashboard

```
 streamlit run streamlit_dashboard.py
```

---

# 🌍 Deployment Branch Guide

## 1️⃣ Clone only deployment branch

```
 git clone -b deployment <repo_url>
```

## 2️⃣ Install dependencies

```
 pip install -r requirements.txt
```

## 3️⃣ Run API

```
 python -m uvicorn api.app:app --reload
```

## 4️⃣ API Docs

Open:

```
 http://127.0.0.1:8000/docs
```

---

# 📡 API Example

## Input

```
{
  "user_id": 1,
  "timestamp": "2026-02-20T14:00:00",
  "temperature": 28,
  "humidity": 60,
  "aqi": 90,
  "occupancy": 3
}
```

## Output

```
{
  "energy_prediction_kwh": 1.82,
  "carbon_kg": 1.49,
  "recommendations": "Shift heavy appliances to off‑peak hours"
}
```

---

# 📊 Machine Learning Performance

Typical metrics:

• MAE
• RMSE
• R²
• MAPE

The model is trained on synthetic but realistic smart‑home data with noise and variability.

---

# 🌎 Real‑World Impact

This project can support:

• Carbon awareness
• Sustainable lifestyle
• Smart energy optimisation
• Climate policy insights

---

# 🔮 Future Enhancements

• Real IoT sensor integration
• Streaming predictions
• User segmentation
• SHAP explainability
• Cost optimisation
• Regional emission factors
• Database and authentication
