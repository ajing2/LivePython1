#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 21:52
# @Author  : lingxiangxiang
# @File    : demon4.py

import subprocess
# result = subprocess.Popen("ipconfig")
result = subprocess.getoutput("ipconfig")

# print(result)


'''
call() 调用系统命令
subprocess.call(["ls", "-l"])



'''
subprocess.Popen(['dir'], stdout=subprocess.PIPE)