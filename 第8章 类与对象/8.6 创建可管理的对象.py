# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2021-01-25 9:57
@author: Li Luyao
"""
# 所谓的@property其实就是将在类中定义的def方法转换为类的属性，通过class.method更优雅的调用，而不是class.method()
# 当然@property的setter和deleter方法

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property # 自定义对属性的访问，以实现对属性的管理
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

a = Person('Guido')
a.first_name # calls getter
a.first_name = 52 # calls the setter
del a.first_name # calls the deleter

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(4.0)
c.area # 而不是c.area()
c.perimeter # 而不是c.perimeter