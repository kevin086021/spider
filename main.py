# -*- coding:utf-8 -*-
#!/usr/bin/python
import sys, warnings
from src.xiaoshuo import Xiaoshuo

'''
主程序入口
author: Kevin
date: 2019-04-21 22:06
'''
class Main():

	def run(self, argv):

		if argv and argv[0] == 'xiaoshuo':
			obj = Xiaoshuo()
			obj.run()
		else:
			print('Nothin to do...')

if __name__ == '__main__':
	
    warnings.filterwarnings("ignore")		#获略警告
    
    work = Main()

    work.run(sys.argv[1:])


'''
执行爬小说网站的示例代码
paython main.py xiaoshuo 
'''