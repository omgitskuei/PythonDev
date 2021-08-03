''' Syntax '''
# A tuple consists of a number of values separated by commas, for instance:
t = 12345, 54321, 'hello!'
# or
t = (12345, 54321, 'hello!')
print(t[0])			# prints 12345
print(t)				# prints (12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)						# prints (12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable:
# t[0] = 88888
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

'''Difference between List and Tuple'''
# Similarities
# Both lists and tuples are sequence data types that can store a collection of items.
# Each item stored in a list or a tuple can be of ANY data type.
# And you can also access any item by its index.

# Differences
# lists are mutable whereas tuples are immutable.
# Eg.
aList = ["apples", "bananas", "oranges"]
aList[0] = "berries"			# we change the value of aList[index#1]
aList							# prints ['berries', 'bananas', 'oranges']
aTuple = ("apples", "bananas", "oranges")

# aTuple[0] = "berries"			# we try to change the value of aTuple[index#1]
# Traceback (most recent call last):
#   File "", line 1, in
# TypeError: 'tuple' object does not support item assignment

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v  # prints ([1, 2, 3], [3, 2, 1])


# Like lists, tuples can hold values of different types
tup1 = ("Python", 131, 3456.23, "beep")
# Similarly, tuples can also be empty
tup2 = ()
# But if there's ONLY ONE value, a comma MUST follow
tupOnly1 = ("Wow",)
# Calling a value from a tuple using index MUST USE [], same as list, NOT ().
# tuple1(2) would be an error.
print(tup1[2])
# A tuple is a sequence of immutable objects
# NOTE: Unlike list, you can't make direct edits to values inside the tuple.
# ^ tuple1[2]=23.3456 would be an error.
# We can add to a tuple using +, but its ID will be different, hence Immutable
print(tup1)
print("old tuple1 ID", id(tup1))
tup1 = tup1 + ("AI", "exp")
print(tup1)
print("new tuple1 ID", id(tup1))
# You can actually hold a list as one of the values of a Tuple
tup3 = ("Python", [22, 1, 2], 77)
# And you can also call a value from the list inside the tuple
print(tup3[1][2])
# Why do you want to use Tuple over List? Tuple doesnt let people make changes as easily. Useful for exams.
