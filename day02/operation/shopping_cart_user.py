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
# print(user_info_list)
# print(user_str_list)

# 查看商品列表
commodity_info = open('commodity_db','r',encoding='utf-8')  #统一编码utf-8
commodity_data = commodity_info.read()
commodity_info.close()
commodity_list = [] #商品信息列表
commodity_str_list = [i for i in commodity_data.split('\n') if i]  #移除data.split()生成的空元素
for commodity_item in commodity_str_list:
    temp = commodity_item.split('|')
    commodity_add = {
        'commodity_name': temp[0],
        'commodity_price': temp[1],
        }
    commodity_list.append(commodity_add)
# print(commodity_list)
# print(commodity_str_list)

# 用户登录后信息
user_login = '%s欢迎您，账户余额：%d' #用户，余额
user_totle_price="账单总金额：%d"
shopping_price_totle=0
shopping_car=[]
shopping_list = []
history_shopping_list= []
history_shopping_str=''
p = 1#购物列表初始页码
state_login = 3

# print(user_login)
# print(user_totle_price)
# print(shopping_list )
hile state_login > 0 :
    user_input = input("请输入用户名：")
    pwd_input = input("请输入密码：")
    for user_item in user_info_list :
        if user_input == user_item['username'] :    # 判断是否数据库内存在的用户
            if int(user_item['times']) > 0 :        # 判断用户登录次数
                if pwd_input == user_item['password'] : # 判断用户密码是否匹配
                    print(user_input %(user_input,user_item['money']))  # 登录成功，列出个人信息
                    # index.py
                    while True :
                        print("***********************************************")
                        user_chose = input("请选择您要的操作：\n1.购物\n2.查询\n3.退出\n")
                        shopping_state = True
                        if user_chose == '1':
                            # print("**********************************************")
                            while True:
                                print("*******商品列表如下：*******")
                                if shopping_state==False:
                                    print("购物清单如下：\n")
                                    print(shopping_car)
                                    print(user_totle_price %(shopping_price_totle))
                                    if shopping_price_totle > int(user_item['money']):
                                        print("余额不足，重新购买")
                                        shopping_car.clear()                #余额不足重新购买
                                        shopping_price_totle = 0
                                        shopping_state = True
                                    else:
                                        print("购买成功")
                                        user_item['money']=int(user_item['money'])-shopping_price_totle
                                        for shopping_car_item in shopping_car:
                                            shopping_list.append(shopping_car_item)

                                            shopping_line = ''
                                            # i = 1
                                            for item5 in shopping_list:
                                                shopping_line = '\n' + shopping_line + name + '|' + item5 + "| " + now_time
                                            # 写入文件，购物记录
                                            shopping_log = open("shopping_log", 'a', encoding='utf-8')
                                            shopping_log.write(shopping_line)
                                            shopping_log.close()
                                            # 写入文件，余额计算
                                            line = ''
                                            i = 1
                                            for item2 in user_info_list:
                                                if i < user_info_list.__len__():
                                                    line = line + item2['username'] + '|' + item2['password'] + '|' + str(
                                                        item2['times']) + '|' + str(item2['money']) + '\n'
                                                    i = i + 1
                                                else:
                                                    line = line + item2['username'] + '|' + item2['password'] + '|' + str(
                                                        item2['times']) + "|" + str(item2['money'])

                                            # 写入文件
                                            f2 = open("user_info", 'w')
                                            f2.write(line)
                                            f2.close()
                                            break






