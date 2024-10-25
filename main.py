import httpx
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

# OpenWeatherMap API key
API_KEY = "e05b30e62c70d7391f9790ecc0303ccf"  # Your API key here

# Metros in India with their latitude and longitude
METROS = {
    'Delhi': (28.6139, 77.2090),
    'Mumbai': (19.0760, 72.8777),
    'Chennai': (13.0827, 80.2707),
    'Bangalore': (12.9716, 77.5946),
    'Kolkata': (22.5726, 88.3639),
    'Hyderabad': (17.3850, 78.4867),
}

@app.get("/")
async def get_weather_data(request: Request):
    weather_data = []

    # Fetch weather data for all metros
    async with httpx.AsyncClient() as client:
        for city, (lat, lon) in METROS.items():
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
            response = await client.get(url)
            data = response.json()
            
            # Log the full response for debugging
            print(f"API response for {city}: {data}")
            
            # Ensure the API response contains the required weather information
            if "main" in data and "weather" in data:
                weather_data.append({
                    "city": city,
                    "temp": data["main"]["temp"],
                    "feels_like": data["main"]["feels_like"],
                    "condition": data["weather"][0]["description"],
                    "temp_min": data["main"]["temp_min"],
                    "temp_max": data["main"]["temp_max"]
                })
            else:
                print(f"No weather data for {city}. Response: {data}")

    # Pass the weather data to the Jinja2 template
    return templates.TemplateResponse("index.html", {"request": request, "weather_data": weather_data})
