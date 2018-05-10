#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 20:54
# @Author  : lingxiangxiang
# @File    : demon2.py


'''
pip install SQLAchemy


cus = engine.connect()  这个跟我们上节课说的游标操作雷同的
'''

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://xiang:xiang@192.168.48.136/sqlalchemy')
print(engine)
sql = '''create table student(
  id int not null PRIMARY KEY,
  name varchar(100),
  age int,
  address varchar(100)
);'''

cus = engine.connect()
cus.execute(sql)
cus.close()
