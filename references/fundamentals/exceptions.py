''' Exceptions '''
# There's two kinds of errors;
# 1) syntax (parsing errors)
# 2) exceptions (run time errors)

''' Exceptions, try, else, finally SYNTAX '''
try:
	print(hi)				# hi not defined
except NameError:
	print("NameError: You didn't define something!")
else:
	print("welp")
finally:
	print("Always execute this")

''' Read More '''
# Python already comes with premade exceptions, which I can read about at docs.python.org/3/library/exceptions.html
# SyntaxError, ZeroDivisionError, etc
