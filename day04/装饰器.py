#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:X.Ning <ngx@ngx.wiki>
import time

def timmer (func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('run time is %s' %(stop_time-start_time))
    return wrapper

@timmer
def index():
    time.sleep(3)
    print('welcome to index')

index()