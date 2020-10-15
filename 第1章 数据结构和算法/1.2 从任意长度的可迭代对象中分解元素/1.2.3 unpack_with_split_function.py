# -*- coding: utf-8 -*-
"""
@author: Li Luyao
"""
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:user/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, fields, homedir, sh)

data = ['ACME', 50, 91.1, (2020,12,21)]
name, *_, (year, *_) = data
print(name, year)