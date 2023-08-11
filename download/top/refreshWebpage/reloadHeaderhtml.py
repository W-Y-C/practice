# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/1 15:42
# @File      :  reloadHeaderhtml.py

class refreshPage():

    # 初始化
    def __init__(self):
        # 源文件路径
        self.source_file = r'C:\Users\WYCDY\Desktop\前端\部分终极版 - 副本\漫画代码temp\html\headertemp.html'
        # 目标文件路径
        self.target_file = r'C:\Users\WYCDY\Desktop\前端\部分终极版 - 副本\漫画代码temp\html\header.html'
        pass

    # 魔法动作
    def overwrite_html(self, html):
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
        html = html

        source_code = source_code.replace("{HTML}", html)

        # 将源文件的内容覆盖到目标文件中
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(source_code)

        print("ok!")


if __name__ == '__main__':
    res = refreshPage()
    # res.overwrite_html('asda')
