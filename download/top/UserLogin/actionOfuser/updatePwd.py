# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 1:17
# @File      :  updatePwd.py

from top.helpClass.DBUntils import DBHelper

class update():
    # 根据用户姓名修改用户密码(因为是登录成功后才进行修改用户密码判断,所以不需要在进行用户姓名,密码的判断了)
    def updateUserpassword(self, name, newPwd):
        data = (newPwd, name)
        update_sql = "update user set userPassword=%s where userName=%s"
        DBHelper().RunSQl(update_sql, data)
