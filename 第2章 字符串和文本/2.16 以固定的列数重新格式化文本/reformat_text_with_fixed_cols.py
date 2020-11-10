# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-11-03 18:18
@author: Li Luyao
"""

# 使用textwrap模块来重新格式化文本输出
# 主要的目的是以简单的方式对文本格式做整理使其适合与打印或者展示在终端
import os
# os.get_terminal_size().columns # Return WinError 6 句柄无效

with open('D:\Personal\Desktop\开机密码.txt') as f:
    s = f.read()

import textwrap
print(textwrap.fill(s, 20, initial_indent=' '))