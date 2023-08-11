# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/7/26 9:49
# @File      :  DBUntils.py


import pymysql
class DBHelper():
    # 只做增删改
    def RunSQl(self,sql,data=None):
        con = pymysql.connect(host='localhost', user='root',
                              password='root', db='item', charset='utf8', port=3306)
        action=sql.split(" ")[0]
        try:
            cmd = con.cursor()

            cmd.execute(sql,data)

            con.commit()
            con.close()
            if action.upper()=="INSERT":
                print('Insertion was successful.')
            elif action.upper()=="DELETE":
                print('Deletion was successful.')
            elif action.upper()=="UPDATE":
                print('Update was successful')
        except Exception as e:
            print(e)
            # 回滚之前的操作--取消操作
            con.rollback()


    #  只做查询
    def RunSQLReturnDS(self,sql,data=None):
        con = pymysql.connect(host='localhost', user='root',
                              password='root', db='item', charset='utf8', port=3306)

        try:
            # 打开数据库,得到数据库操作对象的游标---命令对象
            cmd = con.cursor()
            # 执行sql语句(insert delete update select)
            cmd.execute(sql,data)
            # 把查询的结果返回给一个集合变量
            rs=cmd.fetchall()
            # 提交数据库修改
            con.commit()
            # 返回查询到的集合结果
            con.close()
            return rs
        except Exception as e:
            print(e)
            # 回滚之前的操作--取消操作
            con.rollback()
