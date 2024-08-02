# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem

class BookstoscrapeargumentsPipeline:
    def open_spider(self, spider):
        # スパイダー引数で指定された値を取得する
        self.requirement_price = float((getattr(spider, "price", 50)))
        self.requirement_rate = float(getattr(spider, "rate", 3))
        # 評価レートを数値へ変換するためのdictを作成する
        self.rate_dict = {"star-rating One": 1, "star-rating Two": 2, "star-rating Three": 3, "star-rating Four": 4, "star-rating Five": 5}
        
    def process_item(self, item, spider):
        # 抽出した価格と評価レートを数値へ変換する
        price = float(item["price"].replace('£', ''))
        rate = self.rate_dict[item["rate"]]

        # スパイダー引数で指定された価格以下、かつ、評価レート以上の場合、Itemを出力する
        if price <= self.requirement_price and rate >= self.requirement_rate:
            return item
        # 価格や評価レートの条件を満たさない場合、Itemを破棄する
        else:
            raise DropItem(f"Item does not meet the requirement: {item!r}")