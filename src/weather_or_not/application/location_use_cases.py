from ..domain.interfaces.location_service import LocationService
from ..domain.value_objects.location import Location

class LocationUseCases:
    def __init__(self, location_service: LocationService):
        self._location_service = location_service

    def get_location(self, zipcode: str | None = None) -> Location:
        """Get location either by ZIP code or IP address"""
        if zipcode:
            return self._location_service.get_location_by_zipcode(zipcode)
        return self._location_service.get_location_by_ip()