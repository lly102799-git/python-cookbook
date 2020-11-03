# -*- coding: utf-8 -*-
"""
@project: Python Cookbook
@date: 2020-10-27 18:12
@author: Li Luyao
"""
# format可以作用于任何对象，而ljust()、rjust()、center()方法只作用于字符串
# ljust(), rjust(), center(len, fill)方法，可指定生成字符串的长度和空格填充的符号
text = ' Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

# 填充字符方法
print(text.ljust(20, '-'))

# format函数，>右对齐，<左对齐，^居中对齐
print(format(text, '>20'))
print(format(text, '=<20'))
print(format(text, '*^25'))

print('{:*>10}{:+>10}'.format('Hello', 'World'))

# 用format()函数处理数值或其他任何值
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))  # 总长10位，居中，类型为f，保留两位有效数字；