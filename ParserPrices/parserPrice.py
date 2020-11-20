import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib
import fake_useragent
import dataAutorize


session = requests.Session()

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
    print(items)
    catalog = []
    for item in items:
        cost = item.find('div', class_='js_price_wrapper price')
        numberOf = item.find('div', class_='js_price_wrapper price')
        if cost and numberOf:
             
            cost = cost.find('span', class_='values_wrapper')
            cost2 = cost.get_text()

            numberOf = numberOf.find('span', class_='price_measure')
            numberOf2 = numberOf.get_text()
            print(cost2)
            print(numberOf2)
            price = str(cost2) + ' ' + str(numberOf2)
        else:
            price = 'Цену уточняйте' 


        catalog.append({
            'cost': price

        })
    return catalog




def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='`')
        writer.writerow(['Цена'])
        for item in items:
            writer.writerow([item['cost']])

def parse():
    for URL in [

    'https://www.mir-priaji.ru/catalog/bumaga_gofrirovannaya/',
    'https://www.mir-priaji.ru/catalog/applikatsii_termonakleyki/', 
    'https://www.mir-priaji.ru/catalog/bizhuteriya/', 
    'https://www.mir-priaji.ru/catalog/biseropletenie/', 
    'https://www.mir-priaji.ru/catalog/bumaga_gofrirovannaya/', 
    'https://www.mir-priaji.ru/catalog/nabory_so_strazami/'
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
    'https://www.mir-priaji.ru/catalog/nabory_dlya_vyshivaniya_biserom_/'
    'https://www.mir-priaji.ru/catalog/kanva/'
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
    'https://www.mir-priaji.ru/catalog/kanva/'

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
            FILE = URL[34:-1] + 'price' + '.csv'   
            save_file(catalog, FILE)


            print(f'Получено {len(catalog)} товаров')

        else:
            print('Error')    


parse()

"""     'https://www.mir-priaji.ru/catalog/applikatsii_termonakleyki/', 
    'https://www.mir-priaji.ru/catalog/bizhuteriya/', 
    'https://www.mir-priaji.ru/catalog/biseropletenie/', 
    'https://www.mir-priaji.ru/catalog/bumaga_gofrirovannaya/', 
    'https://www.mir-priaji.ru/catalog/nabory_so_strazami/'
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
    'https://www.mir-priaji.ru/catalog/nabory_dlya_vyshivaniya_biserom_/'
    'https://www.mir-priaji.ru/catalog/kanva/'
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


