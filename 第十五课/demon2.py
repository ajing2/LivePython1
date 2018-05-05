#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/5 21:39
# @Author  : lingxiangxiang
# @File    : demon2.py
import pymysql



class TestMysql(object):
    def __init__(self):
        self.dbConfig = {
            "host": "192.168.48.136",
            "port": 3306,
            "user": "xiang",
            "passwd": "xiang",
            "db": "test"
        }
        conn = pymysql.connect(**self.dbConfig)
        self.a = conn


    def select(self):
        print("select")

    def update(self):
        print("update")





if __name__ == '__main__':
    conn = TestMysql()

