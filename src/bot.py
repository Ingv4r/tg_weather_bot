from src.weather import WeatherManager


class BotManager:
    def __init__(self, bot_api, weather_api):
        self.bot = bot_api
        self.weather_manager = WeatherManager(weather_api)
        self.hello_text = 'Привет, я могу подсказать погоду. Напиши, какой город тебя интересует'
        self.reply_text = 'Не могу ответетить на это. В каком городе тебя интересует погода?'
        self.help_text = 'Напиши название города на русском. Я выведу погоду в нем на сегодня'

    def message_processor(self, message):
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
        x, y = self.weather_manager.took_coord(city.text)
        print(x, y)
        return self.bot.send_message(city.from_user.id, f'Да, есть и такая область на карте {city.text}.\n'
                                                        f'Вот его расположение на карте:\n'
                                                        f'https://yandex.ru/maps/?ll={y},{x}&z=12')

    def send_temp(self, city, temp):
        return self.bot.send_message(city.from_user.id, f'Сейчас в населённом пункте {city.text}: {temp}°C')

    def send_welcome(self, message):
        return self.bot.send_message(message.from_user.id, self.hello_text)

    def send_help(self, message):
        return self.bot.send_message(message.from_user.id, self.help_text)

    def reply_to_message(self, message):
        return self.bot.reply_to(message, self.reply_text)



