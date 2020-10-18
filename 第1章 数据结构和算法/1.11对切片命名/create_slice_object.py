# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/10/17 15:01
Author: Li Luyao
"""

# Create a slice object
record = '.........100  ........513.25  ........'
# 创建切片对象、对切片对象进行命名的目的是：对代码的功能有更清晰的认识
SHARES = slice(20, 32)
PRICE = slice(40, 48)

cost = int(record[SHARES]) * float(record[PRICE])

# slice_object: slice(start, stop, stop)
# seq[start: stop: step] => seq._getitem_(slice(start, stop, step))

# 结合indices函数，确定正确合理的（start, stop, step)元组
s = 'HelloWorld'
a = slice(5, 100, 2)
print(a.indices(len(s)))  # return (5, 10, 2), 所有值被限制在边界内，防止报错StopIteration