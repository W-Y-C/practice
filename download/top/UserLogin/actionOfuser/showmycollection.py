# -*- coding :  utf-8 -*-
# @Author    :  WYCDY
# @Software  :  Pycharm
# @Time      :  2023/8/3 1:29
# @File      :  showmycollection.py


from top.helpClass.DBUntils import DBHelper
from top.allEntity.comicEnity import comic

class collectionofcomic():
    # 我的收藏
    def userCollection(self, name):
        data = (name,)
        select_sql = "select * from usercollectiontable where userName=%s"
        rs = DBHelper().RunSQLReturnDS(select_sql, data)
        for r in rs:
            cartoon = comic(r[0], r[1], r[2], r[3], r[4], r[5],
                            r[6])
            print(cartoon)