from abc import ABC, abstractmethod
from ..value_objects.location import Location

class LocationService(ABC):
    @abstractmethod
    def get_location_by_ip(self) -> Location:
        """Get location based on IP address"""
        pass

    @abstractmethod
    def get_location_by_zipcode(self, zipcode: str) -> Location:
        """Get location based on ZIP code"""
        pass