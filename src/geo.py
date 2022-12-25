from geopy import geocoders


class GeoPos:
    def __init__(self, city: str):
        self.geolocator = geocoders.Nominatim(user_agent="telebot")
        self.latitude = self.geolocator.geocode(city, language='ru').latitude
        self.longitude = self.geolocator.geocode(city, language='ru').longitude

    def get_location(self):
        print(self.latitude, '\n', self.longitude)
        return self.latitude, self.longitude
