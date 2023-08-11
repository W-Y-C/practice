# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/7/30 15:15
# @File      :  comicEnity.py

class comic():
    def __init__(self, comicName=None, comicAuthor=None, comicIntroduction=None, comicState=None,
                 comicPagenumbers=None,comicCover=None,comicStyle=None):
        # 漫画名称
        self.comicName = comicName
        # 漫画作者
        self.comicAuthor = comicAuthor
        # 漫画简介
        self.comicIntroduction = comicIntroduction
        # 漫画状态
        self.comicState = comicState
        # 漫画章节数
        self.comicPagenumbers = comicPagenumbers
        # 漫画类型
        self.comicStyle = comicStyle
        # 漫画封面地址
        self.comicCoveraddress=comicCover

    def __str__(self):
        return (f"漫画名称:{self.comicName}\n"
                f"漫漶作者:{self.comicAuthor}\n"
                f"漫画简介:{self.comicIntroduction}\n"
                f"漫画状态:{self.comicState}\n"
                f"漫画正文数:{self.comicPagenumbers}\n"
                f"漫画类型:{self.comicStyle}"
                f"漫画封面地址:{self.comicCoveraddress}"
                )

if __name__ == '__main__':
    pass
    # comic=comic("偷偷藏不住",'竹已','hhhh','完结','60','asdsa')
    # print(comic)
