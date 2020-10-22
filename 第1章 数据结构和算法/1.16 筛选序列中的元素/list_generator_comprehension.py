# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-20 14:41
@author: Li Luyao
"""

import math
from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]  # 列表推导式
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

# 生成器表达式，处理原始输入很大的情况
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

# 涉及复杂的筛选过程或异常处理时，将筛选逻辑代码放到单独的函数中，使用filter（fun, value）函数处理
values = ['1', '2', '3', '4', '5', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

print([math.sqrt(n) for n in mylist if n > 0])

# 替换不满足条件的值
print([n if n > 0 else 0 for n in mylist])

# 筛选工具：itertools.compress()
names = ['Dell', 'Green', 'Sarah', 'Nicky', "Mana"]
scores = [99, 89, 78, 54, 44]

selector = [n >= 60 for n in scores]
scores_pass = [n for n in scores if n > 60]
names_selected = list(compress(names, selector))
print(names_selected)
# 根据对应关系生成字典
print(dict(zip(names_selected, scores_pass)))