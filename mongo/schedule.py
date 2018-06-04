#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'PJ'
__mtime__ = '2018/5/31'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
from .getter import FreeDataGetter
from multiprocessing import Process


class ValidityTester(object):
	pass


class DataAdder(object):

	def __init__(self):
		self._crawl = FreeDataGetter()


	def add_to_queue(self):
		print('DataAdder is working')
		data_count = 0
		for callback_label in range(self._crawl.__CrawlFuncCount__):
			callback = self._crawl.__CrawlFunc__[callback_label]
			raw_data = self._crawl.get_raw_data(callback)
			data_count += 1
			print(raw_data)
		print(data_count)


class Schedule(object):

	@staticmethod
	def check_data():
		adder = DataAdder()
		adder.add_to_queue()


	def run(self):
		check_process = Process(target=Schedule.check_data)
		check_process.start()

if __name__ == '__main__':
	schedule = Schedule()
	schedule.run()
