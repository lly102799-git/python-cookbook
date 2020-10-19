# -*- coding: utf-8 -*-
"""
@author: Li Luyao
"""

from _collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:   # for key in d.keys()
    print(key, d[key])

#OrderedDict在进行json编码时，可以精准控制各字段的顺序
json.dumps(d)   #Outputs '{"foo":1, --snip--}'