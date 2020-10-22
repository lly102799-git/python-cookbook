# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-20 16:43
@author: Li Luyao
"""

from collections import namedtuple

# 命名元组：通过下标或索引来访问元素使代码难以阅读，希望通过名称来访问元素
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

# 通过位置来引用元素常常使得代码表达力不够强，也很依赖于记录的具体结构
Stock = namedtuple('Stock', ['names', 'shares', 'prices'])
s = Stock('ACME', 100, 123.45)


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)  # 为什么有*号？
        total += s.shares * s.prices
    return total

# namedtuple是不可变的，如果需要改变，须使用_replace()方法生成全新的命名元组
s = s._replace(shares=50)  # s.shares = 50 is wrong
