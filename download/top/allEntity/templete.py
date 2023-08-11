# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/1 14:08
# @File      :  templete.py

class demo():
    def __init__(self,demoName=None,demoAuthorname=None,numberOflikes=None,demoCoveraddress=None):
        # 小样名称
        self.demoName=demoName
        # 小样作者名
        self.demoAuthorname=demoAuthorname
        # 小样点赞数
        self.numberOflikes=numberOflikes
        # 小样封面地址
        self.demoCoveraddress=demoCoveraddress


    def __str__(self):
        return (f"漫画名称:{self.demoName}\n"
                f"漫画作者名称:{self.demoAuthorname}\n"
                f"漫画点赞数:{self.numberOflikes}\n"
                f"漫画封面地址:{self.demoCoveraddress}\n")
