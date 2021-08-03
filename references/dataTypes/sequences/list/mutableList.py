# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 12:25:17 2021
From Automate the Boring stuff with Python
@author: kueif
"""

# Although a list value is mutable, the second line in the following code
# does not modify the list eggs:
eggs = [1, 2, 3]
print(id(eggs))

eggs = [4, 5, 6]
print(id(eggs))


# The list value in eggs isn’t being changed here; rather, an entirely new
# and different list value ([4, 5, 6]) is overwriting the old list value
# ([1, 2, 3]).


# If you wanted to actually modify the original list in eggs to contain
# [4, 5, 6], you would have to do something like this:
eggs = [1, 2, 3]
eggs.clear()
print(id(eggs))

eggs.append(4)
eggs.append(5)
eggs.append(6)
print(id(eggs))