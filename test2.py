import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib


HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0', 'accept': '*/*'}
HOST = 'https://www.mir-priaji.ru/'
URL = 'https://www.mir-priaji.ru/catalog/bumaga_gofrirovannaya/'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_html2(url, params=None):
    d = requests.get(url, headers=HEADERS, params=params)
    return d

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item_block')
    for item in items:
        ImageLargePage = item.find('a').get('href'),
        ImageLargePage2 = str(ImageLargePage)[3:-3]
        PageImageHref =str(HOST) + str(ImageLargePage2)
        html2 = get_html2(PageImageHref)
        get_content2(html2.text)
    
def get_content2(html2):
    soup2 = BeautifulSoup(html2, 'html.parser')
    items2 = soup2.find('li', class_='current')
    bb = items2.find('link').get('href')
    print(bb)
    items3 = soup2.find('div', class_='detail_text')
    text = items3.get_text
    print(text)
def parse():
        html = get_html(URL)
        if html.status_code == 200:
            get_content(html.text)
        else:
            print('Error')    


parse()