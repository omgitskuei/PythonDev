"""A Note on assignment and passing arguments to methods."""


# NOTE: The following snippet shows that variable 'arg' is NOT altered by method 'square'

from sys import getrefcount


def main():
    """Show that arg is not modified."""
    arg = 4
    print(f"Initial ID of arg =         {id(arg)}")
    square(arg)                                      # fails to alter arg
    #arg = square(arg)
    print(f"Post-changes ID of arg =    {id(arg)}")
    print(f"Value of arg =              {arg}")      # returns 4


def square(n):
    """Squares the argument n."""
    print(f"    Initial ID of n =       {id(n)}")
    n *= n
    print(f"    Post-changes ID of n =  {id(n)}")   # id is different here
    # return n


main()

'''
Python does not use pass by references (same ID at all 4 steps)
'''
# As the ID is different after altering it inside square(n), it means python
# does NOT treat supplied argument 'n' as a reference to an existing variable

'''
Python does not pass by value (different ID after passing argument into method)
'''
# As the ID is the same when init passing n into square, Python does NOT pass by value

'''
Python does Pass By Assignment (each function argument becomes a variable to which the passed value is assigned)
'''

'''
If the assignment target is an identifier, or variable name, then this name is bound to the object.
For example, in x = 2, x is the name and 2 is the object.
If the name is already bound to a separate object, then it’s re - bound to the new object.
For example, if x is already 2 and you issue x = 3, then the variable name x is re - bound to 3.
All Python objects are implemented in a particular structure.
One of the properties of this structure is a counter that keeps track of how many names have been bound to this object.

Note: This counter is called a reference counter because it keeps track of how many references, or names, point to the same object.

Let’s stick to the x = 2 example and examine what happens when you assign a value to a new variable:

    If an object representing the value 2 already exists, then it’s retrieved. Otherwise, it’s created.
    The reference counter of this object is incremented.
    An entry is added in the current namespace to bind the identifier x to the object representing 2.
    This entry is in fact a key - value pair stored in a dictionary! A representation of that dictionary is returned by locals() or globals().

Now here’s what happens if you reassign x to a different value:

    The reference counter of the object representing 2 is decremented.
    The reference counter of the object that represents the new value is incremented.
    The dictionary for the current namespace is updated to relate x to the object representing the new value.

Python allows you to obtain the reference counts for arbitrary values with the function sys.getrefcount(). You can use it to illustrate how assignment increases and decreases these reference counters.
https://realpython.com/python-pass-by-reference/#understanding-assignment-in-python
'''

print("Before  assignment")
print(f"References to value_1: {getrefcount('value_1')}")
print(f"References to value_2: {getrefcount('value_2')}")
x = "value_1"
print("After   assignment")
print(f"References to value_1: {getrefcount('value_1')}")
print(f"References to value_2: {getrefcount('value_2')}")
x = "value_2"
print("After reassignment")
print(f"References to value_1: {getrefcount('value_1')}")
print(f"References to value_2: {getrefcount('value_2')}")
