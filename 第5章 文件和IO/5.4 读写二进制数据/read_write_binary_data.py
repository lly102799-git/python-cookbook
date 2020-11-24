# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-24 15:35
@author: Li Luyao
"""

# 使用open()函数的rb或者wb模式就可以实现对二进制数据的读或写

# Write binary data to file
# with open('somefile.txt', 'xb') as f:
#     f.write(b'Hello World!')

# Read the entire file as a single byte string
with open('somefile.txt', 'rb') as f:
    data = f.read()
    print(data)

# Text string 和 Byte string
t = 'Hello World'
b = b'Hello World'

for c in t:
    print(c)

for c in b:
    print(c)

# 在二进制文件中进行读取或写入文本内容，请确保进行编码和解码操作
# with open('some_binfile.bin', 'xb') as bf:
#     bf.write(b'Hello World')

with open('some_binfile.bin', 'rb') as bf:
    data = bf.read()
    text = data.decode('utf-8')
    print(text)
    print(data)

with open('some_binfile.bin', 'wb') as bf:
    text = 'Hello World'
    bf.write(text.encode('utf-8'))