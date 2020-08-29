"""
Using the Random module.

The random module have functions useful for generating random numbers.

Created on Sat Aug 29 10:01:06 2020.

@author: omgitskuei
"""

# -*- coding: utf-8 -*-

import random

"""
[randint] function picks a random number between a range of numbers
"""
num = random.randint(1, 100)
print(num)
# 58
print(random.randint(100, 1000))
# 861

"""
[choice] function picks a Random Item from a List
"""
desserts = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']
print(random.choice(desserts))
# brownies

"""
[shuffle] function mixes up order of items in a list
"""
desserts = ['ice cream',  'pancakes',  'brownies',  'cookies', 'candy']
random.shuffle(desserts)
print(desserts)
# ['pancakes', 'ice cream', 'candy', 'brownies', 'cookies']
