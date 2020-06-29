# In[28]: Logical Operators
# To a boolean, any integar larger than 0 is "True"
print("#1", bool(1))
print("#2", bool(1 and 2)) #and, both need to be True to equal True
print("#3", bool(0 and 43)) #False and True = False
print("#4", bool(0 or 2)) #or, one needs to be True to equal True, False or True = True

# x and y; if x is False, then x, else y.
print("#5", 7 and 6) #x=7 is True (True aka >0), else y.
print("#6", 7 and 0) #x is True, else y.
print("#7", 0 and 1) #x is False, then x.
print("#8", 0 and 0) #x is True, else y.
# x or y; if x is False, then y, else x.
print("#9", 7 or 5) #x is True, else x.
print("#10", 7 or 87) #x is True, else x.
print("#11", 0 or 3) #x is False, then y.
print("#12", 0 or 0) #x is False, then y.
# not x; if x is false, then True, else False.
print("#13", not 3) #3 is  True, else False.

# FYI, all of these are considered FALSE;
#    - False
#    - None
#    - 0
#    - 0.0
#    - empty "", emptylist1[], empty(), emptydict1{}, emptyset()

# Remember that booleans can be compared to each other with And and Or.
print("TaF", True and False)
print("TaT", True and True)
print("FaF", False and False)

print("ToF", True or False)
print("ToT", True or True)
print("FoF", False or False)
