# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/12/3 20:27
Author: Li Luyao
"""

# 程序运行时，创建临时文件或目录以便使用。在这之后，希望将这些文件和目录销毁掉
# tempfile模块.

from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:  # with 上下文管理器
    # Read and write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    # Seek back to beginning and read the data
    f.seek(0)  # 移动文件指针至开始位置，读写模式必备;如果没有seek(0)重置文件指针，读取的文本为空
    data = f.read()
    print(data)

# Temporary file is destroyed

f = TemporaryFile('w+t')
# Use the temp file...
f.close()
# File is destroyed

# 创建命名的临时文件：如果需要将临时文件名传给其他需要打开这个文件的代码时，就显得很有用了
from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print('filename is: ', f.name)

# Temp file automatically destroyed
# 如果不想要临时文件
f = NamedTemporaryFile('w+t')
print(f.name)

f.close()
# Or
with NamedTemporaryFile('w+t', delete=False) as f:
    print(f.name)

f.close()
