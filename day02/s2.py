#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:X.Ning <ngx@ngx.wiki>

#14. 是否是表示符（能否做变量使用【系统关键字也可以，但除外】）
# name1 = 'x.ning'
# name2 = 'User_name'
# v1 = name1.isidentifier()
# v2 = name2.isidentifier()
# print(v1)
# print(v2)

# 15. 是否全部为小写
# name1 = 'X.Ning'
# name2 = 'x.ning'
# v1 = name1.islower()
# v2 = name2.islower()
# print(v1)
# print(v2)

# 16. 是否全部为大写
# name1 = 'X.Ning'
# name2 = 'X.NING'
# v1 = name1.isupper()
# v2 = name2.isupper()
# print(v1)
# print(v2)

# 17. 是否包含隐含的符号（\t,\n等）
# name1 = "老子天下第一"
# name2 = "谦虚 \n"
# v1 = name1.isprintable()
# v2 = name2.isprintable()
# print(v1)
# print(v2)

# 18. 是否全部是空格
# name1 = "老子天下第一"
# name2 = "\n \t"
# name3 = "   "
# v1 = name1.isspace()
# v2 = name2.isspace()
# v3 = name3.isspace()
# print(v1)
# print(v2)
# print(v3)

# 19. 字符串拼接 *****(五星级功能)
# name1 = "老子天下第一"
# name2 = "ning"
# v1 = ' '.join(name1)
# v2 = '_'.join(name2)
# print(v1)
# print(v2)

# 20. 左右填充
# center,ljust,rjust
# name = "ning"
# v = name.center(20,'*')
# v1 = name.rjust(20,'*')
# print(v)
# print(v1)