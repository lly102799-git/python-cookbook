# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2021-01-26 10:46
@author: Li Luyao
"""

# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# 所谓的描述符就是以特殊方法__get__()/__set__()/__delete__()的形式实现了三个核心的属性访问操作的类！
class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 所有针对描述符属性（这里的xy）的访问都会被__get__()/__set__()/__delete__()方法捕获
p = Point(2, 3)
p.x # Calls Point.x.__get__(p, Point)
p.y = 5 # Calls Point.y.__set__(p, 5)