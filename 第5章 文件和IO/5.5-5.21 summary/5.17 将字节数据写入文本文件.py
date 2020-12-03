# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/12/3 19:58
Author: Li Luyao
"""

# 将原始字节写入到以文本模式打开的文件中
# io.TextIOWraaper是文本处理层，负责编码和解码Unicode；
# io.BufferedWriter是缓冲I/O层，负责处理二进制数据 *
# io.FileIO是一个原始文件，代表着操作系统底层的文件描述符

# I/O系统是以不同的层次来构建的。文本文件是通过在缓冲的二进制模式文件之上添加一个Unicode编码/解码层来构建的。
# buffer属性简单地指向底层的文件。如果访问该属性，就可以绕过文本编码/解码层了。

import sys

# print(sys.stdout.write(b'Hello\n'))  # TypeError: write() argument must be str, not bytes
print(sys.stdout.buffer.write(b'Hello\n'))