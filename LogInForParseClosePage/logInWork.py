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
	"backurl": "/auth/",
	"AUTH_FORM": "Y",
	"TYPE": "AUTH",
	"POPUP_AUTH": "N",
	"USER_LOGIN": "xxxxxxx@mail.ru",
	"USER_PASSWORD": "xxxxxxxx",
	"Login": [
		"Войти",
		"Войти"
	]
}


responce = session.post(link, data=data, headers=header).text

href = 'https://www.mir-priaji.ru/catalog/kanitel_dlya_izgotovleniya_bizhuterii/?PAGEN_1=2'
progile_responce = session.get(href, headers=header).text

print(progile_responce)
with open("hh_success1.html","w",encoding="utf-8") as f:
    f.write(progile_responce)