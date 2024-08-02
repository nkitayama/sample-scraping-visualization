# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem

class MyprojectPipeline:
    # コンストラクタ
    def __init__(self):
        # 出力したItemの作者を保持する変数を定義する
        self.authors_seen = set()

    # Itemが処理されるごとに呼び出されるメソッド
    def process_item(self, item, spider):
        # すでに出力したItemの作者である場合、Itemを破棄する
        if item["author"] in self.authors_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        # すでに出力したItemの作者ではない場合、Itemを出力する
        else:
            self.authors_seen.add(item["author"])
            return item
