# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-20 18:06
@author: Li Luyao
"""

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# 假设执行查找操作，得现在a中查找，如果没找到，再去b中查找
from collections import ChainMap
c = ChainMap(a, b)  # 如果有重复的键，则会采用第一个映射中对应的值
print(c['x'])
print(c['y'])
print(c['z'])
a['x'] = 233
print(c['x'])

# Alternative：使用字典的update()方法
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])

# 修改映射的操作总是会作用在列出的第一个映射结构上
c['z'] = 10
c['w'] = 40
del c['x']
print(a)