# -*- coding:utf-8 -*-
#!/usr/bin/python
import sys, json
from tools.db_mysql import Mysql 

def main(argv):
	db = Mysql()

	print('获取一条数据')
	sql = 'SELECT id, name FROM test ORDER BY id ASC LIMIT 1'
	data_object = db.get_data(sql)
	if data_object:
		data_string = json.dumps(data_object)
		print(data_string)
	else:
		print('No data...')
	print('')
	
	print('获取多条数据')
	sql = 'SELECT id, name FROM test ORDER BY id ASC LIMIT 5'
	data_object_list = db.get_data_list(sql)
	if data_object_list:
		data_list_string = json.dumps(data_object_list)
		print(data_list_string)
	else:
		print('No data...')
	print('')

	if data_object and data_object_list:
		print('Congratulations!\n')

if __name__ == '__main__':
    main(sys.argv[1:])


'''
程序执行命令
python test_db.py 
'''