from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urljoin

# 取得するWebページのURLを定義する
base_url = "https://quotes.toscrape.com"
url = urljoin(base_url, "/tag/humor/")

# 出力するファイル名を定義する
filename = 'quotes_bs4.jsonl'

# データを保存するlistを作成する
data = []

# すべてのページへアクセスするまでループする
while True:
    # Webページへリクエストを行う
    r = requests.get(url)

    # HTMLをBeautifulSoupで取得する
    soup = BeautifulSoup(r.text, 'html.parser')

    # "div.quote"要素をループ処理する
    for quote in soup.select('div.quote'):
        # 作者と名言のテキストを抽出する
        author = quote.select('.author')[0].string
        text = quote.select('.text')[0].string
        # データを保存するlistに作者と名言のテキストを追加する
        data.append({"author": author, "text": text})

    # 次のページへのリンクを取得する
    next_page = soup.select_one('.next a')
    # 次のページへのリンクを取得できた場合、次のページへリクエストを行う
    if next_page is None:
        break
    else:
        url = urljoin(base_url, next_page.get('href'))

# 取得したデータを出力する
with open(filename, 'w') as f:
     # データをファイルへ出力する
    for item in data:
        f.write(f'{json.dumps(item)}\n')