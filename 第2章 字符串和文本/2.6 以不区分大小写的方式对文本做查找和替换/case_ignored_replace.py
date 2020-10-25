# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2020/10/24 17:06
Author: Li Luyao
"""
import re
text = 'UPPER PYTHON, lower python, Mixed Python.'
print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))  # Return: UPPER snake, lower snake, Mixed snake.

# 上述例子的局限，IGNORECASE导致待替换的文本与匹配的文本大小写不吻合
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.title()
        else:
            return word

    return replace


print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))  # Return: UPPER SNAKE, lower snake, Mixed Snake.