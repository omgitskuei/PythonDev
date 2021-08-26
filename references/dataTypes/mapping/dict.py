# -*- coding: utf-8 -*-
'''
Dict
A dictionary ('Dict') is a collection of many items.
Each item is a pair of data - key, value- where key
is the index used to return value from the Dict.

A dictionary is typed with braces, {}.
myCat = {'name':'Gustav', 'age':5}
print(myCat[name]) # 'Gustav'

Keys doesn't have to be string, and can be any number.

Dicts are unordered, and can be compared for Equality
like lists, but return true as long as each share the
same items.

'''
# In[1] - Various ways of writing dict
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)]) # dict(list of tuples)
e = dict({'three': 3, 'one': 1, 'two': 2})

# comparing dicts, doesn't check items order
print(a == b == c == d == e)    # True

# In[2] Declaring a dict
dictionary = {"key":"metal thing", "chair":"furniture"}
numbers = dict(one="1", two="2", three="3")

# Retrieve dict value using key
print(numbers.get("key", "notFound"))		# prints notFound, notFound string is optional, default value None
print(numbers.get("one", "returnValueIfKeyNotFound"))		# prints 1, because 2nd declaration of dict overrode first one
print(numbers.get("1","notFound"))						# prints 0 because "1" is a value, not keyword
# Another way of writing .get(key, valueIFNotFound)
print(numbers['three'])

print("omg" in numbers)    # False

# In[3] Retrieving all keys, values, or pairs
spam = {'color': 'red', 'age': 42}
for k in spam:             # if unspecified, returns k => keys
    print(k)
# color
# age
for v in spam.values():
    print(v)
# red
# 42
for k in spam.keys():
    print(k)
# color
# age
for i in spam.items():    # note: returns tuples
    print(i)
# ('color', 'red')
# ('age', 42)
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))
# Key: age Value: 42
# Key: color Value: red

dictKeysAsList = list(spam.keys())    # spam.keys() returns dict_keys obj
dictKeysAsList.sort()                 # dict_keys obj can't be sorted
print(dictKeysAsList)

print('color' not in spam.keys())
# False

# In[4] Set a default value for a key if that key
# doesn't already have a value.
spam = {'name': 'Pooka', 'age': 5}

spam.setdefault('color', 'black')
# returns 'black'

print(f'{spam=}')
# {'color': 'black', 'age': 5, 'name': 'Pooka'}

spam.setdefault('color', 'white')
# returns 'black' - not changed already a key named 'color'.

print(f'{spam=}')
# {'color': 'black', 'age': 5, 'name': 'Pooka'}

# In[5] Python has a set of built-in methods that you can use on dictionaries.
	# get()			Returns the value of the specified key
	# pop()			Removes the element with the specified key
	# fromkeys()	Returns a dictionary with the specified keys and value
	# keys()		Returns a list containing the dictionary's keys
	# values()		Returns a list of all the values in the dictionary
	# clear()		Removes all the elements from the dictionary
	# copy()		Returns a copy of the dictionary
	# items()		Returns a list containing a tuple for each key value pair
	# popitem()		Removes the last inserted key-value pair
	# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
	# update()		Updates the dictionary with the specified key-value pairs
