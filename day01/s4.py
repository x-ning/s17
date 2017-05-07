#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:X.Ning <ngx@ngx.wiki>
user_name = input('请输入用户名：')

if user_name == 'admin':
    user_type = input('请输入用户类型：')
    if user_type == '管理员':
        print('管理员您好！')
    else:
        print('其他人你好！')
else:
    print('好走不送！')