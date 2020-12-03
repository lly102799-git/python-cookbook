# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/12/2 22:56
Author: Li Luyao
"""

# 当文件的名称没有按照sys.getfilesystemencoding()返回的方式进行编码时，会报错
import sys
print(sys.getfilesystemencoding())

def bad_filenames(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')

for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filenames(name))

