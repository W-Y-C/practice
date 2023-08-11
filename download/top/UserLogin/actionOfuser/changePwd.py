# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 1:18
# @File      :  changePwd.py

from top.UserLogin.actionOfuser.userlogin import loginOfuser
from top.UserLogin.actionOfuser.updatePwd import update

class change():
    # 修改用户密码
    def change_password(self):
        # temp = self.login()
        temp = loginOfuser().login()
        test = temp[0]
        userName = temp[1]
        if test:
            print("账户密码校验成功!")
            while True:
                pwd1 = input("请输入新的密码:")
                pwd2 = input("请再次输入新的密码:")
                if pwd1 != pwd2:
                    continue
                else:
                    pwd = pwd2
                    # self.updateUserpassword(userName, pwd)
                    update().updateUserpassword(userName, pwd)
                    break
        else:
            print("账户密码验证失败,修改密码失败")
