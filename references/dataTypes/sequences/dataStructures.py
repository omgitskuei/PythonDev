#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

"""List"""
aList = [1,2,3,3]

"""Tuple"""
aTuple = (1,2,3,3)

"""Set"""
aSet = {1,2,3,3}

aList, aSet, aTuple

"""Convert from String to Sequence of chars"""
aString = 'quux'

aList = list(aString)
# returns ['q', 'u', 'u', 'x']
print(aList)

aTuple = tuple(aString)
# returns ('q', 'u', 'u', 'x')
print(aList)

aSet = set(aString)
# returns {'x', 'u', 'q'} (duplicate removed)
print(aSet)