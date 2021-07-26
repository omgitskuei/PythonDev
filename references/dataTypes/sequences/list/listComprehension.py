# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:48:31 2021

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

# ****************************************************************************
# *                          List Comprehension                              *
# *                               Examples                                   *
# ****************************************************************************

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
print('Set the values in the new list to upper case:')
newList = []
fruits = ["apple", "banana", "cherry"]
for eachStr in fruits:
    newList.append(eachStr.upper())
print(f'{newList=}')       # prints ['APPLE', 'BANANA', 'CHERRY']

# list comprehension equivalent
compList = [x.upper() for x in fruits]
print(f'{compList=}')      # prints ['APPLE', 'BANANA', 'CHERRY']


# In[7]
print('Return list with only values that contain "A":')
allIDs = ['A126123', 'A213333', 'B231111', 'X928193', 'a000111']
newIDs = []
for eachID in allIDs:
    if "A" in eachID:     # "a" != "A"
        newIDs.append(eachID)
print(f'{newIDs=}')       # prints newIDs=['A126123', 'A213333']

# list comprehension equivalent
newIDs = [eachID for eachID in allIDs if "A" in eachID]
print(f'{newIDs=}')       # prints newIDs=['A126123', 'A213333']


# In[8]
print('You can use the range() function to create an iterable')
newList = [x for x in range(5)]
print(f'{newList=}')       # prints newList=[0, 1, 2, 3, 4]

newList = [str(x) for x in range(5)]
print(f'{newList=}')       # prints newList=['0', '1', '2', '3', '4']


# In[9]
print('Return a new list of concatenated values')
a = ['1', '3', '5']
b = ['A', 'B']
c = []
for x in a:
    for y in b:
        c.append(f'{x}{y}') # same as c.append(x+y)
print(f'{c=}')    # prints c=['1A', '1B', '3A', '3B', '5A', '5B']

# list comprehension equivalent
c = [x+y for x in ['1', '3', '5'] for y in ['A', 'B']]
print(f'{c=}')    # prints c=['1A', '1B', '3A', '3B', '5A', '5B']


# In[10]
print('This listcomp combines elements of two lists if they are not equal')
d = []
for x in [1,2,3]:
	for y in [3,1,4]:
		if x != y:
			d.append((x, y))
print(f'{d=}')    # prints d=[(1, 3), (1, 4),
                  # (2, 3), (2, 1), (2, 4),
                  # (3, 1), (3, 4)]

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

# list comprehension equivalent
d = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(f'{d=}')    # prints d=[(1, 3), (1, 4),
                  # (2, 3), (2, 1), (2, 4),
                  # (3, 1), (3, 4)]


# In[11]
print('Return a new list of squares')
squares = []
for x in range(10):
    squares.append(x**2)
print(f'{squares=}')    # prints squares=[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# list comprehension equivalent
squares = [x**2 for x in range(10)]
print(f'{squares=}')    # prints squares=[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# In[12]
# List Comp. can contain complex expressions and nested functions
print('Return a list of values of pi with 1 to 5 decimals:')
from math import pi
a=[str(round(pi, i)) for i in range(1, 6)]
print(f'{a=}')    # prints a=['3.1', '3.14', '3.142', '3.1416', '3.14159']


# In[13]
# The initial expression in a list comprehension can be any arbitrary expression,
# including another list comprehension.
print('Transpose a 3x4 matrix (list[list]) of 3 lists of length 4')
matrix = [
 	[1, 2, 3, 4],
 	[5, 6, 7, 8],
 	[9, 10, 11, 12],
]

transposed = []
for i in range(4):
     transposed_row = []
     for row in matrix:
         transposed_row.append(row[i])
     transposed.append(transposed_row)
print(f'{transposed=}') # prints [
                        # [1, 5, 9],
                        # [2, 6, 10],
                        # [3, 7, 11],
                        # [4, 8, 12]
                        # ]

transposed = []
for i in range(4):
     transposed.append([row[i] for row in matrix])
print(f'{transposed=}') # prints [
                        # [1, 5, 9],
                        # [2, 6, 10],
                        # [3, 7, 11],
                        # [4, 8, 12]
                        # ]

# list comprehension equivalent
transposed = [[row[i] for row in matrix] for i in range(4)]
print(f'{transposed=}') # prints [
                        # [1, 5, 9],
                        # [2, 6, 10],
                        # [3, 7, 11],
                        # [4, 8, 12]
                        # ]

