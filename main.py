import requests
from bs4 import BeautifulSoup
import random
import telebot
from auth_data import token


def get_data():
    rnd = random.randint(1, 26) # page number
    url = f"https://bbf.ru/quotes/?page={rnd}&tag=73"
    headers = {
        "Accept": "*/*",
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
    }
    list_quotes = []
    list_authors = []

    # --- Block to get data ---
    req = requests.get(url=url, headers=headers)
    response = req.text

    soup = BeautifulSoup(response, "lxml")
    quotes = soup.find_all(class_="sentence__body")
    authors = soup.find_all(class_="sentence__author")
    for quote in quotes:
        list_quotes.append(quote.text)
    for author in authors:
        list_authors.append(author.text)
    dict_quotes = dict(zip(list_quotes, list_authors))

    # for key, value in dict_quotes.items():
    #     print(f"{key}{value}")
    return dict_quotes


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Работаем")

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'g':
            try:
                quote, author = random.choice(list(get_data().items()))
                bot.send_message(message.chat.id, f"{quote}{author}")
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error!!!")
        else:
            bot.send_message(message.chat.id, "Талант. Безумие. Свобода")

    bot.polling()


if __name__ == "__main__":
    # get_data()
    telegram_bot(token=token)

