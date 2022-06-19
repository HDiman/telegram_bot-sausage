import requests
from bs4 import BeautifulSoup
import telebot
from auth_data import token

url_1 = "https://edadeal.ru/moskva/offers?retailer=5ka&retailer=ashan&retailer=auchan&retailer=auchan-city&retailer=dixy&retailer=globus&retailer=magnit-giper&retailer=magnit-univer&retailer=market-da&retailer=mgnl&retailer=miasnitskii_riad&retailer=perekrestok&retailer=verno&retailer=victoria&retailer=vkusvill_offline&segment=sausages&sort=aprice"
url_2 = "https://edadeal.ru/moskva/offers?page=2&retailer=5ka&retailer=ashan&retailer=auchan&retailer=auchan-city&retailer=dixy&retailer=globus&retailer=magnit-giper&retailer=magnit-univer&retailer=market-da&retailer=mgnl&retailer=miasnitskii_riad&retailer=perekrestok&retailer=verno&retailer=victoria&retailer=vkusvill_offline&segment=sausages&sort=aprice"
url_3 = "https://edadeal.ru/moskva/retailers/5ka"

headers = {
    "Accept": "*/*",
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
}

# --- Block for use only ones ---
req = requests.get(url=url_3, headers=headers)
response = req.text
print(response)

with open("index.html", "w") as file:
    file.write(response)
