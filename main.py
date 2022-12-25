from yaweather import *
import telebot
from src.secrets_provider import SecretsProvider
from src.bot import BotManager
from src.weather import WeatherManager

provider = SecretsProvider()
# ---------------------
weather = YaWeather(api_key=provider.get_weather_token())
weather_manager = WeatherManager(weather)
# ---------------------
bot = telebot.TeleBot(provider.get_bot_token())
bot_manager = BotManager(bot)


@bot.message_handler(content_types=['text'])
def main(message):
    bot_manager.message_handler(message, weather_manager)


bot.polling(none_stop=True, interval=0)
