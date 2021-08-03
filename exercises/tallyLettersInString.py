# -*- coding: utf-8 -*-
"""
Program name: tallyLettersInString
Summary: Counts the number of times each letter appears in a given String.
Created on: Tue Aug  3 23:34:30 2021
@author: omgitskuei (Github)
"""



message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    # setdefault() method is a nice shortcut to ensure that a key exists.
    # doesn’t throw a KeyError error when count[character] =
    # count[character] + 1 is executed.
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# print(count)
# {'I': 1, 't': 6, ' ': 13, 'w': 2, 'a': 4, 's': 3, 'b': 1, 'r': 5, 'i': 6
# 'g': 2, 'h': 3, 'c': 3, 'o': 2, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1,
# 'p': 1, ',': 1, 'e': 5, 'k': 2, '.': 1}

# the printed dict is unordered

# copy each key from dict_keys into a list, to sort the keys
countKeysAsList = []
for key in count.keys():
    countKeysAsList.append(key)
countKeysAsList.sort()
# print(countKeysAsList)

# retrieve the values in order of sorted keys, concatenate and print string
string = ""
for ind in range(len(countKeysAsList)):
    string = string + "'" + countKeysAsList[ind] + "'" + ":" + str(count.get(countKeysAsList[ind]))
    if ind != len(countKeysAsList)-1:
        string = string + ", "

print(string)
# ' ':13, ',':1, '.':1, 'A':1, 'I':1, 'a':4, 'b':1, 'c':3, 'd':3, 'e':5,
# 'g':2, 'h':3, 'i':6, 'k':2, 'l':3, 'n':4, 'o':2, 'p':1, 'r':5, 's':3,
# 't':6, 'w':2, 'y':1