# -*- coding: utf-8 -*-
"""
Create Time:  
Author: Li Luyao
"""


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item  # 如果没有这行yield，函数将返回None，因为没有相应的return -. -
            seen.add(item)
    # return seen  # 用return返回集合仍无法保证元素顺序不变，写这么多其实直接等效于set(items)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(dedupe(a))
print(list(dedupe(a)))


def dedupe_not_hashable(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 3}]
b = dedupe_not_hashable(a, key=lambda d: (d['x'], d['y']))  # val为x、y键对应值组成的元组，因此代码意义是剔除a中x、y键值相同的元素
print(list(b))
c = dedupe_not_hashable(a, key=lambda d:d['x'])  # val为x键对应的值，因此代码的意义是剔除a中x键值相同的元素
print(list(c))