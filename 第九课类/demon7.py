#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 21:55
# @Author  : lingxiangxiang
# @File    : demon7.py
'''
10学生

id
name
score
'''

# class Student(object):
#     __id = int()
#     __name = str()
#     __score = int()
#
#     def getId(self):
#         return self.__id
#     def setId(self, id):
#         self.__id = id
#
#     def getName(self):
#         return self.__name
#     def setName(self, name):
#         self.__name = name
#
#     def getScore(self):
#         return self.__score
#     def setScore(self, score):
#         self.__score = score
import codecs


class Student(object):
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score



class InitStduents():
    def __init__(self):
        self.students = list()
        self.init()
    def init(self):
        self.students.append(Student(1001, "aaa", 59))
        self.students.append(Student(1002, "bbb", 96))
        self.students.append(Student(1003, "ccc", 87))
        self.students.append(Student(1004, "ddd", 89))
        self.students.append(Student(1005, "eee", 33))
        self.students.append(Student(1006, "fff", 85))
        self.students.append(Student(1007, "ggg", 78))
        self.students.append(Student(1008, "hhh", 97))
        self.students.append(Student(1009, "iii", 31))
        self.students.append(Student(1010, "jjj", 93))

    def sort(self):
        return sorted(self.students, key=lambda student: student.score)

    def writeFile(self, newStudents):
        with codecs.open("sortStudent.txt", "w")as f:
            for i in newStudents:
                f.write("id = {0}".format(i.id))
                f.write("\t")
                f.write("name = {0}".format(i.name))
                f.write("\t")
                f.write("score = {0}".format(i.score))
                f.write("\n")


def main():
    students = InitStduents()
    newStudents = students.sort()
    students.writeFile(newStudents)


if __name__ == "__main__":
    main()
