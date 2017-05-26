#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: X.Ning <ngx@ngx.wiki>
import socket,time,_thread
socket.setdefaulttimeout(5) #设置默认超时时间

def socket_port(ip,port):
    """
    输入IP和端口号，扫描判断端口是否被占用；
    """
    try:
        if port >=65535:
            print ("端口扫描结束")
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=s.connect_ex(ip,port)
        if result==0:
            lock.acquire()
            print(ip,port,"端口已占用")
            lock.release()
    except:
        print("端口扫描异常")

def ip_scan(ip):
    """
    输入IP，扫描IP的0-65535端口情况；
    """
    try:
        print("开始扫描%s",ip)
        star_time=time.time()
        for i in range(0,65535):
            _thread.start_new_thread(socket_port(ip,int(i)))
        print("端口扫描完成，总共用时：%s",(time.time()-star_time))
        #raw_input("Press Enter to Exit")
    except:
        print("扫描IP出错")

if __name__=='__main__':
    url=raw_input('Input the ip you want to scan:')
    lock=_thread.allocate_lock()
    ip_scan(url)