
class BotManager:
    def __init__(self, bot):
        self.bot = bot
        self.hello_text = 'Привет, я могу подсказать погоду. Напиши, какой город тебя интересует'
        self.reply_text = 'Не могу ответетить на это. В каком городе тебя интересует погода?'
        self.help_text = 'Напиши название города на русском. Я выведу погоду в нем на сегодня'

    def message_handler(self, message, weather):
        if message.text == "/start":
            self.send_welcome(message)
        elif message.text == "/help":
            self.send_help(message)
        else:
            try:
                self.send_temp(weather, message)
            except AttributeError:
                self.echo_all(message)

    def what_temp(self, weather, message):
        weather_manager = weather
        city = message.text
        coord = weather_manager.took_coord(city)
        temp = weather_manager.get_temp_now(coord)
        return city, temp

    def send_temp(self, weather, message):
        city, temp = self.what_temp(weather, message)
        return self.bot.send_message(message.from_user.id, f'Сейчас в городе {city}: {temp}°C')

    def send_welcome(self, message):
        return self.bot.send_message(message.from_user.id, self.hello_text)

    def send_help(self, message):
        return self.bot.send_message(message.from_user.id, self.help_text)

    def echo_all(self, message):
        return self.bot.reply_to(message, self.reply_text)



