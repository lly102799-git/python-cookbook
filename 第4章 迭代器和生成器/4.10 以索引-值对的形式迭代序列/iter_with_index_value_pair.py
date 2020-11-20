# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-20 14:34
@author: Li Luyao
"""

# enumerate()返回索引-值对
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

for idx, val in enumerate(my_list, start=1):
    print(idx, val)

# 适用于记跟踪记录文件中的行号，当想在错误信息中加上行号时就特别有用
def parse_date(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, start=1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}').format(lineno, e)


# 将文件中出现的单词和他们所出现的行之间建立映射关系
from collections import defaultdict

word_summary = defaultdict(list)

with open('D:\Personal\Desktop\python test.txt') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)

# 注意事项
data = [(1,2),(3,4),(5,6),(7,8)]
# correct
for n, (x, y) in enumerate(data, start=1):
    print((n, x, y))

# wrong: for n, x, y in enumerate(data, starts=1):