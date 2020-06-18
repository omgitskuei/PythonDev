# Arithmetic Operators:

# In[1]: Modulo:
# A percent sign % is the "modulo operator", this returns the remainder of a division
# Eg. 31 % 7 = 3, because 7 goes into 31 four times for 28, and 31-28=3.
remainder=17%6;
print(remainder) 	# equals 5, because 6*2=12, 17-12=remainder 5

remainder=10%2;
print(remainder) 	# equals 0, 10/2=5r0

# In[2]: Powers:
# Also found in dataTypes > numerics > powers.py
# '**' two multiple symbols are for a power relationship (squared, cubed, etc)
squared=9**2;
print(squared) 		# equals 81, 9**2=9^2=9*9=81

# In[3]: Floor Division:
# '//' two division symbols are for floor division, where division between two numbers is done but numbers after the decimal are ignored.
# NOTE: floor division resulting in a negative answer is still rounded down
x = -9//2;
print("-9//2=", x)	# NOTE: equals -5, not -4

x = 4.0 // 2.0;		# NOTE: Floats can be used with // too.
print("4//2=", x)	# 4/2 and 4//2 both = 2 because either way both have no decimals

x = 9 // 2;
print("9//2", x)	# 9/2 is 4.5, while 9//2=4
