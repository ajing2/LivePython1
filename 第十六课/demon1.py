#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 20:33
# @Author  : lingxiangxiang
# @File    : demon1.py
import pymysql

# 创建连接
conn = pymysql.connect(host="192.168.48.136", port=3306, user="xiang", passwd="xiang", db="test")
# 创建游标
cus = conn.cursor()
# 定义sql
sql = "select * from test2;"

# 执行
# cus.execute(sql)
# 取所有的结果,取结果之前，一定要先执行sql
# cus.fetchall()
# 取一个结果
# cus.fetchone()
# 取10行数据
# cus.fetchmany(size=10)
# 关闭游标
# cus.close()
# cus.executemany()
try:
    cus.execute(sql)
    result = cus.fetchone()
    print(result)
except Exception as e:
    raise e
finally:
    cus.close()
    conn.close()