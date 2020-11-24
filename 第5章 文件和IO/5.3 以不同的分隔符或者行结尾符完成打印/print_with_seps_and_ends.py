# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-24 15:25
@author: Li Luyao
"""

# print()函数sep和end关键字
row = ('ACME', 50, 91.5)
a = print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!\n')

for i in range(5):
    print(i)

for i in range(5):
    print(i, end=' ')

# 其他方法
print('!'.join(str(x) for x in row))
print(row, sep='!')
print(*row, sep='!')