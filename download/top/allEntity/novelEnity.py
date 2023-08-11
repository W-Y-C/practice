# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 14:39
# @File      :  novelEnity.py


# 小说实体类
class novel():
    def __init__(self, style=None, urlOfnovel=None, coverofnovelurl=None, nameOfnovel=None,
                 tagOfnovel=None, stateOfnovel=None, briefintroductionOfnovel =None,authorOfnovel=None):
        # 定义了8个属性
        # 小说的类型
        self.style = style
        # 具体小说的超链接(比如偷偷藏不住,斗破苍穹的跳转地址等等)
        self.urlOfnovel = urlOfnovel
        # 具体小说封面地址(用来做前后端交互使用)
        self.coverofnovelurl = coverofnovelurl
        # 具体小说名称(比如偷偷藏不住,斗破苍穹)
        self.nameOfnovel = nameOfnovel
        # 具体小说的标签(比如霸道总裁等等)
        self.tagOfnovel = tagOfnovel
        # 具体小说的状态(比如连载中,完结等等)
        self.stateOfnovel = stateOfnovel
        # 具体小说简介
        self.briefintroductionOfnovel = briefintroductionOfnovel
        # 具体小说作者及最后更新时间
        self.authorOfnovel = authorOfnovel

    def __str__(self):
        return (f"小说类型:{self.style}\n"
                f"具体小说超链接:{self.urlOfnovel}\n"
                f"具体小说封面地址:{self.coverofnovelurl}\n"
                f"具体小说名称:{self.nameOfnovel}\n"
                f"具体小说的标签:{self.tagOfnovel}\n"
                f"具体小说的状态:{self.stateOfnovel}\n"
                f"具体小说简介:{self.briefintroductionOfnovel}\n"
                f"具体小说作者及最后更新时间:{self.authorOfnovel}\n"
                )


if __name__ == '__main__':
    pass
    # nove=novel("偷偷藏不住",'竹已','hhhh','完结','60','asdsa')
    # print(nove)