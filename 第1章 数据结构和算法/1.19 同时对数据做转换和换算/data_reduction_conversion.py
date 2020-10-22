# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-20 17:43
@author: Li Luyao
"""

nums = [1, 2, 3, 4, 5]
s = sum(x ** 2 for x in nums)  # 在函数参数中使用生成器表达式

# Determine if any .py files exist in a directory
import os

files = os.listdir('F:\规划设计运营管理-李路遥\数据、程序及仿真结果\工商居负荷评估小工具')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('No python!')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(', '.join(str(x) for x in s)) # S.join: S is the seperator

# Data reduction across fields of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 20},
    {'name': 'ACME', 'shares': 70},
    {'name': 'APPL', 'shares': 75},
    {'name': 'MCFT', 'shares': 20},
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)  # Return 20
max_shares = max(portfolio, key=lambda s: s['shares'])
print(max_shares)  # Return {'name': 'APPL', 'shares': 75}