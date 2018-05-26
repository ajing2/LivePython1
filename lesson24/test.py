#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/26 21:51
# @Author  : lingxiangxiang
# @File    : test.py
import time

from demon3 import *

re1 = taskA.delay(10, 20)

re2 = taskB.delay(100, 200, 300)

re3 = add.delay(1000, 2000)

time.sleep(2)
print(re1.result)
print(re2.result)
print(re3.status)
print(re3.result)