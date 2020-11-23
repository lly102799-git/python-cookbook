# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-23 16:06
@author: Li Luyao
"""

# heapq.merge():
import heapq

a = [1, 34, 4, 1]
b = [2, 4, 6, 2]
for c in heapq.merge(a, b):
    print(c)

c = heapq.merge(a, b)
print(type(c))
for item in c:
    print(item)

# 合并两个有序文件
with open('sorted_file_1', 'rt') as file1, \
    open('sorted_file_2', 'rt') as file2, \
    open('merged_file', 'wt') as outf:

    for line in heapq.merge(file1, file2):
        outf.write(line)
