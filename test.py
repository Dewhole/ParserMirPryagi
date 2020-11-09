import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib

URL = 'https://www.mir-priaji.ru/catalog/aksessuary_dlya_vyshivaniya/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0', 'accept': '*/*'}
HOST = 'https://www.mir-priaji.ru/'
FILE = 'catalog.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    paginationTo = soup.find('div', class_='navigation-pages')
    pagination = paginationTo.find_all('a')
    print(pagination)
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item_block col-4 col-md-3 col-sm-6 col-xs-6')

    catalog = []
    for item in items:
        image = str(item.find('img'))
        cost = item.find('span', class_='grey size13')
        if cost:
            cost = cost.get_text()
        else:
            cost = 'Цену уточняйте' 


        catalog.append({
            'title': item.find('a', class_='dark_link').get_text(strip=True),

            'image': HOST + (image),
            'kol-vo': item.find('span', class_='value').get_text(strip=True),
        })
    return catalog


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Изображение', 'Наличие',])
        for item in items:
            writer.writerow([item['title'], item['image'], item['kol-vo']])


def parse():
    """ URL = input('Введите URL: ')
    URL = URL.strip() """
    html = get_html(URL)
    if html.status_code == 200:
        catalog = []
        pages_count = get_pages_count(html.text)
        for page in range (1, pages_count + 1):
            print(f'Парсинг страницы {page} {pages_count}...')
            html = get_html(URL, params={'page': page})
            catalog.extend(get_content(html.text))
            time.sleep(1)

        save_file(catalog, FILE)


        print(f'Получено {len(catalog)} товаров')

    else:
        print('Error')    


parse()