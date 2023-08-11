# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/2 23:15
# @File      :  changePwd.py

from top.AdministratorLogin.actionOfadmin.adminlogin import loginOfadmin
from top.AdministratorLogin.actionOfadmin.updatePwd import update


# # 修改管理员密码模块
class change():
    def change_password(self):
        temp = loginOfadmin().login()
        test = temp[0]
        adminName = temp[1]
        if test:
            print("账户密码校验成功!")
            while True:
                pwd1 = input("请输入新的密码:")
                pwd2 = input("请再次输入新的密码:")
                if pwd1 != pwd2:
                    continue
                else:
                    pwd = pwd2
                    # self.updateAdminpassword(adminName, pwd)
                    update().updateAdminpassword(adminName, pwd)
                    break
        else:
            print("账户密码验证失败,修改密码失败")