# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-27 19:20
@author: Li Luyao
"""
# 使用format()方法
s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

# 使用format_map()和vars()联合
name = 'Guido'
n = 37
print(s.format_map(vars()))  # vars(): without argument equivalent to locals()
print(s.format_map(vars(dict)))