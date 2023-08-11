# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/1 15:42
# @File      :  reloadCenterhtml.py

from top.helpClass.DBUntils import DBHelper
import requests
import random
from top.allEntity.templete import demo


class refreshPage2():
    # 初始化
    def __init__(self):
        # 初试化数据库
        self.db=DBHelper()
        # 源文件路径
        self.source_file=r'C:\Users\WYCDY\Desktop\前端\部分终极版 - 副本\漫画代码temp\html\czj\classifysecondtemp.html'
        # self.source_file=r'C:\Users\WYCDY\Desktop\前端\部分终极版 - 副本\漫画代码temp\html\czj\classifythirdtemp.html'
        # 目标文件路径
        self.target_file=r'C:\Users\WYCDY\Desktop\前端\部分终极版 - 副本\漫画代码temp\html\czj\classifysecond.html'
        # self.target_file=r'C:\Users\WYCDY\Desktop\前端\部分终极版 - 副本\漫画代码temp\html\czj\classifythird.html'


    # 获取root用户item数据库demo数据表中所有的demo对象
    def getAlldemo(self):
        demoList=[]
        select_sql='select * from demo'
        res=self.db.RunSQLReturnDS(select_sql)
        for re in res:
            comic=demo(re[0],re[1],re[2],re[3])
            demoList.append(comic)
        return demoList


    # 魔法动作
    def overwrite_html(self,html):
        # 源文件路径
        source_file = self.source_file

        # 目标文件路径
        target_file = self.target_file

        # 创建一个变量用于保存源文件的内容
        source_code = ""

        # 读取源文件的内容
        with open(source_file, 'r', encoding='utf-8') as f:
            source_code = f.read()

        # 网页动态修改的部分
        html=html

        source_code=source_code.replace("{HTML}",html)

        # 将源文件的内容覆盖到目标文件中
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(source_code)

        print("ok!")


if __name__ == '__main__':
    res=refreshPage2()
    # res.getRandomerequests('asda')
