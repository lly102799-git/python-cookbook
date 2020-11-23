# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-20 16:13
@author: Li Luyao
"""

# 对在不同容器中的对象执行相同的操作: itertools.chain()
# zip是把迭代对象并起来形成元组，chain是把迭代对象串起来
from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)

# chain()比首先将各个序列合并在一起再迭代要更加高效