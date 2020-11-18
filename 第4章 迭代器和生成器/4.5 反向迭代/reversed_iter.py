# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-17 18:46
@author: Li Luyao
"""
# 内建函数reversed()
a = range(1, 5)
for x in reversed(a):
    print(x)

# 方向迭代前提：确定大小或__reversed__()特殊方法，若都不行，必须先将这个对象转换为列表
with open(r'D:\Personal\Desktop\essValidate输入json.txt') as f:
    for line in reversed(list(f)):  # f object itself is not reversible
        print(line, end='')


# 实现__reversed__()方法
class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

    # Reverse iterator
    def __reversed__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1


for i in Countdown(5):
    print(i)

for i in reversed(Countdown(5)):
    print(i)
