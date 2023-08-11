# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/2 20:09
# @File      :  MongodbUntils.py


# demo数据库中的test数据表
from pymongo import MongoClient
from top.allEntity.novelEnity import novel
from top.helpClass.packageClass import package

class MongoDBHandler:
    # temp1数据库中的alltypenovel中有所有的小说数据,包括了所有类型(恋爱,穿越.....)
    # 现在默认使用的是demo数据库下的test数据库做测试

    # 类对象初始化
    def __init__(self, host='localhost', port=27017, db_name='temp1'):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        # 小说实体类,用于直接返回novel()类对象,调用的时候只进行一步初始化就行,然后不断地覆盖这个对象
        self.novel=novel()

    # 根据小说名称查询数据
    def find_data_by_name(self,property_name='nameOfnovel', property_value='宝可梦之路过的假面骑士',collection_name="alltypenovel"):
        collection = self.db[collection_name]
        query = {property_name: property_value}
        result = collection.find_one(query)
        print(result)


    # 根据小说名称查看这一个小说
    # filter = {'name': 'Alice'}
    # handler.delete_document(filter)
    # 搜索小说名称不存在,直接退出搜索
    def findonenovelByname(self,filter,collection_name="alltypenovel"):
        if filter['nameOfnovel'] not in self.queryAllnameofnovel():
            print(f"{filter['nameOfnovel']}不存在!")
            exit()
        collection = self.db[collection_name]
        result = collection.find_one(filter)
        print(f"Find {result.deleted_count} document")


    # 输出所有的小说记录,所有的
    def find_alldocument(self,collection_name="alltypenovel"):
        collection = self.db[collection_name]
        # 获取集合中的全部文档（数据记录）
        documents = collection.find()
        # 遍历打印每个文档的内容
        for document in documents:
            if 'style' in document:
            # print(document)
            # 调用进一步封装类的对象
                novel=package().changeFaceofclass(self.novel,document)
                print(novel)
                print("-"*100)

    # handler.insert_document(data)
    def insert_document(self,data,collection_name='alltypenovel'):
        collection = self.db[collection_name]
        result = collection.insert_one(data)
        print(f"Inserted document with ID: {result.inserted_id}")

    # 根据筛选条件进行删除小说记录
    # 删除数据
    # filter = {'name': 'Alice'}
    # handler.delete_document(filter)

    # filter = {'nameOfnovel': '鬼灭之刃—无殇'}
    # 按照'nameOfnovel'进行删除
    def delete_document(self,filter= {'nameOfnovel': '宝可梦之路过的假面骑士'},collection_name='alltypenovel'):
        # 如果不存在'nameOfnovel'的话直接结束删除操作
        if filter['nameOfnovel'] not in self.queryAllnameofnovel():
            print(f"{filter['nameOfnovel']}不存在!")
            exit()
        collection = self.db[collection_name]
        result = collection.delete_one(filter)
        print(f"Deleted {result.deleted_count} document")


    #根据小说名称修改小说的状态(完结,连载中,爆更....)
    # query={'nameOfnovel':"太古封魔"}
    # update = {'$set': {'stateOfnovel': '爆更'}}
    # handler.update_document(
    # {'nameOfnovel':"太古封魔"},{'$set': {'stateOfnovel': '爆更'}})
    def update_document(self, filter, update, collection_name='alltypenovel'):
        collection = self.db[collection_name]
        result = collection.update_one(filter, update)
        print(f"Modified {result.modified_count} document")

    # 检索同类型的所有小说
    # query={'style':"玄幻奇幻"}
    def query_documents(self, query={'style':"玄幻奇幻"}, collection_name='alltypenovel'):
        collection = self.db[collection_name]
        result = collection.find(query)
        i=0
        for document in result:
            i+=1
            # print(document)
            novel=package().changeFaceofclass(self.novel,document)
            print(novel)
            print("-"*100)
        print(f"一共为您检索到{i}条相关小说信息")

    # 返回小说姓名组成的列表(改变一下代码)
    # def queryAllnameofnovel(self,collection_name='alltypenovel'):
    #     collection = self.db[collection_name]
    #     nameList=[]
    #     # 查询指定属性的全部内容
    #     result = collection.find({}, {"nameOfnovel": 1})
    #     for i in result:
    #         nameList.append(i['nameOfnovel'])
    #     return nameList

    # 返回小说封面地址组成的列表(用以后面的网页动态刷新)
    def queryAllcoverurlofnovel(self,collection_name='alltypenovel'):
        collection = self.db[collection_name]
        coverurlList = []
        # 查询指定属性的全部内容
        result = collection.find({}, {"coverofnovelurl": 1})
        for i in result:
            coverurlList.append(i['coverofnovelurl'])
        return coverurlList

    # 返回所有类型小说的封面地址,但我们只截取了15条数据
    def getonetypenovelcoveraddress(self,style,collection_name='alltypenovel'):
        collection = self.db[collection_name]
        onetypenovel = []
        # 查询指定属性的全部内容
        result = collection.find({}, {"style": style})
        for i in result:
            onetypenovel.append(i)
        # 返回15条小说封面地址,用于动态刷新网页使用
        return onetypenovel[0:15]


if __name__ == '__main__':
    handler = MongoDBHandler()
    handler.find_data_by_name()


#-------------------------------------------------------------------------------------------------

#

