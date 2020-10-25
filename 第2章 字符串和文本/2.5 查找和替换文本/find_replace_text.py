# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-23 10:06
@author: Li Luyao
"""

# 简单模式：str.replace()
text = 'yeah, but no, but yeah, but no, but yeah.'
text.replace('yeah', 'yep')

# 复杂模式： re模块，sub()函数/方法
text = 'Today is 11/12/2012. PyCon starts at 3/13/2013.'
import re
pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
print(text, '\n', re.sub(pattern, r'\3-\1-\2', text))
print(pattern.sub(r'\3-\1-\2', text))

# 更加复杂情况：为sub()方法指定替换回调函数
from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


# 替换回调函数的输入为匹配对象（m = pattern.match(text))，用group()方法来提取匹配中的特定部分
print(pattern.sub(change_date, text))