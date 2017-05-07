#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: X.Ning <ngx@ngx.wiki>

#读取登录信息
"""
login_info = open('login.db')
login_data = login_info.read()
login_info.close()
"""
login_info = [{'name':'alex', 'pwd':'sb250','times':'1',
'name':'eric', 'pwd':'123123','times':'2',
'name':'ngx','pwd':'ngx123','times':'3',
'name':'wpq','pwd':'wpq123','times':'0',}]

#输入登录信息
user_name = ("请输入用户名：")
user_password = ("请输入密码：")

#判断登录条件
"""
user_info = login_datas.split('\n')
"""


for user_info_list in login_info :
    if user_name == user_info_list['name'] and user_password == user_info_list['pwd'] :
        print("登录成功！")
        break
    elif:
        print("密码不正确，请重新输入...")
        i = 1
        while   i < int (user_info_list['times']):
            new_password = input("请重新输入密码：")
            if new_password == user_info_list['pwd'] :
                print("登录成功！")
                break
            else:
                print("密码不正确，请重试...")
            i += 1
            if  i == 3 :
                print("错误次数过多，用户被锁定...")
                break
    else:
        print("你不是这儿的，再见...!")