# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/10/25 12:52
Author: Li Luyao
"""
import unicodedata
import sys

s = 'python\fis\tawsome\r\n'
print(s)

# ord()函数：将单字符转换为Unicode ordinal值，chr()函数将ordinal值转换为Unicode string
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None,
    ord('\n'): '!'
}
# 以下代码无法完成替换，因为s前没有r''转义，\f不是文本，而是换页的转义符
# s = r'python\fis\tawsome\r\n'
# remap = {
#     '\t': ' ',
#     '\f': ' ',
#     '\r': None,
#     '\n': '!'
# }
a = s.translate(remap)
print(a)

# 去除文本中的所有Unicode
import unicodedata
import sys

# 通过dict.fromkeys(keys[, value])生成转换表，将所有Unicode组合字映射为None
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
b.translate(cmb_chrs)
print(b)

# 将所有的Unicode十进制数字字符映射为他们对应的ascii版本
digit_map = {
    c: ord('0') + unicodedata.digit(chr(c))
    for c in range(sys.maxunicode)
    if unicodedata.category(chr(c)) == 'Nd'
}
print(len(digit_map))
x = '\u0661\u0662\u0663'
x.translate(digit_map)
print(x)

pass