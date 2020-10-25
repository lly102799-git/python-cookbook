# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/10/24 16:36
Author: Li Luyao
"""
# 简单理解：将A函数作为B函数的输入，则A函数被称为回调函数。该过程被称为“登记回调函数”。
def double(x):
    return x * 2

def quadra(x):
    return x * 4

def getOddnumbers(k, getEvennumber):
    return 1 + getEvennumber(k)

print(getOddnumbers(5, quadra))