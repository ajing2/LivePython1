#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/5 20:30
# @Author  : lingxiangxiang
# @File    : demon1.py

# mysql
# ORM
# java
# django  mysql  filter  __id
# select update delete insert

import pymysql

# 1. 开启事务
# 2. 执行sql语句（update100， insert1000， alter10）
# 3. commit；


conn = pymysql.connect(host="192.168.48.136", port=3306, user="xiang", passwd="xiang", db="test")
cus = conn.cursor()
sql = "select * from test2;"

cus.execute(sql)
result = cus.fetchall()
print(result)
cus.close()
conn.close()




