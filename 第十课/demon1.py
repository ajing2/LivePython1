#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 20:44
# @Author  : lingxiangxiang
# @File    : demon1.py


# reset 接口
# {"msg": "除数不能为0", code: 255, data: [{"a": 1}, {"b": 2}]}
import json


def test():
    result = dict()
    try:
        print(2/0)
    except Exception as a:
        result["msg"] = "除数不能为0"
        result["code"] = 403
        result["data"] = [{"a": 1}, {"b": 2}]
    finally:
        return json.dumps(result)

if __name__ == '__main__':
    print(test())