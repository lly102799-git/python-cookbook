# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-20 19:33
@author: Li Luyao
"""

# 相较于startswith和endswith方法，Shell通配符可以匹配中间，匹配操作介于简单的字符串方法和全功能的正则表达式之间
from fnmatch import fnmatch, fnmatchcase
fnmatch('foo.txt', '*.txt')  # *代表任意字符，0个或多个
fnmatch('foo.txt', '?oo.txt')  # ？不在括号内时，代表任意1个字符
fnmatch('Dat45.csv', 'Dat[0-9]*')

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

# fnmatch与fnmatchcase区别：后者区分大小写
# glob模块：匹配文件名称