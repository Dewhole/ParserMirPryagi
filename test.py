import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib


HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0', 'accept': '*/*'}
HOST = 'https://www.mir-priaji.ru/'



def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    paginationTo = soup.find('div', class_='navigation-pages')
    if paginationTo:
        paginationTo = soup.find('div', class_='navigation-pages')
        pagination = paginationTo.find_all('a') 
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
            'kategory': soup.find('h1', id='pagetitle').get_text(strip=True),
            'image': HOST + (image),
            'kol-vo': item.find('span', class_='value').get_text(strip=True),
        })
    return catalog



def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Категория', 'Название', 'Наличие',])
        for item in items:
            writer.writerow([item['kategory'], item['title'], item['kol-vo']])


def parse():
    for URL in ['https://www.mir-priaji.ru/catalog/aksessuary_dlya_vyshivaniya/', 
    'https://www.mir-priaji.ru/catalog/applikatsii_termonakleyki/', 
    'https://www.mir-priaji.ru/catalog/bizhuteriya/', 
    'https://www.mir-priaji.ru/catalog/biseropletenie/', 
    'https://www.mir-priaji.ru/catalog/bumaga_gofrirovannaya/', 
    'https://www.mir-priaji.ru/catalog/businy/',
    'https://www.mir-priaji.ru/catalog/valyanie/',
    'https://www.mir-priaji.ru/catalog/dekor_dlya_doma/',
    'https://www.mir-priaji.ru/catalog/dekupazh/',
    'https://www.mir-priaji.ru/catalog/zagotovka_forma_dlya_tvorchestva/',
    'https://www.mir-priaji.ru/catalog/zakolka_zastezhka_dekorativnaya/',
    'https://www.mir-priaji.ru/catalog/igrushka_tekstilnaya/',
    'https://www.mir-priaji.ru/catalog/igry_igrovye_nabory_i_aksessuary_k_nim/',
    'https://www.mir-priaji.ru/catalog/kanva/'
    'https://www.mir-priaji.ru/catalog/kanitel_dlya_izgotovleniya_bizhuterii/'
    'https://www.mir-priaji.ru/catalog/kviling/',
    'https://www.mir-priaji.ru/catalog/kleevye_podkladochnye_materialy/',
    'https://www.mir-priaji.ru/catalog/kley_kleevye_pistolety/',
    'https://www.mir-priaji.ru/catalog/korobka_organayzer_boksy_dlya_melochey/',
    'https://www.mir-priaji.ru/catalog/kosmetika/',
    'https://www.mir-priaji.ru/catalog/kraski_i_sostavy/',
    'https://www.mir-priaji.ru/catalog/kryuchki_vyazalnye/',
    'https://www.mir-priaji.ru/catalog/lenta_atlasnaya/',
    'https://www.mir-priaji.ru/catalog/mashinki_i_komplektuyushchie/',
    'https://www.mir-priaji.ru/catalog/muline/',
    'https://www.mir-priaji.ru/catalog/nabory_dlya_vyshivaniya/',
    'https://www.mir-priaji.ru/catalog/nabory_dlya_tvorchestva/',
    'https://www.mir-priaji.ru/catalog/nozhi_i_maty/',
    'https://www.mir-priaji.ru/catalog/organza/',
    'https://www.mir-priaji.ru/catalog/osnovy_s_risunkom_dlya_vyshivaniya/',
    'https://www.mir-priaji.ru/catalog/perya/',
    'https://www.mir-priaji.ru/catalog/pechatnye_izdaniya/',
    'https://www.mir-priaji.ru/catalog/prirodnye_materialy/',
    'https://www.mir-priaji.ru/catalog/pryazha/',
    'https://www.mir-priaji.ru/catalog/pugovitsy/',
    'https://www.mir-priaji.ru/catalog/ramki_dlya_gotovykh_rabot/',
    'https://www.mir-priaji.ru/catalog/rasprodazha/',
    'https://www.mir-priaji.ru/catalog/skrapbuking_1/',
    'https://www.mir-priaji.ru/catalog/spitsy_vyazalnye/',
    'https://www.mir-priaji.ru/catalog/stendy/',
    'https://www.mir-priaji.ru/catalog/suvenirnaya_produktsiya/',
    'https://www.mir-priaji.ru/catalog/termomodelirovanie/',
    'https://www.mir-priaji.ru/catalog/tesma_kruzhevo_lenta/',
    'https://www.mir-priaji.ru/catalog/tovary_dlya_lepki/',
    'https://www.mir-priaji.ru/catalog/tovary_dlya_shitya_i_pechvorka/',
    'https://www.mir-priaji.ru/catalog/ukrasheniya_/',
    'https://www.mir-priaji.ru/catalog/upakovka/',
    'https://www.mir-priaji.ru/catalog/fatin/',
    'https://www.mir-priaji.ru/catalog/fetr/',
    'https://www.mir-priaji.ru/catalog/floristika/',
    'https://www.mir-priaji.ru/catalog/foamiran/',
    'https://www.mir-priaji.ru/catalog/furnitura/',
    'https://www.mir-priaji.ru/catalog/furnitura_dlya_igrushek/',
    'https://www.mir-priaji.ru/catalog/tsvety_buketiki_dekorativnye_/',
    'https://www.mir-priaji.ru/catalog/shkatulki_gazetnitsy_keysy_sumki_dlya_rukodeliya/',
    'https://www.mir-priaji.ru/catalog/shnury_dlya_rukodeliya/',
    'https://www.mir-priaji.ru/catalog/emalirovanie/',
    ]:

        html = get_html(URL)
        if html.status_code == 200:
            catalog = []
            pages_count = get_pages_count(html.text)
            for page in range (1, pages_count + 1):
                print(f'Парсинг страницы {page} {pages_count}...')
                html = get_html(URL, params={'page': page})
                catalog.extend(get_content(html.text))
                time.sleep(1)
            FILE = URL[34:-1] + '.csv'   
            save_file(catalog, FILE)


            print(f'Получено {len(catalog)} товаров')

        else:
            print('Error')    


parse()