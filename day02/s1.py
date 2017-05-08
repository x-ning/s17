#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:X.Ning <ngx@ngx.wiki>

# 1. capitalize首字母大写；
name1 = 'x.ning'
new_name1 = name1.capitalize()
print(new_name1)

# 2. 将所有大小变小写，casefold牛逼，德语...
name2 = 'X.Ning'
v = name2.casefold() # 跟牛逼，德语...
print(name2)
print(v)

# 3. 将所有大小变小写
name3 = 'X.Ning'
v = name3.lower()
print(v)

# 4. 文本居中,center宽度;
# 参数1: 表示总长度
# 参数2：空白处填充的字符（长度为1）；
name4 = 'X.Ning'
new_name4 = name4.center(20)
new_name4_1 = name4.center(20,'*')
print(new_name4)
print(new_name4_1)

#