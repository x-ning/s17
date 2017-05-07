#!/usr/bin/env python
# -*- coding:utf-8 -*-
import getpass

name = input("请输入姓名：")
pwd = getpass.getpass("请输入密码：")
age = input("请输入年龄：")

# print(name)
# print(pwd)
# print(age)
if name == 'alex' and pwd == 'sb':
    print('欢迎使用！')
else:
    print('滚蛋！')