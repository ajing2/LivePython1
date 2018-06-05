#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 21:02
# @Author  : lingxiangxiang
# @File    : demon3.py
import yagmail


args={
    "user": "15616166428@163.com",
    "password": "xxxx",
    "host": "smtp.163.com",
    "port": "465"
}


emailList=["1330101907@qq.com","zyy@mealkey.cn","2174018087@qq.com", "974644081@qq.com"]
email = yagmail.SMTP(**args)
email.send(to='974644081@qq.com',subject="原因分析",contents='''DT:SPM 是出错信息的关键词，可以在这个网页中找到出错的原因http://help.163.com/09/1224/17/5RAJ4LMH00753VB8.html，原因：550 DT:SPM 邮件正文带有很多垃圾邮件特征或发送环境缺乏规范性。需调整邮件内容或优化发送环境；原因分析邮件中带有敏感关键词，例如促销，发票等。邮件中包含超级链接，或者超级链接太多。垃圾邮件特征比较明显，例如：只有一张图片，或只有一张图片。发送相同的邮件内容太多了。处理这种情况的方法是：换其他邮箱发送，或调整邮件内容。''',cc="974644081@qq.com")







