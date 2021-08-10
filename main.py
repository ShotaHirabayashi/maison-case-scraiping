import csv

import requests
from bs4 import BeautifulSoup
import ssl
import time
import os
import sys

ssl._create_default_https_context = ssl._create_unverified_context

# カレントディレクトリ取得
d = os.path.dirname(sys.argv[0])


def get_tiam():
    # タイトル、画像URL、価格、詳細ページURL
    print(d)
    print("================")

    with open(d + "/tiam.csv", "w", encoding='utf-8') as file:
        writer = csv.writer(file)
        try:
            response = requests.get(f'https://tiam.official.ec/10', headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
            bsObj = BeautifulSoup(response.content, "html.parser")
            product_section = bsObj.find('section', {'id': 'mainContent'})
            product_list_div = product_section.find_all(
                'div', {'class': 'item'})
            for item in product_list_div:
                csvRow = []
                title = item.find('div', {'class': 'itemTitle'}).get_text()
                print(title)
                price = item.find('li', {'class': 'itemPrice'}).get_text()
                print(price)
                img_url = item.find('img').get('src')
                print(img_url)
                url = item.find('a').get('href')
                print(url)

                csvRow.append(title)
                csvRow.append(price)
                csvRow.append(img_url)
                csvRow.append(url)
                writer.writerow(csvRow)
            time.sleep(2)
        except Exception as e:
            print(e)


def get_her_mosa():
    # タイトル、画像URL、価格、詳細ページURL

    with open(d + "/her-mosa.csv", "w", encoding='utf-8') as file:
        writer = csv.writer(file)
        try:
            response = requests.get(f'https://hermosa2.thebase.in/10', headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
            bsObj = BeautifulSoup(response.content, "html.parser")

            product_section = bsObj.find_all('section', {'id': 'products'})
            product_li = bsObj.find_all('li', {'class': 'product_list'})
            print(len(product_li))
            for item in product_li:
                csvRow = []
                title = item.find('h2').get_text().strip()
                print(title)
                price = item.find(
                    'div', {'class': 'price'}).get_text().strip()

                print(price)

                img_url = item.find('img').get('src')
                print(img_url)

                url = item.find('a').get('href')
                print(url)

                csvRow.append(title)
                csvRow.append(price)
                csvRow.append(img_url)
                csvRow.append(url)
                writer.writerow(csvRow)
            time.sleep(2)
        except Exception as e:
            print(e)


def main():
    # get_tiam()
    get_her_mosa()


if __name__ == "__main__":
    main()
