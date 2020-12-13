# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/12/13 8:57
Author: Li Luyao
"""

import csv
from collections import namedtuple

headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [
    ('AA',39.48,'6/11/2007','9:36am',-0.18,181800),
    ('AIG',49.48,'6/11/2007','9:36am',-0.15,481800),
    ('AXP',69.48,'6/11/2007','9:36am',-0.46,201800),
]
with open('stocks.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

# # 如果写入的输入是字典序列
# headers = ['Symbol','Price','Data','Time','Change','Volume']
# rows = [
#     {'Symbol':'AA','Price':39.48,'Date':'6/11/2007','Time':'9:36am','Change':-0.18,'Volume':181800}
# ]
# with open('stocks.csv', 'w') as f:
#     f_csv = csv.DictWriter(f, headers)
#     f_csv.writeheader()
#     f_csv.writerows(rows)

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # process row
        print(row)

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)

    for r in f_csv:
        if r:
            row = Row(*r)
            # Proceed row
            # row.Symbol/row.Change
            print(row.Symbol)

# 将数据读取为字典
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # Proceed row
        # row['Symbol']/row['Change']
        print(row['Change'])

# 修改分隔符
with open('stocks.csv') as f:
    f_csv = csv.reader(f, delimiter='\t')
    headers = next(f_csv)
    for row in f_csv:
        print(row)

# 处理非法字符
import re
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = [re.sub('^a-zA-Z_', '_', h) for h in next(f_csv)]  # 将非a-zA-Z_的字符替换成_
    Row = namedtuple('Row', headers)
    for r in f_csv:
        if r:
            row = Row(*r)
            # Proceed row

# csv读取到的数据都是字符串格式，因此需要转换
col_types = [str, float, str, str, float, int]
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        if row:
            # row = tuple(convert(value) for convert, value in zip(col_types, row))
            row = [convert(value) for convert, value in zip(col_types, row)]
            print(row)

# 转换为字典
field_types = [
    ('Price', float),
    ('Change', float),
    ('Volume', int)
]
with open('stocks.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key])) for key, conversion in field_types)
        print(row)