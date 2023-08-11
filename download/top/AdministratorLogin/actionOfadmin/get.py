# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/2 23:33
# @File      :  get.py

from top.helpClass.DBUntils import DBHelper

# 获取管理员密码模块
class getadminPwd():
    def getAdminpassword(self, name):
        data = (name,)
        select_sql = "select adminPassword from admin where adminName=%s"
        rs = DBHelper().RunSQLReturnDS(select_sql, data)[0][0]
        return rs
