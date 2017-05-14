#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:X.Ning <ngx@ngx.wiki>

reade_info = open('a',encoding='utf-8')
# data_reade = reade_info.read()
# print(data_reade)

data_reade1 = reade_info.readline()
print(data_reade1)
print(reade_info.readline(),end='')

reade_info.close()