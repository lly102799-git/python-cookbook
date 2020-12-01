# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/12/1 20:49
Author: Li Luyao
"""

# os.path模块
import os

path = r'5.10 对二进制文件做内存映射.py'
# 检查文件是否存在
print(os.path.exists('5.11 处理路径名.py'))

print(os.path.isfile('5.11 处理路径名.py'))

print(os.path.isdir(path))
# 获取文件大小和访问、修改、创建时间
abs_path = path  # 这里的路径只能是绝对路径或者文件名吗？
# abs_path = os.path.abspath(path)
print(os.path.getsize(abs_path))
print(os.path.getatime(abs_path))
print(os.path.getctime(abs_path))