#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/26 20:26
# @Author  : lingxiangxiang
# @File    : utils.py
import codecs
from threading import Thread, Lock

import os


class TraceLog(Thread):
    def __init__(self, logName):
        super(TraceLog, self).__init__()
        self.logName = logName
        self.lock = Lock()
        self.contexts = []
        self.isFile()

    def isFile(self):
        if not os.path.exists(self.logName):
            with codecs.open(self.logName, 'w') as f:
                f.write("this log name is: {0}\n".format(self.logName))
                f.write("start log\n")

    def write(self, context):
        self.contexts.append(context)

    def run(self):
        while 1:
            self.lock.acquire()
            if len(self.contexts) !=0:
                with codecs.open(self.logName, "a") as f:
                    for context in self.contexts:
                        f.write(context)
                del self.contexts[:]#注意不能忘记清空
            self.lock.release()
