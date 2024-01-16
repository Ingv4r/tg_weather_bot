from os import getenv
from dotenv import load_dotenv


load_dotenv()

class SecretsProvider(object):
    """Singleton class for secrets telegram token and yandex weather api key."""
    def __new__(cls, *args, **kwargs):
        """Return a singleton instance."""
        if not hasattr(cls, 'instance'):
            cls.instance = super(SecretsProvider, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        """Initial constructor. Keep secrets in the dictionary."""
        self.secrets = {}
        self._load_secrets()

    def get_bot_token(self) -> str:
        """Get the telegram bot token."""
        return self.secrets['bot_key']

    def get_weather_token(self) -> str:
        """Get the yandex weather api key."""
        return self.secrets['weather_key']

    def _load_secrets(self) -> None:
        """Load secrets from the .env file."""
        self.secrets['weather_key'] = getenv('YA_WEATHER_KEY')
        self.secrets['bot_key'] = getenv('TELEGRAM_TOKEN')
