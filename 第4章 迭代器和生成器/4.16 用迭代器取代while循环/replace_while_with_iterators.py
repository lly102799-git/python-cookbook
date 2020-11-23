# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-23 16:28
@author: Li Luyao
"""

# iter()
CHUNKSIZE = 8192

def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)  # 网络编程、套接字完整接收数据相关
        if data == b'':
            break
        process_data(data)


def process_data(data):
    pass

