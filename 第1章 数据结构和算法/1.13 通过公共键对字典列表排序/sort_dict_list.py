# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/10/18 11:46
Author: Li Luyao
"""
from operator import itemgetter

rows = [
    {'fname':'Brain', 'lname': 'Jones', 'uid': 1003},
    {'fname':'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname':'John', 'lname': 'Cheese', 'uid': 1004},
    {'fname':'Big', 'lname': 'Jones', 'uid': 1001}
]

rows_by_uid = sorted(rows, key=lambda k: k['lname'])
print(rows_by_uid)

# Use itemgetter
rows_by_lname = sorted(rows, key=itemgetter('lname'))
print(rows_by_lname)

# mutiple key inputs for itemgetter
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))