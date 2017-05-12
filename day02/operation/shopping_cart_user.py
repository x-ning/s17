#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: X.Ning <ngx@ngx.wiki>
"""
作业：购物系统
    - 个人账户,文件： user,pwd,3,余额
    - 商品，文件
    - 查看商品分页显示：

"""

# 读取用户信息：
user_info = open('user_db','r')
user_info_data = user_info.read()
user_info.close()

user_info_list = []     #用户信息列表
user_str_list = [i for i in user_info_data.split('\n') if i]  # 移除user.split()生成的空元素
for user_item in user_str_list:
    temp = user_item.split('|')
    user_add = {
        'username': temp[0],
        'password': temp[1],
        'times': temp[2],
        'money':int(temp[3])
    }
    user_info_list.append(user_add)

# 查看商品列表
f3 = open('goods_list','r',encoding='utf-8')#需要转为utf-8
data = f3.read()
f3.close()
goods_list = []#商品信息列表
goods_str_list = [i for i in data.split('\n') if i]  # 移除data.split()生成的空元素
for goods_item in goods_str_list:
    temp = goods_item.split('|')
    v = {
        'goods_name': temp[0],
        'goods_price': temp[1],
        }
    goods_list.append(v)










