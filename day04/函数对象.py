#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:X.Ning <ngx@ngx.wiki>
def select (sql):
    print('==========>select')

def inster(sql):
    print('==========>add')

def update(sql):
    print('==========>update')

def delete(sql):
    print('==========>del')

func_dic={
    'select':select,
    'update':update,
    'inster':inster,
    'delete':delete
}



