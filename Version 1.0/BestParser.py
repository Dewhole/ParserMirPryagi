import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib
import fake_useragent
import dataAutorize

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0', 'accept': '*/*'}
session = requests.Session()
HOST = 'https://www.mir-priaji.ru/'
link = 'https://www.mir-priaji.ru/auth/?login=yes'
user = fake_useragent.UserAgent().random

header = {
    'user-agent': user
}

data = dataAutorize.data

responce = session.post(link, data=data, headers=header).text



def get_html(url, params=None):
    r = session.get(url, headers=header)
    return r

def get_html2(url, params=None):
    d = requests.get(url, headers=HEADERS, params=params)
    return d

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
        ImageLargePage = item.find('a').get('href'),
        ImageLargePage2 = str(ImageLargePage)[3:-3]
        PageImageHref =str(HOST) + str(ImageLargePage2)
        html2 = get_html2(PageImageHref)
  

        soup2 = BeautifulSoup(html2.text, 'html.parser')
        items2 = soup2.find('li', class_='current')
        bb = items2.find('link').get('href')        


        items3 = soup2.find('div', class_='detail_text')
        if items3:
            text = str(items3.get_text)

            text2 = text.replace('<br/>', '')

            text3 = text2.replace('</div>>', '')

            text4 = text3.replace('<bound method Tag.get_text of <div class="detail_text">', '')

        else:
            text4 = ''     


        cost = item.find('div', class_='js_price_wrapper price')
        numberOf = item.find('div', class_='js_price_wrapper price')
        if cost and numberOf:

            cost = cost.find('span', class_='values_wrapper')
            cost2 = cost.get_text()
            cost3 = cost2.replace(' руб.', '')
            cost123 = ''.join(cost3.split())

            
            intcost = float(cost123)
            cost5 = intcost * 0.5 + intcost

            cost5 = float('{:.0f}'.format(cost5))

            cost7 = str(cost5)
            cost8 = cost7[:-2]
            print(cost8)

            visible = 'visible'
            
            
            numberOf = numberOf.find('span', class_='price_measure')
            numberOf2 = 'руб. ' + numberOf.get_text()
            print(numberOf2)
        else:
            cost = 'Цену уточняйте' 
            numberOf = ' '


        catalog.append({
            'title': item.find('a', class_='dark_link').get_text(strip=True),
            'kategory': soup.find('h1', id='pagetitle').get_text(strip=True),
            'image': HOST + bb[1:],
            'kol-vo': item.find('span', class_='value').get_text(strip=True),
            'text': text4,
            'cost': cost8,
            'numberOf': numberOf2,
            'visible': visible
        })
    return catalog




def save_file(items, path):
    with open(path, 'w',  encoding='utf8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Категории', 'Имя', 'Изображения', 'Описание', 'Базовая цена', 'Видимость в каталоге'])
        for item in items:
            writer.writerow([item['kategory'], item['title'], item['image'], item['text'], item['cost'], item['visible']])

def parse():
    for URL in [


 'https://www.mir-priaji.ru/catalog/osnovy_s_risunkom_dlya_vyshivaniya/',
    'https://www.mir-priaji.ru/catalog/nabory_so_strazami/',
        'https://www.mir-priaji.ru/catalog/nabory_dlya_vyshivaniya_biserom_/',
            'https://www.mir-priaji.ru/catalog/kleevye_podkladochnye_materialy/',
                'https://www.mir-priaji.ru/catalog/kanitel_dlya_izgotovleniya_bizhuterii/',
                
             'https://www.mir-priaji.ru/catalog/aksessuary_dlya_vyshivaniya/',
                

    ]:

        html = get_html(URL)
        if html.status_code == 200:
            catalog = []
            pages_count = get_pages_count(html.text)
            for page in range (1, pages_count + 1):
                print(f'Парсинг страницы {page} {pages_count} {URL}...')
                html = get_html(URL, params={'page': page})
                catalog.extend(get_content(html.text))
                time.sleep(1)
            FILE = URL[34:-1] + ',' + '.csv'   
            save_file(catalog, FILE)


            print(f'Получено {len(catalog)} товаров')
        else:
            print('Error')    





parse()




""" 'https://www.mir-priaji.ru/catalog/applikatsii_termonakleyki/', 
    'https://www.mir-priaji.ru/catalog/bizhuteriya/', 
    'https://www.mir-priaji.ru/catalog/biseropletenie/', 
    'https://www.mir-priaji.ru/catalog/bumaga_gofrirovannaya/', 
    'https://www.mir-priaji.ru/catalog/nabory_so_strazami/'

    'https://www.mir-priaji.ru/catalog/valyanie/',
    'https://www.mir-priaji.ru/catalog/dekor_dlya_doma/',
    'https://www.mir-priaji.ru/catalog/dekupazh/',
    'https://www.mir-priaji.ru/catalog/zagotovka_forma_dlya_tvorchestva/',
    'https://www.mir-priaji.ru/catalog/zakolka_zastezhka_dekorativnaya/',
    'https://www.mir-priaji.ru/catalog/igrushka_tekstilnaya/',
    'https://www.mir-priaji.ru/catalog/igry_igrovye_nabory_i_aksessuary_k_nim/',
    'https://www.mir-priaji.ru/catalog/kanitel_dlya_izgotovleniya_bizhuterii/'
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
    'https://www.mir-priaji.ru/catalog/nabory_dlya_vyshivaniya_biserom_/'
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
    'https://www.mir-priaji.ru/catalog/kviling/',
    'https://www.mir-priaji.ru/catalog/kanva/' """


"""     'https://www.mir-priaji.ru/catalog/applikatsii_termonakleyki/', 
    'https://www.mir-priaji.ru/catalog/bizhuteriya/', 
    'https://www.mir-priaji.ru/catalog/biseropletenie/', 
    'https://www.mir-priaji.ru/catalog/bumaga_gofrirovannaya/', """