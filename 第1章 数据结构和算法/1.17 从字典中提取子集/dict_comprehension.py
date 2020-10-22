# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-20 16:02
@author: Li Luyao
"""
prices = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM": 205.55,
    "HBQ": 37.20,
    "FB": 10.75
}

# Make a dict of all prices over 200
p1 = {key: val for key, val in prices.items() if val > 40}
# p1 = dict((key, val) for key, val in prices.items() if val > 40)
print(p1)

# Make a dict of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: val for key, val in prices.items() if key in tech_names}
# p2 = {key: prices[key] for key in prices.keys() & tech_names}
print(p2)