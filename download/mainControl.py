# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/2 19:51
# @File      :  mainControl.py

from scrapy.cmdline import execute
import sys
import os



class center():
    def control(self):
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        execute(["scrapy","crawl","qimao"])