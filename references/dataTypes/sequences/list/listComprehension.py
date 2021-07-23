# -*- coding: utf-8 -*-
"""
List Comprehensions
List comprehension offers a shorter syntax when you want to create a new list
based on the values of (an) existing list(s).

Syntax
newlist = [EXPRESSION for ITEM in ITERABLE if CONDITION]
- The 'CONDITION' is a filter that only accepts items that valuate to True.
- The 'ITERABLE' can be any iterable object, like a list, tuple, set etc.
- The 'EXPRESSION' is the current item in the iteration, but it is also the
  outcome, which you can manipulate before it ends up like a list item in the
  new list.
A list comprehension consists of brackets '[]' containing an expression
followed by a for clause, then zero or more for or if clauses.

@author: omgitskuei
"""
# In[0]
print('Return a new list that is the SAME as the iterable')
things = [1, 2.2, "a"]
newList = []
for item in things:
    newList.append(item)
print(f'{newList=}')    # prints newList=[1, 2.2, 'a']

# list comprehension equivalent
newList = [item for item in things]    # no CONDITION after ITERBLE
print(f'{newList=}')


# In[1]
print('Return a new list with 1 condition')
numbers = [1, 2.2, 4, 6, 10]
newList = []
for number in numbers:
    if number < 5:
        newList.append(number)
print(f'{newList=}')    # prints newList=[1, 2.2, 4]

# list comprehension equivalent
newList = [number for number in numbers if number < 5]
print(f'{newList=}')    # prints newList=[1, 2.2, '4']

# Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry"]
newList = []
for fruit in fruits:
    if fruit != 'apple':
        newList.append(fruit)
print(f'{newList=}')    # prints ["banana", "cherry"]

# list comprehension equivalent
newList = [fruit for fruit in fruits if fruit != 'apple']
print(f'{newList=}')    # prints ["banana", "cherry"]


# In[2]
print('Return a new list with 2 conditions')
numbers = [1, 2.2, 4, 6, 10]
newList = []
for number in numbers:
    if number < 5 and number > 1:
        newList.append(number)
print(f'{newList=}')    # prints newList=[2.2, 4]

# list comprehension equivalent
newList = [number for number in numbers if number < 5 and number > 1]
print(f'{newList=}')    # prints newList=[2.2, '4']


# In[3]
print('Return a new list with overwritten Static values')
fruits = ["apple", "banana"]
newList = []
for eachStr in fruits:
    newList.append('hello')    # Set all values in the new list to "hello"
print(f'{newList=}')      # prints ['hello', 'hello']

# list comprehension equivalent
compList = ['hello' for each in fruits]
print(f'{compList=}')     # prints ['hello', 'hello']


# In[4]
print('Return a new list where a specific value is overwritten')
fruits = ["apple", "banana", "mango", "pear"]
newList = []
for eachFruit in fruits:
    # ternary
    newList.append('Bleh' if eachFruit == "mango" else eachFruit)
print(f'{newList=}')      # prints newList=['apple', 'banana', 'Bleh', 'pear']

# list comprehension equivalent
compList = [fruit if fruit != "mango" else 'Bleh' for fruit in fruits]
print(f'{compList=}')     # prints ['apple', 'banana', 'Bleh', 'pear']


# In[5]
print('Return "orange" instead of "banana":')
newList = []
fruits = ["apple", "banana", "cherry", "banana"]
for eachStr in fruits:
    if eachStr == "banana":
        newList.append("orange")
    else:
        newList.append(eachStr)
print(f'{newList=}')      # prints ['apple', 'orange', 'cherry', 'orange']

# list comprehension equivalent
compList = [x if x != "banana" else "orange" for x in fruits]
print(f'{compList=}')     # prints ['apple', 'orange', 'cherry', 'orange']


# In[6]










# In[2]: Set the values in the new list to upper case:
newList2 = []
fruits = ["apple", "banana", "cherry"]
for eachStr in fruits:
    newList2.append(eachStr.upper())
print(f'{newList2=}')       # prints ['APPLE', 'BANANA', 'CHERRY']
# list comprehension equivalent
compList2 = [x.upper() for x in fruits]
print(f'{compList2=}')      # prints ['APPLE', 'BANANA', 'CHERRY']





You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

With no if statement:
newlist = [x for x in fruits]





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
