#!/usr/bin/env python3
import click
import requests
import socket
import time


def get_location_info(zipcode=None):
    headers = {"User-Agent": f"weather-cli-app/1.0 ({socket.gethostname()})"}

    if zipcode:
        click.echo(f"Looking up ZIP code {zipcode}...", err=True)
        time.sleep(2)  # More conservative rate limiting
        url = f"https://nominatim.openstreetmap.org/search?country=USA&postalcode={zipcode}&format=json&addressdetails=1"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if not response.ok:
                click.echo(
                    f"Error: API request failed with status {response.status_code}"
                )
                exit(1)

            data = response.json()
            if not data:
                click.echo(f"Error: Could not find location for ZIP code {zipcode}")
                exit(1)

            address = data[0]["address"]
            return {
                "city": address.get(
                    "city", address.get("town", address.get("village", "Unknown"))
                ),
                "state": address.get("state", "Unknown"),
                "lat": float(data[0]["lat"]),
                "lng": float(data[0]["lon"]),
                "zipcode": zipcode,
            }
        except requests.exceptions.RequestException as e:
            click.echo(f"Error: Failed to lookup location: {str(e)}")
            exit(1)
    else:
        try:
            ip_response = requests.get("http://ip-api.com/json/", timeout=10)
            if not ip_response.ok:
                click.echo("Error: Could not determine current location")
                exit(1)
            data = ip_response.json()
            return {
                "city": data["city"],
                "state": data["regionName"],
                "lat": data["lat"],
                "lng": data["lon"],
                "zipcode": data.get("zip", "Unknown"),
            }
        except requests.exceptions.RequestException as e:
            click.echo(f"Error: Failed to determine current location: {str(e)}")
            exit(1)


def get_weather(lat, lng):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&current=temperature_2m,weather_code&temperature_unit=fahrenheit"
    response = requests.get(url)
    if response.status_code != 200:
        click.echo("Error: Could not fetch weather data")
        exit(1)
    return response.json()["current"]


def get_weather_condition(code):
    # Simplified weather code mapping
    conditions = {
        0: "clear sky",
        1: "mainly clear",
        2: "partly cloudy",
        3: "overcast",
        45: "foggy",
        48: "depositing rime fog",
        51: "light drizzle",
        53: "moderate drizzle",
        55: "dense drizzle",
        61: "slight rain",
        63: "moderate rain",
        65: "heavy rain",
        71: "slight snow fall",
        73: "moderate snow fall",
        75: "heavy snow fall",
        77: "snow grains",
        80: "slight rain showers",
        81: "moderate rain showers",
        82: "violent rain showers",
        85: "slight snow showers",
        86: "heavy snow showers",
        95: "thunderstorm",
    }
    return conditions.get(code, "unknown conditions")


@click.group()
def cli():
    """Weather CLI application"""
    pass


@cli.command()
@click.option("--zipcode", help="ZIP code to look up")
def where_is(zipcode):
    """Show the city and state for a location"""
    location = get_location_info(zipcode)
    click.echo(f"{location['zipcode']} is in {location['city']}, {location['state']}.")


@cli.command()
@click.option("--zipcode", help="ZIP code to look up weather for")
def current(zipcode):
    """Show current weather conditions"""
    location = get_location_info(zipcode)
    weather_data = get_weather(location["lat"], location["lng"])
    condition = get_weather_condition(weather_data["weather_code"])
    temp = round(weather_data["temperature_2m"])
    click.echo(
        f"It is currently {temp}ºF, and {condition} in {location['city']}, {location['state']}."
    )


if __name__ == "__main__":
    cli()
