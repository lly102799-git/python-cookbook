# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/11/30 20:54
Author: Li Luyao
"""

# 问题：将二进制数据直接读取到一个可变缓冲区中，中间不经过任何拷贝环节
# 要将数据读取到可变数组中，使用文件对象的readinto()方法

import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
print(buf)
print(buf[0:5])

with open('newsample.bin' , 'wb') as f:
    f.write(buf)

# 与read()不同的是，readinto()是为已存在的缓冲区填充内容，而不是分配新的对象然后再将他们返回。
record_size = 32

buf = bytearray(record_size)
with open('somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)  # n表示返回读取到的字节数
        if n < record_size:  # 使用f.readinto()需要注意的是，必须总是确保要检查他的返回值，即实际读取的字节数；
            break  # 不等时，可能表示数据遭到破坏
        # Use the content of buf