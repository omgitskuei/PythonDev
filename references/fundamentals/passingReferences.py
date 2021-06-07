# -*- coding: utf-8 -*-
"""
Passing References.

When a function is called, the values of the arguments are copied
to the parameter variables. For lists (and dictionaries), a copy of the
reference is used for the parameter.

To avoid mutating the original data, use py module copy - see below.
"""


# In[1]: Notice that eggs() doesn't have a return value, yet list spam is
# still appended a new item.
def eggs(someParameter):
    """Append a string 'Hello' to parameter someParameter of type list."""
    someParameter.append('Hello')
spam = [1, 2, 3]
# This is because It modifies the list in place, directly
eggs(spam)
# [1, 2, 3, 'Hello']
print(spam)


"""Even though spam and someParameter contain separate references, they
both refer to the same list. This is why the append('Hello') method call
inside the function affects the list even after the function call has returned.
Keep this behavior in mind: Forgetting that Python handles list and
dictionary variables this way can lead to confusing bugs."""
try:
    spam = (1, 2, 3)
    eggs(spam)
    # does not print this
    print(spam)
except AttributeError:
    # prints this
    print("AttributeError: 'tuple' object has no attribute 'append'")


"""
copy Module’s copy() and deepcopy() Functions.

Sometimes, you may not want changes in the original list or dictionary
value after using it as a function parameter.
"""
import copy
spam = ['A', 'B', 'C', 'D']
# In[1]: copy.copy() duplicates a mutable value (eg.list, dict), not a
# reference.
spamCopy = copy.copy(spam)
spamCopy[1] = 42
# ['A', 'B', 'C', 'D']
print(spam)
# ['A', 42, 'C', 'D'] - spamCopy references a different list from spam
print(spamCopy)

# In[2]: copy.deepcopy() duplicates a mutable value and also the value's items
# if the items are lists.
spam = [[1, 2, 3], ["a", "b", "c"]]
spamDeepCopy = copy.deepcopy(spam)
spamDeepCopy[0] = ["d", "e", "f"]
# [[1, 2, 3], ['a', 'b', 'c']]
print(spam)
# [['d', 'e', 'f'], ['a', 'b', 'c']]
print(spamDeepCopy)