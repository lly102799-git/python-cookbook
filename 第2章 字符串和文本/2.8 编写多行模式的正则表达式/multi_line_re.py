# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/10/25 10:38
Author: Li Luyao
"""
# .并不能匹配换行符
# 解决方案一：添加对换行符的支持 \n
import re

comment1 = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
multiline comment*/'''
print(comment1.findall(text1))
print(comment1.findall(text2))

comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment2.findall(text1))
print(comment2.findall(text2))
comment2 = re.compile(r'/\*((.|\n)*?)\*/')
print(comment2.findall(text1))
print(comment2.findall(text2))

# 解决方案二：re.DOTALL标记，使正则表达式中句点.能够匹配所有字符，包括换行符
comment3 = re.compile(r'/\*(.*?)\*/', flags=re.DOTALL)
print(comment3.findall(text2))