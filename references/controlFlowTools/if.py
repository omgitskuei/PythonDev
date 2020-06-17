# NOTE: An if … elif … elif … sequence is a substitute for
# the switch or case statements found in other languages.

# NOTE: Short-hand if statement for single statements:
a = 3
b = 2
if a > b: print(a > b)	# prints True

# Example:
x = int(input("Please enter an integer: "))
if x < 0:
	x = 0
	print('Negative changed to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('Single')
else:
	print('More')
