# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 0:34
# @File      :  menueofamin.py


class menueOfadmin():
    def administrator_menue(self):
        temp = "*" * 50
        print(temp.ljust(90))
        print("管理员后台系统")
        print("1.管理员修改密码")
        print("2.用户管理")
        print("3.漫画管理")
        print("4.漫画爬虫开启")
        # 5.对应的是root用户item数据库中的demo数据表,只起到了辅助作用(操作时请注意)
        print("5.漫画封面抓取")
        print("-"*50)
        print("6.小说管理")
        print("7.小说爬虫开启")
        # 8.对应的是MongoDB数据库中的demo数据库下的一些数据表,只起到了辅助作用(用于后续前后端交互时的页面刷新)
        print("8.小说封面抓取")
        print("9.退出登录")
        print(temp.ljust(90))