Python Variables
In Python, variables are created when you assign a value to it:

Example
Variables in Python:

x = 5
y = "Hello, World!"

Python has no command for declaring a variable - though there is a way to specify the type;
If you want to specify the data type, you can use the following constructor functions:
x = str("Hello World")	str

A variable is created the moment you first assign a value to it.
Variables do not need to be declared with any particular type.

Variables can even change type after they have been set;
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
Example
#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"

Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

To combine both text and a variable, Python uses the + character:
x = "awesome"
print("Python is " + x)

For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

If you try to combine a string and a number, Python will give you an error:
x = 5
y = "John"
print(x + y) # this will print out error message


Create a global variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

Also, use the global keyword if you want to change a global variable inside a function.
To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
