# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 1:12
# @File      :  get.py


from top.helpClass.DBUntils import DBHelper
class getuserPwd():
    # 根据用户姓名获取到用户密码
    def getUserpassword(self, name):
        data = (name,)
        select_sql = "select userPassword from user where userName=%s"
        rs = DBHelper().RunSQLReturnDS(select_sql, data)[0][0]
        return rs