#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 22:09
# @Author  : lingxiangxiang
# @File    : demon4.py
'''

pip install celery
pip install redis

安装redis，并启动redis


'''
import time

from ajing import add
re = add.delay(10, 20)
print(re.task_id)
print(re)
print(re.status)
time.sleep(2)
print(re.status)
print(re.get(timeout=1))
print(re.result)