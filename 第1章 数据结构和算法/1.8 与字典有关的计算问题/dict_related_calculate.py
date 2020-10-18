# -*- coding: utf-8 -*-
"""
Create Time:  
Author: Li Luyao
"""
prices = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM": 205.55,
    "HBQ": 37.20,
    "FB": 10.75
}

# 利用zip()函数，将字典打包为（值，键）元组，通过比较元组(按位置顺序，先比较值，再比较键)，得出最小值及对应的键
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

sorted_price = sorted(zip(prices.values(), prices.keys()), reverse=True)
print(sorted_price)

# zip（）函数返回的是迭代器，其内容只能被消费一次
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
print(max(prices_and_names))   # Error

# 直接对字典进行数据操作，只会处理键
min(prices)
max(prices)

# 处理值，不会返回键
min(prices.values())
max(prices.values())

# 如何返回键
min(prices, key=lambda k: prices[k])

# 匿名函数 lambda： fn = lambda x: y, x是输入，y是输出
# min(prices, key=lambda k: prices[k]) key=指定了min函数比较的是prices[k],即字典的值，但是返回的仍然是键，参考min(prices)
