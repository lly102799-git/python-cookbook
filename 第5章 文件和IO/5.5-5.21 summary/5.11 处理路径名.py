# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/12/1 20:24
Author: Li Luyao
"""

# 处理路径名以找出基文件名、目录名、绝对路径等相关信息
import os

path = r'/5.5-5.21 summary/5.11 处理路径名.py' # 第一个 / 有没有都可以
# Get the last component of the path (basename)
print(os.path.basename(path))

# Get the directory name
print(os.path.dirname(path))

# Get the absolute directory name
abs_path = os.path.abspath(path)
print(abs_path)

# Join path components together
print(os.path.join('tmp', 'data', os.path.basename(path)))

# Expand the user's home directory
print(os.path.expanduser(r'~/5.5-5.21 summary/5.11 处理路径名.py'))  # Return: C:\Users\Administrator/5.5-5.21 summary/5.11 处理路径名.py

# Split the fil extension (扩展名)
print(os.path.splitext(abs_path))