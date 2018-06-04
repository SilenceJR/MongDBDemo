#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'PJ'
__mtime__ = '2018/6/1'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
from mongo.schedule import Schedule
from mongo.api import app


def main():
	schedule = Schedule()
	schedule.run()
	app.run()

if __name__ == '__main__':
	main()