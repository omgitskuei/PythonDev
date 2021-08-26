# -*- coding: utf-8 -*-
"""
Program name: Notes on continue in Python.

Summary: Notes on syntax, usage, and example snippets of continue
Created on: Sat Oct 24 11:37:09 2020
@author: omgitskuei (Github)
"""

# The continue statement, also borrowed from C, continues with the next
# iteration of the loop:
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue		# when triggered, skips the 2nd print
    print("Found a number", num)
# prints
# Found an even number 2
# Found a number 3
# Found an even number 4
# Found a number 5
# Found an even number 6
# Found a number 7
# Found an even number 8
# Found a number 9
