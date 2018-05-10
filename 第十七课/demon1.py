#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 20:36
# @Author  : lingxiangxiang
# @File    : demon1.py

'''
stduent  id, name, age, sex, grader

[
(1, 'ling', 18, 'M', 59)
(2, 'shang', 26, 'F', 88)
(3, 'ajing', 31, 'M', 94)
]

tuple  数据不可变
想知道表的结构，int  varchar



[
Student1
Student2
Student3
Student4
Student5
]
获取具体对象，遍历一遍就可以了，然后通过对象的属性获取到对应值

ORM 思想
object-relation mapping
'''

# SQLAlchemy

#
# for x in student:
#     for y in studnet[x]:
#         student[x][y]


'''
表  student
id, name, age, sex, grander

类  module
id, name, age, sex, grander
类的属性和表字段是一一对应的

每张表都会有一个对应的类

'''


class Student(object):
    def __init__(self, id, name, age, sex, grander):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.grander = grander

student1 = Student('10001', 'ling', 25, 'M', 78)
print(student1.name)

