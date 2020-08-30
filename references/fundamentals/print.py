"""
Printing with Python.

Created on Mon Aug 31 01:06:03 2020.

@author: omgitskuei
"""
# -*- coding: utf-8 -*-

# NOTE: The print() function writes the value of the argument(s) it is given.
# It handles multiple arguments, floating point quantities, and strings slightly
# differently from normal value assignment.

# Strings are printed without quotes
print('This is surrounded in single-quotes')
print("This is surrounded in double-quotes")

# f-Strings can take variables
name = "Kuei"
print(f"{name} is my name.")

# NOTE: a space is inserted between items so you can format like this:
i = 256*256
print('The value of i is', i, ".")
# Prints The value of i is 65536

# NOTE: The keyword argument [end] can be used to avoid the newline after the
# output, or end the output with a different string:
a, b = 0, 1
while a < 60:
    print(a, end=',')
    a, b = b, a+b
    # prints 0,1,1,2,3,5,8,13,21,34,55,
a, b = 0, 1
while a < 60:
    print(a)
    a, b = b, a+b

