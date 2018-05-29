#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 20:44
# @Author  : lingxiangxiang
# @File    : createtable.py
import codecs



from sqlalchemy import Column, MetaData, Table
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://xiang:xiang@192.168.48.136/sqlalchemy')

metadata = MetaData(engine)

dictionary = Table('dictionary', metadata,
             Column('id', Integer, primary_key=True),
             Column('key', String(50)),
             Column('value', String(50))
             )
metadata.create_all(engine)









