import requests


API_KEY = "8251dbb012654b7c970190420250412"


WEATHER_URL = "https://api.weatherapi.com/v1/current.json"
FORECAST_URL = "https://api.weatherapi.com/v1/forecast.json"


def get_weather(city):
    """Fetch current weather from WeatherAPI"""
    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"
    }
    r = requests.get(WEATHER_URL, params=params, timeout=10)
    data = r.json()

    if r.status_code != 200:
        raise ValueError(data.get("error", {}).get("message", "Weather fetch failed"))

    return {
        "temperature": data["current"]["temp_c"],
        "humidity": data["current"]["humidity"],
        "rainfall": data["current"].get("precip_mm", 0)
    }


def get_forecast(city, days=7):
    """Fetch 7-day forecast from WeatherAPI"""
    params = {
        "key": API_KEY,
        "q": city,
        "days": days,
        "aqi": "no",
        "alerts": "no"
    }
    r = requests.get(FORECAST_URL, params=params, timeout=10)
    data = r.json()

    if r.status_code != 200:
        raise ValueError(data.get("error", {}).get("message", "Forecast fetch failed"))

    forecast_days = data["forecast"]["forecastday"]

    forecast = []
    for day in forecast_days:
        forecast.append({
            "date": day["date"],
            "temp": day["day"]["avgtemp_c"],
            "humidity": day["day"]["avghumidity"],
            "rain": day["day"]["totalprecip_mm"]
        })

    return forecast
