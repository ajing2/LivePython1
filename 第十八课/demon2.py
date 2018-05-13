#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/13 20:55
# @Author  : lingxiangxiang
# @File    : demon2.py

from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    address = Column(String(100))






def update(session):
    student1 = session.query(Student).filter(Student.id == 1001).one()
    student1.name='test123'
    session.commit()
    student2 = session.query(Student).filter(Student.id == 1001).one()
    print(student2.name)
def delete(session):
    session.query(Student).filter(Student.id == 1001).delete()
    session.commit()

def insert(session):
    student1 = Student(id=1004, name='ling', age=28, address='shanxi')
    session.add(student1)
    session.commit()

def count(session):
    numnber = session.query(Student).filter().count()
    print("total student is {0}".format(numnber))

def groupBy(session):
    groupByAge = session.query(Student).group_by(Student.age).all()
    print(groupByAge)
    for i in groupByAge:
        print(i.id, i.name, i.age, i.address)

def orderBy(session):
    orderByAge = session.query(Student).order_by(Student.age.desc()).all()
    for x in orderByAge:
        print(x.id, x.name, x.age, x.address)





def main():
    engine = create_engine('mysql+pymysql://xiang:xiang@192.168.48.136/sqlalchemy')
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    # insert(session)
    # update(session)
    # delete(session)
    # count(session)
    # groupBy(session)
    orderBy(session)


if __name__ == '__main__':
    main()