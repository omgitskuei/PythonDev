# In[1]: Triple quotes, syntax

# Use triple single or double quotes '''this''' to create strings that span more than 1 line. It prints Carriage returns/Enter.
dashedPageEnd='''--------------------------------------------------
''';						# the newline \n escape is equivalent to the Carriage return at the end of this string
a="""Hello world [Carriage Return here]
omg this is so long I must [an Enter here]
to continue writing!
""";
print(dashedPageEnd, a, dashedPageEnd);


# In[2]: Triple quotes, convention

#It is better to use """double-quotes""" than single because there's a convention PEP 257 for docstring convention
#... that prefers double-quotes.


# In[3]: blackslash for Enter

#can use \ backslash/rightslash to Enter and carry on next line
total = 'score1 \
     +score2 \
     +score3'
print(total)

#Don't need \ backslash if already inside brackets [], {}, ().
total = ["Sun", "Mon",
        "Tues", "Wedn"]
print(total)

# You Don't necessarily have to print or store it. a long triple quote string can be used as //comments
def triangleArea(base, height):
	'''Calculates area with passed params'''
	area = base * height / 2
	return area
triangleArea(3,5)
