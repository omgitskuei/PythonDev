# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 12:49:34 2021

@author: kueif
"""

# If you have only one value in your tuple, you can indicate
# this is of type Tuple by placing a trailing comma after
# the value inside the parentheses.
# Otherwise, Python will think you’ve just typed a value
# inside regular parentheses.

print(type(('hello',)))
# <class 'tuple'>

print(type(('hello')))
# <class 'str'>