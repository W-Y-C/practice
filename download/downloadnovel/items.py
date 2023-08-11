# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class DownloadnovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass




# 生成爬取不同类型小说网址的item
class DownloadfictionItem(scrapy.Item):
    # 定义了2个属性
    # 类型的链接
    urlOfdifferentTypenovel = scrapy.Field()
    # 小说类型(现代言情,古代言情.......)
    NameofdifferentNovel = scrapy.Field()



# 每一个类型的小说item(比如恋爱类型)
class styleoffictionItem(scrapy.Item):
    # 定义了8个属性
    # 小说的类型
    style=scrapy.Field()
    # 具体小说的超链接(比如偷偷藏不住,斗破苍穹的跳转地址等等)
    urlOfnovel=scrapy.Field()
    # 具体小说封面地址(用来做前后端交互使用)
    coverofnovelurl=scrapy.Field()
    # 具体小说名称(比如偷偷藏不住,斗破苍穹)
    nameOfnovel=scrapy.Field()
    # 具体小说的标签(比如霸道总裁等等)
    tagOfnovel=scrapy.Field()
    # 具体小说的状态(比如连载中,完结等等)
    stateOfnovel=scrapy.Field()
    # 具体小说简介
    briefintroductionOfnovel=scrapy.Field()
    # 具体小说作者及最后更新时间
    authorOfnovel=scrapy.Field()







