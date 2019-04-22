# -*- coding:utf-8 -*-
#!/usr/bin/python
from tools.function import * 
from tools.collect import Collect
from bs4 import BeautifulSoup
from tools.db_mysql import Mysql
import requests
import json


'''
抓取接口数据
author:zhangxiaoyan
date:2019-04-22
'''
class Api(object):
	url = 'http://ushq.stock.sohu.com/AFundFlow/NetValIn3Day.html'
	data = [1,3,5]
	for i in data:
		url = 'http://ushq.stock.sohu.com/AFundFlow/NetValIn'+ repr(i)+'Day.html'
		response = requests.get(url)
		if response:
			content = response.content
			print(content)
		else:
			print(repr(i)+'无返回内容')






