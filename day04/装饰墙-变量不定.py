#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:X.Ning <ngx@ngx.wiki>
import time

def timmer (func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res=func(*args,**kwargs)
        stop_time = time.time()
        print('run time is %s' %(stop_time-start_time))
        return res
    return wrapper()

@timmer
def index():
    time.sleep(3)
    print('welcome to index')
    return 1

@timmer
def foo():
    time.sleep(1)
    print('from foo')

res=index()
print(res)

res1=foo('egon')
print(res1)

