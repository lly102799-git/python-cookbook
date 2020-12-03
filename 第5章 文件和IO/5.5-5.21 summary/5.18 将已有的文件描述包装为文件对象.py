# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/12/3 20:10
Author: Li Luyao
"""

# python文件描述符！fd = file descriptor
# open()函数，python文件对象

# Open a low-level file descriptor
import os
fd = os.open('newsample.bin', os.O_WRONLY | os.O_CREAT)

print(fd)

# Turn into a proper file
f = open(fd, 'wt')
f.write('Hello World!')
print(f)
f.close()

# 获取文件描述符：fd = fileObject.fileno()
