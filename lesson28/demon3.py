#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 22:00
# @Author  : lingxiangxiang
# @File    : demon3.py

import xlwt

workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet("test1", cell_overwrite_ok=True)
sheet1.write(0,0,"hello1")
sheet1.write(0,1,"hello2")
sheet1.write(0,2,"hello3")
sheet1.write(1,0,"word1")
sheet1.write(1,1,"word2")
sheet1.write(1,2,"word3")
sheet1.write(1,3,"word4")

workbook.save("testwrite.xls")
print("create ok")