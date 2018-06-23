#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/23 20:37
# @Author  : lingxiangxiang
# @File    : demon2.py

import os

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.python.org")
time.sleep(10)
driver.quit()
