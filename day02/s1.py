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

# 5. 表示传入之在字符串中出现的次数

name5 = "alexasdfdsafsdfasdfaaaaaaaa"

# 5.1. 该字节存在的个数
v = name5.count('a')
print(v)

v = name5.count('df')
print(v)

# 5.2 该字节存在12位之后的个数
v = name5.count('df',12)
print(v)

# 5.3 表示传入之在字符串中出现的次数
# 参数1： 要查找的值（子序列）
# 参数2： 起始位置（索引）
# 参数3： 结束位置（索引）
v = name5.count('df',0,15)
print(v)

# 6. 是否以xx结尾
name6 = 'X.Ning'
v = name6.endswith('ng')
print(v)

# 7. 是否以xx开头
name7 = 'X.Ning'
v = name7.startswith('X')
print(v)

# 8. encode欠

# 9. 找到制表符\t,进行替换（包含前面的值）
# PS: \n
name9 = "al\te\tx\nalex\tuu\tkkk"
# 此处20代表20个空格
v = name9.expandtabs(20)
print(v)

# 10. 找到指定子序列的索引位置：
# find 不存在返回-1
name10 = 'alex'
v = name10.find('o')
print(v)
# index 不存在会报错
v = name10.index('l')
print(v)

# 11.字符串格式化

# tpl = "我是:%s;年龄:%s;性别:%s"

# 11.1 使用索引位置
tpl11_1 = "我是:{0};年龄:{1};性别:{2}"
v = tpl11_1.format("李杰",19,'都行')
print(v)

# 11.2 使用类似变量的效果定义
tpl11_2 = "我是:{name};年龄:{age};性别:{gender}"
v = tpl11_2.format(name='李杰',age=19,gender='随意')
print(v)

# 11.3 使用字典进行效果定义
tpl11_3 = "我是:{name};年龄:{age};性别:{gender}"
v = tpl11_3.format_map({'name':"李杰",'age':19,'gender':'中'})
print(v)


# 12. 是否是数字、汉字
name12 = 'alex8汉字'
v = name12.isalnum() #数字，汉字
print(v) # True
v2 = name12.isalpha()
print(v2)# False


# 13. 判断是否是数字
num = '②'
v1 = num.isdecimal() # '123'
v2 = num.isdigit()   # '123'，'②'
v3 = num.isnumeric() # '123'，'二'，'②'
print(v1,v2,v3)
