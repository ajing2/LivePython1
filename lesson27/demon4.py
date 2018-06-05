#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 22:07
# @Author  : lingxiangxiang
# @File    : demon4.py
import email.mime.multipart
import email.mime.text
import smtplib



msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '974644081@qq.com'
msg['to'] =  '1414873973@qq.com'
msg['subject'] = 'ajing is very very cool'

context = '''
    <h1>老师好</h1>
    你好，
     这是一封自动发送的邮件。
      www.ustchacker.com hello
    '''
text = email.mime.text.MIMEText(_text=context, _subtype="html")
msg.attach(text)

em = smtplib.SMTP_SSL()
em.connect("smtp.qq.com", 465)
em.login("974644081@qq.com", 'xxxxxxxxxxxxxx')
em.sendmail(from_addr='974644081@qq.com', to_addrs='1414873973@qq.com', msg=msg.as_string())
em.quit()