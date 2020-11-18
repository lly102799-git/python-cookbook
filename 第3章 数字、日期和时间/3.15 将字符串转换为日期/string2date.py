# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-17 14:29
@author: Li Luyao
"""
from datetime import datetime
text = '2020-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
print(z-y)

nice_z = datetime.strftime(z, '%a %b %d, %Y')
print(nice_z)

# 已知日期字符串格式(如'YYYY-MM-DD')，自己编写解析函数
from datetime import datetime
def parse_ymd(s):
    year_s, month_s, day_s = s.split('-')
    return datetime(int(year_s), int(month_s), int(day_s))

print(parse_ymd(text))