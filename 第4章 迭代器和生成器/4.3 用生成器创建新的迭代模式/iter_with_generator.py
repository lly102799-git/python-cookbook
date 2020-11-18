# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-17 16:55
@author: Li Luyao
"""
# 用生成器创建新的迭代模式
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))

# 迭代器和next函数底层机制
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

# Create generator, and no output appears
c = countdown(3)
print(c)
print(next(c))
print(next(c))
print(next(c))
print(next(c))