# -*- coding:utf-8 -*-
#!/usr/bin/python

'''
标识是开发环境还是生产环境
environmental : development 开发环境
environmental : testing 测试环境
environmental : production 生产环境
'''
import sys

env_name = 'development' 		#注意只能是这三个值中的任何一个[development,production,testing]

if env_name == 'development':
	from config.db_config_dev import * 
elif env_name == 'testing':
	from config.db_config_test import *
elif env_name == 'production':
	from config.db_config_pro import * 	 
else:
	print('环境变量配置出错, 位置 ：' + str(sys._getframe().f_code.co_filename) + ' 第'+ str(sys._getframe().f_lineno - 9) + '行')
	print('提示：env_name 值必须为[development,production,testing]其中之一')
	exit()
