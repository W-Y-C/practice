# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 1:02
# @File      :  getNamelist.py


from top.helpClass.DBUntils import DBHelper

class getNameset():
    # 得到用户姓名列表
    def getUserNameList(self):
        userNamelist = []
        select_sql = "select userName from user"
        rs = DBHelper().RunSQLReturnDS(select_sql)
        for r in rs:
            userNamelist.append(r[0])
        return userNamelist
