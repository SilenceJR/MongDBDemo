#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'PJ'
__mtime__ = '2018/5/31'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
from flask import Flask, g


__all__ = ['app']

app = Flask(__name__)


@app.route('/')
def index():
	return '<h2>Welcome to Data System</h2>'

@app.route('/get')
def get_Data():
	pass