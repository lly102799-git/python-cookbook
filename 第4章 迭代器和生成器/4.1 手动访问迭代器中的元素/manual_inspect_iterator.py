# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-17 15:29
@author: Li Luyao
"""
# next()函数
with open(r'D:\Personal\Desktop\essValidate输入json.txt') as f:
    try:
        while True:
            line = next(f)
            print(line, end='\r')
    except StopIteration:
        pass

with open(r'D:\Personal\Desktop\essValidate输入json.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='\r')

items = [1, 2, 3, 4]
# Get the iterator
it = iter(items)  # Invokes items.__iter__()
# Run the iterator
while True:
    try:
        print(next(it))
    except StopIteration:
        break