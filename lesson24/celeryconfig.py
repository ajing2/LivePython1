#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 22:55
# @Author  : lingxiangxiang
# @File    : celeryconfig.py
from kombu import Queue, Exchange

BROKER_URL = "redis://192.168.48.136:6379/1"
CELERY_RESULT_BACKEND = "redis://192.168.48.136:6379/2"


CELERY_QUEUES = {
    Queue("default",Exchange("default"),routing_key="default"),
    Queue("for_task_A",Exchange("for_task_A"),routing_key="for_task_A"),
    Queue("for_task_B",Exchange("for_task_B"),routing_key="for_task_B")
}

CELERY_ROUTES = {
    "demon3.taskA":{"queue":"for_task_A","routing_key":"for_task_A"},
    "demon3.taskB":{"queue":"for_task_B","routing_key":"for_task_B"}
}
CELERY_TIMEZONE = 'UTC'
CELERYBEAT_SCHEDULE = {
    'taskA_schedule' : {
        'task':'demon3.taskA',
        'schedule':2,
        'args':(5,6)
    },
    'taskB_scheduler' : {
        'task':"demon3.taskB",
        "schedule":10,
        "args":(10,20,30)
    },
    'add_schedule': {
        "task":"demon3.add",
        "schedule":5,
        "args":(1,2)
    }
}
