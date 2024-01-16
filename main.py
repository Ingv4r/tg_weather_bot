from yaweather import YaWeather
import telebot
from src.secrets_provider import SecretsProvider
from src.bot import BotManager


def main() -> None:
    """Main function. Create instances of all managers and tart bots polling."""
    provider = SecretsProvider()
    # ---------------------
    weather_api = YaWeather(api_key=provider.get_weather_token())
    bot_api = telebot.TeleBot(provider.get_bot_token())
    bot_manager = BotManager(bot_api, weather_api)

    @bot_api.message_handler(content_types=['text'])
    def bot_activity(message):
        """Handle incoming telegram messages."""
        bot_manager.message_processor(message)

    bot_api.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    main()
