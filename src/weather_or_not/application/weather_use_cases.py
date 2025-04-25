from ..domain.interfaces.weather_service import WeatherService
from ..domain.value_objects.location import Location
from ..domain.value_objects.weather import Weather

class WeatherUseCases:
    def __init__(self, weather_service: WeatherService):
        self._weather_service = weather_service

    def get_current_weather(self, location: Location) -> Weather:
        """Get current weather for a location"""
        return self._weather_service.get_current_weather(location)