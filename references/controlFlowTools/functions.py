# Defining Functions

# The keyword def introduces a function definition
# It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line, and must be indented.

# The first statement of the function body can optionally be a string literal; this string literal is the function’s documentation string, or docstring. There are tools which use docstrings to automatically produce online or printed documentation, or to let the user interactively browse through code; it’s good practice to include docstrings in code that you write, so make a habit of it.

# We can create a function that writes the Fibonacci series to an arbitrary boundary:
def fibonnaci(n):    							# def [functionName]([parameters])
	"""Print a Fibonacci series up to n."""		# docstring
	a, b = 0, 1
	# count = 0
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
		# count = count+1
	# print('count =',count)
# Now call the function we just defined:
fibonnaci(2000)		# prints 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597


# NOTE: You can rename functions
fibonnaci
f = fibonnaci
f(100)				# prints 0 1 1 2 3 5 8 13 21 34 55 89


# Even functions without a return statement do return a value, albeit a rather boring one. This value is called None (it’s a built-in name). Writing the value None is normally suppressed by the interpreter if it would be the only value written. You can see it if you really want to using print():

fibonnaci(0)
print(fibonnaci(0))	# prints None
print(None)


# It is simple to write a function that returns a list of the numbers of the Fibonacci series, instead of printing it:
def fib2(n):  # return Fibonacci series up to n
	"""Return a list containing the Fibonacci series up to n."""
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)    # see below
		a, b = b, a+b
	return result

f100 = fib2(100)    # call it
f100                # prints [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# result.append(a) calls a method of the list object result. A method is a function that ‘belongs’ to an object and is named obj.methodname, where obj is some object (this may be an expression), and methodname is the name of a method that is defined by the object’s type. Different types define different methods. Methods of different types may have the same name without causing ambiguity. (It is possible to define your own object types and methods, using classes) The method append() shown in the example is defined for list objects; it adds a new element at the end of the list. In this example it is equivalent to result = result + [a], but more efficient.

# NOTE: Different ways of defining Functions
# below function ask_ok is
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        userResponse = input(prompt)
        if userResponse in ('y', 'ye', 'yes'):
            return True
        if userResponse in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
# This function can be called in several ways:
# giving only the mandatory argument:
ask_ok('Do you really want to quit?')
# giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
# or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# # NOTE: This example also introduces the in keyword. This tests whether or not a sequence contains a certain value.
