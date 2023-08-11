# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/7/30 15:00
# @File      :  temp2.py

import threading
import requests
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from top.allEntity.comicEnity import comic
from top.helpClass.DBUntils import DBHelper
import random


base_url='https://www.kuaikanmanhua.com/'

urls=['https://www.kuaikanmanhua.com/web/topic/13455']


# 获得无头的浏览器
def getChromewithNohead():
    o = Options()
    o.add_argument('--headless')
    chrome = webdriver.Chrome(options=o)
    # 设置隐式等待时间为10秒
    chrome.implicitly_wait(60)
    return chrome

# 获得具体的漫画
def getParticularcomic(url,free,vip,title,type):
    chrome = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
              "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
              "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
              "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
              "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
              "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
              "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
              "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
              "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
              "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
              "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
              "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
              "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
              "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
              "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36",
              "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
              "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",
              "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
              "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",
              "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
              "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"]
    # 随机请求头
    myheaders = {"User-Agent": random.choice(chrome)}

    chrome=getChromewithNohead()
    chrome.get(url)

    # 章节标签
    chapterTag = chrome.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div[1]/div[1]/div[1]')
    # 点击章节标签
    chapterTag.click()
    # 获取到所有的章节名li
    chapterNamelist = chrome.find_elements(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div[1]/div[1]/div[2]/ul/li')
    new_list = []
    for chapterName in chapterNamelist:
        if chapterName.get_attribute("style") == "" and chapterName.find_element(By.XPATH, './a').text.strip() in free:
            url = chapterName.find_element(By.XPATH, './a').get_attribute('href')
            new_list.append(url)

    # 倒置章节序列(让其按照顺序来排列)
    new_list = new_list[::-1]

    # 关闭浏览器释放资源
    chrome.close()

    for one in new_list:
        chrome = getChromewithNohead()
        chrome.get(one)
        div_list = chrome.find_elements(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div[1]/div[4]/div')
        temp = chrome.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div[1]/div[2]/h3').text
        chapter_name = temp.split("-")[2]  # 章节名

        # 定义目录路径
        base_dir = "./"
        sub_dir1 = type
        sub_dir2 = title
        sub_dir3 = chapter_name

        # 创建目录路径
        dir_path = os.path.join(base_dir, sub_dir1, sub_dir2, sub_dir3)

        # 检查目录是否已存在
        if os.path.exists(dir_path):
            # print("目录已存在，无需创建！")
            pass
        else:
            # 创建目录
            os.makedirs(dir_path)
            print("目录已成功创建！")

        i = 1
        # 获取持久化session
        session=requests.Session()
        for div in div_list:
            img = div.find_element(By.CLASS_NAME, 'img')
            img_src = img.get_attribute('data-src')
            # img_data = requests.get(img_src, headers=myheaders).content
            img_data = session.get(img_src,headers=myheaders).content
            with open(f"./{type}/{title}/{chapter_name}/" + f'{i}.jpg', "wb") as f:
                f.write(img_data)
                print(f'正在下载第{i}张照片')
                i = i + 1

        chrome.close()



# def crawl(url='https://www.kuaikanmanhua.com/web/topic/13455',chrome=None):
def crawl(url,type=None,choose=None):
    # 爬取网页的代码
    chrome=getChromewithNohead()
    chrome.get(url)
    # 漫画名称
    comicName=chrome.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div/div[1]/div/div[2]/h3').text.strip().replace(" ","")
    # 漫画作者
    comicAuthor=chrome.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div/div[1]/div/div[2]/div[1]').text.strip().replace(" ","")
    # 漫画简介
    comicIntroduction=chrome.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div/p').text.strip()
    pattern = r"漫画简介:\s(.+)"
    comicIntroduction = re.search(pattern, comicIntroduction).group(1)
    # 漫画状态
    comicState=chrome.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[2]').text.strip().replace(" ","")
    # 漫画章节数
    comicPagenumbers=chrome.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[4]').text
    comicPagenumbers = re.findall(r'\d+', comicPagenumbers)[0]

    # 漫画封面地址
    comicCoveraddress = chrome.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div/div[1]/div/div[1]/img[3]').get_attribute('src')

    # 用于插入数据库使用
    cartoon = comic(comicName, comicAuthor, comicIntroduction, comicState, comicPagenumbers, type,comicCoveraddress)

    # 向root用户下的item数据库中的cartoon数据表中插入cartoon(comicName,comicAuthor,comicIntroduction,comicState,comicPagenumbers,comicCoveraddress)
    itemDB = DBHelper()
    insert_query = "insert into cartoon values(%s, %s, %s,%s,%s,%s,%s)"
    data = (cartoon.comicName, cartoon.comicAuthor, cartoon.comicIntroduction, cartoon.comicState,
            cartoon.comicPagenumbers, cartoon.comicCoveraddress,cartoon.comicStyle)
    itemDB.RunSQl(insert_query, data)

    if choose=='2':
        # 查看第一话的url(用于进行页面跳转,首先跳转到漫画的第一节内容)
        new_url=chrome.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div/a[1]').get_attribute('data-href')
        base_url='https://www.kuaikanmanhua.com/'
        new_url=base_url+re.sub(r'^/', '', new_url)
        # 章节列表
        allChapter = chrome.find_elements(By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div[3]/div')
        # 1.免费章节
        freeViewchapterList = []
        # 2.会员章节
        vipViewchapterList = []
        for chapter in allChapter:
            # 章节名字
            chapterName = chapter.find_element(By.XPATH, './span').text.strip()
            # 章节权限
            chapterAuthority = chapter.find_element(By.XPATH, './span').get_attribute('class').strip()

            if chapterAuthority=='text':
                # 将免费章节的名字添加到免费阅读列表
                freeViewchapterList.append(chapterName)
            else:
                # 将会员章节的名字添加到会员阅读列表
                vipViewchapterList.append(chapterName)

        # 跳转到另一个章节栏(但不刷新网址)
        sencondTag=chrome.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[2]').click()

        # 继续进行添加章节操作
        allChapter=chrome.find_elements(By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div[3]/div')
        for chapter in allChapter:
            # 章节名字
            chapterName = chapter.find_element(By.XPATH, './span').text.strip()
            # 章节权限
            chapterAuthority = chapter.find_element(By.XPATH, './span').get_attribute('class').strip()

            if chapterAuthority=='text':
                # 将免费章节的名字添加到免费阅读列表
                freeViewchapterList.append(chapterName)
            else:
                # 将会员章节的名字添加到会员阅读列表
                vipViewchapterList.append(chapterName)


        # 释放浏览器资源
        chrome.close()


        # 调用getParticularcomic()函数,用于解析单节漫画
        # new_url是每一个具体小说界面上的查看第一话
        getParticularcomic(new_url,freeViewchapterList,vipViewchapterList,comicName,type)

        print('-'*115)


if __name__ == '__main__':

    threads = []
    for url in urls:
        t = threading.Thread(target=crawl, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()







