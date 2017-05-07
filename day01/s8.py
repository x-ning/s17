#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:X.Ning <ngx@ngx.wiki>

num_input = input('请输入数字：')
net_num = int(num_input)
name = '   我叫李杰，性别：%s,我今年%s岁；   '
new_name = name %('男',net_num)

new_val = new_name.strip() #左右都去掉；
new_lval = new_name.lstrip()
new_rval = new_name.rstrip()

print(net_num)
print(type(net_num))

print(new_name)

