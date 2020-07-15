''' Dict '''
# Various ways of writing dict
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e				# returns True, mutable

''' SYNTAX - Declaring map'''
# constructor/declaring a dict (two different ways to declare):
# 1) its key-value pairs are separated by : colon (not = sign), surrounded by {}
dictionary = {"key":"a unique id for mapping", "chair":"a four-legged furniture one sits in"}
# 2) its key-value pairs are separated by = equals, surrounded by ()
dictionary = dict(one="1", two="2", three="3")			# overwrite

''' SYNTAX - Retrieving value'''
# Retrieve dict value using key
print(dictionary.get("key", "returnValueIfKeyNotFound"))		# returnValueIfKeyNotFound is optional, default value None
print(dictionary.get("one", "returnValueIfKeyNotFound"))		# prints 1, because 2nd declaration of dict overrode first one
print(id(dictionary))
# only matches KEYS
print(dictionary.get("1","not found"))						# prints 0 because "1" is a value, not keyword

# Another way of writing .get(key, valueIFNotFound)
thesaurus={"mean":"unkind", "welcoming":"likable", "sword":"blade"}
print(thesaurus["mean"])
# remember that the format of dict is always KEY:VALUE (key on left)
# because format is always KEY:VALUE, print(thesaurus["unkind"]) WILL NOT return "mean", because "unkind" is not a key
# print(thesaurus["unkind"])
print(thesaurus["welcoming"])
print(thesaurus["sword"])

# Python has a set of built-in methods that you can use on dictionaries.
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
