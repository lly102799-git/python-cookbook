# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-19 15:20
@author: Li Luyao
"""
# itertools.isslice()
import itertools

def count(n):
    while True:
        yield n
        n += 1

c = count(0)
try:
    print(c[10:20])  # 迭代器和生成器是无法普通切片的
except TypeError:
    for x in itertools.islice(c, 10, 20):
        print(x)