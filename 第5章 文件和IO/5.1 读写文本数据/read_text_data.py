# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-24 9:31
@author: Li Luyao
"""

# 文本数据读写操作与编码
# 常见编码格式：ASCII、UTF-8、UTF-16

# Read the entire file as a single string
with open(r'D:\Personal\Desktop\python test.txt', 'rt') as f:
    data = f.read()
    print(data)

# Iterate over the lines of the file
with open(r'D:\Personal\Desktop\python test.txt', 'rt') as f:
    for line in f:
        print(line)


# Write chunks of text data
with open(r'D:\Personal\Desktop\python test 2.txt', 'wt') as f:
    f.write('aaa')
    f.write('\nbbb')  # 多次写入，效果类似于append，添加\r换行符为什么没作用？\n就有用了。牵扯到newline=参数

# Redirected print statement，重定向
with open(r'D:\Personal\Desktop\python test 2.txt', 'wt') as f:
    print('ccc', file=f)
    print('ddd', file=f)

# 当程序的控制流程离开with语句块后， 文件将自动关闭。不一定使用with语句，但是不用的话请确保手动关闭文件。
f = open(r'D:\Personal\Desktop\python test 2.txt', 'rt')
data = f.read()
f.close()

#编码错误处理：不用常常摆弄open()函数的encoding和errors参数，并为此做大量技巧性操作，那就适得其反了，因为生活本不应该如此艰难。
f = open('somefile.txt', 'rt', encoding='ascii', errors='replace')
f = open('somefile.txt', 'rt', encoding='ascii', errors='ignore')