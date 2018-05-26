#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 22:52
# @Author  : lingxiangxiang
# @File    : demon3.py

from celery import Celery

app = Celery()
app.config_from_object("celeryconfig")

@app.task
def taskA(x, y):
    return x*y

@app.task
def taskB(x, y, z):
    return x+y+z

@app.task
def add(x, y):
    return x+y