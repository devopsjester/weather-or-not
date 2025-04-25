from abc import ABC, abstractmethod
from ..value_objects.weather import Weather
from ..value_objects.location import Location

class WeatherService(ABC):
    @abstractmethod
    def get_current_weather(self, location: Location) -> Weather:
        """Get current weather for a location"""
        pass