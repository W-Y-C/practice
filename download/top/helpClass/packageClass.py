# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 17:26
# @File      :  packageClass.py

class package():
    def changeFaceofclass(self,enity,document):
        # 进行类对象的重新改造
        enity.style = document['style']
        enity.urlOfnovel = document['urlOfnovel']
        enity.coverofnovelurl = document['coverofnovelurl']
        enity.nameOfnovel = document['nameOfnovel']
        enity.tagOfnovel = document['tagOfnovel']
        enity.stateOfnovel = document['stateOfnovel']
        enity.briefintroductionOfnovel = document['briefintroductionOfnovel']
        enity.authorOfnovel = document['authorOfnovel']
        # 返回改造后的类对象
        return enity


