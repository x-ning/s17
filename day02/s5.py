#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:X.Ning <ngx@ngx.wiki>

# ##### tuple:远祖，不可被修改的列表；不可变类型 #####

user_tuple = ('FCC','ngx','X','N','FCC')

# 1. 获取个数
v = user_tuple.count('FCC')
print(v)

# 2. 获取值的第一个索引位置
v = user_tuple.index('FCC')
print(v)

# ##### 额外：
for i in user_tuple:
    print(i)

v = user_tuple[0:2]
print(v)





