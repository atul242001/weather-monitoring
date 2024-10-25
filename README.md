# weather-monitoring

# Real-Time Weather Monitoring System

This project is a **Real-Time Weather Monitoring System** that fetches live weather data for major metro cities in India using the OpenWeatherMap API, processes it to provide insights through daily summaries, and issues alerts based on specified conditions. The application utilizes **FastAPI** for the backend API and **Jinja templates** for the frontend, displaying up-to-date weather data, historical trends, and daily summaries. 

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)


## Features

1. **Real-Time Weather Fetching**:
   - Fetches real-time weather data every 5 minutes for six Indian cities: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
   - Converts temperature from Kelvin to Celsius and stores it for further analysis.
   
2. **Data Processing and Aggregation**:
   - Provides daily weather summaries, including:
     - Average, minimum, and maximum temperatures.
     - Dominant weather conditions for each day.
   - Summarized data is stored for further analysis.

3. **Alerting Mechanism**:
   - Configurable alerting thresholds (e.g., if temperature exceeds 35°C).
   - Generates alerts and displays them if any threshold conditions are met.

4. **Visualization**:
   - Displays real-time weather data, daily summaries, and alerts on a simple, user-friendly web interface.

## Technologies Used

- **FastAPI**: Web framework for building APIs.
- **APScheduler**: For scheduling periodic tasks (fetching weather data).
- **Jinja2**: Templating for rendering HTML.
- **OpenWeatherMap API**: Data source for live weather information.

## Project Structure

weather-monitoring/
│
├── main.py                    # Main FastAPI application and backend logic
├── README.md                  # Project documentation
├── .gitignore                 # Git ignore file
├── requirements.txt           # List of dependencies
├── templates/
│   └── index.html             # Frontend Jinja template for displaying data
└── static/                    # Optional: Static assets (e.g., CSS/JS files if needed)
## Start the FastAPI application:
- **uvicorn main:app --reload**
