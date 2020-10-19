# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/10/18 8:33
Author: Li Luyao
"""
# collections模块 Counter类
from collections import Counter  # 用于数据制表或者计数问题

nums = [1, 3, 3, 1, 5, 1, 2, 5, 5, 5, 5, 3, 2, 3]
# Counter的输入为任何可哈希对象，其底层实现为字典，在元素和其出现次数间做了映射
num_count = Counter(nums)
top_three = num_count.most_common(3)
print(top_three)
print(num_count[1])

more_nums = [4, 3, 3, 3, 1]
# 使用update方法，更新Counter类元素和次数
num_count.update(more_nums)

# Counter对象的数学运算
a = Counter(nums)
b = Counter(more_nums)
# Combine nums
c = a + b
# Subtract counts
d = a - b