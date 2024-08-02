# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem

class BookstoscrapePipeline:
    def process_item(self, item, spider):
        # 抽出した価格を数値へ変換する
        price = float(item["price"].replace('£', ''))
        # 価格が20£以下の場合、Itemを出力する
        if price <= 20:
            return item
        # 価格が20£より大きい場合、Itemを破棄する
        else:
            raise DropItem(f"Item is higher than the requirement price: {item!r}")