#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 21:24
# @Author  : lingxiangxiang
# @File    : demon3.py

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('mysql+pymysql://xiang:xiang@192.168.48.136/sqlalchemy')
metadata = MetaData(engine)

teacher = Table('teacher', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(50), ),
            Column('age', Integer),
            Column('sex', String(10)),
)
metadata.create_all(engine)