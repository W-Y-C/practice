# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 1:25
# @File      :  comicwatch.py

from top.allEntity.comicEnity import comic
from top.helpClass.DBUntils import DBHelper

class viewcomic():
    # 查看漫画
    def comicView(self, username):
        while True:
            print("-----------------------------------------------")
            print("1.查看所有漫画")
            print("2.按名称查找漫画")
            print("3.按作者查找漫画")
            print("4.用户退出漫画查看")
            print("-----------------------------------------------")
            choose = input("请输入你的选择:")
            if choose == "1":
                select_sql = "select * from cartoon"
                rs_list = DBHelper().RunSQLReturnDS(select_sql)
                list = []
                for rs in rs_list:
                    cartoon = comic(rs[0], rs[1], rs[2], rs[3], rs[4], rs[5])
                    list.append(cartoon)
                    print(cartoon)
                    print("-----------------------------------------------")

                # 上述显示了所有漫画的内容,故可以根据漫画名字挑出自己的喜欢的添加到用户收藏表
                i = input("是否需要添加收藏 1-是2-否:")
                if i == '1':
                    name = input("请输入你要添加的漫画名字:")
                    for i in list:
                        if i.comicName == name:
                            insert_sql = 'insert into usercollectiontable values(%s,%s,%s,%s,%s,%s,%s,%s)'
                            data = (i.comicName, i.comicAuthor, i.comicIntroduction, i.comicState, i.comicPagenumbers,
                                    i.comicStyle, i.comicCoveraddress, username)
                            DBHelper().RunSQl(insert_sql, data)
                else:
                    pass

            elif choose == "2":
                name = input("请输入你要搜索的漫画名称:")
                data = (name,)
                select_sql = "select * from cartoon where comicName=%s"
                rs = DBHelper().RunSQLReturnDS(select_sql, data)[0]
                cartoon = comic(rs[0], rs[1], rs[2], rs[3], rs[4], rs[5])
                print(cartoon)

            elif choose == "3":
                author = input("请输入你要查找漫画的作者:")
                data = (author,)
                select_sql = "select * from cartoon where comicAuthor=%s"
                rs = DBHelper().RunSQLReturnDS(select_sql, data)[0]
                cartoon = comic(rs[0], rs[1], rs[2], rs[3], rs[4], rs[5])
                print(cartoon)
            elif choose == "4":
                break
            else:
                print("输入无效,请重新输入相应的选项")