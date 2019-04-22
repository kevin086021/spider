# -*- coding:utf-8 -*-
#!/usr/bin/python

import time, socket, random
from datetime import datetime

'''
主要用来存放常用的函数
author: Kevin
date: 2019-04-21 16:45
'''

#获取当前日期或时间戳
def get_date_time(format=0, num=0):
	time_str = time.localtime(time.time()+num*24*3600)
	if format == 1:
		return time.strftime('%Y-%m-%d %H:%M:%S', time_str)
	elif format == 2:
		return time.strftime('%Y-%m-%d', time_str)	
	elif format == 3:
		return time.strftime('%Y%m%d%H%M%S', time_str)
	elif format == 4:
		return time.strftime('%Y%m%d', time_str)
	else:
		return int(time.time())
		

def get_share_code(code):
	strCode = str(code) 
	num = len(strCode)

	if num == 1:
		return '00000' + strCode
	elif num == 2: 
		return '0000' + strCode 
	elif num == 3:
		return '000' + strCode
	elif num == 4:
		return '00' + strCode
	elif num == 5:
		return '0' + strCode 
	else:
		return strCode 

#获取主机名
def get_host_name():
	return socket.getfqdn(socket.gethostname())

#获取主机IP
def get_host_ip():
	return socket.gethostbyname(get_host_name())

#生成随机数
def get_rand(begin_num=0, end_num=999999):
	return int(random.uniform(begin_num, end_num))

#调试打印
def prt(my_object='', not_stop=0):
	print('\n\n')
	print(get_date_time(1) + ' 输出结果开始')
	print('###################################')
	print(my_object)
	print('###################################')
	print(get_date_time(1) + ' 输出结果结束')
	print('\n\n\n')
	if not not_stop:
		exit()
