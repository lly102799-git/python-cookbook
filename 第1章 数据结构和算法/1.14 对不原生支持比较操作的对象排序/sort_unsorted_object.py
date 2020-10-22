# -*- coding: utf-8 -*-
"""
@author: Li Luyao
"""
from operator import attrgetter


class User:
    def __init__(self, user_id, user_fname='', user_lname=''):
        self.user_id = user_id
        self.user_lname = user_lname
        self.user_fname = user_fname

    def __repr__(self):
        return '{}({})'.format(self.user_fname, self.user_id)  # format方法：“{}的性别是：{}”.format('小明', '男')


users = [User(23, 'Dell', 'Green'), User(31, 'Joey', 'Tribianni'), User(23, 'Chandler', 'Bin')]
print(users)
a = sorted(users, key=lambda u: u.user_id, reverse=True)
b = sorted(users, key=attrgetter('user_id'), reverse=True)
c = sorted(users, key=attrgetter('user_id', 'user_lname'))
print(a)
print(b)
print(c)