#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'PJ'
__mtime__ = '2018/5/31'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
from .utils import get_page, get_page_to_json
import re
import requests


class MetaClass(type):

	def __new__(cls, name, bases, attrs):
		count = 0
		attrs['__CrawlFunc__'] = []
		for k, v in attrs.items():
			if 'crawl_' in k:
				attrs['__CrawlFunc__'].append(k)
				count += 1
		attrs['__CrawlFuncCount__'] = count
		return type.__new__(cls, name, bases, attrs)


class FreeDataGetter(object, metaclass=MetaClass):

	def get_raw_data(self, callback):
		datas = []
		print('Callback', callback)
		for data in eval("self.{}()".format(callback)):
			print('Getting', data, 'from', callback)
			datas.append(data)
		return datas

	def crawl_ip181(self):
		start_url = 'https://recommender-api-ms.juejin.im/v1/get_recommended_entry?suid=3rryayuNbjzyNEyifVER&ab=welcome_3&src=web'
		html = get_page_to_json(start_url)
		# ip_adress = re.compile('<tr.*?>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
		# # \s* 匹配空格，起到换行作用
		# re_ip_adress = ip_adress.findall(html)
		# for adress, port in re_ip_adress:
		# 	result = adress + ':' + port
		# 	yield result.replace(' ', '')
		yield html

	def crawl_xicidaili(self):
		for page in range(1, 4):
			start_url = 'http://www.xicidaili.com/wt/{}'.format(page)
			html = get_page(start_url)
			ip_adress = re.compile(
				'<td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
			# \s* 匹配空格，起到换行作用
			re_ip_adress = ip_adress.findall(html)
			for adress, port in re_ip_adress:
				result = adress + ':' + port
				yield result.replace(' ', '')