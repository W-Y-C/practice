import os
# 导入管理员模块
from top.AdministratorLogin.admin import Administrator
# 导入注册用户模块
from top.RegisteredUsers.register import RegistrationSystem
# 导入用户管理模块
from top.UserLogin.consumer import Consumer
# 导入页面模块
from top.allMenue.mainpage import centerofcontrol


if __name__ == '__main__':
    while True:
        centerofcontrol().menue_show()
        choose = input("尊敬的顾客,请输入您的选择:")
        # 1.管理员登录
        if choose=="1":
            # # 导入管理员模块
            # from top.AdministratorLogin.admin import Administrator
            Administrator().mainPart()
        # 2.用户登录
        elif choose=="2":
            # 导入用户管理模块
            # from top.UserLogin.consumer import Consumer
            Consumer().mainPart()
        # 3.注册用户
        elif choose=="3":
            # 导入注册用户模块
            # from top.RegisteredUsers.register import RegistrationSystem
            RegistrationSystem().register()
        # 4.退出系统
        elif choose=="4":
            print("是否确定退出后台管理系统:\n1-暂不退出\n其它-立刻退出")
            choose=input("请输入你的选择:")
            if choose=="1":
                print("暂不退出!")
                continue
            else:
                break
        # 无效输入，重新选择
        else:
            print("请重新输入!")

        os.system("cls")
        os.system("pause")


