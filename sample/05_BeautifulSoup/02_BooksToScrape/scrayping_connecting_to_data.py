from bs4 import BeautifulSoup
import requests
import csv
from urllib.parse import urljoin

# 取得するWebページのURLを定義する
base_url = "https://books.toscrape.com/"
url = urljoin(base_url, "/catalogue/page-1.html")

# 出力するファイル名を定義する
filename = 'books.csv'

# データを保存するlistを作成する
data = []

# すべてのページへアクセスするまでループする
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
        # データを保存するlistに商品名と価格、評価レートを追加する
        data.append([name, price, rate])

    # 次のページへのリンクを取得する
    next_page = soup.select_one('.next a')
    # 次のページへのリンクを取得できた場合、次のページへリクエストを行う
    if next_page is None:
        break
    else:
        url = urljoin(base_url, f"/catalogue/{next_page.get('href')}")

# 取得したデータをCSVへ出力する
with open(filename, 'w', encoding="utf8", errors='ignore', newline='') as f:
    # openで開いたファイルにCSVで出力するように設定する
    writer = csv.writer(f)
    # ヘッダーを出力する
    writer.writerow(['Name', 'Price', 'Star Rating'])
    # データを出力する
    writer.writerows(data)