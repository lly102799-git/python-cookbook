# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2021-01-22 16:57
@author: Li Luyao
"""

from functools import partial
import math

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2-x1, y2-y1)

points = [(1,2), (3,4), (5,6), (7,8)]
pt = (4,3)
# 根据points中点到pt的距离，对points进行排序
# points.sort(key=distance(points, pt)) # 错误！sort方法中key=函数名，只能接受points为输入
points.sort(key=partial(distance, pt))
print(points)