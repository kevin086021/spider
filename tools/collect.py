# -*- coding:utf-8 -*-
#!/usr/bin/python
import requests
from tools.function import * 
from bs4 import BeautifulSoup

'''
采集类
author:Kevin
date:2019-04-21 21:54
'''
class Collect(object):

	agent = False		#是否使用代理，默认不使用

	def __init__(self, is_agent=False):
		self.agent = is_agent
		if is_agent:
			self.get_agent()

	#从代理网站抓取代理的IP地址和端口号
	def get_agent(self):
		
		rand_str = str(get_rand(1, 3000))
		url='https://www.xicidaili.com/nn/'+rand_str

		headers = self.get_headers()

		session = requests.session()

		html = session.get(url, headers=headers).text
		table = BeautifulSoup(html).find('table', attrs={'id':'ip_list'}).find_all('tr')

		self.ip_list = []
		for item in table[1:]:
			lists=item.find_all('td')
			ip={'ip':'','port':''}
			if lists[5].get_text()=='HTTP':
				ip['ip']=lists[1].get_text()
				ip['port']=lists[2].get_text()
				self.ip_list.append(ip)

		del html, table, url, headers, session

	#获取头信息
	def get_headers(self):
		return {
			'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate',
			'Connection': 'keep-alive'
		}

	#返回代理服务器的URL
	def get_proxies(self):
		ip = self.ip_list[get_rand(0, len(self.ip_list)-1)]
		return {
			'http':'http://'+ip['ip']+':'+ip['port']
		}

	#提取网页内容
	def get_html(self, url):
		if self.agent:
			return requests.get(url, headers=self.get_headers(), proxies=self.get_proxies(), timeout=10).text
		else:
			response = requests.get(url)
			html = response.text
			del response
			return html

	#从指定内容中切割内容
	def cut(self, content_str, from_str, to_str='', direct='in'):
		
		if not content_str:
			return False

		from_pos = 0
		to_pos = 0

		if from_str:
			from_pos = content_str.find(from_str)

		if from_pos and to_str:
			to_pos = content_str.find(to_str)

		end = len(content_str)

		if direct == 'in':
			start = from_pos + len(from_str)
			if to_str:
				end = to_pos
		else : 
			start = from_pos
			if to_str:
				end = to_pos + len(to_str)

		result = content_str[start:end]

		#释放内存
		del content_str, from_str, to_str, direct, from_pos, to_pos

		return result 





