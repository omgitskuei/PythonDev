# -*- coding: utf-8 -*-
"""
f-strings
Introduced in PEP 498, F-strings provide a concise and convenient way to
embed python expressions inside string literals for formatting.
It is also known as Literal String Interpolation.
To create an f-string, prefix the string with the letter “f”.
The syntax is f'{expression}' where the string content is inside the ''.
"""

# Concatenating strings
a="eggs"; b="toast"
debugStr = f'{a} and {b} are amazing.'
print(debugStr)

# Calculate numbers or pass numbers
passingNum = 4
debugStr = f'1+3 is [{passingNum}], and 1+4 is {1+4}.'
print(debugStr)

# Pass in dictionary values using keys
comedian = {"name": "Eric Idle", "age": 74}
print(f"The comedian is {comedian['name']}, aged {comedian['age']}.")
print(f'The comedian is {comedian["name"]}, aged {comedian["age"]}.')
# NOTE: that the dictionary key uses string too, but must use another symbol
# "" or '', because f-string is already using the other.

# Pass arrays and tuples using index
fruitsTuple = ("apple", "banana", "cherry")
print(f'{fruitsTuple[1]}s are not my favorite fruit.')
fruitsList = ["apple", "banana", "cherry"]
print(f'{fruitsList[1]}s are not my favorite fruit.')

# Short-hand print out variables for debugging.
aVar = "someText"
anotherVar = 1
lastVar = 41.44
print(f'{aVar=},{anotherVar=},{lastVar=}')
