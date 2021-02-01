# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2021-01-22 16:00
@author: Li Luyao
"""

add_two_nums = lambda x, y: x + y
print(add_two_nums(2,3))
print(add_two_nums('Hello', 'World'))

names = ['David Beazley', 'Brian Joes', 'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))

x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
# lambda中用到的x是自由变量，在运行时才进行绑定，而不是定义的时候绑定
print(a(10)) # return 30
print(b(10)) # return 30

# 如果希望匿名函数可以在定义的时候绑定变量，并保持不变，那么可以将那个值作为默认参数实现
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10)) # return 20
print(b(10)) # return 30

# 其他例子
funcs = [lambda x: x+n for n in range(5)] # list里每个元素都是lambda匿名函数
for f in funcs:
    print(f(0))

# VS
funcs = [lambda x, n=n: x+n for n in range(5)] # list里每个元素都是lambda匿名函数
for f in funcs:
    print(f(0))