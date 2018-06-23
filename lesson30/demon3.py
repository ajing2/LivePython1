#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/23 21:09
# @Author  : lingxiangxiang
# @File    : demon3.py
import random
import time

import os

from selenium import webdriver


def randomSleep(minS, maxS):
    time.sleep((maxS-minS)*random.random() + minS)


url = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F'
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(url)
randomSleep(1, 3)
driver.find_elements_by_xpath('//a[@clstag="pageclick|keycount|login_pc_201804112|10"]')[0].click()

randomSleep(1, 2)
driver.find_element_by_id('loginname').clear()
randomSleep(1, 3)
driver.find_element_by_id('loginname').send_keys("18910148469")
randomSleep(1, 2)
driver.find_element_by_id('nloginpwd').send_keys("xxxx")

randomSleep(3, 5)
driver.find_element_by_id('loginsubmit').click()
randomSleep(5, 10)

print(driver.get_cookies())

driver.close()
