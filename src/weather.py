from src.geo import GeoPos


class WeatherManager:
    def __init__(self, weather):
        self.weather = weather

    def took_coord(self, city):
        coordinates = GeoPos(city).get_location()
        return coordinates

    def get_temp_now(self, coord):
        temp = self.weather.forecast(coordinates=coord).fact.temp
        return temp

