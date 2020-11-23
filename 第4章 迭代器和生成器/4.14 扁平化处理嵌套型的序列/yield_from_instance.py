# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-23 15:40
@author: Li Luyao
"""

# yield from: 将嵌套型序列扁平化
from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

# 如果不用yield from，就需要编写有额外for循环的代码
def flatten_worse(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
            else:
                yield x

items = [1,2,3,[4,5,6],[[7,8],9]]
for x in flatten(items):
    print(x)

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)