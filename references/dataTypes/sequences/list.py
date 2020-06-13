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
