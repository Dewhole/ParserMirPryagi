import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib
import fake_useragent

session = requests.Session()

link = 'https://www.mir-priaji.ru/auth/?login=yes'
user = fake_useragent.UserAgent().random

header = {
    'user-agent': user
}

data = {
    'backurl': '/auth/',
    'AUTH_FORM': 'Y',
    'TYPE': 'AUTH',
    'POPUP_AUTH': 'N',
    'username': 'xxxxxx@mail.ru',
    'password': 'xxxxx',
    'Login': 'Войти',
    'Login': 'Войти',
}

responce = session.post(link, data=data, headers=header).text

href = 'https://www.mir-priaji.ru/personal/'
progile_responce = session.get(href, headers=header).text

print(progile_responce)
with open("hh_success.html","w",encoding="utf-8") as f:
    f.write(progile_responce)