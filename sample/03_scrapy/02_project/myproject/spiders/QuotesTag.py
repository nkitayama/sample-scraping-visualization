import scrapy
from myproject.items import MyprojectItem

class QuotestagSpider(scrapy.Spider):
    name = "QuotesTag"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    # クロールを開始するURLを定義するメソッド
    def start_requests(self):
        # ベースとなるURLを定義する
        url = "https://quotes.toscrape.com/"
        # スパイダー引数で指定されたタグの値を取得する
        tag = getattr(self, "tag", None)
        # スパイダー引数が指定されている場合、タグを指定したURLを生成する
        if tag is not None:
            url = url + "tag/" + tag
        # 生成したURLへリクエストを行う
        yield scrapy.Request(url, self.parse)

    # コールバックメソッド
    def parse(self, response):
        # CSSセレクターを利用して取得した"div.quote"要素をループ処理する
        for quote in response.css("div.quote"):
            # 作者と名言のテキストを抽出し、MyprojectItemで返却する
            yield MyprojectItem(
                author = quote.css("small.author::text").get(),
                text = quote.css("span.text::text").get(),
            )

        # CSSセレクターを利用して次のページへのリンクを取得する
        next_page = response.css("li.next a::attr(href)").get()
        # 次のページへのリンクを取得できた場合、次のページへリクエストを行う
        if next_page is not None:
            yield response.follow(next_page, self.parse)