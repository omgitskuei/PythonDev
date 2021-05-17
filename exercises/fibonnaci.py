# Fibonacci series [the sum of two elements defines the next]:
a, b = 0, 1		# multiple assignment
while a < 10:
	# loop body is indented: indentation is Python’s way of grouping statements
	print("a",a)	# See below

	# NOTE: expressions on the right are ALL evaluated BEFORE any assignments on the left take place
	# right-hand side expressions are evaluated from the left to the right

	# a, b = b, a+b
	# print("a",a,"b",b)

	b, a = a+b, b
	print("a",a,"b",b)
	# In[10] and In[13] are equivalent

# so, In[10] uses 'old' values when doing a = b; a = b = 2, NOT 3, even though b = a+b = 1+2 = 3
