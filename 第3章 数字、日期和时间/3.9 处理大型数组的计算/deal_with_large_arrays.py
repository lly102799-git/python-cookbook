# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-11-10 19:22
@author: Li Luyao
"""

# python lists VS numpy arrays
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(a * 2)
print(a + b)
try:
    print(a + 10)
except TypeError as e:
    print(e)

# Numpy库
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
print(x * 2)
print(x + y)
print(y + 10)


def f(x):
    return 3 * x ** 2 + 2 * x - 7


print(f(x))
print(np.sqrt(y))
print(np.cos(x))

# 多维数组
# grid = np.zeros(shape=(1000, 1000), dtype=float)
# print(grid)


11111