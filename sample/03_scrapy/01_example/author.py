import scrapy

# Spiderを定義するクラス
class AuthorSpider(scrapy.Spider):
    # Spiderを識別する名前を定義する
    name = "author"
    # クロールを開始するURLを定義する
    start_urls = ["https://quotes.toscrape.com/"]

    # コールバックメソッド
    def parse(self, response):
        # CSSセレクターを利用して、作者のリンクを取得する
        author_page_links = response.css(".author + a")
        # 作者のリンクへリクエストを行う
        # コールバックメソッドはparse_authorメソッドとする
        yield from response.follow_all(author_page_links, self.parse_author)

        # CSSセレクターを利用して次のページへのリンクを取得する
        pagination_links = response.css("li.next a")
        # 次のページへリクエストを行う
        # コールバックメソッドはparseメソッドとする
        yield from response.follow_all(pagination_links, self.parse)

    # コールバックメソッド
    def parse_author(self, response):
        # CSSセレクターを利用するメソッドを定義する
        def extract_with_css(query):
            return response.css(query).get(default="").strip()

        # 作者、誕生日、説明のテキストを抽出し、dict型で返却する
        yield {
            "name": extract_with_css("h3.author-title::text"),
            "birthdate": extract_with_css(".author-born-date::text"),
            "bio": extract_with_css(".author-description::text"),
        }