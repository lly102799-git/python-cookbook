# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/12/3 19:44
Author: Li Luyao
"""

# 为一个已经以二进制模式打开的文件添加或修改Unicode编码，但不必首先将它关闭：io.TextIOWrapper()
# import urllib.request
# import io
#
# url = urllib.request.urlopen('http://www.python.org')
# f = io.TextIOWrapper(url, encoding='utf-8')
# text = f.read()
# print(text)

# io.TextIOWraaper是文本处理层，负责编码和解码Unicode
# io.BufferedWriter是缓冲I/O层，负责处理二进制数据 *
# io.FileIO是一个原始文件，代表着操作系统底层的文件描述符
f = open('data', 'w')
print(f)
print(f.buffer)
print(f.buffer.raw)
f.close()

