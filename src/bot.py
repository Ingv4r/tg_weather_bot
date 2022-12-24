class BotAnswers:
    def __init__(self, bot):
        self.bot = bot
        self.hello_text = 'Привет, я могу подсказать погоду. Напиши, какой город тебя интересует'
        self.reply_text = 'Не могу ответетить на это. В каком городе тебя интересует погода?'
        self.help_text = 'Напиши название города на русском. Я выведу погоду в нем на сегодня'

    def answer(self, message):
        if message.text == "/start":
            self.send_welcome(message)
        elif message.text == "/help":
            self.send_help(message)
        else:
            self.echo_all(message)

    def send_welcome(self, message):
        print(message.text)
        return self.bot.send_message(message.from_user.id, self.hello_text)

    def send_help(self, message):
        print(message.text)
        return self.bot.send_message(message.from_user.id, self.help_text)

    def echo_all(self, message):s
        print(message.text)
        return self.bot.reply_to(message, self.reply_text)
