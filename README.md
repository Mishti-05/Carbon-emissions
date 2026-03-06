# Carbonly

An end-to-end AI + IoT-inspired system that predicts household energy usage, estimates carbon emissions, and provides personalized recommendations to reduce environmental impact.

This project demonstrates real-world machine learning, sustainability analytics, and production-ready deployment.

## Project Overview

The Smart Home Carbon Intelligence System is designed to help households monitor and reduce their carbon footprint through intelligent energy prediction and behavioral insights. By leveraging machine learning models trained on smart home data, the system forecasts energy consumption, converts it to carbon emissions, and offers actionable recommendations for sustainable living.

### Key Components

- **Data Processing**: Handles smart home sensor data including temperature, humidity, occupancy, and air quality.
- **Feature Engineering**: Creates time-series features, lag variables, and rolling statistics for accurate predictions.
- **Machine Learning Model**: Trains and evaluates models for energy consumption forecasting.
- **Carbon Pipeline**: Converts energy usage to carbon emissions using emission factors and predicts lifestyle-based carbon contributions.
- **Recommendations Engine**: Generates personalized tips based on usage patterns and carbon impact.
- **API Backend**: Provides a FastAPI-based REST API for real-time predictions and integrations.

## Features

### Machine Learning
- Time-series energy forecasting using historical data
- Feature engineering with lag features, rolling statistics, and categorical encoding
- Model evaluation with metrics like MAE, RMSE, and R²

### Carbon Tracking
- Real-time energy-to-carbon conversion
- Lifestyle carbon prediction based on transport, electricity, water, and flight usage
- Weekly carbon footprint estimation

### Personalized Recommendations
- Appliance usage optimization
- Behavioral nudges for sustainable habits

### Production API
- FastAPI backend for scalable deployments
- RESTful endpoints for predictions and recommendations

## Repository Structure

```
├── api/                    # FastAPI backend
│   ├── app.py             # Main API application
│   └── schemas.py         # Pydantic models
├── data/                  # Dataset files
├── models/                # Trained ML models
├── src/                   # Source code modules
│   └── smart_home/        # Core modules
├── carbon_pipeline.py     # Carbon calculation pipeline
├── data_processing.py     # Data loading and preprocessing
├── feature_engineering.py # Feature creation
├── main.py                # Main execution script
├── recommendations.py     # Recommendation logic
├── train_model.py         # Model training
├── requirements.txt       # Python dependencies
└── README.md              # This file

```
## Future Enhancements

- Real IoT sensor integration
- Streaming data processing
- User authentication and database
- Advanced explainability with SHAP
- Regional emission factors
- Cost optimization features
- Mobile app integration

