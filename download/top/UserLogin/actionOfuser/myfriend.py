# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 1:31
# @File      :  myfriend.py


from top.helpClass.DBUntils import DBHelper
from top.allEntity.userEnity import user

class Friend():
    def __init__(self):
        self.use=user()
        self.db=DBHelper()

    # 显示所有的用户
    def userFriend(self):
        select_sql = "select * from user"
        rs = DBHelper().RunSQLReturnDS(select_sql)
        for r in rs:
            self.use.userName=r[0]
            self.use.userPassword=r[1]
            self.use.userPhone=r[2]
            self.use.userGender=r[3]
            self.use.userAge=r[4]
            self.use.userState=r[5]
            self.use.userRegistTime=r[6]
            self.use.userRegistMethod=r[7]
            print(self.use)
            print("-"*100)

    def addFriend(self,addname='葛竞',myname='凤婷婷'):
        # 凤婷婷向添加杜雨龙未好友
        data1=(addname,)

        select_sql="select * from user where userName=%s"
        res=self.db.RunSQLReturnDS(select_sql,data1)[0]
        # ('杜雨龙', 'root', '123456789', '男', '21', '失联', '2023-7-31', 'QQ')
        use=user(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7])
        # print(use)
        data2 = (res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],myname)
        insert_sql="insert into friendtable values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.db.RunSQl(insert_sql,data2)
        print("你添加的好友信息如下:")
        print(use)
        print("-"*100)
        print(f"{myname}已经成功添加添加{addname}为好友!")



if __name__ == '__main__':
    Friend().addFriend()