# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/2 23:26
# @File      :  updatePwd.py

from top.helpClass.DBUntils import DBHelper


# 根据管理员姓名修改管理员密码(因为是登录成功后才进行修改管理员密码判断,所以不需要在进行管理员姓名,密码的判断了)
class update():
    def updateAdminpassword(self, name, newPwd):
        data = (newPwd, name)
        update_sql = "update admin set adminPassword=%s where adminName=%s"
        # self.db.RunSQl(update_sql, data)
        DBHelper().RunSQl(update_sql, data)