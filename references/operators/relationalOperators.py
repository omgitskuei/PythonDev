# Comparison / Relational Operators

# In[1]: EQUALS:
#"==" tests to see if two operands are equal, if so, True
a=1
b=2
print("#1", a==b)		# prints False

# In[2]: NOT EQUALS:
#"!=" is the opposite of "==", means IS NOT EQUAL.
# NOTE: Alternatively spelt "<>" in Python 2 but NOT existent in 3+.
a=1
b=2
print("#2", a!=b)		# prints True

# In[3]: GREATER/LESS THAN (OR EQUALS):
#>, <, >=, and <= for greater, less than, etc
a=1
b=2
print("#3", a>b)

# In[4]: Compound comparisons:
#You can link many variables together, more than 2
print(4 <= 6)			# prints True
print(6 > 7)			# prints False
print("#4", 4 <= 6 > 7) # so True AND False, prints False
