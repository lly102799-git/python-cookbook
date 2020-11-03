# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-27 18:37
@author: Li Luyao
"""
# join()方法
parts = ['Is', 'Chicago', 'In', 'America?']
print(' '.join(parts))
print(', '.join(parts))

# +操作符和format()方法
a = 'I am'
b = 'from China.'
print(a + ' ' + b)
print('{1} {0}'.format(a, b))

# 大量+操作符会严重影响效率，原因是内存拷贝和垃圾收集产生的影响
# 技巧：利用生成器表达式+join()方法
data = ['ACME', 50, 91.1]
print(' '.join(str(c) for c in data))