# -*- coding:utf-8 -*-
#!/usr/bin/python
from tools.function import * 
from tools.collect import Collect
from bs4 import BeautifulSoup
from tools.db_mysql import Mysql 

'''
小说爬虫类示例
author:Kevin
date:2019-04-21 21:44
'''
class Xiaoshuo(object):

	_db = None

	def __init__(self):
		super(Xiaoshuo, self).__init__()
		self.check_table()

	def run(self):
		self.get_content()

	def check_table(self):
		sql = "SELECT `table_name` FROM information_schema.TABLES WHERE TABLE_SCHEMA=(select database()) and `table_name` ='xiaoshuo';"
		self._db = Mysql()
		exist = self._db.get_data(sql)
		if not exist:
			sql = "CREATE TABLE `xiaoshuo` (\
  					`id` int(11) NOT NULL AUTO_INCREMENT,\
  					`title` varchar(256) NOT NULL,\
  					`url` varchar(512) NOT NULL,\
  					PRIMARY KEY (`id`),\
  					UNIQUE KEY `url` (`url`(255))\
					) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
			self._db.execute(sql)

	def get_content(self):
		base_url = 'https://wap.qisuu.la'
		url = base_url + '/soft/sort02/'
		collect = Collect()

		html = collect.get_html(url)	#获取网页内容
		html = collect.cut(html, '<body>', '</body>')	#提取指定模块的内容

		li_list = BeautifulSoup(html).find('div', attrs={'class':'menu_nav'}).find_all('li')
		for item in li_list:
			a_obj = item.find_all('a')

			if a_obj:
				name = a_obj[0].get_text()
				pageUrl = base_url + a_obj[0].get('href')
				if name:
					sql = "REPLACE INTO `xiaoshuo` SET `title`='" + name + "', `url`='" + pageUrl + "';"
					self._db.execute(sql)

		print('完成: ' + url + ' ' + get_date_time(1))
		del html, li_list, collect, url

			

		
