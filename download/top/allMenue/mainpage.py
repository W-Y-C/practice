# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 1:48
# @File      :  mainpage.py


class centerofcontrol():
    def menue_show(self):
        temp = "*" * 50
        print(temp.ljust(90))
        print("1.管理员登录")
        print("2.用户登录")
        print("3.注册用户")
        print("4.退出系统")
        print(temp.ljust(90))