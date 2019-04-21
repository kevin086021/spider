# -*- coding:utf-8 -*-
#!/usr/bin/python

import pymysql
from config.db_config import * 
'''
连接Mysql的数据库类
author: Kevin
date: 2019-04-21 16:46
'''
class Mysql:

	_db_host = DB_HOST				#数据库地址
	_db_user = DB_USER_NAME				#数据库连接用户名
	_db_pass = DB_PASSWORD				#数据库密码
	_db_name = DB_NAME				#数据库名称
	_db_port = DB_PORT				#数据库端口号
	_db_charset = DB_CHARSET			#数据库编码方式

	_db_connect = None				#连接数据库的实例对象
	_db_connect_flag = True	 			#数据库连接标识

	# 初始化
	def __init__(self):
		self._db_connect()

	# 释放数据库的连接
	def __del__(self):
		if self._db_connect_flag:
			self._db_connect.close()

	# 打开数据库连接
	def _db_connect(self):
		try:
			self._db_connect = pymysql.connect(
					host = self._db_host,
	                user = self._db_user,
	                password = self._db_pass,
	                port = self._db_port,
	                db = self._db_name,
	                charset = self._db_charset,
	                cursorclass = pymysql.cursors.DictCursor
	            )
		except Exception as e:
			self._db_connect_flag = False
			print(e)
			exit()

	# 获取游标
	def _db_cusor(self, sql):
		cursor = []
		try:
			cursor = self._db_connect.cursor()
			cursor.execute(sql)
			return cursor
		except Exception as e:
			print(e)
			exit()
		return cursor

	# 获取一条数据
	def get_data(self, sql):
		try:
			cursor = self._db_connect.cursor()
		except Exception as e:
			print(e)
			exit()
		cursor.execute(sql)	
		try:
			record = cursor.fetchone()
			if not record:
				return None	
		except Exception as e:
			print(e)
			exit()
		del cursor
		return record

	# 获取影响行数
	def get_count(self, sql):
		result = 0
		try:
			cursor = self._db_connect.cursor()
			result =  cursor.execute(sql)
		except Exception as e:
			print(e)
			exit()
		return result

	# 获取多条行数
	def get_data_list(self, sql):
		try:
			cursor = self._db_connect.cursor()
		except Exception as e:
			print(e)
			exit()
		cursor.execute(sql)	
		try:
			recordList = cursor.fetchall()
			if not recordList:
				return None	
		except Exception as e:
			print(e)
			exit()
		del cursor
		return recordList		

	# 执行SQL，一般用于插入，更新或删除
	def execute(self, sql):
		try:
			self._db_cusor(sql)
			self._db_connect.commit()
		except:
			self._db_connect.rollback()



