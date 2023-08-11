# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 1:23
# @File      :  menuofuser.py


class menueOfuser():
    def user_menue(self):
        temp = "*" * 50
        print(temp.ljust(90))
        print("用户后台系统")
        print("1.用户修改密码")
        print("2.查看漫画")
        print("3.我的漫画收藏")
        print("4.查看小说")
        print("5.我的小说收藏")
        print("6.我的好友")
        print("7.退出登录")
        print(temp.ljust(90))