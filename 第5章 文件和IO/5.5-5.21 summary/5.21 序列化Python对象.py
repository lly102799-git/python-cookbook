# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/12/3 21:16
Author: Li Luyao
"""

# 我们需要将Python对象序列化为字节流，这样就可以将其保存到文件中、储存到数据库中或者通过网络连接进行传输
# pickle模块

data = [1,2,3,4,5,56]

import pickle

# 将某个对象转储到文件中
f = open('somefile', 'wb')
pickle.dump(data, f)
f.close()

# 将某个对象转储为字符串
s = pickle.dumps(data)
print(s)

# 从字节流中重新创建对象
# Restore form a file
f = open('somefile', 'rb')
data = pickle.load(f)
print(data)
f.close()

# Restore from a string
data = pickle.loads(s)
print(data)