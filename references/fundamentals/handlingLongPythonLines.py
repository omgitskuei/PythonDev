# -*- coding: utf-8 -*-
"""
Exceptions to Indentation Rules in Python.

These tricks are useful when you want to rearrange long lines of Python
code to be a bit more readable.

- P.92, Automating the boring stuff with Python Ed.2 (2015) by Al Sweigart
"""

"""
In most cases, the amount of indentation for a line of code tells Python what
block it is in. There are some exceptions to this rule, however.

For example, lists can actually span several lines in the source code file.
The indentation of these lines do not matter; the list is not finished until
Python sees the ending square bracket.

Practically speaking, most people make their lists look pretty and readable.
"""

# In[1]: A list spanning multiple lines
spam = ['apples',
'oranges',
    # Indents between list items are irrelevant
    'bananas',
'cats']
print(spam)



"""
You can also split up a single instruction across multiple lines using the \
line continuation character at the end.

The indentation on the line after a \ line continuation is irrelevant.
"""

# In[2]: A line of Python spanning multiple lines
print('Four score and seven ' + \
'years ago...')
