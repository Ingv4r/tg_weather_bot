from src.geo import GeoPos


class WeatherManager:
    """Manager class for yandex weather api."""
    def __init__(self, weather_api) -> None:
        """Initialize the weather manager."""
        self.weather = weather_api

    def took_coord(self, city):
        """Return the coordinates of the given city."""
        coordinates = GeoPos(city).get_location()
        return coordinates

    def get_temp_now(self, city):
        """Return the temperature of the given city."""
        coord = self.took_coord(city)
        temp = self.weather.forecast(coordinates=coord).fact.temp
        return temp

