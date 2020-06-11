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
print(aListOfSubjects[-1:1])	# prints 'Politics', 'Economics'.
