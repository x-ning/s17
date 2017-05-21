#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:X.Ning <ngx@ngx.wiki>

def foo():
    print("one")
    yield 1
    print("two")
    yield 2
    print("three")
    yield 3
    print("four")
    yield 4

g=foo()
print(next(g))
print(next(g))
print(next(g))
print(next(g))