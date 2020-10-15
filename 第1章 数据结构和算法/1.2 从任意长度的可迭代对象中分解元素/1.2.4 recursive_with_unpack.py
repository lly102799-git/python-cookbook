# -*- coding: utf-8 -*-
"""
@author: Li Luyao
"""


def new_sum(items):
    head, *tail = items
    return head + new_sum(tail) if tail else head


print(new_sum([1, 2, 3, 4, 5]))