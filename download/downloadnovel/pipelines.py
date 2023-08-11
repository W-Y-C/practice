# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 用于连接数据库操作
import pymongo
from scrapy.item import Item
from downloadnovel.items import DownloadfictionItem

# class DownloadnovelPipeline:
#     def process_item(self, item, spider):
#         return item

# ITEM_PIPELINES = {
#     'yourproject.pipelines.PrintItemPipeline': 300,
# }

# 在上述示例中，PrintItemPipeline是我们自定义的Item Pipeline类，
# 300是一个数字，用于指定Pipeline的执行顺序。数字越小，优先级越高。

# mongoDB 是无模式（Schema-less）的，并不需要在创建集合时指定固定的属性。
# 对于每个文档，您可以根据需要插入不同的属性组合。
# 集合内的文档可以具有不同的属性集。


class PrintItemPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        # self.db = self.client['test_db']
        self.db = self.client['temp3']
        self.collection = self.db['typeofnovel']

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        field_count = ""
        if item is not None:
            field_count = len(item.fields)
        if field_count==2:
            data = dict(item)  # 将 Item 对象转换为字典
            self.collection.insert_one(data)
            # print("insert successful!")
            # print(item['urlOfdifferentTypenovel'])
            return item


class PrintonetypenovelItemPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client['temp3']

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.client.close()


    def process_item(self, item, spider):
        field_count=""
        if item is not None:
            field_count = len(item.fields)
        if field_count==8:
            self.db[item["style"]].insert_one(dict(item))
            print("insert successful!")
            # print(item['style'])
            return item

