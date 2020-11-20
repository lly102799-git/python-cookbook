# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-20 15:45
@author: Li Luyao
"""

# 当我们想要迭代的元素包含在多个序列中时
xpts = [1,2,3,4,5]
ypts = ['a','b','c','d','e']

# for key, val in zip(dict.keys(), dict.values()):
for x, y in zip(xpts, ypts):
    print(x, y)

# zip()迭代的长度和其中最短的输入序列长度相同
a = [1,2,3,4]
b = ['a','v','c']
for i in zip(a, b):
    print(i)

# 若按照最长的输入序列长度
from itertools import zip_longest
for i in zip_longest(a, b):
    print(i)

for i in zip_longest(a, b, fillvalue=0):
    print(i)

# 使用zip构建字典
headers = ['name','shares','price']
values = ['ACME',100,490.1]
adict = dict(zip(headers, values))
print(adict)
from collections import defaultdict
bdict = defaultdict(None, zip(headers, values))
bdict['arg'] = [1,2,3,4]
print(bdict)

# zip()也可以接受多余两个序列作为输入，返回的迭代器中元组将有多个元素
a = [1,2,3]
b = [10,11,12]
c = ['a','c','bv']
for i in zip(a, b, c):
    print(i)

# 需要注意的是，zip()创建的结果是迭代器，如果需要保存，则需要转换为list
baz = list(zip(a, b, c))