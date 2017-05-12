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
commodity_info = open('commodity_db','r',encoding='utf-8')  #统一编码utf-8
commodity_data = commodity_info.read()
commodity_info.close()
commodity_list = [] #商品信息列表
commodity_str_list = [i for i in commodity_data.split('\n') if i]  #移除data.split()生成的空元素
for commodity_item in commodity_str_list:
    temp = commodity_item.split('|')
    v = {
        'goods_name': temp[0],
        'goods_price': temp[1],
        }
    commodity_list.append(v)










