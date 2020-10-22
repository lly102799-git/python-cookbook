# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-20 14:12
@author: Li Luyao
"""


def maker(n):  # 内嵌函数和闭包
    k = 8

    def action(x):
        return x ** n + k

    return action


f = maker(2)
print(f(4))


def test(num):
    in_num = num

    def nested(label):
        nonlocal in_num  # 内嵌函数内部想对嵌套作用域中的变量进行修改，就要使用nonlocal进行声明
        in_num += 1
        print(label, in_num)
    return nested


F = test(0)
F('a')
F('b')
F('c')