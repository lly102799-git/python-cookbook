# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2021-01-22 14:43
@author: Li Luyao
"""

# 参数注解
def add_num(x:int, y:int) -> int:
    return x + y

if __name__ == '__main__':
    print(add_num.__annotations__)