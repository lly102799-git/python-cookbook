# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-20 18:29
@author: Li Luyao
"""
# 拆分字符串：re.split()
line = 'asdf fsdfk; kadf, sdfs,asdf,    foo'
import re
print(line.split(';', 4))
print(re.split(r'[;,\s]', line))  # 分隔符为分号、逗号、空格
print(re.split(r'[;,\s]\s*', line))  # 分隔符为分号、逗号、空格且后面可以跟任意数量的空格

# 正则表达式模式中的捕获组与非捕获组
print(re.split(r'[;,\s]\s*', line))  # 非捕获组1
print(re.split(r'(;|,|\s)\s*', line))  # 捕获组
print(re.split(r'(?:;|,|\s)\s*', line))  # 非捕获组2
