# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/12/1 21:03
Author: Li Luyao
"""

# 疑问：为什么有的时候会报系统找不到文件错误呢？明明路径都是对的
# 建议了解一下pathlib模块

# 获取某个目录下所包含的文件列表：os.listdir()
import os

# path = r'第5章 文件和IO'
# abspath = os.path.abspath(path)  # 为什么获取的绝对路径不行？是因为获取的绝对路径是\\吗？不对，获取绝对路径返回的值有问题
# 我傻逼了，listdir(dir)中输入是目录啊！不是文件绝对路径！
# abspath = os.path.abspath(path)
# dir = os.path.dirname(abspath)

dir = 'G:\\python-cookbook\\第5章 文件和IO\\5.5-5.21 summary'
# dir = r'G:\python-cookbook\第5章 文件和IO'  # 这里的目录应当是完整目录
names = os.listdir(dir)
print(names)

# 获取names之后的解决方案：如果需要以某种方式筛选数据，可以考虑利用列表推导式和os.path模块完成

import os.path

# Get all regular files
filenames = [name for name in os.listdir(dir)
             if os.path.isfile(os.path.join(dir, name))]
print(filenames)

# Get all dirs
dirnames = [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]
print(dirnames)

# 利用startswith和endswith筛选目录中的内容
pyfiles = [name for name in os.listdir(dir)
           if name.endswith('.py')]

# 利用glob和fnmatch进行文件名匹配
import glob
pyfiles = glob.glob(dir+'\*.py')  # 只有glob()方法会返回每个文件的绝对路径
print(pyfiles)

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir(dir)
           if fnmatch(name, '*.py')]
print(pyfiles)

# 附加数据和元数据的获取
# 元数据：又称中介数据、中继数据，是描述数据的数据，主要是描述数据的属性信息
import os
# import os.path
import glob

pyfiles = glob.glob(dir+'\*.py')
# Get file sizes and modification dates
name_size_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                  for name in pyfiles]
print(name_size_date)
for name, size, date in name_size_date:
    print(name, size, date)

# Get file metadata: os.stat(name)
file_metadata = [(name, os.stat(name))
                 for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime, meta.st_ctime)