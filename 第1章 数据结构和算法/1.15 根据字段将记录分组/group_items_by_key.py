# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-20 9:25
@author: Li Luyao
"""
from operator import itemgetter
from itertools import groupby
from collections import defaultdict

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5412 S CLARK', 'date': '07/02/2012'},
    {'address': '5412 E 58TH', 'date': '07/03/2012'},
    {'address': '5412 SE CLARK', 'date': '07/02/2012'},
    {'address': '5412 W RAVENSWOOD', 'date': '07/01/2012'},
    {'address': '5412 NW BROADWAY', 'date': '07/04/2012'},
    {'address': '5412 SW GRANVILLE', 'date': '07/03/2012'},
    {'address': '5412 S 57TH', 'date': '07/01/2012'},
]

# Sort by desired field first
# rows.sort(key=itemgetter('date'))  # 请查看如果不先排序的计算结果：不排序无法返回正确的分组结果

a = groupby(rows, key=itemgetter('date'))
print(a)
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('  ', i)

# 对列表中的值分组
nums = [2, 3, 15, 31, 17, 798, 21, 43, 65, 4]


def compare_num(num):
    if num <= 10:
        return 'small'
    elif num <= 50:
        return 'middle'
    elif num > 50:
        return 'big'


print([(key, list(gnum)) for key, gnum in groupby(sorted(nums), key=compare_num)])  # nums.sort()不会返回新的list

# 通过defalutdict(list)创建一键多值字典，随机访问同日期下的元素；list为工厂函数
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)
