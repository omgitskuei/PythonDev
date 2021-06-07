# -*- coding: utf-8 -*-
"""
Assignment Operators.

When assigning values to a variable, sometimes the variable itself is used.
Assignment operators does this in short-hand form.

Assignment operator eg.:
    a = a + 1
    a += 1
    ^ both of the above equivalent

Automating the boring stuff with python Ed.2 by Al Sweigart calls assignment
operators 'augmented assignment operators'.

Augmented assignment statement | Equivalent assignment statement
    spam += 1   ==   spam = spam + 1
    spam -= 1   ==   spam = spam - 1
    spam *= 1   ==   spam = spam * 1
    spam /= 1   ==   spam = spam / 1
    spam %= 1   ==   spam = spam % 1
"""

# In[1]: Addition '+=':
#"b = b+a" can be written as "b += a", this can be repeatedly used.
a=2
b=3
b+=a;
print(b)		#b = 3+2 = 5
b+=a;
print(b)		#b = 5+2 = 7


# In[2]: Subtraction '-=', Multiplication '*=', Division '/=':
a=7
b=9
b-=a; 				# NOTE: Order of vars b-=a = b-a
print(b) 			# prints 2

a=3
b=2
b*=a; 				# (b*=a) = (b*a) = 2*3 = 6
print(b)

a=2
b=14
b/=a;
print(b) 			# NOTE: Order of vars (b/=a) = (b/a) = 14/2 = 7


# In[3]: Modulo %=:
# modulo returns remainder
a=3
b=8
b%=a;
print(b) 			# 8/3 = 2r2, b = b%a = 8%3 = 2


# In[4]: Power **=, Floor division //=:
b**=a; 				# b = b^a = 2^3
print(b) 			# prints 8

b//=a;				# b = b//a = 8//3
print(b) 	 		# prints 2 (regular division wouldve given you 2.6667)


# In[5]: Multiplying a list:
bacon = ['Zophie']
bacon *= 3
# ['Zophie', 'Zophie', 'Zophie']
bacon
