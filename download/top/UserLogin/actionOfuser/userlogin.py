# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 1:00
# @File      :  userlogin.py


from top.UserLogin.actionOfuser.getNamelist import getNameset
from top.UserLogin.actionOfuser.get import getuserPwd

class loginOfuser():
    # 验证登录
    def login(self):
        # user_names = self.nameList  # 管理员姓名列表
        user_names = getNameset().getUserNameList()  # 管理员姓名列表
        for _ in range(3):
            userName = input("请输入用户姓名：")

            if userName not in user_names:
                print("用户名不存在")
                continue  # 继续输入用户名

            for _ in range(3):
                password = input("请输入密码：")
                # 从数据库中获取用户密码,用以校验用户密码是否正确
                # user_password = self.getUserpassword(userName)  # 用户密码
                user_password = getuserPwd().getUserpassword(userName)  # 用户密码

                if password != user_password:
                    print("密码错误")
                else:
                    return (True, userName)  # 登录成功

            print("输入错误次数过多，登录失败")
            return (False, userName)  # 登录失败

        print("输入错误次数过多，登录失败")

        return (False, None)  # 登录失败