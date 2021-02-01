# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2021-01-26 14:31
@author: Li Luyao
"""

# 定义一个惰性属性的最好方法是使用描述符
class Lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value) # 该代码是“惰性”的核心
            return value

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @Lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @Lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

c = Circle(4.0)
c.radius
c.area
c.perimeter
# 计算后，通过setattr(instance, self.func.__name__, value)代码，c中将有area和perimeter属性，再次调用c.area和c.perimeter
# 时，不再调用计算过程，而是直接访问属性
c.area
c.perimeter


