# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-24 15:19
@author: Li Luyao
"""

# 只需要为print()函数加上file关键字参数即可，需保证文件是以文本模式打开的
with open(r'D:\Personal\Desktop\python test.txt', 'wt') as f:
    print('Hello World, 111!', file=f)