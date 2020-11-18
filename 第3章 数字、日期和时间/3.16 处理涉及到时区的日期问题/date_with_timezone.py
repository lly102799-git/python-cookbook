# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-17 14:47
@author: Li Luyao
"""
# 时区模块pytz
from datetime import datetime, timedelta
from pytz import timezone
import pytz

d = datetime(2012, 12, 21, 9, 30, 0)
# Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# Convert to Bangalore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

# 将时间转换为世界统一时间（避免时区、夏令时等问题）
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)
later_utc = utc_d + timedelta(minutes=30)
# 将世界统一时间UTC转换为地区夏令时
print(later_utc.astimezone(central))