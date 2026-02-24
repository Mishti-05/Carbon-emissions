import numpy as np

def weather(hour, day_of_year):
    seasonal_temp = 25 + 10 * np.sin(2 * np.pi * day_of_year / 365)
    daily_temp = 5 * np.sin(2 * np.pi * hour / 24)

    temperature = seasonal_temp + daily_temp + np.random.normal(0, 1)

    humidity = np.clip(np.random.normal(60, 10), 30, 90)
    aqi = np.clip(np.random.normal(90, 25), 40, 200)

    return temperature, humidity, aqi
