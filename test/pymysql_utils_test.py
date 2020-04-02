# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     pymysql_utils_test
   Description :
   Author :       zenquan
   date：          2019/12/24
-------------------------------------------------
   Change Activity:
                   2019/12/24:
-------------------------------------------------
"""
__author__ = 'zenquan'

from lib.pymsql_utils import PyMysqlUtils

if __name__ == '__main__':
    # db = MyPyMysql(host="120.79.145.200", user="tiger_test", password="123123", db="tiger_test", port=3306)
    sql = "select * from t_users where id='4294'"
    # print(db)
    # print(db.db_obj())
    # print(db.cursor_obj())

    db1 = PyMysqlUtils(host="127.0.0.1", user="root", password="12345678", db="okc", port=3306)
    sql1 = "select * from okc where id=1"  # 查
    sql2 = "insert into okc(id,name) values(2,'okc')"  # 增
    sql3 = "update okc set name = '999999999999' where id = 2"  # 改
    sql4 = "delete from okc where id = 2"  # 删
    # print(db1.read_data(sql1))
    # print(db1.create_data(sql=sql2))
    # print(db1.update_data(sql=sql3))
    # print(db1.del_data(sql=sql4))