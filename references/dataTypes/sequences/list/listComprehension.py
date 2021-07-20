# -*- coding: utf-8 -*-
"""
List Comprehensions
List comprehension offers a shorter syntax when you want to create a new list
based on the values of (an) existing list(s).

Syntax
A list comprehension consists of brackets '[]' containing an expression
followed by a for clause, then zero or more for or if clauses.

newlist = [expression for item in iterable if condition == True]
- The 'condition' is like a filter that only accepts the items that valuate to
  True.
- The 'iterable' can be any iterable object, like a list, tuple, set etc.
- The 'expression' is the current item in the iteration, but it is also the
  outcome, which you can manipulate before it ends up like a list item in the
  new list.
"""

# Set all values in the new list to 'hello'
fruits = ["apple", "banana"]
newList1 = []
for eachStr in fruits:
    newList1.append('hello')
print(f'{newList1=}')      # prints ['hello', 'hello']
# list comprehension equivalent
compList1 = ['hello' for x in fruits]
print(f'{compList1=}')     # prints ['hello', 'hello']

# Return "orange" instead of "banana":
newList2 = []
fruits = ["apple", "banana", "cherry"]
for eachStr in fruits:
    if eachStr == "banana":
        newList2.append("orange")
    else:
        newList2.append(eachStr)
print(f'{newList2=}')      # prints ['apple', 'orange', 'cherry']
# list comprehension equivalent
compList2 = [x if x != "banana" else "orange" for x in fruits]
print(f'{compList2=}')     # prints ['apple', 'orange', 'cherry']

# Set the values in the new list to upper case:
newList3 = []
fruits = ["apple", "banana", "cherry"]
for eachStr in fruits:
    newList3.append(eachStr.upper())
print(f'{newList3=}')       # prints ['APPLE', 'BANANA', 'CHERRY']
# list comprehension equivalent
compList3 = [x.upper() for x in fruits]
print(f'{compList3=}')      # prints ['APPLE', 'BANANA', 'CHERRY']

Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]

You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

With no if statement:
newlist = [x for x in fruits]

Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]



# Based on a list of fruits, you want a new list, containing only the fruits
# with the letter "a" in the name.
oldList = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []
for eachStr in oldList:
    if "a" in eachStr:    # if String contains 'a'
        newList.append(eachStr)
# prints ['apple', 'banana', 'mango']
print(newList)

# With list comprehension you can do all that with only one line of code:
oldList = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [eachStr for eachStr in oldList if "a" in eachStr]
# prints ['apple', 'banana', 'mango']
print(newList)



# this listcomp combines the elements of two lists if they are not equal:
combinedList = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# prints [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
print(combinedList)

# Step by Step process for getting combinedList;
# |  x  |  y  |  !=?  |  append  |
# --------------------------------
# |  1  |  3  |  yes  |  (1, 3)  |
# |  1  |  1  |  no   |          |
# |  1  |  4  |  yes  |  (1, 4)  |
# --------------------------------
# |  2  |  3  |  yes  |  (2, 3)  |
# |  2  |  1  |  yes  |  (2, 1)  |
# |  2  |  4  |  yes  |  (2, 4)  |
# --------------------------------
# |  3  |  3  |  no   |          |
# |  3  |  1  |  yes  |  (3, 1)  |
# |  3  |  4  |  yes  |  (3, 4)  |

# this listcomp is equivalent to:
combinedList = []
for x in [1,2,3]:
	for y in [3,1,4]:
		if x != y:
			combinedList.append((x, y))
# prints [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
print(combinedList)



# ****************************************************************************
# *                          List Comprehensions                             *
# *                                                                          *
# ****************************************************************************


#
#
#
#
# and
#
# assume we want to create a list of squares, like:
# squares = []
# for x in range(10):
# 	squares.append(x**2)
# 	squares													# prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# List comprehensions can contain complex expressions and nested functions:
# from math import pi
# [str(round(pi, i)) for i in range(1, 6)]					# prints ['3.1', '3.14', '3.142', '3.1416', '3.14159']
#
#
# The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.
#
# Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
# matrix = [
# 	[1, 2, 3, 4],
# 	[5, 6, 7, 8],
# 	[9, 10, 11, 12],
# ]
# The following list comprehension will transpose rows and columns
# [[row[i] for row in matrix] for i in range(4)]				# prints [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# this example is equivalent to:
# transposed = []
# for i in range(4):
# ...     transposed.append([row[i] for row in matrix])
# ...
# transposed
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# which, in turn, is the same as:
#
# >>>
# transposed = []
# for i in range(4):
# ...     # the following 3 lines implement the nested listcomp
# ...     transposed_row = []
# ...     for row in matrix:
# ...         transposed_row.append(row[i])
# ...     transposed.append(transposed_row)
# ...
# transposed
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
