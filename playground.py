import requests
from bs4 import BeautifulSoup
import telebot
from auth_data import token


def get_data():
    url_parsing = "https://edadeal.ru/moskva/offers?page=1&retailer=5ka&retailer=ashan&retailer=auchan&retailer=auchan-city&retailer=dixy&retailer=globus&retailer=magnit-giper&retailer=magnit-univer&retailer=market-da&retailer=mgnl&retailer=miasnitskii_riad&retailer=perekrestok&retailer=verno&retailer=victoria&retailer=vkusvill_offline&segment=sausages&sort=aprice"
    headers = {
        "Accept": "*/*",
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
    }

    # --- Block to get data ---
    # req = requests.get(url=url_parsing, headers=headers)
    # response = req.text
    #
    # soup = BeautifulSoup(response, "lxml")
    # products = soup.find_all(class_="b-offer__root")
    # for product in products:
    #     print(product.text)

    # --- Block for use only ones ---
    req = requests.get(url=url_parsing, headers=headers)
    response = req.text
    # print(response)

    with open("index.html", "w") as file:
        file.write(response)

    # with open("index.html", "r") as file:
    #     src = file.read()
    #
    # soup = BeautifulSoup(src, "lxml")
    #
    # all_title = soup.find_all(class_="yl27R")
    # for title in all_title:
    #     print(title.text)





# def telegram_bot(token):
#     bot = telebot.TeleBot(token)
#
#     @bot.message_handler(commands=['start'])
#     def start_message(message):
#         bot.send_message(message.chat.id, "Работаем")
#
#     @bot.message_handler(content_types=['text'])
#     def send_text(message):
#         if message.text.lower() == 'ss':
#             try:
#                 all_title = get_data()
#                 for title in all_title:
#                     bot.send_message(message.chat.id, title.text)
#             except Exception as ex:
#                 print(ex)
#                 bot.send_message(message.chat.id, "Disconnection!!!")
#         else:
#             bot.send_message(message.chat.id, "Голоден? )) Набирай: 'ss'")
#
#     bot.polling()
#
#
# if __name__ == "__main__":
#     telegram_bot(token=token)

get_data()