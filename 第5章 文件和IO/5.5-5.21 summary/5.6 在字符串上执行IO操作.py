# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-24 16:42
@author: Li Luyao
"""

# 需求：将一段文本或二进制字符串写入类似于文件的对象上
# 使用io.StringIO()或io.BytesIO() 类 来创建类似于文件的对象，这些对象可操作字符串数据
import io

s = io.StringIO()
s.write('Hello World\n')
print(s.getvalue())
print('This is a test', file=s)  # print()函数有file关键字后，不会再打印
# Get all of the data written so far
print(s.getvalue())

# Wrap a file interface around an existing string
s = io.StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())  # 只会读出来上一步读取后剩下的文本