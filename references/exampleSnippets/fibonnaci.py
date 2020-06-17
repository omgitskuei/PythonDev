# Fibonacci series [the sum of two elements defines the next]:
a, b = 0, 1		# multiple assignment
while a < 10:
	# loop body is indented: indentation is Python’s way of grouping statements
     print(a)	# See below
	 # NOTE: expressions on the right side are all evaluated first before any
	 # assignments on the left take place
	 # right-hand side expressions are evaluated from the left to the right
     a, b = b, a+b
