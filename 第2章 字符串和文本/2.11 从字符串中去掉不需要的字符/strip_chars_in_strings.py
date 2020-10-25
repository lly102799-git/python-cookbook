# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/10/25 12:24
Author: Li Luyao
"""
# strip()方法可以用来从字符串的开始和结尾处去掉字符，lstrip()和rstrip()可以分别从左侧或者右侧执行去除字符的操作。
# Whitespace stripping
s = '   Hello World!    \n'
print(s.strip())
print(s.lstrip(), s.rstrip())

# Character stripping
t = '----------hello++++++'
print(t.strip('-+'), t.lstrip('-'))

# 由于strip()处理开始和结尾处，因此不会对位于字符串中间的任何文本起作用
s = '   Hello world   \n'
print(s.strip())

# 如果要替换中间的空格或文本，可以使用replace()方法或者正则表达式替换
print(s.replace(' ', ''))
import re
print(re.sub('\s+', ' ', s))

# 去除字符的操作结合迭代操作
filename = r'C:\Users\Administrator\Desktop\密码.txt'
with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)