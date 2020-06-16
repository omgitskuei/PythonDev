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
aListOfSubjects = ['Economics', 'Maths', 'English', 'Biology', 'Maths', 'Politics']
print(aListOfSubjects[0:2])	# prints 'Economics', 'Maths'.

# Lists might contain items of different types, but usually the items all have the same type.
aMixedList = ['Socks', 1, "Foot"]
aMixedList


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
