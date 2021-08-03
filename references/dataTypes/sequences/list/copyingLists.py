# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 12:25:17 2021
From Automate the Boring stuff with Python
@author: kueif
"""

'''
Although passing around references is often the handiest way
to deal with lists and dictionaries, if the function modifies
the list or dictionary that is passed, you may not want these
changes in the original list or dictionary value.

For this, Python provides a module named copy that provides
both the copy() and deepcopy() functions.
'''

import copy as copyModule

list1 = ['A', 'B', 'C', 'D']

list2 = copyModule.copy(list1)
list2[1] = 42

print(f'{list1=}')
print(id(list1))

print(f'{list2=}')
print(id(list2))