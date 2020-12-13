# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/12/13 10:49
Author: Li Luyao
"""

import json

data = {
    'name':'ACME',
    'shares':100,
    'price':542.3
}

json_str = json.dumps(data)
print(json_str)
data = json.loads(json_str)

# 同json文件打交道
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json') as f:
    data = json.load(f)
    print(data)

from urllib.request import urlopen
import json
from pprint import pprint

# u = urlopen('https://www.baidu.com/')
# response = json.loads(u.read().decode('utf-8'))
# pprint(response)