from src.weather import WeatherManager


class BotManager:
    """
    Bot manager class.
    Sends messages through message_processor method.

    """
    def __init__(self, bot_api, weather_api):
        self.bot = bot_api
        self.weather_manager = WeatherManager(weather_api)
        self.hello_text = 'Привет, я могу подсказать погоду. Напиши, какой город тебя интересует'
        self.reply_text = 'Не могу ответетить на это. В каком городе тебя интересует погода?'
        self.help_text = 'Напиши название города на русском. Я выведу погоду в нем на сегодня'

    def message_processor(self, message):
        """Parse the incoming text and call the appropriate method."""
        if message.text == "/start":
            self.send_welcome(message)
        elif message.text == "/help":
            self.send_help(message)
        else:
            try:
                temp = self.weather_manager.get_temp_now(message.text)
                self.send_temp(message, temp)
                self.send_coord(message)
            except AttributeError:
                self.reply_to_message(message)

    def send_coord(self, city):
        """
        Determine the coordinates and send a link to the map, if city exist.

        """
        x, y = self.weather_manager.took_coord(city.text)
        return self.bot.send_message(city.from_user.id, f'Да, есть и такая область на карте {city.text}.\n'
                                                        f'Вот его расположение на карте:\n'
                                                        f'https://yandex.ru/maps/?ll={y},{x}&z=12')

    def send_temp(self, city, temp):
        """Send a temperature message by the city."""
        return self.bot.send_message(city.from_user.id, f'Сейчас в населённом пункте {city.text}: {temp}°C')

    def send_welcome(self, message):
        """Send a welcome message."""
        return self.bot.send_message(message.from_user.id, self.hello_text)

    def send_help(self, message):
        """Send a help text message."""
        return self.bot.send_message(message.from_user.id, self.help_text)

    def reply_to_message(self, message):
        """Send a reply to a message."""
        return self.bot.reply_to(message, self.reply_text)



