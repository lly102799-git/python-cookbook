# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-20 9:27
@author: Li Luyao
"""

with open('D:\Personal\Desktop\python test.txt') as f:
    for line in f:
        print(line)

# 剔除前几个满足函数返回为True的元素
from itertools import dropwhile
with open('D:\Personal\Desktop\python test.txt') as f:
    for line in dropwhile(lambda astr: astr.startswith('#'), f):
        print(line)

# 如果已知要跳过多少个元素，可以使用isslice()
from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10]
for x in islice(items, 3, None):  # 切片[3:]
    print(x)

# 剔除所有满足条件的元素
with open('D:\Personal\Desktop\python test.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')
