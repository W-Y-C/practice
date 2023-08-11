# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 0:22
# @File      :  managementofnovel.py

from top.helpClass.MongodbUntils import MongoDBHandler

class manageNovel():
    def __init__(self):
        self.client=MongoDBHandler()
    def novelManagement(self):
        while True:
            print("-----------------------------------------------")
            print("1.查看所有小说")
            print("2.按相关属性查找小说")
            print("3.按名称修改指定小说")
            print("4.管理员退出小说管理")
            print("-----------------------------------------------")
            choose = input("请输入你的选择:")
            if choose == "1":
                self.client=MongoDBHandler()
                self.client.find_alldocument()


                # 动态刷新网页部分(之后再添加)

            elif choose == "2":
                print("1-根据小说类型查询\n2-根据小说标签查询\n3-根据具体小说名称查询")
                while True:
                    yourchoose=input("请输入你的选择")
                    query=''
                    if yourchoose=='1':
                        print("根据小说类型查询")
                        temp=input("请输入你要查询的小说类型:")
                        query={'style':temp}
                        break
                    elif yourchoose=='2':
                        print("tagOfnovel")
                        temp = input("根据小说标签查询")
                        query = {'tagOfnovel': temp}
                        break
                    elif yourchoose=='3':
                        print("根据具体小说名称查询")
                        temp = input("请输入你要查询的小说类型:")
                        query = {'nameOfnovel': temp}
                        break
                    elif yourchoose=='0':
                        print('退出选择查询功能')
                        break
                    else:
                        print("输入无效,请重新输入1-3的数字")
                        continue
                # 查询数据
                self.client.query_documents(query)

            elif choose == "3":
                name=input("请输入要修改小说的名称:")
                # 获取数据库存在的所有小说名称(用来判断搜索的小说是否存在)
                namelist=self.client.queryAllnameofnovel()
                if name in namelist:
                    filter = {'nameOfnovel': name}
                    update = {'$set': {'stateOfnovel': input("请输入更新后的小说状态:")}}
                    self.client.update_document(filter,update)
                else:
                    break
            # 傅总别跪了，夫人要带着你的崽再嫁
            elif choose == "4":
                break
            else:
                print("输入无效,请重新输入相应的选项")
        pass


if __name__ == '__main__':
    manageNovel().novelManagement()
    pass