# Telegram weather bot
[![Python](https://img.shields.io/badge/Python-v3.10.0-blue)](https://www.python.org/) 
[![Telebot](https://img.shields.io/badge/pyTelegramBotAPI-v4.8.0-green)](https://pypi.org/project/pyTelegramBotAPI/)
[![Yaweather](https://img.shields.io/badge/yaweather-v1.2.2-red)](https://pypi.org/project/yaweather/)

## Описание проекта
Телеграм бот на питоне с использованим библиотеки pyTelegramBotAPI(telebot) и открытого api Яндекса yaweather.
Возможо получать от бота по запросу прогноз погоды по названию города. Бот может проверять, существует ли введенный город
и может прислать его координаты, а так же ссылку на карты.

## Запуск проекта
1. Клонировать репозиторий и перейти в него в командной строке:
   ```
   git clone https://github.com/Ingv4r/tg_weather_bot.git
   ```
   ```
   cd tg_weather_bot
   ```
2. Cоздать и активировать виртуальное окружение
   ```
   py -3.10 -m venv venv # Для Windows
   python3 -3.10 -m venv venv # Для Linux и macOS
   ```
   ```
   source venv/Scripts/activate # Для Windows
   source venv/bin/activate # Для Linux и macOS
   ```
3. Установите зависимости из файла requirements.txt
   ```
   pip install -r requirements.txt
   ```
4. Перейдите в дирректорию src и создайте там .env файл для хранения api токена вашего telegram бота и ключа yaweather.
(Сначала вам потребует получить эти ключи через @BotFather в telegram и на странице документации yaweather https://developer.tech.yandex.ru/services/18)
   ```
   cd src
   ```
   - для Windows:
   ```
   copy con .env
   YA_WEATHER_KEY=<your api key>
   TELEGRAM_TOKEN=<your api token>^Z
   ```
   - для Для Linux и macOS:
   ```
   nano .env
   YA_WEATHER_KEY=<your api key>
   TELEGRAM_TOKEN=<your api token>
   ```

## Пример работы с ботом
Для начала работы просто напишите боту название города на русском языке. И если такой город есть, бот выведет погоду и ссылку на карту.  
![image](https://github.com/Ingv4r/tg_weather_bot/assets/87081544/a0fdb068-723f-4add-ade6-e7389a4e6de5)
