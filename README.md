# Smart Home Carbon Intelligence System

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
- **Dashboard**: Interactive Streamlit app for visualization and monitoring.

## Features

### Machine Learning
- Time-series energy forecasting using historical data
- Feature engineering with lag features, rolling statistics, and categorical encoding
- Model evaluation with metrics like MAE, RMSE, and R²

### Carbon Tracking
- Real-time energy-to-carbon conversion
- Lifestyle carbon prediction based on transport, electricity, water, and flight usage
- Weekly and annual carbon footprint estimation

### Personalized Recommendations
- Appliance usage optimization
- Peak hour scheduling suggestions
- Behavioral nudges for sustainable habits

### Explainability
- Feature importance analysis
- Model interpretation for transparency

### Production API
- FastAPI backend for scalable deployments
- RESTful endpoints for predictions and recommendations
- Automatic documentation with Swagger UI

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

## Installation and Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Mishti-05/Carbon-emissions.git
   cd Carbon-emissions
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the main pipeline:
   ```bash
   python main.py
   ```

## Usage

### Training the Model
Run the training script to build and evaluate the energy prediction model:
```bash
python train_model.py
```

### Running the API
Start the FastAPI server:
```bash
uvicorn api.app:app --reload
```
Access the API documentation at `http://127.0.0.1:8000/docs`

### Example API Request
```json
{
  "energy_kwh": 3.06,
  "transport_km": 800,
  "electricity_consumption": 3.0,
  "water_usage": 1.0,
  "flights_taken": 1.0
}
```

## Model Performance

The energy prediction model achieves:
- **MAE**: ~0.2 kWh
- **RMSE**: ~0.3 kWh
- **R²**: >0.85

Trained on synthetic smart home data with realistic noise and variability.

## Future Enhancements

- Real IoT sensor integration
- Streaming data processing
- User authentication and database
- Advanced explainability with SHAP
- Regional emission factors
- Cost optimization features
- Mobile app integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open-source. Please check the license file for details.

## Contact

For questions or collaborations, feel free to open an issue or contact the maintainers.
