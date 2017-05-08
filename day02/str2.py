#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:X.Ning <ngx@ngx.wiki>

#14. 判断是否是表示符（能否做变量使用【系统关键字也为正确，但除外】）
name14_1 = 'x.ning'
name14_2 = 'User_name'
v1 = name14_1.isidentifier()
v2 = name14_2.isidentifier()
print(v1)
print(v2)

# 15. 判断是否全部为小写
name15_1 = 'X.Ning'
name15_2 = 'x.ning'
v1 = name15_1.islower()
v2 = name15_2.islower()
print(v1)
print(v2)

# 16. 是否全部为大写
name16_1 = 'X.Ning'
name16_2 = 'X.NING'
v1 = name16_1.isupper()
v2 = name16_2.isupper()
print(v1)
print(v2)

# 17. 是否包含隐含的符号（\t,\n等）
name17_1 = "老子天下第一"
name17_2 = "谦虚 \n"
v1 = name17_1.isprintable()
v2 = name17_2.isprintable()
print(v1)
print(v2)

# 18. 是否全部是空格
name18_1 = "老子天下第一"
name18_2 = "\n \t"
name18_3 = "   "
v1 = name18_1.isspace()
v2 = name18_2.isspace()
v3 = name18_3.isspace()
print(v1)
print(v2)
print(v3)

# 19. 字符串拼接 *****(五星级功能)
name19_1 = "老子天下第一"
name19_2 = "ning"
v1 = ' '.join(name19_1)
v2 = '_'.join(name19_2)
print(v1)
print(v2)

# 20. 左右填充
# center,ljust,rjust
name20 = "ning"
v = name20.center(20,'*')
v1 = name20.rjust(20,'*')
v2 = name20.ljust(10,'.')
print(v)
print(v1)
print(v2)