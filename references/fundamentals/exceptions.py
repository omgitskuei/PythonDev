# -*- coding: utf-8 -*-
"""
Exceptions
There's two kinds of errors;
1) syntax (parsing errors)
2) exceptions (run time errors)

SYNTAX for try-catch:
try:
    # execute this
except NameError as ne:
    # execute this if try FAILS
else:
    # execute this if try SUCCEEDS
finally:
    # always execute this
"""

try:
    print('print this')
except NameError as ne:
    print('not printing this')
else:
    print('print this')
finally:
    print('print this')

try:
    print('hi')     # this is printed
    # hi not defined
    print(hi)       # this is not printed, throws Error
except NameError as ne:
    # name 'hi' is not defined
    print(ne)
    # ("name 'hi' is not defined",)
    print(ne.args)
    # <traceback object at 0x0000023A312E8E80>
    print(ne.__traceback__)
    # None
    print(ne.__context__)
    # None
    print(ne.__cause__)
    # Name not found globally.
    print(ne.__doc__)
else:
    print("welp")
finally:
    # prints this
    print("Always execute this")

''' Read More '''
# Python already comes with premade exceptions, which I can read about at
# docs.python.org/3/library/exceptions.html
# SyntaxError, ZeroDivisionError, etc
