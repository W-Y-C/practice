# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/2 23:21
# @File      :  adminlogin.py

# 导入动态刷新头部网页的部分
from top.refreshWebpage.reloadHeaderhtml import refreshPage
from top.AdministratorLogin.actionOfadmin.getNamelist import getNameset
from top.AdministratorLogin.actionOfadmin.get import getadminPwd


# 验证登录模块
class loginOfadmin():
    def login(self):
        # admin_names = self.nameList  # 管理员姓名列表
        admin_names = getNameset().getAdminNameList()  # 管理员姓名列表
        for _ in range(3):
            adminName = input("请输入管理员姓名：")

            if adminName not in admin_names:
                print("用户名不存在")
                continue  # 继续输入用户名

            for _ in range(3):
                password = input("请输入密码：")
                # 从数据库中获取管理员密码,用以校验用户密码是否正确
                # admin_password = self.getAdminpassword(adminName)  # 管理员密码
                admin_password = getadminPwd().getAdminpassword(adminName)  # 管理员密码

                if password != admin_password:
                    print("密码错误")
                else:
                    # html = f'<a href="../html/czj/kuaikanlanding.html" target="_parent"><span style="white-space: nowrap";>{adminName}</span></a>'
                    # refreshPage().overwrite_html(html)
                    return (True, adminName)  # 登录成功
                    pass

            print("输入错误次数过多，登录失败")
            return (False, adminName)  # 登录失败

        print("输入错误次数过多，登录失败")

        return (False, None)  # 登录失败

if __name__ == '__main__':
    temp=loginOfadmin()
    temp.login()
