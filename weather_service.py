import requests
from datetime import datetime

API_KEY = 'YOUR_API_KEY'
CITIES = {
    'Delhi': '1273294',
    'Mumbai': '1275339',
    'Chennai': '1264527',
    'Bangalore': '1277333',
    'Kolkata': '1275004',
    'Hyderabad': '1269843'
}

def get_weather_data(city_id):
    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'city': data['name'],
            'temp': round(data['main']['temp'] - 273.15, 2),  # Kelvin to Celsius
            'feels_like': round(data['main']['feels_like'] - 273.15, 2),
            'main': data['weather'][0]['main'],
            'timestamp': datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
        }
    else:
        return None
