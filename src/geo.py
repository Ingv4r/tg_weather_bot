from geopy import geocoders


class GeoPos:
    """Geo position object by coordinates."""
    def __init__(self, city: str):
        self.geolocator = geocoders.Nominatim(user_agent="telebot")
        self.latitude = self.geolocator.geocode(city, language='ru').latitude
        self.longitude = self.geolocator.geocode(city, language='ru').longitude

    def get_location(self):
        """Return latitude and longitude."""
        print(self.latitude, '\n', self.longitude)
        return self.latitude, self.longitude
