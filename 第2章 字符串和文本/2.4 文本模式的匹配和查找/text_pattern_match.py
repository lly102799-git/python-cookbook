# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-22 18:12
@author: Li Luyao
"""

# 基本的字符串匹配方法：str.find(), str.startsiwth(), str.endswith(), fnmatch(str, ())
import re

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

# Simple matching
if re.match(r'\d+/\d+/\d+', text1):
    print('Yes')
else:
    print('No')

# 针对同一模式做多次匹配，可先将模式用re.compile（）编译为一个模式对象
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('Yes')
else:
    print('No')

# match只找到第一个匹配项，要想找到所有匹配项，用findall()
text = 'Today is 12/28/2012. PyCon starts at 3/13/2013.'
print(datepat.findall(text))

# 编译捕获组模式
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# 捕获组的内容可以单独提取出来，因此可以简化对后续文本的处理
m= datepat.match('11/27/2011')
print(m.group())
m.group(0)
m.group(1)
m.group(2)
month, year, day = m.groups()

# pat.findall(text)捕获组以元组列表形式返回，所有匹配项以列表形式返回
print(datepat.findall(text))
for m in datepat.findall(text):
    print(m)
for m in datepat.finditer(text):
    print(m.groups())
    print(type(m))

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(month, day, year))

# match只会检测字符串开头，如果先要精确匹配，需要在模式末尾添加结束标记$
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
m = datepat.match('11/27/2012abdcdef')
print(m.group())