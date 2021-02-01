# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2021-01-22 14:02
@author: Li Luyao
"""


# 由于*的存在，block参数必须通过关键字才能访问
def recv(maximize, *, block):
    'Receive a message'
    print(maximize)

def minimum_val(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


if __name__ == '__main__':
    # recv(1024, True) # TypeError: recv() takes 1 positional argument but 2 were given
    recv(1024, block=True)
    print(minimum_val(1,5,2,-5, 0))
    print(minimum_val(1,5,2,-5, clip=0))

