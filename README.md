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

### From Source

1. Clone the repository:
```bash
git clone https://github.com/devopsjester/weather-or-not.git
cd weather-or-not
```

2. Install the package:
```bash
pip install .
```

### From Release

Download the pre-built binary for your platform from the [releases page](https://github.com/devopsjester/weather-or-not/releases).

## Usage

If installed from source:
```bash
# Show current location
weather where-is

# Show location for a ZIP code
weather where-is --zipcode 94105

# Show current weather for your location
weather current

# Show current weather for a ZIP code
weather current --zipcode 94105
```

If using the binary, replace `weather` with the binary name (e.g., `./weather-linux`, `./weather-macos`, or `weather-windows.exe`).

## Project Structure

The project follows clean architecture principles with the following layers:

- **Domain Layer**: Core business logic and interfaces
  - Value Objects: `Location`, `Weather`, `WeatherCondition`
  - Interfaces: Service interfaces for weather and location

- **Application Layer**: Use cases implementing business logic
  - Location and weather use cases

- **Infrastructure Layer**: External service implementations
  - OpenStreetMap location service
  - OpenMeteo weather service

- **Presentation Layer**: CLI interface using Click

## Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install development dependencies:
```bash
pip install -r requirements.txt
pip install -e .
```

## APIs Used

This application uses free, no-registration-required APIs:
- IP-based geolocation: ip-api.com
- Geocoding: OpenStreetMap Nominatim
- Weather data: Open-Meteo

## License

MIT License