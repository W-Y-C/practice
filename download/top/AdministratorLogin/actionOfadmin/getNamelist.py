# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/2 23:39
# @File      :  getNamelist.py


from top.helpClass.DBUntils import DBHelper


# 获取管理员姓名模块
class getNameset():
    def getAdminNameList(self):
        adminNamelist = []
        select_sql = "select adminName from admin"
        rs = DBHelper().RunSQLReturnDS(select_sql)
        for r in rs:
            adminNamelist.append(r[0])
        return adminNamelist
