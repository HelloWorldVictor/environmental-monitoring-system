import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
AIRVISUAL_API_KEY = os.getenv("AIRVISUAL_API_KEY")


def get_weather_data(lat, lon):
    """Fetches weather data from OpenWeatherMap."""
    if not OPENWEATHER_API_KEY:
        raise ValueError(
            "OpenWeatherMap API key not found. Please set OPENWEATHER_API_KEY in your .env file."
        )

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url, timeout=5000)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print(f"Error decoding JSON from weather API. Response text: {response.text}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
