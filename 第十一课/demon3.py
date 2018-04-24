#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 21:14
# @Author  : lingxiangxiang
# @File    : demon3.py
'''
os模块

os.name
如果结果为nt， 则为windows系统，
如果结果为posix， 则为unix系统

os.system(cmd)   纯粹的执行系统命令，但是没有返回结果
result = os.popen(cmd)
result.read()  这样你就可以对reuslt进行控制了

os.

'''


import os

print(os.name)

if os.name == "nt":
    cmd = "ipconfig"
elif os.name == "posix":
    cmd = "ifconfig"

# os.system(cmd)

print(os.listdir("C:"))   #列出当前目录， ls
# os.chdir("..")   #改变目录， cd
print(os.listdir())
print(os.getcwd())  #pwd
# os.mkdir("test")
# os.remove("myapp.log")
# os.rmdir("test")
# os.rename("demon1.py", "demon111.py")
print(os.linesep)
# windows换行符\n\r  linux换行符\n   mac \r

if not os.path.exists("test"):
    os.mkdir("test")

print(os.path.abspath("./"))
print(os.path.split("E:\LivePython1\第十一课"))

