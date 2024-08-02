from bs4 import BeautifulSoup

# 取得するHTMLを定義する
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="topic"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# HTMLをBeautifulSoupで取得する
soup = BeautifulSoup(html_doc, 'html.parser')

# 出力するファイル名を定義する
filename = 'quick_start.txt'

# 取得したHTMLを整形して出力する
with open(filename, 'w') as f:
    f.write('soup.prettify()\n----\n')
    f.write(soup.prettify())
    f.write('----\n')

# 取得したHTMLから、タイトルに関連するデータを出力する
with open(filename, 'a') as f:
    # titleタグとタグ内のテキスト
    f.write(f'soup.title: {soup.title}')
    f.write('\n----\n')
    # タイトルのタグ名
    f.write(f'soup.title.name: {soup.title.name}')
    f.write('\n----\n')
    # titleタグ内のテキスト
    f.write(f'soup.title.string: {soup.title.string}')
    f.write('\n----\n')
    # titleタグの親要素のタグ名
    f.write(f'soup.title.parent.name: {soup.title.parent.name}')
    f.write('\n----\n')

# 取得したHTMLから、pタグに関連するデータを出力する
with open(filename, 'a') as f:
    # 1つ目のpタグとタグ内のテキスト
    f.write(f'soup.p: {soup.p}')
    f.write('\n----\n')
    # 1つ目のpタグのclass属性
    f.write(f'soup.p[\"class\"]: {soup.p["class"]}')
    f.write('\n----\n')

# 取得したHTMLから、aタグに関連するデータを出力する
with open(filename, 'a') as f:
    # 1つ目のaタグとタグ内のテキスト
    f.write(f'soup.a: {soup.a}')
    f.write('\n----\n')
    # すべてのaタグとタグ内のテキスト
    f.write('soup.find_all(\"a\")\n')
    for i, text in enumerate(soup.find_all('a')):
        f.write(f'{i}: {text}\n')
    f.write('----\n')
    # idが"link3"のタグとタグ内のテキスト
    f.write(f'soup.find(id=\"link3\"): {soup.find(id="link3")}')
    f.write('\n----\n')