from src.geo import GeoPos


class WeatherManager:
    def __init__(self, weather_api):
        self.weather = weather_api

    def took_coord(self, city):
        coordinates = GeoPos(city).get_location()
        return coordinates

    def get_temp_now(self, city):
        coord = self.took_coord(city)
        temp = self.weather.forecast(coordinates=coord).fact.temp
        return temp

