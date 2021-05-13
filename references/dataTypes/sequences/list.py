# -*- coding: utf-8 -*-
"""
Lists
A list is a valu containing multiple values in an << ordered >> sequence.

Values inside the list are comma-delimited.
A list begins with an opening square bracket, [.
A list ends with a closing square bracket, ].

animals = ['cat', 'bat', 'rat', 'elephant']
emptyList = []

There are important differences between list and tuple - see below*
"""
# ****************************************************************************
# *                          C.R.U.D.                                        *
# ****************************************************************************
"""
Creating a list

NOTE:
- Duplicates are allowed
- A list allows items of any data type, including other lists

"""
# there's a duplicate
subjects = ['Econ', 'Math', 'Math', 'Bio', 'Engl', 'Poli']

# contains mix of string and int
unsortableList = [1, 2, 'a']

# lists containing other lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
# prints [['a', 'b', 'c'], [1, 2, 3]]
x
# prints ['a', 'b', 'c']
x[0]
# prints 'b'
x[0][1]

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
# ['cat', 'bat']
spam[0]
# 'bat'
spam[0][1]
# 50
spam[1][4]

# NOTE: We are actually telling python that the two variables should
# reference the same list object - perhaps leading to unintended behaviors
aList = [1, 3, 5, 7]
notANewList = aList             # NOT copying the list values to new list!!!
notANewList[0] = -10            # changes to 2nd list affects 1st list
print(aList)                    # [-10, 3, 5, 7]


"""
Retrieving value(s) from a list

NOTE:
- Indexes can be negative, returning values from the end of the list.
"""
# To read items of a list, we use Indexing.
subjects = ['Econ', 'Math', 'Math', 'Bio', 'Engl', 'Poli']
# 'Econ'
print(subjects[0])
# 'Bio'
print(subjects[3])
# prints LAST element 'Politics'
print(subjects[-1])

a = [1, 2, 3, 4]
# prints True
print(2 in a)

# Also, [X:Y:Z] Z is used if you want to periodically skip indexes
Ingredients = [1, "potato", 3, "eggs", 2, "chicken", 20.50, "salt"]
print("Ingredients", Ingredients)
# Starts on the 2nd value, goes to end, skips every other value (removes nums)
print("Ingredients w/o Numbers", Ingredients[1::2])

"""
Updating value(s) of a list

NOTE:
- Lists are a mutable type, i.e. can change their content
"""
#
# the cube of 4 is 64, not 65!
cubes = [1, 8, 27, 65]
# replace the wrong value
cubes[3] = 64
# [1, 8, 27, 64]
cubes

"""
Deleting values from a list
"""


# ****************************************************************************
# *                          Useful Methods                                  *
# ****************************************************************************
"""
Append
Add new items at the end of the list
a.append(x) is Equivalent to a[len(a):] = [x].
"""
cubes = [1, 8, 27, 65]
# Append the cube of 5
cubes.append(125)
# [1, 8, 27, 65, 125]
cubes
# Append the cube of 6
cubes.append(6 ** 3)
# [1, 8, 27, 65, 125, 216]
cubes

aList = [1, 3]
aList.append(5)
aList[len(aList):] = [5]
# [1, 3, 5, 5]
print(aList)

aList = ['bat', 'cat']
aString = 'sat'
aList.append(aString)
# ['bat', 'cat', 'sat']
print(aList)

# COMMON MISTAKE, see list.extend()
aList = [1, 3]
bList = [5]
aList.append(bList)
# [1, 3, [5]]
print(aList)


"""
Extend
Add new items at the end of the list
Given a list, the list's items are added
NOTE: list.append(x) will add the LIST itself, not just its items
a.append(x) is Equivalent to a[len(a):] = [x].
a.extend(x) is Equivalent to a[len(a):] = x.
"""
bList = ["Ashley"]
aList = ["Bob", "Dylan"]
aList.append(bList)
# ["Bob", "Dylan", ["Ashley"]]
print("aList.append(bList) => ", aList)

aList = ["Bob", "Dylan"]
aList.extend(bList)
# ["Bob", "Dylan", "Ashley"]
print("aList.extend(bList) =>", aList)

aList = ["Bob, Dylan"]
aString = 'Ashley'
aList.append(aString)
print("aList.append(aString) =>", aList)

# COMMON MISTAKE, Extend() takes any sequence
# meaning you could extend(aString) with perhaps surprising results
aList = ["Bob, Dylan"]
aList.extend(aString)
# ^ Same as aList[len(aList):] = aString
print("aList.extend(aString) =>", aList)


"""
Sort
Re-arrange order of items in the list in (by default) ASCIIbetical order
Eg. [A, a, B, b, C, c] -> [A, B, C, a, b, c]
Notice how ASCIIbetical puts 'Z' before 'a'

list.sort() takes optional params 'key' and 'reverse'
list.sort(key=None, reverse=False)
"""
# Ignoring capital cases
letters = ['a', 'z', 'A', 'Z']
letters.sort(key=str.lower)
# ['a', 'A', 'z', 'Z']
print(letters)

letters.sort(key=str.upper)
# ['a', 'A', 'z', 'Z']
print(letters)

# Sort in reverse order (but NOT ignoring capital cases)
letters = ['a', 'z', 'A', 'Z']
letters.sort(reverse=True)
# ['z', 'a', 'Z', 'A']
print('.sort(reverse=True) =>', letters)

# Sort in reverse order AND ignoring capital cases
letters = ['a', 'z', 'A', 'Z']
letters.sort(key=str.upper, reverse=True)
# ['z', 'Z', 'a', 'A']
print('.sort(key=str.upper, reverse=True) =>', letters)

# Works with numbers
a = [4.1, 3.4, 2.1, 1.0, -2.1]
a.reverse()
# [-2.1, 1.0, 2.1, 3.4, 4.1]
print(a)

#  Strange behavior when mixing int and float
a = [1, 3, 4, -4, 4.3]
a.reverse()
# [4.3, -4, 4, 3, 1]
print(a)



list.reverse()
# Reverse the elements of the list in place.

"""
Clear
Remove all items from the list.
aList.clear() is Equivalent to del a[:]
"""
aList = [1, 3]
print(aList)
aList.clear()
print(aList)

aList = [1, 4]
print(aList)
del aList[:]
print(aList)


"""
Insert
Insert an item at a given position.
The first argument is the index of the element BEFORE which to insert
So;
a.insert(0, x) inserts at the front
a.insert(len(a), x) inserts at the end, is equivalent to a.append(x)
"""
aList = [1, 3, 5]
index = 1
item = 2
aList.insert(index, item)
print(aList)

aList.insert(0, 43)
print(aList)

aList.insert(len(aList), 56)
aList.append(56)
print(aList)


"""
Remove
a.remove(x)
Remove the first item from list 'a' whose value is equal to x
It raises a ValueError if there is no such item.
"""
aList = [1, 3]
aList.remove(3)
print('after removing 3, aList =', aList)
# Throws ValueError
try:
    aList.remove(4)
except ValueError as ve:
    print('A ValueError was thrown!', ve)


"""
Count
Given aList.count(x), Return the number of times x appears in aList.
"""
aList = [4, 3, 3]
print('aList.count(4) =>', aList.count(4))
print('aList.count(3) =>', aList.count(3))
print('aList.count(99) =>', aList.count(99))

aList = ['Bob', 'Dylan', 'Bob', 'Bob']
print('aList.count(\'Bob\') =>', aList.count('Bob'))


"""
Len
Returns size of list
"""
letters = ['a', 'b', 'c', 'd']
print('len(letters) =>', len(letters))
letters.clear()
print('len(letters) =>', len(letters))


"""
Slice
Retrieve a sub-list (a set of values preserving order) from the list,
and Create a new list containing those values.

Note: end index is Exclusive
"""
# NOTE: Slice indices use defaults if omitted
# an omitted first index defaults to zero
# an omitted second index defaults to the size of the string being sliced.
word = 'Python'

# NOTE: This means that word[:i] + word[i:] is always equal to word:
# prints 'Python'
print(word[:2] + word[2:])
# prints 'Python'
print(word[:4] + word[4:])
# prints '', because end index is exclusive
print(word[1:1])

# Attempting to use an index that is too large will result in an IndexError:
try:
    # the word only has 6 characters
    word[42]
except IndexError as ie:
    print('IndexError is thrown!', ie)


# However, slice indexes are handled "gracefully" if out of bounds
# returns 'hon'
word[-3:23]
# returns 'ython'
word[1:30]
# returns 'n'
word[-1:19]
# returns 'Pyt'
word[-6:3]
# Consider this table of indices
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
#  -6  -5  -4  -3  -2  -1
#   0   1   2   3   4   5
# If end index for slice is GREATER than len(word), then return word[start:]
# start index also rolls over like this table shows if it becomes negative

allSquares = [1, 4, 9, 16, 25]
# return new list; [9, 16, 25]
sublist = allSquares[-3:]
# no start/end indices provided returns the whole list
sameList = allSquares[:]

# Lists also support operations like concatenation:
allSquares = [1, 4, 9]
allSquares + [36, 49]             # [1, 4, 9, 36, 49]

# Assignment to slices is also possible,
# NOTE: this can change the size of the list/clear it:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters				# prints ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
letters 			# prints ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
letters				# prints ['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
letters				# prints "" (nothing)

# ****************************************************************************
# *                          Difference between List and Tuple               *
# ****************************************************************************
"""
Similarities
- Both can store a collection of items.
- Each item stored in a list or a tuple can be of ANY data type.
- Both can read any item in the collection by its index.
"""

"""
Differences
- Lists are mutable whereas tuples are Immutable
...
"""
aList = ["apples", "bananas"]
print(id(aList))
aList[0] = "berries"			# change the value
print(aList)					# ['berries', 'bananas']
print(id(aList))				# same id as Ln[71]

aTuple = ("apples", "bananas")
print(id(aTuple))
# aTuple[0] = "berries"			# can't change the value - throws TypeError
# >>> Traceback (most recent call last):
# >>>   File "", line 1, in
# >>> TypeError: 'tuple' object does not support item assignment
aTuple = ("pear", "bananas")
print(aTuple)					# (pear, bananas) - overwritten, not modified
print(id(aTuple))				# NOTE: ID is different


























# Note you cant 'divide' the list, that just gives an error

""" Arithmetic with lists """
# NOTE: no such thing as division and subtraction of lists, will give TypeError
# Addition
list1 = [5, 4, 3, 2, 1]
list2 = [3, 9]
# NOTE: APPENDS list2 items after list1 items
list3 = list1 + list2
list3

# Multiplying
list1 = [1, 2]
print(list1 * 5) 		# prints [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]


""" Order of operation is paramount: """
list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4]		# NOTE: += means plus THEN equals
print(list1)
print(list2)

list1 = [5, 4, 3, 2, 1]
list2 = list1				# NOTE: WRONG you did the equals before the plus
list1 = list1 + [1, 2, 3, 4]
print(list1)
print(list2)				# list2 are different from above

list1 = [5, 4, 3, 2, 1]
list1 = list1 + [1, 2, 3, 4]   # NOTE: plus
list2 = list1					   # NOTE: then equals
print(list1)
print(list2)				         # both are same as above



# Remember; Membership Operators; tests if value is in data sequence, True or False
print(2 in [1, 2, 3, 4])  #True

# For example; a list of values where each index is squared, and the list has goes from 0*0, 1*1, etc, up to 9*9
S = [x**2 for x in range(10)]
print(S)



""" Other useful methods """







list.pop([i])		# [indexOfItem] optional
# Remove the item at the given position in the list, ...
# ... AND RETURN IT.
# If no index is specified, a.pop() removes and returns the LAST item.
# NOTE: (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)







fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.index('banana')			# returns 3
# Find next banana starting a position 4
fruits.index('banana', 4)		# returns 6
fruits.reverse()				# doesn't return anything
fruits
fruits.append('grape')			# doesn't return anything
fruits
fruits.sort()					# elements are all strings, so alphabetically sorted ascending
fruits
fruits.pop()				# returns 'pear'

# NOTE: not all data can be sorted. For instance, [None, 'hello', 10] doesn’t sort because integers can’t be compared to strings and None can’t be compared to other types.

Using Lists as Stacks (Last-In-First-Out)
To add an item to the top of the stack, use append().
To retrieve an item from the top of the stack, use pop() without an explicit index.

stack = [3, 4, 5]
stack.append(6)w
stack.append(7)
stack
[3, 4, 5, 6, 7]
stack.pop()
7
stack
[3, 4, 5, 6]
stack.pop()
6
stack.pop()
5
stack
[3, 4]


Using Lists as Queues (First-In-First-Out)
You can but lists aren't efficient for this.
While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
'Eric'
queue.popleft()                 # The second to arrive now leaves
'John'
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])


"""List Comprehensions"""
A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.

For example, this listcomp combines the elements of two lists if they are not equal:
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]		# prints [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
and it’s equivalent to:
combs = []
for x in [1,2,3]:
	for y in [3,1,4]:
		if x != y:
			combs.append((x, y))
combs														# prints [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

assume we want to create a list of squares, like:
squares = []
for x in range(10):
	squares.append(x**2)
	squares													# prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

List comprehensions can contain complex expressions and nested functions:
from math import pi
[str(round(pi, i)) for i in range(1, 6)]					# prints ['3.1', '3.14', '3.142', '3.1416', '3.14159']


The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.

Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
]
The following list comprehension will transpose rows and columns
[[row[i] for row in matrix] for i in range(4)]				# prints [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
this example is equivalent to:
transposed = []
for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
which, in turn, is the same as:

>>>
transposed = []
for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]



The del statement
Removes an item from a list given its index instead of its value.
This differs from the pop() method which returns a value.
The del statement can also be used to remove slices from a list or
clear the entire list (which we did earlier by assignment of an
empty list to the slice). For example:

>>>
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a
[1, 66.25, 333, 333, 1234.5]
del a[2:4]
a
[1, 66.25, 1234.5]
del a[:]
a
[]
