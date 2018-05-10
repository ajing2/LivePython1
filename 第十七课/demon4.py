#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 22:04
# @Author  : lingxiangxiang
# @File    : demon4.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://xiang:xiang@192.168.48.136/sqlalchemy')
DBsession = sessionmaker(bind=engine)
session = DBsession()

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    address = Column(String(100))

student1 = Student(id=1001, name='ling', age=25, address="beijing")
student2 = Student(id=1002, name='molin', age=18, address="jiangxi")
student3 = Student(id=1003, name='karl', age=16, address="suzhou")

# session.add_all([student1, student2, student3])
# session.commit()
# session.close()

a = session.query(Student).filter(Student.id>1001).all()
print(a)
for i in a:
    print(i.id)
    print(i.name)
    print(i.age)
    print(i.address)


'''
filter和filter_by

filter_by(name="ling")  不能使用>  <  =
filter(Student.id>1001)  这个就必须使用Student.id  可以使用> < =等
'''