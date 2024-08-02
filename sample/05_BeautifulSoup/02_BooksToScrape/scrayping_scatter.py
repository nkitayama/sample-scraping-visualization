from bs4 import BeautifulSoup
import requests
import csv
from urllib.parse import urljoin

# 取得するWebページのURLを定義する
base_url = "https://books.toscrape.com/"

# 出力するファイル名を定義する
filename = 'books_and_categories.csv'

# データを保存するlistを作成する
data = []

# 評価レートの文字列と数値の対応付けを行うためのdictを作成する
word_to_number = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

# Webページへリクエストを行う
r = requests.get(base_url)

# HTMLをBeautifulSoupで取得する
soup = BeautifulSoup(r.text, 'html.parser')

# カテゴリごとのリンクとカテゴリ名を取得する
categories = [(tag.get('href'), tag.string.strip()) for tag in soup.select('.nav ul li a')]

# カテゴリごとにループする
for category_url, category in categories:
    # カテゴリへアクセスするURLを作成する
    url = urljoin(base_url, category_url)
    # カテゴリごとのすべてのページのデータを取得するまでループする
    while True:
        # Webページへリクエストを行う
        r = requests.get(url)

        # HTMLをBeautifulSoupで取得する
        soup = BeautifulSoup(r.text, 'html.parser')

        # 'article.product_pod'要素をループ処理する
        for product in soup.select('article.product_pod'):
            # 商品名と価格、評価レートを抽出する
            name = product.select('a')[1].get('title')
            price = product.select_one('.price_color').string
            rate = product.select_one('.star-rating').get('class')[1]
            # 価格から不要な文字列を削除し、数値に変換する
            price = float(price.replace('Â£', ''))
            # 評価レートの文字列を数値へ変換する
            rate = word_to_number[rate]
            # データを保存するlistに商品名と価格、評価レート、カテゴリを追加する
            data.append([name, price, rate, category])

        # 次のページへのリンクを取得する
        next_page = soup.select_one('.next a')
        # 次のページへのリンクを取得できた場合、次のページへリクエストを行う
        if next_page is None:
            break
        else:
            url = urljoin(url, next_page.get('href'))

# 取得したデータをCSVへ出力する
with open(filename, 'w', encoding="utf8", errors='ignore', newline='') as f:
    # openで開いたファイルにCSVで出力するように設定する
    writer = csv.writer(f)
    # ヘッダーを出力する
    writer.writerow(['Name', 'Price', 'Star Rating', 'Category'])
    # データを出力する
    writer.writerows(data)