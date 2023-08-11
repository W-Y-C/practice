# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/2 19:18
# @File      :  startScrapy.py


from scrapy.crawler import CrawlerProcess
from downloadnovel.spiders.qimao import QimaoSpider
from scrapy.settings import Settings


# from project.spiders.spider_name import spider_class
#配置setting，可自定义setting属性

settings = Settings()

process = CrawlerProcess()

#执行spider
process.crawl(QimaoSpider)
process.start()





