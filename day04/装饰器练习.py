#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:X.Ning <ngx@ngx.wiki>
# 身份验证功能

def auth(func):
    def wrapper(*args,**kwargs):
        name = input("name >> :")
        password = input("password >> :")
        if name == 'egon' and password == '123':
            print('认证通过')
            res=func(*args,**kwargs)
            return res
        else:
            print("认证失败")
    return wrapper

@auth
def index():
    print("welcome!!!")

@auth
def home(name):
    print("welcome %s" %name)

index()
home('X')