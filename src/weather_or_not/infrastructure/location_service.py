import socket
import time
import requests
from ..domain.interfaces.location_service import LocationService
from ..domain.value_objects.location import Location

class OSMLocationService(LocationService):
    def __init__(self):
        self.headers = {"User-Agent": f"weather-cli-app/1.0 ({socket.gethostname()})"}

    def get_location_by_ip(self) -> Location:
        try:
            response = requests.get("http://ip-api.com/json/", timeout=10)
            response.raise_for_status()
            data = response.json()
            
            return Location(
                city=data["city"],
                state=data["regionName"],
                latitude=float(data["lat"]),
                longitude=float(data["lon"]),
                zipcode=data.get("zip")
            )
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to determine location: {str(e)}")

    def get_location_by_zipcode(self, zipcode: str) -> Location:
        try:
            # Rate limiting
            time.sleep(2)
            url = f"https://nominatim.openstreetmap.org/search?country=USA&postalcode={zipcode}&format=json&addressdetails=1"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if not data:
                raise RuntimeError(f"Could not find location for ZIP code {zipcode}")
                
            location_data = data[0]
            address = location_data["address"]
            
            return Location(
                city=address.get("city", address.get("town", address.get("village", "Unknown"))),
                state=address.get("state", "Unknown"),
                latitude=float(location_data["lat"]),
                longitude=float(location_data["lon"]),
                zipcode=zipcode
            )
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to lookup location: {str(e)}")