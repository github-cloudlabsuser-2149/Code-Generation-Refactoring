import requests
import datetime

# Constants
API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
CITY = "Pilar,AR"  # Pilar, Buenos Aires, Argentina

def get_weather_data():
    # Request weather data from OpenWeatherMap API
    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data (HTTP {response.status_code})")
        return None

def parse_weather_data(data):
    # Extract and format weather data for the current and next 3 days
    forecast = {}
    today = datetime.datetime.now().date()

    for entry in data["list"]:
        date = datetime.datetime.fromtimestamp(entry["dt"]).date()
        if today <= date <= today + datetime.timedelta(days=3):
            if date not in forecast:
                forecast[date] = {
                    "max_temp": entry["main"]["temp_max"],
                    "min_temp": entry["main"]["temp_min"],
                    "sky_conditions": entry["weather"][0]["description"],
                    "rain_probability": entry.get("pop", 0) * 100  # Probability of precipitation
                }
            else:
                # Update max and min temperatures
                forecast[date]["max_temp"] = max(forecast[date]["max_temp"], entry["main"]["temp_max"])
                forecast[date]["min_temp"] = min(forecast[date]["min_temp"], entry["main"]["temp_min"])

    return forecast

def display_forecast(forecast):
    # Display the weather forecast
    print(f"Weather forecast for {CITY}:")
    for date, data in forecast.items():
        print(f"\nDate: {date}")
        print(f"  Max Temperature: {data['max_temp']}°C")
        print(f"  Min Temperature: {data['min_temp']}°C")
        print(f"  Sky Conditions: {data['sky_conditions']}")
        print(f"  Rain Probability: {data['rain_probability']}%")

def main():
    weather_data = get_weather_data()
    if weather_data:
        forecast = parse_weather_data(weather_data)
        display_forecast(forecast)

if __name__ == "__main__":
    main()