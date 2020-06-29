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
