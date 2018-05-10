#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 22:17
# @Author  : lingxiangxiang
# @File    : demon5.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from 第十七课.demon4 import Student

engine = create_engine('mysql+pymysql://xiang:xiang@192.168.48.136/sqlalchemy')
DBsession = sessionmaker(bind=engine)
session = DBsession()

session.query(Student)
