# -*- coding: utf-8 -*-
"""
List-To-String Function.

Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item.

For example, say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']

Return this string:
'apples, bananas, tofu, and cats'.

- P.102, Automating the boring stuff with Python Ed.2 (2015) by Al Sweigart
"""

# In[1]: Functions
def listToString(aList):
    """
    Convert a list to string.

    Convert a list into a string delimited with commas. The last comma has
    a " and" appended to it (to be grammatically correct).

    Parameters
    ----------
        aList (list[]): A list containing items of any type

    Returns
    -------
        aString (str): A string of list items delimited with ", {and}" commas
    """
    aString = ""
    for index in range(len(aList)):
        if(index != 0):
            if(index != len(aList)-1):
                # % operator: equivalent to aString = aString + ", "
                aString = "%s, " % (aString)
            else:
                aString = aString + (", and ")
        # append the list item, convert to type str if items are not type str
        if(type(aList[index]) == str):
            aString = aString + (aList[index])
        else:
            aString = aString + (str(aList[index]))
    print(aString)
    return aString

# In[2]: Main...
fruitList = ["banana", "mango", "apple"]
result = listToString(fruitList)
print(result)
# note, you can't concat int to str without type-casting with str(someInt)
numList = [1, 2, 3]
listToString(numList)