# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-11-10 17:51
@author: Li Luyao
"""

# 将浮点数取整到固定的小数位：roundn(value, ndigits)
x = 1234.5678
print(round(x, 3))
print(round(x,-1))

# 取整和格式化
print(format(x, '.2f'))
print('Value is {:.2f}'.format(x))

# 浮点数精度的问题：浮点数天生的误差
a = 2.1
b = 4.3
print(a+b) # Return: 6.300000000000001

# 如何避免浮点数精度问题：decimal模块
from decimal import Decimal
a = Decimal('2.1') # 不能是 a = Decimal(2.1)，这样赋值仍然会出误差
b = Decimal('4.3')
print(a+b)

# decimal模块控制数字的位数
from decimal import localcontext
print(a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)

# 大小数相加减
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))  # Return 0 instead of 1
import math
print(math.fsum(nums))  # Return 1

# 对数值做格式化输出
x = 1234.5678
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '<8.3f'))
print(format(x, '^15,.2e'))
print('The result is {:^15,.2e}'.format(x))

# 二进制、八进制与十六进制
y = 1234
print(bin(y))
print(format(y, 'b'))
print(oct(y))
print(hex(y))

# 复数运算
a = complex(2,4)
b = 3 - 5j
print(a+b)
print(a.real, a.imag, a.conjugate())
# 对复数执行函数操作需要导入cmath模块
import cmath
print(cmath.sin(a))

# 处理无穷大和NaN
# Python中并没有特殊的语法用来表达这些特殊的浮点数值，但是可以通过float()创建：
a = float('inf')
b = float('-inf')
c = float('nan')

# 检测是否出现了这些值：
import math
math.isinf(a)
math.isnan(c)
# inf和nan的计算特性：
print(a+b)
print(c == float('nan'))

# 分数的计算：fractions模块
from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a+b) #  Return 27/16: Fraction 的计算结果以分数展示
print(a-2)
# 获取分数的分子和分母
print(a.numerator)
print(a.denominator)
# 分数转换为小数
print(float(a))
# 小数转分数
x = 3.75
print(Fraction(*x.as_integer_ratio()))  # *将as_integer_ratio()返回的tuple拆分成单个元素
print(Fraction(x))  # 直接将x作为Fraction输入即可。。。
