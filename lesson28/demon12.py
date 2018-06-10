#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 21:40
# @Author  : lingxiangxiang
# @File    : demon12.py
import random
import string

from PIL import Image, ImageFont, ImageDraw, ImageFilter

font_path = "msyh.ttf"
number = 4
size = (100, 30)
bgcolor = (255, 255, 255)
fontcolor = (0, 0, 255)
linecolor = (255, 0, 0)
draw_line = True
# 加入干扰线条数的上下限
line_number = 30


#生成一个随机字符串

def getNumber():
    source = list(string.ascii_letters) + list(string.digits)
    return "".join(random.sample(source, number))

#绘制干扰线
def getLine(draw, width, height):
    begin = random.randint(0, width), random.randint(0, height)
    end  = random.randint(0, width), random.randint(0, height)
    draw.line([begin, end], fill=linecolor)

def getCode():
    width, height = size
    image = Image.new("RGBA", size, bgcolor)
    font = ImageFont.truetype(font_path, 25)
    draw = ImageDraw.Draw(image)
    text = getNumber()
    font_width, font_height = font.getsize(text)
    draw.text(((width - font_width) / 2, (height - font_height) / 2), text, font=font, fill=fontcolor)  # 填充字符串
    if draw_line:
        for i in range(line_number):
            getLine(draw, width, height)

    # image = image.transform((width + 20, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)  # 创建扭曲
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强
    image.save('idencode.png')  # 保存验证码图片
    # image.show()
if __name__ == '__main__':
    getCode()
