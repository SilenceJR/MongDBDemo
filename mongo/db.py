#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'PJ'
__mtime__ = '2018/6/1'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
from setting import HOST, PORT, DB_NAME
import pymongo


class MongoClient(object):

	def __init__(self, host=HOST, port=PORT):
		conn = pymongo.MongoClient(host=host, port=port)
		self.db = conn.DB_NAME


	def insert(self):
		print(type(self.db))
		self.db.insert({"accout":21,"user_name":"xiao"})

	def find_one(self):
		data = self.db.find_one()
		print(data)

if __name__ == '__main__':
	db = MongoClient()
	db.insert()