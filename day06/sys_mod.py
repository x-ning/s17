#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: X.Ning <ngx@ngx.wiki>
import sys,os

# print(sys.argv)
#
# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

BASE_DIR=os.path.normpath(os.path.join(__file__,
    os.pardir,
    os.pardir,
    ))

print(BASE_DIR)