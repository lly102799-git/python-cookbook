# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2021-01-22 13:35
@author: Li Luyao
"""
# 任意数量位置参数：以元组形式存储
def avg_nums(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

# 任意数量关键字参数，以字典形式存储
def sum_nums(first, **rest):
    dict_list = [val for val in rest.values()]
    return first + sum(dict_list)

if __name__ == '__main__':
    print(avg_nums(5,4,3,2))
    print(sum_nums(5, age=5, height=4))