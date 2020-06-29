# In[194]: Bitwise Operators

# AND; a&b means both must be 1's to be True.
# OR; a|b means AT LEAST one must be 1's to be True.
# NOT OR; a^b means EXACTLY one must be 1's to be True. Aka, a and b must be different 0 and 1 or 1 and 0 to be True.
print("a", "b", "&", "|", "^")
a = 0; b = 0
print(a, b, a&b, a|b, a^b)
a = 0; b = 1
print(a, b, a&b, a|b, a^b)
a = 1; b = 1
print(a, b, a&b, a|b, a^b)
a = 1; b = 0
print(a, b, a&b, a|b, a^b, "\n") #\n means "new line", or Enter

#To format a int into binary, use "{index:b}".format(variable).
a=60
print("a=60,", "{0:b}".format(a))
#If you see >> or <<, eg. a>>2, it means you convert to binary, add <<x or  subtract >>x (x number of) zeros from the back.
print("a<<2, ", "{0:b}".format(a<<1), "a=","{}".format(a<<1))
print("a<<2, ", "{0:b}".format(a<<2), "a=","{}".format(a<<2))
print("a<<3, ", "{0:b}".format(a<<3), "a=","{}".format(a<<3))
print("a=60,", "{0:b}".format(a))
print("a>>1, ", "{0:b}".format(a>>1), "a=","{}".format(a>>1))
print("a>>2, ", "{0:b}".format(a>>2), "a=","{}".format(a>>2))
print("a>>3, ", "{0:b}".format(a>>3), "a=","{}".format(a>>3), "\n")

#You can do math with binary:
#(Step 1) Convert both numbers into binary
#(Step 2) Look at the operator (&, |, ^) and apply their logic to it...
#    & - if both are 1's, then 1, else 0.
#    | - if at least one is 1, then 1, else 0.
#    ^ - if exactly one is 1, then 1, else 0.
print("60 in binary,", "{0:b}".format(60))
print("13 in binary,", "{0:b}".format(13))
print(60&13, "{0:b}".format(60&13)) #Note this is VERY DIFFERENT from "60 and 13"
print(60|13)
print(60^13)
