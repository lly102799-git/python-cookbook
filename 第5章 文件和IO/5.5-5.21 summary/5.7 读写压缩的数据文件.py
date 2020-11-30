# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-24 17:05
@author: Li Luyao
"""

# 读写以gzip或bz2格式压缩过的文件中的数据
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with open('somefile.gz', 'wt') as f:
    f.write(text)

import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

with open('somefile.bz2', 'wt') as f:
    f.write(text)

# 特性：能够对已经以二进制模式打开的文件进行叠加操作，可以同各种类型的类文件对象比如套接字、管道和内存文件一起工作
f = open('somefile.gz', 'rb')  # 类文件对象
with gzip.open(f, 'rt') as g:
    text = g.read()