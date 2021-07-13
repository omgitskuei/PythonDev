# -*- coding: utf-8 -*-
"""
Lists
A list is a value containing multiple values in an << ordered >> sequence.

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
classes = ['Econ', 'Math', 'Math']

# contains mix of string and int
unsortableList = [1, 2, 'a']

# lists containing other lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
# prints [['a', 'b', 'c'], [1, 2, 3]]
print(x)
# prints ['a', 'b', 'c']
print(x[0])
# prints 'b'
print(x[0][1])

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
# ['cat', 'bat']
print(spam[0])
# 'bat'
print(spam[0][1])
# 50
print(spam[1][4])

# NOTE: We are actually telling python that the two variables should
# reference the same list object - perhaps leading to unintended behaviors
aList = [1, 3, 5, 7]
notANewList = aList             # NOT copying the list values to new list!!!
notANewList[0] = -10            # changes to 2nd list affects 1st list
print(aList)                    # [-10, 3, 5, 7]

# Eg; a list of values where each index is squared, and the list has goes from
# 0*0, 1*1, etc, up to 9*9
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
S = [x**2 for x in range(10)]
print(S)


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

Ingredients = [1, "potato", 3, "eggs", 2, "chicken", 20.50, "salt"]
# Ingredients [1, 'potato', 3, 'eggs', 2, 'chicken', 20.5, 'salt']
print("Ingredients", Ingredients)
# Some ingredients [1, 'potato', 3, 'eggs']
print("Some ingredients", Ingredients[0:4])
# Also, [Start:End:Step] Step is used if you want to periodically skip indexes
# Ingredients w/o Numbers ['potato', 'eggs', 'chicken', 'salt']
print("Ingredients w/o Numbers", Ingredients[1::2])
# Ingredients w/o Numbers ['potato', 'eggs', 'chicken']
print("Some Ingredients w/o Numbers", Ingredients[1:6:2])

# Membership Operator
# Membership Operators; tests if value is in data sequence, returns True/False
# True
print(2 in [1, 2, 3, 4])

# True
print('howdy' in ['hello', 'hi', 'howdy', 'hey'])
# False
print('cat' in ['hello', 'hi', 'howdy', 'hey'])
# False
print('howdy' not in spam)

# Using Lists as Stacks (Last-In-First-Out) and Queues (First-In-First-Out)
# To add and retrieve from the end, use list.append() and list.pop()
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
# stack=[3, 4, 5, 6, 7]
print(f'{stack=}')
# 7
print(stack.pop())
# stack=[3, 4, 5, 6]
print(f'{stack=}')
# 6
print(stack.pop())
# stack=[3, 4, 5]
print(f'{stack=}')
# 5
print(stack.pop())
# stack=[3, 4]
print(f'{stack=}')

# To add and retrieve from the beginning, using lists aren't efficient (slow)
# and incur O(n) memory movement costs for pop(0) and insert(0, v) operations
# because each operation changes both the size and position of the underlying
# data representation by shifting all items by 1 each time.
# To implement a queue (First-In-First-Out), use collections.deque.
# Deques support thread-safe, memory efficient appends and pops from either
# side of the deque with approximately the same O(1) performance in either
# direction.
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
# queue=deque(['Eric', 'John', 'Michael', 'Terry'])
print(f'{queue=}')
queue.append("Graham")
# queue=deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
print(f'{queue=}')
leavingPerson = queue.popleft()
# leavingPerson='Eric'
print(f'{leavingPerson=}')
# queue=deque(['John', 'Michael', 'Terry', 'Graham'])
print(f'{queue=}')
leavingPerson = queue.popleft()
# leavingPerson='John'
print(f'{leavingPerson=}')
# queue=deque(['Michael', 'Terry', 'Graham'])
print(f'{queue=}')


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
print(cubes)

"""
Deleting values from a list
"""
aList = [1, 2, 3]
aList.remove(3)
# [1, 2]
print(aList)
del aList[1]
# [1]
print(aList)

aList.clear()
# []
print(aList)

"""
Iterating
"""
# 0, 1, 2, 3, 4
for i in range(5):
    print(i)

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
print(cubes)
# Append the cube of 6
cubes.append(6 ** 3)
# [1, 8, 27, 65, 125, 216]
print(cubes)

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
aString = 'Kat'
# ['Bob, Dylan', 'K', 'a', 't']
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
print('list.sort(reverse=True) =>', letters)

# Sort in reverse order AND ignoring capital cases
letters = ['a', 'z', 'A', 'Z']
letters.sort(key=str.upper, reverse=True)
# ['z', 'Z', 'a', 'A']
print('list.sort(key=str.upper, reverse=True) =>', letters)

a = [4, 4.12, 4.5, 4.0000]
a = sorted(a, key=float)
# [4, 4.0, 4.12, 4.5]
print(a)


"""
Pop
Remove item at a given Index, or last item, and Return it.
"""
names = ["Jack", "Bro", "Spencer", "Dude"]
lastDude = names.pop();
# "Dude"
print(lastDude)
secondDude = names.pop(1)
# Bro
print(secondDude)


"""
Reverse
Remove all items from the list.
"""
# Works with mixed types
a = [4.1, "3.4", 2.1, 1, -2.1]
a.reverse()
# [-2.1, 1, 2.1, '3.4', 4.1]
print(a)

a = [1, 3, 4, 5, -4, 4.3]
a.reverse()
# [4.3, -4, 5, 4, 3, 1]
print(a)


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
try:
    # Throws ValueError
    aList.remove(4)
except ValueError as ve:
    print('A ValueError was thrown!', ve)


"""
Del
Removes an item from a list given its index instead of its value.
This differs from the pop() method which returns a value.
The del statement can also be used to remove slices from a list or clear the 
entire list.

"""
aList = [-1, 1, 333, 333, 1234.5]
del aList[0]                    # -1 is removed
# aList=[1, 333, 333, 1234.5]
print(f'{aList=}')
del aList[1:3]                  # 333 and 333 are removed
# aList=[1, 1234.5]
print(f'{aList=}')
del aList[:]
# aList=[]
print(f'{aList=}')


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
Index
Given a value, Return its index in the list
"""
# NOTE: This list has a duplicate
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'banana']
# Find index of first 'banana'
ind = fruits.index('banana')
# ind=3
print(f'{ind=}')
# Find index of second 'banana' - search starting from position 4
ind = fruits.index('banana', 4)
# ind=5
print(f'{ind=}')

# NOTE: Return all occurrences of 'banana'; one solution is list comprehension
allInd = [i for i, x in enumerate(fruits) if x == "banana"]
# allInd=[3, 5]
print(f'{allInd=}')

# another solution using loop & if
allInd = []
for i in range(len(fruits)):
    if fruits[i] == 'banana':
        allInd.append(i)
# allInd=[3, 5]
print(f'{allInd=}')


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
# 'Python'
print(word[:2] + word[2:])
# 'Python'
print(word[:4] + word[4:])

# prints '', because end index is exclusive, so the 2 index have no overlap
print(word[1:1])

# list[index] where index is too large will result in an IndexError:
try:
    # the word only has 6 characters
    word[42]
except IndexError as ie:
    print('IndexError is thrown!', ie)

# However, slice indexes are handled "gracefully" if out of bounds
# returns 'hon'
print(word[-3:23])
# returns 'ython'
print(word[1:30])
# returns 'n'
print(word[-1:19])
# returns 'Pyt'
print(word[-6:3])
# Consider this table of indices
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
#  -6  -5  -4  -3  -2  -1
#   0   1   2   3   4   5
# If end index for slice is GREATER than len(word), then return word[start:]
# start index also rolls over like this table shows if it becomes negative

allSquares = [1, 4, 9, 16, 25]
# return new list; [9, 16, 25], -3 means 'last 3'
sublist = allSquares[-3:]
# no start/end indices provided returns the whole list
sameList = allSquares[:]

# Lists also support operations like concatenation:
allSquares = [1, 4, 9]
# [1, 4, 9, 36, 49]
print(allSquares + [36, 49])

# Assignment to slices is also possible,
# NOTE: this can change the size of the list/clear it:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
# prints ['a', 'b', 'C', 'D', 'E', 'f', 'g']
print(letters)
# now remove them
letters[2:5] = []
# prints ['a', 'b', 'f', 'g']
print(letters)
# clear the list by replacing all the elements with an empty list
letters[:] = []
# prints "" (nothing)
print(letters)



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


# ****************************************************************************
# *                          Arithmetic with lists                           *
# *   # Note you cant 'subtract' OR 'divide' lists, gives an error           *
# ****************************************************************************
"""
Addition
"""
list1 = ["car", "bus", "bike"]
list2 = [3, 9]
# NOTE: APPENDS list2 items after list1 items
list3 = list1 + list2
# ['car', 'bus', 'bike', 3, 9]
print(list3)

"""
Multiplying
"""
list1 = [1, 2]
# [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(list1 * 5)

list1 = ["dog", "cat"]
# ['dog', 'cat', 'dog', 'cat', 'dog', 'cat']
print(list1 * 3)

try:
    list1 = [1, 3]
    list2 = ["ham", "pam"]
    print(list1 * list2)
except TypeError as error:
    # TypeError: can't multiply sequence by non-int of type 'list'
    print(error)
























# ****************************************************************************
# *                          List Comprehensions                             *
# *                                                                          *
# ****************************************************************************
# """List Comprehensions"""
# A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
#
# For example, this listcomp combines the elements of two lists if they are not equal:
# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]		# prints [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
# and it’s equivalent to:
# combs = []
# for x in [1,2,3]:
# 	for y in [3,1,4]:
# 		if x != y:
# 			combs.append((x, y))
# combs														# prints [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
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


""" Order of operation is paramount: """
list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4]		    # NOTE: += means plus THEN equals
# [5, 4, 3, 2, 1, 1, 2, 3, 4]
print(list1)
# [5, 4, 3, 2, 1, 1, 2, 3, 4]
print(list2)

list1 = [5, 4, 3, 2, 1]
list1 = list1 + [1, 2, 3, 4]    # NOTE: plus
list2 = list1					# NOTE: then equals
# [5, 4, 3, 2, 1, 1, 2, 3, 4]
print(list1)
# [5, 4, 3, 2, 1, 1, 2, 3, 4]
print(list2)				    # both are same as above

list1 = [5, 4, 3, 2, 1]
list2 = list1				    # NOTE: You did the equals before the plus
list1 = list1 + [1, 2, 3, 4]
# [5, 4, 3, 2, 1, 1, 2, 3, 4]
print(list1)
# [5, 4, 3, 2, 1]
print(list2)				    # list2 are different from above
