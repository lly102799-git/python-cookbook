# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-11-10 17:32
@author: Li Luyao
"""

# 字节串和文本字符串
data = b'Hello World'
print(data[0])
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

import re
btext = b'FOO:BAR,SPAM'
# print(re.split('[:,]', btext))
print(re.split(b'[:,]', btext))

# 字节串无格式化操作，只能先格式化文本字符再encode
print(data.decode('ascii'))
print('{:10s}{:10d}{:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))
print('{} {} {}'.format('ACME', 100, 490.1).encode('ascii'))