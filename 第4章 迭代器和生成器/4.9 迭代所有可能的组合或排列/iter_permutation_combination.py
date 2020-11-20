# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-20 14:20
@author: Li Luyao
"""

items = ['a', 'b', 'c']
# 排列:itertools.permutations()
from itertools import permutations
print(permutations(items))
for p in permutations(items):
    print(p)

for p2 in permutations(items, 2):
    print(p2)

# 组合:itertools.combinations()
from itertools import combinations
for p in combinations(items, 3):
    print(p)

for p2 in combinations(items, 2):
    print(p2)

# 允许元素重复选择的组合:itertools.combinations_with_replacement()
from itertools import combinations_with_replacement
