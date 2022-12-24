from yaweather import *
import telebot
from src.secrets_provider import SecretsProvider
from src.bot import BotAnswers
from src.geo import GeoPos

provider = SecretsProvider()
weather = YaWeather(api_key=provider.get_weather_token())
bot = telebot.TeleBot(provider.get_bot_token())


@bot.message_handler(content_types=['text'])
def bot_messages(message):
    answer = BotAnswers(bot)
    answer.answer(message)


bot.polling(none_stop=True, interval=0)


geo = GeoPos('Москва')
coordinates = geo.get_location()
res = weather.forecast(coord inates=coordinates).fact.temp

print(res)
