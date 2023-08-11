# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 0:30
# @File      :  takespider.py

from top.AdministratorLogin.spider import steal_spider

class actionofspdier():
    # 开启爬虫
    def stratSpider(self):
        spider = steal_spider()
        spider.main_loop()
