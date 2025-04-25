import click
from ..application.location_use_cases import LocationUseCases
from ..application.weather_use_cases import WeatherUseCases
from ..infrastructure.location_service import OSMLocationService
from ..infrastructure.weather_service import OpenMeteoWeatherService

# Initialize services and use cases
location_service = OSMLocationService()
weather_service = OpenMeteoWeatherService()
location_use_cases = LocationUseCases(location_service)
weather_use_cases = WeatherUseCases(weather_service)

@click.group()
def cli():
    """Weather CLI application"""
    pass

@cli.command()
@click.option("--zipcode", help="ZIP code to look up")
def where_is(zipcode: str | None):
    """Show the city and state for a location"""
    try:
        location = location_use_cases.get_location(zipcode)
        click.echo(f"{location.zipcode or 'Your location'} is in {location.city}, {location.state}.")
    except RuntimeError as e:
        click.echo(f"Error: {str(e)}", err=True)
        exit(1)

@cli.command()
@click.option("--zipcode", help="ZIP code to look up weather for")
def current(zipcode: str | None):
    """Show current weather conditions"""
    try:
        location = location_use_cases.get_location(zipcode)
        weather = weather_use_cases.get_current_weather(location)
        click.echo(
            f"It is currently {weather.temperature_fahrenheit}ºF, and "
            f"{weather.condition.value} in {location.city}, {location.state}."
        )
    except RuntimeError as e:
        click.echo(f"Error: {str(e)}", err=True)
        exit(1)