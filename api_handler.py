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


def get_air_quality_data(lat, lon):
    """Fetches air quality data from AirVisual."""
    if not AIRVISUAL_API_KEY:
        raise ValueError(
            "AirVisual API key not found. Please set AIRVISUAL_API_KEY in your .env file."
        )

    url = f"http://api.airvisual.com/v2/nearest_city?lat={lat}&lon={lon}&key={AIRVISUAL_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print(f"Error decoding JSON from AirVisual API. Response text: {response.text}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching air quality data: {e}")
        return None


def fetch_and_parse_data(lat=35.6895, lon=139.6917):  # Default to Tokyo
    """Fetches and parses data from all configured APIs."""
    weather_raw = get_weather_data(lat, lon)
    air_quality_raw = get_air_quality_data(lat, lon)

    # --- Parse and combine data into a standardized format ---
    parsed_data = {}

    # Parse weather data
    if weather_raw and "main" in weather_raw:
        parsed_data["temperature"] = weather_raw["main"].get("temp")
        parsed_data["humidity"] = weather_raw["main"].get("humidity")

    # Parse air quality data
    if (
        air_quality_raw
        and air_quality_raw.get("data")
        and air_quality_raw["data"].get("current")
        and air_quality_raw["data"]["current"].get("pollution")
    ):
        pollution = air_quality_raw["data"]["current"]["pollution"]

        # PM2.5 (using aqius if mainus is p2)
        if pollution.get("mainus") == "p2" and pollution.get("aqius") is not None:
            parsed_data["pm25"] = pollution["aqius"]
        else:
            parsed_data["pm25"] = None  # Explicitly set to None if not found

        # CO (no direct equivalent in current raw data, keeping as None)
        parsed_data["co"] = None

        # PM10 (using aqicn if maincn is p1)
        if pollution.get("maincn") == "p1" and pollution.get("aqicn") is not None:
            parsed_data["pm10"] = pollution["aqicn"]
        else:
            parsed_data["pm10"] = None  # Explicitly set to None if not found
    else:
        parsed_data["pm25"] = None
        parsed_data["co"] = None
        parsed_data["pm10"] = None

    # CO2 (still a placeholder as AirVisual API typically doesn't provide it)
    parsed_data.setdefault("co2", 450)  # Placeholder

    return parsed_data
