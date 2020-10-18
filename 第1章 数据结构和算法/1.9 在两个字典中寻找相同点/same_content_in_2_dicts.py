# -*- coding: utf-8 -*-
"""
Create Time:  
Author: Li Luyao
"""
a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 20, 'y': 2}

# Find keys in commom
print(a.keys() & b.keys())

# Find keys in a that are not in b
print(a.keys() - b.keys())

# Find (key, value) in commom
print(a.items() & b.items())

# 字典推导式： Make a new dict with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)

# 列表推导式：[out_list_expr for var in input_list if ...]
# 字典推导式：[out_dict_expr for key in keys if ...], out_dict_expr is in key: value format
# 集合推导式：

# D.keys()返回的keys-view 和 D.items()返回的items-view对象，支持集合操作（+，-，&）