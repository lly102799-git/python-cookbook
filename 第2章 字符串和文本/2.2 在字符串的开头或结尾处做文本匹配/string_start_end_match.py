# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-20 18:57
@author: Li Luyao
"""
# 在字符串的开头或结尾按照指定的文本模式做检查，比如检查文件的扩展名
# str.startswith()、str.endswith()
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))

url = 'http://www.python.com'
print(url.startswith('http:'))

# 针对多个选项做检查，需要提供包含可能选项的元组; 如果多个备选项不是元组，要确保使用tuple()将其转换为元组
import os

filenames = os.listdir('F:\规划设计运营管理-李路遥\数据、程序及仿真结果\工商居负荷评估小工具')
docs = [name for name in filenames if name.endswith(('.m', '.txt'))]
print(docs)
print(any(name.endswith('.py') for name in filenames))

from urllib.request import urlopen


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp')):
        return urlopen(name).read
    else:
        with open(name) as f:
            return f.read()


# 和其他操作结合使用
from os import listdir
dirname = r'F:\规划设计运营管理-李路遥\数据、程序及仿真结果\工商居负荷评估小工具'
any(name.endswith(('.c', '.py', '.m')) for name in listdir(dirname))