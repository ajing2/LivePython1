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
position = (320, 65, 460, 220)
cutjpg = image.crop(position).transpose(Image.ROTATE_180)
image.paste(cutjpg, position)
image.show()

