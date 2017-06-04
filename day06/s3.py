#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: X.Ning <ngx@ngx.wiki>
import os,sys,time


# sys_path=os.path.abspath(__file__)
# print(sys_path)

# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
# print(__file__)

for i in range(50):
    sys.stdout.write('%s\r' %('#'*i))
    sys.stdout.flush()
    time.sleep(0.1)
