# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-27 19:20
@author: Li Luyao
"""
# 使用format()方法
s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

# 使用format_map()和vars()联合
name = 'Guido'
n = 37
print(s.format_map(vars()))  # vars(): without argument equivalent to locals()

# vars()可作用于类实例上：将类属性与值映射为字典
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info(name, n)
print(s.format_map(vars(a)))

#format和format_map无法处理缺少某对键值的情况
try:
    print(s.format(name='Guido'))
except KeyError:
    pass

# 避免方法：单独定义一个带有__missing()方法的字典类
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
print(s.format_map(safesub(vars())))

n = 37
# 其他的变量插值解决方案
# '%(name) has %(n) messages.' % vars()
import string
s = string.Template('$name has $n messages.')
print(s.substitute(vars()))
