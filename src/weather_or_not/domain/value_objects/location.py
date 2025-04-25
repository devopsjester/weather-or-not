from dataclasses import dataclass

@dataclass(frozen=True)
class Location:
    city: str
    state: str
    latitude: float
    longitude: float
    zipcode: str | None = None