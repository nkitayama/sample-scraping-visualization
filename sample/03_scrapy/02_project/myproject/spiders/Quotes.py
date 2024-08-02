import scrapy
from myproject.items import MyprojectItem

class QuotesSpider(scrapy.Spider):
    name = "Quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    # コールバックメソッド
    def parse(self, response):
        # CSSセレクターを利用して取得した"div.quote"要素をループ処理する
        for quote in response.css("div.quote"):
            # 作者と名言のテキストを抽出し、MyprojectItemで返却する
            yield MyprojectItem(
                author = quote.xpath("span/small/text()").get(),
                text = quote.css("span.text::text").get(),
            )

        # CSSセレクターを利用して次のページへのリンクを取得する
        next_page = response.css('li.next a::attr("href")').get()
        # 次のページへのリンクを取得できた場合、次のページへリクエストを行う
        if next_page is not None:
            yield response.follow(next_page, self.parse)