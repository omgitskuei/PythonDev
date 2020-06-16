# There are three numeric types in Python:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# To verify the type of any object in Python, use the type() function:
print(type(x))
print(type(y))
print(type(z))

# Int, or integer, is a WHOLE number, positive or negative, without decimals, of UNLIMITED length.
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

# Float, or "floating point number" is a number, positive or negative, containing one or more DECIMALS.
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

# Complex numbers are written with a "j" as the imaginary* part:
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

# Type Conversion
# NOTE: CANNOT convert complex numbers into another number type.
x = 1    # int
y = 2.8  # float
z = 1j   # complex
# convert int to float:
a = float(x)
# convert float to int:
b = int(y)
# convert int to complex:
c = complex(x)
print(a)			# prints 1.0
print(b)			# prints 2
print(c)			# prints (1+0j)
print(type(a))		# prints class 'float'
print(type(b))		# prints class 'int'
print(type(c))		# prints class 'complex'
# convert float to complex???
# long numerics type???




# Random Number
# Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers:
# Import the random module, and display a random number between 1 and 9:
import random
print(random.randrange(1, 10)) # NOTE: end-range (in this case 10) is exclusive
