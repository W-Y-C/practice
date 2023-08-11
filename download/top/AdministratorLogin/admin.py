import os
# 导入mysql数据库增删改查模块
from top.helpClass import DBUntils
# 导入爬取漫画封面模块
from top.AdministratorLogin.spider2 import stealData
# 导入管理员的修改密码操作
from top.AdministratorLogin.actionOfadmin.changePwd import change
# 导入验证登录的模块
from top.AdministratorLogin.actionOfadmin.adminlogin import loginOfadmin
# 导入漫画管理模块
from top.AdministratorLogin.actionOfadmin.managementOfcomic import manageComic
# 导入获取管理员姓名模块(用于登录校验)
from top.AdministratorLogin.actionOfadmin.getNamelist import getNameset
# 导入用户管理模块
from top.AdministratorLogin.actionOfadmin.managementofuser import manageuser
# 导入开启漫画爬虫模块
from top.AdministratorLogin.actionOfadmin.takespider import actionofspdier
# 导入管理员后台登录系统界面模块
from top.allMenue.menueofamin import menueOfadmin
# 导入漫画管理模块
from top.AdministratorLogin.actionOfadmin.managementofnovel import manageNovel

import mainControl

from top.helpClass.MongodbUntils import MongoDBHandler

class Administrator():
    def __init__(self):
        self.db = DBUntils.DBHelper()
        # 管理员姓名列表
        # self.nameList = self.getAdminNameList()
        self.nameList = getNameset().getAdminNameList()


    def mainPart(self):
        if loginOfadmin().login()[0]:
            while True:
                menueOfadmin().administrator_menue()
                choose = input("尊敬的顾客,请输入您的选择:")
                # 1.管理员修改密码
                if choose == "1":
                    change().change_password()
                # 2.用户管理
                elif choose == "2":
                    manageuser().userManagement()
                # 3.漫画管理
                elif choose == "3":
                    manageComic().comicManagement()
                # 4.漫画爬虫开启
                elif choose == "4":
                    actionofspdier().stratSpider()
                # 5.漫画封面抓取(root用户下的item中的demo数据表已填充数据库,此功能轻易不要使用)
                elif choose == "5":
                    print("开始漫画封面爬取:")
                    stealData().takeaction()
# -----------------------------------------------------------------------------------------------
                # 6.小说管理
                elif choose=="6":
                    manageNovel().novelManagement()
                elif choose=="7":
                    # 这个部分先不做,只是在我之前已经爬取好的mongodb数据库中拿到图片的封面地址就可以了,用于前后端交互
                    # 先获得所有小说封面地址
                    allurllist=MongoDBHandler().queryAllcoverurlofnovel()
                    print("小说爬虫开启")
                elif choose=="8":
                    mainControl.center().control()
                # 7.退出登录
                elif choose == "9":
                    break
                # 无效输入，重新选择
                else:
                    print("输入无效,请从新输入!")
                os.system("cls")
                os.system("pause")
        else:
            print("管理员登录失败")


if __name__ == '__main__':
    admin = Administrator()
    admin.mainPart()
