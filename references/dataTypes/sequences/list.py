# Creating Lists
# Lists are created by enclosing elements within [square] brackets and each item is separated by a comma:
# Duplicates are allowed
aListOfSubjects = ['Economics', 'Maths', 'English', 'Biology', 'Maths', 'Politics']

# Retrieving Elements
# To access elements of a list, we use Indexing.
print(aListOfSubjects[0])	# prints 'Economics'
print(aListOfSubjects[3]) 	# prints 'Biology'

# But indexes can be negative too. Negative indexes return values from the end of the list.
print(aListOfSubjects[-1])	# prints LAST element 'Politics'

# Slicing - return a range of elements between two positions in the lists; List_name[start : end].
# Note: end index is Exclusive

# NOTE: indexing returns the item WHILE slicing returns a NEW list
squares = [1, 4, 9, 16, 25]
>>> squares[0]
>>> squares[-1]	# returns item; 25
>>> squares[-3:]  		# returns new list; [9, 16, 25]

squares[:] # default indices together returns the whole list

# Lists also support operations like concatenation:
squares + [36, 49, 64]	# returns new list; [1, 4, 9, 16, 25, 36, 49, 64]


# NOTE: lists are a mutable type, i.e. can change their content
cubes = [1, 8, 27, 65]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
>>> cubes[3] = 64  # replace the wrong value
>>> cubes				# prints [1, 8, 27, 64]

# You can also add new items at the end of the list, by using the append() method
>>> cubes.append(125)  # add the cube of 5
cubes
cubes.append(6 ** 3)  # and the cube of 6
cubes


# Assignment to slices is also possible,
# NOTE: this can change the size of the list/clear it:
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters				# prints ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters 			# prints ['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters				# prints ['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters				#prints "" (nothing)


# NOTE: Built-in len() function applies to lists
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)		# prints 4


# NOTE: It is possible to nest lists (create lists containing other lists), for example:
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x 					# prints [['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]				# prints ['a', 'b', 'c']
>>> x[0][1]				# prints 'b'

print(aListOfSubjects[-1:1])	# prints 'Politics', 'Economics'.


# NOTE: Slice indices use defaults if omitted
# an omitted first index defaults to zero
# an omitted second index defaults to the size of the string being sliced.
>>> word = 'Python'


# NOTE: This means that s[:i] + s[i:] is always equal to s:
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
^ ??????????????????????????????????????????????????????

# Attempting to use an index that is too large will result in an error:
>>> word[42]  # the word only has 6 characters
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range


# NOTE: However, out of range slice indexes are handled gracefully when used for slicing:
>>> word[4:42]
'on'
# Consider this table of indices - out-of-bounds index wraps around word;
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
-6  -5  -4  -3  -2  -1
 0   1   2   3   4   5   6
 7   8   9   10  11  12  13
 14  15  16  17  18  19  20
 21  22  23  24  25  26  27
 28  29  30  31  32  33  34
 35  36  37  38  39  40  41

 a=[1, 2, 3, 4]
 print(2 in a)


"""Order of operation is paramount: See Below"""
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
list1 = list1 + [1, 2, 3, 4]	# NOTE: plus
list2 = list1					# NOTE: then equals
print(list1)
print(list2)				# both are same as above


"""Count matches"""
list1 = [5, 4, 3, 2, 1, 5,5,5,5,5,5]
list1.count(5)		# seven 5s


"""Other methods"""
list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.count(x)
Return the number of times x appears in the list.

list.sort(key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.


>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'

not all data can be sorted or compared. For instance, [None, 'hello', 10] doesn’t sort because integers can’t be compared to strings and None can’t be compared to other types.


Using Lists as Stacks (Last-In-First-Out)
To add an item to the top of the stack, use append().
To retrieve an item from the top of the stack, use pop() without an explicit index.

>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]


Using Lists as Queues (First-In-First-Out)
You can but lists aren't efficient for this.
While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
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
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
which, in turn, is the same as:

>>>
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]



The del statement
There is a way to remove an item from a list given its index instead of its value: the del statement. This differs from the pop() method which returns a value. The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice). For example:

>>>
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
