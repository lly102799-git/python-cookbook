# -*- coding: utf-8 -*-
"""
@author: Li Luyao
"""

from _collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(1)
d['b'].append(4)

c = defaultdict(set)
c['a'].add(1)
c['a'].add(2)
c['b'].add(4)

# defaultdict的优点：自动初始化第一个值
pairs = [('name', 'age', 'school'), ('Dell', 25, 'Qsinghua')]
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)

#若不使用defaultdict:
d = {}
for key, value in pairs:
    # 初始化
    if key not in d:
        d[key] = []
    d[key].append(value)