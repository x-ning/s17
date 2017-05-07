#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:X.Ning <ngx@ngx.wiki>

# 1. 追加
user_list1 = ['范春成','FCC','武沛齐','Alex'] # 可变类型;
user_list1.append('X')
print(user_list1)

# 2. 清空
user_list2 = ['范春成','FCC','武沛齐','Alex']
user_list2.clear()
print(user_list2)

# 3. 拷贝（浅拷贝）
user_list3 = ['范春成','FCC','武沛齐','Alex']
v = user_list3.copy()
print(v)
print(user_list3)

# 4. 计数
user_list4 = ['范春成','FCC','武沛齐','Alex']
v = user_list4.count('FCC')
print(v)


# 5. 扩展原列表
user_list5 = ['范春成','FCC','武沛齐','Alex']
user_list5.extend(['X','N'])
print(user_list5)

# 6. 查找元素索引，没有则报错
user_list6 = ['范春成','FCC','武沛齐','Alex']
v = user_list6.index('FCC')
#v1 = user_list6.index('X')
print(v)
#print(v1)

# 7. 删除并且获取元素 -- 通过索引
user_list7 = ['范春成','FCC','武沛齐','Alex']
v = user_list7.pop(1)
print(v)
print(user_list7)

# 8. 删除  --通过值
user_list8 = ['范春成','FCC','武沛齐','Alex']
v = user_list8.remove("FCC")
print(user_list8)
print(v)

# 9. 翻转
user_list9 = ['范春成','FCC','武沛齐','Alex']
user_list9.reverse()
print(user_list9)

# 10.排序；欠参数
nums = [1,2,4,5,3,8,0,9,7]
print(nums)
# 排序，从小到大
nums.sort()
print(nums)
# 排序，从大到小
nums.sort(reverse=True)
print(nums)




