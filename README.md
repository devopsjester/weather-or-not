# Weather Or Not

A simple CLI weather app that shows location and current weather information based on ZIP code or current location.

## Features

- `where-is`: Shows city and state information
  - Without arguments: Uses your current location
  - With `--zipcode`: Shows location for a specific ZIP code

- `current`: Shows current weather conditions
  - Without arguments: Shows weather for your current location
  - With `--zipcode`: Shows weather for a specific ZIP code

## Installation

1. Clone the repository:
```bash
git clone https://github.com/devopsjester/weather-or-not.git
cd weather-or-not
```

2. Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
# Show current location
./weather.py where-is

# Show location for a ZIP code
./weather.py where-is --zipcode 94105

# Show current weather for your location
./weather.py current

# Show current weather for a ZIP code
./weather.py current --zipcode 94105
```

## APIs Used

This application uses free, no-registration-required APIs:
- IP-based geolocation: ip-api.com
- Geocoding: OpenStreetMap Nominatim
- Weather data: Open-Meteo

## License

MIT License