# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-24 16:32
@author: Li Luyao
"""

# x模式
# 首先检查文件是否已经存在
import os

if not os.path.exists('somefile.txt'):
    with open('somefile.txt', 'xt') as f:
        f.write('Hello!\n')
else:
    print('File already exists!')
    with open('somefile.txt', 'rt') as f:
        data = f.read()
        print(data)
        for line in f:
            print(line)

