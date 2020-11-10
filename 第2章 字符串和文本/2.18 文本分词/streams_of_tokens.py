# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-11-03 19:16
@author: Li Luyao
"""

import re

text = 'foo = 23 + 42 * 10'
NAME = r'(?P<NAME>[a-zA-Z][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# 使用模式对象scanner()方法进行分词操作：创建扫描对象，在给定的文本中重复调用match()，一次匹配一个模式
scanner = master_pat.scanner(text)
a = scanner.match()
print(a.lastgroup, a.group())
b = scanner.match()
print(b.lastgroup, b.group())

# 利用生成器函数处理：
from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])


def generate_tokens(pat, text):
    scanners = pat.scanner(text)
    for m in iter(scanners.match, None): # 方法有括号和没括号的区别
        yield Token(m.lastgroup, m.group())


for tok in generate_tokens(master_pat, text):
    print(tok)

# 结合生成器表达式，过滤内容：
tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')
for tok in tokens:
    print(tok)
