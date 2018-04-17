#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 22:09
# @Author  : lingxiangxiang
# @File    : demon3.py


def startEnd(author):
    def a(fun):
        def b(name):
            print("this author is {0}".format(author))
            print("start")
            fun(name)
            print("end")
        return b
    return a

@startEnd("lingxiangxiang")
def hello(name):
    print("hello {0}".format(name))


# hello = startEnd("lingxiangxiang")(hello)
# hello("ajing")

hello("ajing")