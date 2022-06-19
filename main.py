import requests
from bs4 import BeautifulSoup
import telebot
from auth_data import token


def get_data():
    url_parsing = ""
    headers = {
        "Accept": "*/*",
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
    }

    # --- Block to get data ---
    req = requests.get(url=url_parsing, headers=headers)
    response = req.text

    soup = BeautifulSoup(response, "lxml")
    all_title = soup.find_all(class_="g-user-content")
    return all_title


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Code to solve problems")

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'hh':
            try:
                all_title = get_data()
                for title in all_title:
                    bot.send_message(message.chat.id, title.text)
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Disconnection!!!")
        else:
            bot.send_message(message.chat.id, "More coding")

    bot.polling()


if __name__ == "__main__":
    telegram_bot(token=token)