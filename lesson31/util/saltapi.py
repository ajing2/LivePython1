#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 20:37
# @Author  : lingxiangxiang
# @File    : saltapi.py
import json

import requests


class SaltServer(object):
    def __init__(self):
        self.session = requests.session()
        self.token = self.getToken()
        print(self.token)


    def getToken(self):
        url =  "http://192.168.48.137:8000/login"
        headers = {"Accept": "application/json"}
        data = {
            "username": "saltapi",
            "password": "saltapi",
            "eauth": "pam"
        }
        res = self.session.post(url=url, headers=headers, data=data)
        text = res.text
        result = json.loads(text)
        token = result.get("return")[0].get("token")
        return token

    def runModules(self, minionid, fun, arg=None):
        url = "http://192.168.48.137:8000"
        data = {
            "client": "local",
            "tgt": minionid,
            "fun": fun,
            "arg": arg
        }
        resultBean = dict()
        try:
            res = self.session.post(url=url,  data=data)
            text = res.text
            data = json.loads(text).get("return")
            resultBean['code'] = 0
            resultBean['message'] = "success"
            resultBean['data'] = data
        except Exception as e:
            resultBean['code'] = 0
            resultBean['message'] = "success"
            resultBean['data'] = e
        finally:
            return resultBean


    def runRunner(self, fun, **kwargs):
        url = "http://192.168.48.137:8000"
        data = {
            "client": "runner",
            "fun": fun,
        }
        data.update(kwargs)
        print(data)
        resultBean = dict()
        try:
            res = self.session.post(url=url,  data=data)
            text = res.text
            print(text)
            data = json.loads(text).get("return")
            resultBean['code'] = 0
            resultBean['message'] = "success"
            resultBean['data'] = data
        except Exception as e:
            resultBean['code'] = 0
            resultBean['message'] = "success"
            resultBean['data'] = e
        finally:
            return resultBean
