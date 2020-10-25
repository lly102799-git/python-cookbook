# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/10/24 17:50
Author: Li Luyao
"""
import re
#  正则表达式的贪婪匹配与最小匹配
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

str_pat2 = re.compile(r'\"(.*?)\"')
print(str_pat2.findall(text2))