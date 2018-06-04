#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'PJ'
__mtime__ = '2018/5/31'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import requests


def get_page(url, options={}):
	base_headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Accept-Language': 'zh-CN,zh;q=0.8'
	}
	headers = dict(base_headers, **options)
	print('Getting', url)
	try:
		r = requests.get(url, headers=headers)
		print('Getting result', url, r.status_code)
		if r.status_code == 200:
			return r.text
	except ConnectionError:
		print('Crawling Failed', url)
		return None

def get_page_to_json(url, options={}):
	base_headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Accept-Language': 'zh-CN,zh;q=0.8'
	}
	headers = dict(base_headers, **options)
	print('Getting', url)
	try:
		r = requests.get(url, headers=headers)
		print('Getting result', url, r.status_code)
		if r.status_code == 200:
			return r.json()
	except ConnectionError:
		print('Crawling Failed', url)
		return None