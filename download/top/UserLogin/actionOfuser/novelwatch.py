# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 17:10
# @File      :  novelwatch.py

from top.helpClass.MongodbUntils import MongoDBHandler
class viewnovel():
    def __init__(self):
        # 初始化mongodb数据库连接对象
        self.mdb=MongoDBHandler()

    # 检索同类型的所有小说
    # query={'style':"玄幻奇幻"}
    # 根据小说名称修改小说的状态(完结,连载中,爆更....)
    # 插入数据
    # 根据小说名称查看这一个小说
    def Novel(self, username="凤婷婷"):
        while True:
            print("-----------------------------------------------")
            print("1.查看所有小说")
            print("2.按小说名称查找小说")
            print("3.检索同类型的所有小说")
            print("4.按名称查找小说")
            print("5.按照小说名称进行删除")
            print("0.用户退出小说查看")
            print("-----------------------------------------------")
            choose = input("请输入你的选择:")
            if choose == "1":
                # def find_alldocument(self,collection_name="alltypenovel"):
                self.mdb.find_alldocument()
            # 上述显示了所有小说的内容,故可以根据漫画名字挑出自己的喜欢的添加到用户收藏表
            #     i = input("是否需要添加收藏 1-是2-否:")
            #     if i == '1':
            #         name = input("请输入你要添加的小说名字:")
            #         if name in self.mdb.queryAllnameofnovel():
            #             # 虽然在这里我们可能只添加了一个想要收藏的小说,但是我同时刷新四个上去
            #             # 进行数据库添加
            #             pass
            #         else:
            #             print("退出收藏小说操作!")
            #             exit()
            #     else:
            #         print("退出收藏小说操作!")
            #         exit()

            elif choose == "2":
                print("2.按小说名称查找小说")
                #def find_data_by_name(self,
                # property_name='nameOfnovel',
                # property_value='鬼灭之刃—无殇',
                # collection_name="alltypenovel"):
                # 默认查找'鬼灭之刃—无殇'
                property_value=input("请输入你要查询的小说名称:")
                self.mdb.find_data_by_name(property_value)
            elif choose == "3":
                print("3.检索同类型的所有小说")
                # query={'style':"玄幻奇幻"}
                # 默认查找 query={'style':"玄幻奇幻"}
                # query={'style':input("请输入你要检索的小说类型")}
                # def query_documents(self, query, collection_name='alltypenovel'):
                self.mdb.query_documents()
            elif choose == "4":
                # def find_data_by_name(self,property_name='nameOfnovel',
                # property_value='鬼灭之刃—无殇',collection_name="alltypenovel"):
                # 默认查找property_value='鬼灭之刃—无殇'
                # property_value=input("请输入你要搜索小说的名称")
                self.mdb.find_data_by_name()
                print("4.按名称查找小说")
            elif choose == "5":
                print("5.按照小说名称进行删除")
                #def delete_document(self,filter,collection_name='alltypenovel'):
                #filter = {'nameOfnovel': '鬼灭之刃—无殇'}
                #默认删除filter = {'nameOfnovel': '鬼灭之刃—无殇'}
                # filter={'nameOfnovel':input("请输入你要删除小说的名称:")}
                self.mdb.delete_document()
            elif choose=="0":
                print("用户退出操作")
                break
            else:
                print("输入无效,请重新输入相应的选项")


if __name__ == '__main__':
    vie=viewnovel()
    vie.Novel()
