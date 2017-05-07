#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: X.Ning <ngx@ngx.wiki>


user_info_list = [{'name': 'alex', 'pwd': '123123', 'times': '3'}, {'name': 'eric', 'pwd': '123123', 'times': '3'}]
user_name = input("请输入用户名：")
user_passwd = input("请输入密码：")

for item in user_info_list:
    if user_name == item['name']:
        if user_passwd == item['pwd']:
            print("登录成功")
            break
        else:
            print("密码不正确,请重试....")
            y = 1
            while y < int(item['times']):
                new_passwd = input("请重新输入密码：")
                if  new_passwd == item['pwd']:
                    print("登录成功")
                    break
                else:
                    print("密码不正确，请重试.....")
                y += 1
                if y==3:
                    print("错误次数过多，用户被锁定....")
                    break
    else:
        print ("用户不存在.......")