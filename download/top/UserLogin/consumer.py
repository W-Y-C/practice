# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/7/29 20:19
# @File      :  consumer.py

import os
from top.helpClass import DBUntils
from top.allEntity.comicEnity import comic
from top.allEntity.userEnity import user

from top.allMenue.menuofuser import menueOfuser

from top.UserLogin.actionOfuser.changePwd import change

from top.UserLogin.actionOfuser.comicwatch import viewcomic

from top.UserLogin.actionOfuser.showmycollection import collectionofcomic

from top.UserLogin.actionOfuser.myfriend import Friend

from top.UserLogin.actionOfuser.getNamelist import getNameset

from top.UserLogin.actionOfuser.userlogin import loginOfuser

from top.helpClass.MongodbUntils import MongoDBHandler

# 导入小说查看模块
from top.UserLogin.actionOfuser.novelwatch import viewnovel



class Consumer():
    def __init__(self):
        self.db = DBUntils.DBHelper()
        self.nameList = getNameset().getUserNameList()

    def mainPart(self):
        temp=loginOfuser().login()
        test=temp[0]
        userName=temp[1]
        if test:
            while True:
                # from top.allMenue.menuofuser import menueOfuser
                menueOfuser().user_menue()
                choose = input("尊敬的用户,请输入您的选择:")
                # 1.用户修改密码
                if choose == "1":
                    change().change_password()
                # 2.查看漫画
                elif choose == "2":
                    # 可以根据不同条件进行查看
                    viewcomic().comicView(userName)
                # 3.我的漫画收藏
                elif choose == "3":
                    # 动态刷新部分
                    # 1.先展示所有的漫画
                    # 2.然后选择喜欢的漫画添加到我的漫画收藏中心,在我的收藏中展示
                    collectionofcomic().userCollection(userName)
                # 4.查看小说
                elif choose=="4":
                    viewnovel().Novel(userName)
                # 5.我的小说收藏
                elif choose=="5":
                    # 动态刷新部分
                    # 1.先展示所有的小说
                    # 2.然后选择喜欢的小说添加到我的小说收藏中心,在我的收藏中展示

                    print("我的小说收藏")
                # 6.我的好友
                elif choose=="6":
                    # 可以添加好友
                    # 1.先展示所有的用户
                    # ('杜雨龙', 'root', '123456789', '男', '21', '活跃', '2023-7-31')
                    # ('杨宜林', 'root', '123456789', '男', '21', '活跃', '2023-7-31')
                    Friend().userFriend()
                    print("以上显示的是所有注册用户的信息,请根据姓名添加某某为你的好友!")
                    # 2.根据喜好进行双向添加好友操作(主要是涉及数据库中的表的操作)
                    addname=input("请输入入你想要添加的好友姓名:")
                    Friend().addFriend(addname,userName)
                # 7.退出登录
                elif choose == "7":
                    break
                # 无效输入，重新选择
                else:
                    print("输入无效,请从新输入!")
        else:
            print("用户登录失败")


if __name__ == '__main__':
    user = Consumer()
    user.mainPart()
