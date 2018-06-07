#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 21:15
# @Author  : lingxiangxiang
# @File    : demon2.py
import xlrd

data = xlrd.open_workbook("test.xlsx")

table = data.sheets()[0]
rows = table.nrows
cols = table.ncols
print(cols)
for i in range(rows):
    print(table.row_values(i))


print("##"*10)
for j in range(cols):
    print(table.col_values(j))


print("###"*10)
for row in range(rows):
    for col in range(cols):
        cell = table.cell_value(row, col)
        print(cell)