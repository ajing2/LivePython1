#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 21:17
# @Author  : lingxiangxiang
# @File    : demon8.py

'''python3 操作图片需要
pip install pillow
'''
from PIL import Image
image = Image.open("test.jpg")

cutjpg = image.crop((320, 65, 460, 220))
cutjpg.show()

