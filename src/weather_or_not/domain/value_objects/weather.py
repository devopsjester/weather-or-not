from dataclasses import dataclass
from enum import Enum

class WeatherCondition(Enum):
    CLEAR_SKY = "clear sky"
    MAINLY_CLEAR = "mainly clear"
    PARTLY_CLOUDY = "partly cloudy"
    OVERCAST = "overcast"
    FOGGY = "foggy"
    DEPOSITING_RIME_FOG = "depositing rime fog"
    LIGHT_DRIZZLE = "light drizzle"
    MODERATE_DRIZZLE = "moderate drizzle"
    DENSE_DRIZZLE = "dense drizzle"
    SLIGHT_RAIN = "slight rain"
    MODERATE_RAIN = "moderate rain"
    HEAVY_RAIN = "heavy rain"
    SLIGHT_SNOW = "slight snow fall"
    MODERATE_SNOW = "moderate snow fall"
    HEAVY_SNOW = "heavy snow fall"
    SNOW_GRAINS = "snow grains"
    SLIGHT_RAIN_SHOWERS = "slight rain showers"
    MODERATE_RAIN_SHOWERS = "moderate rain showers"
    VIOLENT_RAIN_SHOWERS = "violent rain showers"
    SLIGHT_SNOW_SHOWERS = "slight snow showers"
    HEAVY_SNOW_SHOWERS = "heavy snow showers"
    THUNDERSTORM = "thunderstorm"
    UNKNOWN = "unknown conditions"

    @classmethod
    def from_code(cls, code: int) -> "WeatherCondition":
        code_map = {
            0: cls.CLEAR_SKY,
            1: cls.MAINLY_CLEAR,
            2: cls.PARTLY_CLOUDY,
            3: cls.OVERCAST,
            45: cls.FOGGY,
            48: cls.DEPOSITING_RIME_FOG,
            51: cls.LIGHT_DRIZZLE,
            53: cls.MODERATE_DRIZZLE,
            55: cls.DENSE_DRIZZLE,
            61: cls.SLIGHT_RAIN,
            63: cls.MODERATE_RAIN,
            65: cls.HEAVY_RAIN,
            71: cls.SLIGHT_SNOW,
            73: cls.MODERATE_SNOW,
            75: cls.HEAVY_SNOW,
            77: cls.SNOW_GRAINS,
            80: cls.SLIGHT_RAIN_SHOWERS,
            81: cls.MODERATE_RAIN_SHOWERS,
            82: cls.VIOLENT_RAIN_SHOWERS,
            85: cls.SLIGHT_SNOW_SHOWERS,
            86: cls.HEAVY_SNOW_SHOWERS,
            95: cls.THUNDERSTORM,
        }
        return code_map.get(code, cls.UNKNOWN)

@dataclass(frozen=True)
class Weather:
    temperature_fahrenheit: float
    condition: WeatherCondition