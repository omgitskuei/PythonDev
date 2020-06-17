# Strings count as sequence type because it can be indexed and sliced

# NOTE: Strings in Python are immutable/cannot be changed!!!
word = 'Python'
# word[0] = 'J'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment

# if you need a new string, just make one
'J' + word[1:]
'Jython'

# String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'

#  \ can be used to escape quotes:
>>> 'doesn\'t'  # use \' to escape the single quote...
# "doesn't"
>>> "doesn't"  # ...or use double quotes instead
# "doesn't"
>>> '"Yes," they said.'
# '"Yes," they said.'
>>> "\"Yes,\" they said."
# '"Yes," they said.'
>>> '"Isn\'t," they said.'
# '"Isn\'t," they said.'


# NOTE: special characters like \n for newline are ignore without print()
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), \n is included in the output
# 'First line.\nSecond line.'
>>> print(s)  # with print(), \n produces a new line
# First line.
# Second line.


# NOTE: Using 'raw String' to ignore special characters
# If you don’t want characters prefaced by \ to be interpreted as special
# characters, you can use raw strings by adding an r before the first quote:
>>> print('C:\some\name')  # here \n means newline!
# C:\some
# ame
>>> print(r'C:\some\name')  # note the r before the quote
# C:\some\name


# NOTE: String literals can span multiple lines.
# One way is using triple-quotes: """...""" or '''...'''.
# End of lines are automatically included in the string, but it’s possible to
# prevent this by adding a \ at the end of the line.
# The following example:
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# produces the following output (note that the initial newline is not included):
# Usage: thingy [OPTIONS]\
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to

# this """\ ...some text""" is the same as;
print("\
Usage: thingy [OPTIONS]\
     -h                        Display this usage message\
     -H hostname               Hostname to connect to
")


# NOTE: Strings can be repeated with *
# eg. 3 times 'um', followed by 'ium'
>>> 3 * 'um ' + 'ium'	# answer = 'um um um ium'


# NOTE: 2 string literals will auto-concatenate
# string literals (i.e. the ones enclosed between quotes)
>>> 'Py' 'thon'
# 'Python'
# This feature is particularly useful when you want to break long strings:
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text	# answer = 'Put several strings within parentheses to have them joined together.'


# NOTE: This only works with literals (does not work with variables)
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
#   File "<stdin>", line 1
#     prefix 'thon'
#                 ^
# SyntaxError: invalid syntax

# The built-in function len() returns the length of a string:
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s) # answer = 34
