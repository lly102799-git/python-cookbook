# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/10/25 10:54
Author: Li Luyao
"""
# 什么是Unicode？一种字符编码方案，为每种语言的每个字符设定了统一且唯一的二进制编码，用2个字节表示1个字符
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1, s2)
print(s1 == s2)

print(len(s1))
print(len(s2))
# 对一个字符比较程序而言，同一个文本拥有多种不同的表示形式是个大问题。
# 因此，应该先将文本统一表示为规范形式。
import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(ascii(t1), t1 == t2)

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(ascii(t3), t3 == t4)

print(''.join([t for t in t3 if not unicodedata.combining(t)]))


