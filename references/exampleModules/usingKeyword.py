"""
Using the Keyword module.

A Python keyword is any word in Python that is part of the language itself.
The keyword module contains a function [iskeyword] and a variable [kwlist].

Function [iskeyword] returns true if any string is a Python keyword.
Variable [kwlist] returns a list of all Python keywords.

We print the contents of variable [kwlist] because different versions of
Python may have different keywords.

Created on Sat Aug 29 10:01:06 2020.

@author: omgitskuei
"""
# -*- coding: utf-8 -*-

import keyword


print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
# 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with',
# 'yield']

print(keyword.iskeyword('kuei'))
# false

print(keyword.iskeyword('if'))
# true
