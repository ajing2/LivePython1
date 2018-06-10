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
print(image.format, image.size, image.mode)
image.show()

#image的方法
#image.show()
#image.open(file)
#image.save(outputfile)
#image.crop(left, upper, right, lower)#抠图

# Image的几何处理：
# out = im.resize((128, 128))                     #调整图片大小
# out = im.rotate(45)                             #逆时针旋转 45 度角。
# out = im.transpose(Image.FLIP_LEFT_RIGHT)       #左右对换。
# out = im.transpose(Image.FLIP_TOP_BOTTOM)       #上下对换。
# out = im.transpose(Image.ROTATE_90)             #旋转 90 度角。
# out = im.transpose(Image.ROTATE_180)            #旋转 180 度角。
# out = im.transpose(Image.ROTATE_270)            #旋转 270 度角。
