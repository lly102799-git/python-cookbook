# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/12/1 19:49
Author: Li Luyao
"""

# 通过内存映射的方式将一个二进制二建加载到可变的字节数组中，以随机访问其内容，或者实现就地修改
import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

# 创建一个数据初始文件
size = 10000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

m = memory_map('data')
print(len(m))
print(m[0:10])
m[0:11] = b'Hello World'
m.close()

# Verify that changes are made
with open('data', 'rb') as f:
    print(f.read(11))

# 由mmap()返回的对象也可以在上下文管理器中使用，在这种情况下，底层的文件会自动关闭
with memory_map('data') as m:
    print(len(m))
    print(m[0:10])
print(m.closed)
