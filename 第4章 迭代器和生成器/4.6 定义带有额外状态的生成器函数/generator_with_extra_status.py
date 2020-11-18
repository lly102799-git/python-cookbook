# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-17 19:10
@author: Li Luyao
"""
# 定义一个生成器函数，但是它还涉及一些额外的状态，我们希望以某种形式将这些状态暴露给用户
from collections import deque

class LineHistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, start=1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open(r'D:\Personal\Desktop\essValidate输入json.txt') as f:
    lines = LineHistory(f)
    for lineno, hline in lines.history:
        print('{}:{}'.format(lineno, hline), end='')