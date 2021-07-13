# There are four collection data types in the Python programming language:

# Dictionary is a collection which is unordered, changeable and indexed. No
# duplicate members.

#When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

# List is a collection which is ordered and changeable.
aList = [1,2,3,3]

# Tuple is a collection which is ordered and unchangeable (READ ONLY).
aTuple = (1,2,3,3)

# Set is a collection which is unordered and unindexed. No duplicate members.
aSet = {1,2,3,3}

"""Convert from String to Sequence of chars"""
aList = list('quux')
# returns ['q', 'u', 'u', 'x']
print(aList)

aTuple = tuple('quux')
# returns ('q', 'u', 'u', 'x')
print(aList)

aSet = set('quux')
# returns {'q', 'u', 'x'} (duplicate removed)
print(aSet)