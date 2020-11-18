# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-17 10:59
@author: Li Luyao
"""
from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = datetime.today().replace(day=1)
    # start_date = start_date.replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)

a_day = timedelta(days=1)
first_day, last_day = get_month_range(datetime.today())
while first_day < last_day:
    print(first_day)
    first_day += a_day

# 日期生成器
def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

for d in date_range(datetime(2019, 9, 1), datetime(2019, 9, 5), timedelta(hours=6)):
    print(d)