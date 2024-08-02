import scrapy
from BooksToScrapeArguments.items import BookstoscrapeargumentsItem

class BooksargumentsSpider(scrapy.Spider):
    name = "BooksArguments"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    # コールバックメソッド
    def parse(self, response):
        # CSSセレクターを利用して取得した"article.product_pod"要素をループ処理する
        for product in response.css("article.product_pod"):
            # 商品名と価格、評価レートを抽出し、BookstoscrapeargumentsItemで返却する
            yield BookstoscrapeargumentsItem(
                name = product.css("a::attr(title)").get(),
                price = product.css(".price_color::text").get(),
                rate = product.xpath("p/@class").get(),
            )

        # CSSセレクターを利用して次のページへのリンクを取得する
        next_page = response.css('li.next a::attr("href")').get()
        # 次のページへのリンクを取得できた場合、次のページへリクエストを行う
        if next_page is not None:
            yield response.follow(next_page, self.parse)
