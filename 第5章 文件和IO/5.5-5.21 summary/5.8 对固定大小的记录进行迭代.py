# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/11/30 20:46
Author: Li Luyao
"""

# 与其按照行来迭代文件，我们想对一系列固定大小的记录或者数据块进行迭代
# 利用iter()和functools.partial()来完成这个巧妙的技巧
# 应用场景：二进制模式固定长度，文本模式按行读取

from functools import partial

record_size = 32  # 从文件中读取固定字节数
with open('somefile.data', 'rb') as f:
    records = iter(partial(f.read(), record_size), b'')
    for r in records:
        pass