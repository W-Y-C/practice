# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/2 1:03
# @File      :  __init__.py.py

import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

url="https://www.qimao.com/shuku/a-a-a-a-a-a-a-click-1/"
c=Chrome()
c.get(url)


li_list=c.find_elements(By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[1]/ul/li')
for li in li_list:
    a=li.find_element(By.XPATH,'./div[2]/span[1]').text
    b=li.find_element(By.XPATH,'./div[2]/span[2]').text
    c=li.find_element(By.XPATH,'./div[2]/span[3]').text
    d=li.find_element(By.XPATH,'./div[2]/p/span').text
    print(f"{a}\n{b}\n{c}\n{d}")
    print("-"*60)










