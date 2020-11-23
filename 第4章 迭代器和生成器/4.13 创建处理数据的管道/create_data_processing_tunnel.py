# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2020-11-23 14:21
@author: Li Luyao
"""

# 问题：有海量数据需要处理，但是没法完全将数据加载到内存中去
import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        yield from it  # 处理压缩文件


def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines.
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


# 找出www文件夹下所有日志文件中，所有包含关键字python的日志行
filepat = 'access-log*'
top_dir = 'wwww'
logfile_names = gen_find(filepat, top_dir)
logfiles = gen_opener(logfile_names)
lines = gen_concatenate(logfiles)
line_pat = '(?i)python'
pylines = gen_grep(line_pat, lines)
for line in pylines:
    print(line)
