import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define the start and end dates for the dataset
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)

# Generate date range
date_range = pd.date_range(start=start_date, end=end_date, freq='H')

# Generate synthetic data for temperature, humidity, and rainfall
temperature = np.random.normal(25, 5, len(date_range))  # Mean temperature of 25°C with standard deviation of 5°C
humidity = np.random.normal(60, 10, len(date_range))    # Mean humidity of 60% with standard deviation of 10%
rainfall = np.random.randint(0, 10, len(date_range))    # Random rainfall values between 0 and 10 mm

# Create DataFrame
weather_data = pd.DataFrame({
    'Date': date_range,
    'Temperature (C)': temperature,
    'Humidity (%)': humidity,
    'Rainfall (mm)': rainfall
})

# Save the dataset to a CSV file
weather_data.to_csv('weather_data.csv', index=False)
