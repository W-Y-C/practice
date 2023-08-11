# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/7/31 19:50
# @File      :  userEnity.py
from datetime import datetime


class user():
    # 用户类属性初始化
    def __init__(self, userName=None, userPassword=None, userPhone=None, userGender=None,
                 userAge=None, userState=None, userRegistTime=None, userRegistMethod=None):
        # 用户名称
        self.userName = userName
        # 用户密码
        self.userPassword = userPassword
        # 用户号码
        self.userPhone = userPhone
        # 用户性别
        self.userGender = userGender
        # 用户年龄
        self.userAge = userAge
        # 用户状态
        self.userState = userState
        # 用户注册时间
        self.userRegistTime = userRegistTime
        # 用户注册方式
        self.userRegistMethod = userRegistMethod

    def __str__(self):
        return (f"用户名称:{self.userName}\n"
                f"用户密码:{self.userPassword}\n"
                f"用户号码:{self.userPhone}\n"
                f"用户性别:{self.userGender}\n"
                f"用户年龄:{self.userAge}\n"
                f"用户状态:{self.userState}\n"
                f"用户注册时间:{self.userRegistTime}\n"
                f"用户注册方式:{self.userRegistMethod}")


if __name__ == '__main__':
    pass
    # time = str(datetime.now().date().strftime("%Y-%m-%d"))
    # user = user("凤婷婷", "123456789", "123456789", "女", "21", "活跃", str(datetime.now().date().strftime("%Y-%m-%d")),
    #             "QQ")
    # print(user)
