# -*- coding: utf-8 -*-
"""
Using the Pretty Print module.
omgitskuei
Aug 25th 2021

Sources:
https://docs.python.org/3/library/pprint.html
"Automate the Boring Stuff with Python, 2nd Edition" by Al Sweigart, 2019

The pprint module provides a capability to “pretty-print”
Python data structures in a form which can be
used as input to the interpreter.

Note that not all objects can be pretty-printed by this module,
some such as classes, files, sockets, may not be loadable,
as well as other objects which aren't representable as Python literals.
"""

import pprint as pprint

messageString = 'It was a beautiful morning. Now go die.'
lettersFrequencyDict = {}

for char in messageString:
    # prints each letter in the string; I, t,  , w, a, s (without the commas)
    print(char)
    # sets each letter (in the string)'s frequency to 0 by default
    lettersFrequencyDict.setdefault(char, 0)
    # count each letter
    lettersFrequencyDict[char] = lettersFrequencyDict[char] + 1

# printing a dict with regular print function,
# key-value pairs are not sorted in any order
# (or is in the order which pairs are added)
print(lettersFrequencyDict)
# {'I': 1, 't': 2, ' ': 7, 'w': 2, 'a': 3, 's': 1, 'b': 1, 'e': 2, 'u': 2,
# 'i': 3, 'f': 1, 'l': 1, 'm': 1, 'o': 3, 'r': 1, 'n': 2, 'g': 2, '.': 2,
# 'N': 1, 'd': 1}

# printing a dict with pprint, key-value pairs are
# sorted into ascending alphabetical order by KEY
# SYMBOLS > UPPER CASE > LOWER CASE
pprint.pprint(lettersFrequencyDict)
# {' ': 7,
#  '.': 2,
#  'I': 1,      # note that 'I' and 'i' are counted separately
#  'N': 1,
#  'a': 3,
#  'b': 1,
#  'd': 1,
#  'e': 2,
#  'f': 1,
#  'g': 2,
#  'i': 3,
#  'l': 1,
#  'm': 1,
#  'n': 2,
#  'o': 3,
#  'r': 1,
#  's': 1,
#  't': 2,
#  'u': 2,
#  'w': 2}
