# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2021-01-22 15:55
@author: Li Luyao
"""

# 判断用户是否提供了参数的稳定方法：
_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied.')
    pass

def spam2(a, b=None):
    if not b: # No! Use 'if b is None:' instead. 因为许多其他对象，包括长度为0的字符串、列表、元组、字典等都会被判定为False.
        b = []
    pass