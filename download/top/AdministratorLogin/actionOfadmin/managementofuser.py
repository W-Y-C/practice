# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 0:25
# @File      :  managementofuser.py

from top.allEntity.userEnity import user
from top.helpClass.DBUntils import DBHelper
class manageuser():
    def userManagement(self):
        # 1.查看所有用户，2.按名称查找用户3.修改用户状态（状态）
        while True:
            print("-----------------------------------------------")
            print("1.查看所有用户")
            print("2.按名称查找用户")
            print("3.修改用户状态（状态）")
            print("4.管理员退出用户管理")
            print("-----------------------------------------------")
            choose = input("请输入你的选择:")
            if choose == "1":
                select_sql = "select * from user"
                rs_list = DBHelper().RunSQLReturnDS(select_sql)
                for rs in rs_list:
                    use = user(rs[0], rs[1], rs[2], rs[3], rs[4], rs[5], rs[6], rs[7])
                    print(use)
                    print("-----------------------------------------------")

            elif choose == "2":
                name = input("请输入你要搜索的用户名:")
                data = (name,)
                select_sql = "select * from user where userName=%s"
                rs = DBHelper().RunSQLReturnDS(select_sql, data)[0]
                use = user(rs[0], rs[1], rs[2], rs[3], rs[4], rs[5], rs[6], rs[7])
                print(use)

            elif choose == "3":
                name = input("请输入你要修改的用户名称:")
                name2 = input("请输入你修改后的用户状态:")
                update_sql = "update user set userState=%s where userName=%s"
                data = (name2, name)
                DBHelper().RunSQl(update_sql, data)
            elif choose == "4":
                break
            else:
                print("输入无效,请重新输入相应的选项")