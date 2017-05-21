#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:X.Ning <ngx@ngx.wiki>

def f1():
    x = 1
    y = 2
    def f2():
        print(x,y)
    return f2
f=f1()
print(f.__closure__)
print(f.__closure__[0].cell_contents)