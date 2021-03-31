# Getting the Data Type
# You can get the data type of any object by using the type() function:
x = 5
print(type(x))

# In Python, the data type is set when you assign a value to a variable:
x = "Hello World"	# str
x = 20	# int
x = 20.5	# float
x = 1j	# complex
x = ["apple", "banana", "cherry"]	# list
x = ("apple", "banana", "cherry")	# tuple
x = range(6)	# range
x = {"name" : "John", "age" : 36}	# dict
x = {"apple", "banana", "cherry"}	# set
x = frozenset({"apple", "banana", "cherry"})	# frozenset
x = True	# bool
x = b"Hello"	# bytes
x = bytearray(5)	# bytearray
x = memoryview(bytes(5))	# memoryview

# If you want to specify the data type, you can use the following constructor functions:
x = str("Hello World")	# str
x = int(20)	# int
x = float(20.5)	# float
x = complex(1j)	# complex
x = list(("apple", "banana", "cherry"))	# list
x = tuple(("apple", "banana", "cherry"))	# tuple
x = range(6)	# range
x = dict(name="John", age=36)	# dict
x = set(("apple", "banana", "cherry"))	# set
x = frozenset(("apple", "banana", "cherry"))	# frozenset
x = bool(5)	# bool
x = bytes(5)	# bytes
x = bytearray(5)	# bytearray
x = memoryview(bytes(5))	# memoryview

# NOTE: typecasting will work between string and numerics
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# More examples of typecasting
age = '10'
converted_age = int(age)
age = 10
converted_age = str(age)
age = '10.5'
converted_age = float(age)
print(converted_age) # 10.5

# Example of typecasting with errors
age = '10.5'
converted_age = int(age)
'''Traceback (most recent call last):
    File "<pyshell#35>", line 1, in <module>
    converted_age = int(age)
    ValueError: invalid literal for int() with base 10: '10.5' '''

# NOTE: Multiple assignment can be different TYPES
# fyi; a, b, c = "Kuei", 26, "Taiwan".
a, b, c, d, e="hello", "my", "age", "is", 2
print(a, b, c, d, e)

