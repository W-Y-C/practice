# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/1 13:58
# @File      :  spider2.py

import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from top.AdministratorLogin.temp2 import crawl
from top.AdministratorLogin.temp2 import getChromewithNohead
from top.AdministratorLogin.spider import steal_spider
from top.helpClass.DBUntils import DBHelper
from top.allEntity.templete import demo
from bs4 import BeautifulSoup
from top.AdministratorLogin.temp2 import getChromewithNohead
from top.helpClass.DBUntils import DBHelper

class stealData():

    def __init__(self):
        # 初试化数据库连接
        self.db=DBHelper()

    # 获取抓取页面的地址
    def getFirstpage(self):
        return steal_spider().getFirstpage()

    #开始爬取
    def takeaction(self):
        # 获取抓取页面地址
        url=self.getFirstpage()

        # 开始抓取动作
        chrome=getChromewithNohead()
        chrome.get(url)

        # 操作浏览器下拉至浏览器底部,是网页完成全部渲染
        chrome.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        div_list=chrome.find_elements(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[3]/div')
        for div in div_list:
            # 小样名称
            demoName=div.find_element(By.XPATH,'./a/span[2]').text.strip()
            # 小样作者名
            demoAuthorname=div.find_element(By.XPATH,'./p/span[1]').text.strip()
            # 小样点赞数
            numberOflikes=div.find_element(By.XPATH,'./p/span[2]/span').text.strip()
            # 小样封面
            demoCoveraddress=div.find_element(By.XPATH,'./a/span[1]/img[2]').get_attribute('src')
            # 建立demo类实例
            comic=demo(demoName,demoAuthorname,numberOflikes,demoCoveraddress)

            # 准备向root下的item下的demo表中插入comic小样
            insert_sql = 'insert into demo values(%s,%s,%s,%s)'
            data = (comic.demoName,comic.demoAuthorname,comic.numberOflikes,comic.demoCoveraddress)
            self.db.RunSQl(insert_sql, data)

if __name__ == '__main__':
    # stealData().getFirstpage()
    stealData().takeaction()


