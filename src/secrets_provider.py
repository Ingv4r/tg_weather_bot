class SecretsProvider(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SecretsProvider, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.secrets = {}
        self._load_secrets()

    def get_bot_token(self):
        return self.secrets['bot_key']

    def get_weather_token(self):
        return self.secrets['weather_key']

    def _load_secrets(self):
        with open('apikeys.txt') as file:
            self.secrets['weather_key'] = file.readline().strip()
            self.secrets['bot_key'] = file.readline().strip()
