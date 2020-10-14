# -*- coding: utf-8 -*-
"""
@author: Li Luyao
"""
import numpy as np


def drop_first_last(grades):
    first, *middle, last = grades
    return np.mean(middle)


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


ans = drop_first_last([1, 2, 3, 4, 5, 6, 7])

records = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4)]
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
