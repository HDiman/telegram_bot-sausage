import requests
from bs4 import BeautifulSoup
import random
import telebot
from auth_data import token


def get_data():
    url = "https://www.forbes.ru/forbeslife/dosug/262327-na-vse-vremena-100-vdokhnovlyayushchikh-tsitat"
    headers = {
        "Accept": "*/*",
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
    }
    list = []
    # --- Block to get data ---
    req = requests.get(url=url, headers=headers)
    response = req.text

    soup = BeautifulSoup(response, "lxml")
    context = soup.find_all(class_="yl27R")
    for item in context:
        list.append(item.text)
    return list

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Работаем")

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'g':
            try:
                rnd = random.randrange(0, 100, 2)
                text_data = get_data()[rnd] + " " + "(" + get_data()[rnd+1] + ")"
                bot.send_message(message.chat.id, text_data)
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error!!!")
        else:
            bot.send_message(message.chat.id, "Талант. Безумие. Свобода")

    bot.polling()


if __name__ == "__main__":
    telegram_bot(token=token)
    # list = get_data()
    # for _ in range(200):
    #     rnd = random.randrange(0, 200, 2)
    #     print(list[rnd] + " " + "(" + list[rnd+1] + ")")
