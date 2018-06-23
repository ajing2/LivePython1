#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/23 21:42
# @Author  : lingxiangxiang
# @File    : demon4.py
import random
import time

import os

from selenium import webdriver

url = 'https://kyfw.12306.cn/otn/login/init'

def randomSleep(minS, maxS):
    time.sleep((maxS-minS)*random.random() + minS)
    time.sleep((maxS-minS)*random.random() + minS)

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)


driver.get(url=url)
randomSleep(2, 5)
driver.find_element_by_id("username").clear()
randomSleep(1, 3)
driver.find_element_by_id("username").send_keys("974644081@qq.com")
randomSleep(3, 5)
driver.find_element_by_id("password").send_keys("xxx")
randomSleep(10, 15)

driver.find_element_by_id("loginSub").click()
randomSleep(10, 20)
print(driver.get_cookies())
driver.close()






