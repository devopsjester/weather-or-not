import requests
from ..domain.interfaces.weather_service import WeatherService
from ..domain.value_objects.weather import Weather, WeatherCondition
from ..domain.value_objects.location import Location

class OpenMeteoWeatherService(WeatherService):
    def get_current_weather(self, location: Location) -> Weather:
        try:
            url = (
                f"https://api.open-meteo.com/v1/forecast"
                f"?latitude={location.latitude}"
                f"&longitude={location.longitude}"
                f"&current=temperature_2m,weather_code"
                f"&temperature_unit=fahrenheit"
            )
            response = requests.get(url)
            response.raise_for_status()
            
            data = response.json()["current"]
            return Weather(
                temperature_fahrenheit=round(data["temperature_2m"]),
                condition=WeatherCondition.from_code(data["weather_code"])
            )
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch weather data: {str(e)}")