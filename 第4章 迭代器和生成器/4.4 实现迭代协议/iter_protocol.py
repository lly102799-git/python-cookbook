# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-17 17:54
@author: Li Luyao
"""

# yield 与 yield from
# 字符串
astr='ABC'
# 列表
alist=[1,2,3]
# 字典
adict={"name":"wangbm","age":18}
# 生成器
agen=(i for i in range(4,8))

def gen(*args, **kw):
    for item in args:
        for i in item:
            yield i

def gen_2(*args, **kw):
    for item in args:
        yield from item

new_list1=gen(astr, alist, adict, agen)
print(list(new_list1))

new_list2=gen_2(astr, alist, adict, agen)
print(list(new_list2))

# 迭代器、委托迭代器，实现迭代协议
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch, 'tag')  # 加上'tag'之后观察输出