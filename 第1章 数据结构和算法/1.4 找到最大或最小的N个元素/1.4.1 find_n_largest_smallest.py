# -*- coding: utf-8 -*-
"""
@author: Li Luyao
"""

import heapq
# heap: 堆； queue: 队列；

nums = [1, 8, 2, 23, 7, -4, 18, 22, 42, 31]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
    {'name':'IBM', 'shares':100, 'prices':91.1},
    {'name':'AAPL', 'shares':50, 'prices':543.22},
    {'name':'FB', 'shares':50, 'prices':43.22},
    {'name':'ACME', 'shares':50, 'prices':22.22},
    {'name':'YHOO', 'shares':50, 'prices':13.22},
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['prices'])
print(cheap)

# cheap = heapq.nsmallest(3, portfolio, key='prices')
# print(cheap)