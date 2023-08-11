import random
from datetime import datetime
from top.helpClass.DBUntils import DBHelper
import os
from top.allEntity.userEnity import user


class RegistrationSystem:  # 定义注册名单及初始化
    def __init__(self):
        self.db = DBHelper()

    # 获取所有已经注册过的用户名,用于判断输入的用户名是否已经存在
    def getAlluserNamelist(self):
        select_sql = "select userName from user"
        rs = self.db.RunSQLReturnDS(select_sql)
        userNamelist = []
        for r in rs:
            userNamelist.append(r[0])
        return userNamelist


    def register(self):
        name = None
        count = 0  # 计数器用于统计密码不一致的次数
        while True:
            name = input("请输入用户名:")
            if name not in self.getAlluserNamelist():  # 检查用户名是否已存在
                gender = input("请输入用户性别:")
                phone = input("请输入用户手机号:")
                state = input("请输入用户状态:")
                age = input("请输入用户年龄:")
                method = input("请输入用户注册方式:")
                regist = str(datetime.now().date().strftime("%Y-%m-%d"))  # 获取当前日期作为注册日期
                password = input("请输入注册密码:")
                second_password = input("请再一次输入密码:")

                while password != second_password:
                    count += 1
                    print("两次密码不相同")
                    if count >= 3:
                        print("重新输入密码超过三次,注册机会用完,请等待一段时间后再注册")
                        break
                    second_password = input("请再一次输入密码:")

                if count < 3:
                    use = user(name, password, phone, gender, age, state, regist, method)  # 创建User对象
                    print(use)

                    generated_verification_code = self.generate_verification_code()  # 生成验证码
                    print("验证码:", generated_verification_code)

                    user_input_verification_code = input("请输入验证码:")  # 获取用户输入的验证码

                    if user_input_verification_code == generated_verification_code:  # 验证码验证通过
                        self.insert_table(use)  # 插入用户数据到表中
                        break
                    else:
                        print("验证码验证失败，请重新输入")
                else:
                    print("超过3次注册机会，暂时无法注册")
                    break
            else:
                print("该用户已存在，请重新输入")

    # 将新用户的身份信息插入到item数据库的user数据表之中
    def insert_table(self, use):
        insert_sql = "INSERT INTO user (userName, userPassword, userPhone, userGender, userAge, userState, userRegistTime, userRegistMethod) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        # 要插入的数据
        data = (
            use.userName, use.userPassword, use.userPhone, use.userGender, use.userAge, use.userState,
            use.userRegistTime,
            use.userRegistMethod)
        self.db.RunSQl(insert_sql, data)

    # 产生0~10 A~Z a~z的数组
    def password(self):
        list_temp = []
        i = 0
        s = ""
        for i in range(0, 10):
            list_temp.append(str(i))
        for i in range(65, 91):
            list_temp.append(chr(i))
        for i in range(97, 123):
            list_temp.append(chr(i))
        return list_temp

    # 产生六位的验证码
    def generate_verification_code(self):
        i = 0
        verification_code = ""
        while i <= 5:
            verification_code += random.choice(self.password())
            i += 1
        return verification_code


if __name__ == '__main__':
    registration_system = RegistrationSystem()
    registration_system.register()

