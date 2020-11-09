# -*- coding: utf-8 -*-
"""
Program name: Notes on Default Argument values in Python.

Summary: Notes on syntax, usage, and example snippets of default arguments
Created on: Sat Oct 24 11:37:09 2020
@author: omgitskuei (Github)
"""

def prompt_for_yes_no(promptMsg, retries=4, reminder='Please try again!'):
    """Prompt user for yes or no - retry if user input is not yes or no.

    Keyword Arguments:
    -----------------
    promptMsg -- a String, what message to print and show user during prompt.
    retries -- how many numbers of retries does the user get (default 4)
    reminder -- print msg if input isn't yes or no (default Please try again!)
    """
    while True:
        ok = input(promptMsg)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# This function can be called in several ways:
# 	giving only the mandatory argument:
prompt_for_yes_no('Do you really want to quit?')
#	giving one of the optional arguments:
prompt_for_yes_no('OK to overwrite the file?', 2)
#	or even giving all arguments:
prompt_for_yes_no('OK to overwrite the file?', 2, 'Come on, only yes or no!')




# NOTE: ^ , at the point of function definition in the defining scope
i = 5
def test_arg_value(arg=i):  # here, arg value is set to i
    """Notice default value is evaluated only once."""
    i = 6                       # i is changed but arg isn't set again
    args = 6
    print(arg)
test_arg_value()				# prints 5, NOT 6


'''using mutables as default values'''

# NOTE: Because the default is only evaluated ONCE on Define, a default value could end up
# ... calling the same mutable object across subsequent calls
def f(a, L=[]):		# this function's L argument is SET as an empty list ONLY ONCE
    L.append(a)
    return L
# Even though it says the default value is an Empty list, python 'remembers' the list and its elements
print(f(1))			# prints [1]
print(f(2))			# prints [1, 2]
print(f(3))			# prints [1, 2, 3]

# Below is a way to 'reset' the default value to an empty list, using immutable None
def f(a, L=None):
    if L is None:	# this is always true
        L = []
    L.append(a)
    return L
print(f(1))			# prints [1]
print(f(2))			# prints [2]
# This also works with other immutables like Strings
def f(a, L="hi"):
    if L == "hi":	# this is always true
        L = []
    L.append(a)
    return L
print(f(1))			# prints [1]
print(f(2))			# prints [2]


'''Calling functions using keyword arguments'''

def cat(name, action="fart",color="black"):	# name doesn't have a default value
	print("The",color,"cat named",name,"did a",action)
# cat(loveInterest="Barack Obama")			# keyword arguments must match one of the param keywords
# ^ returns "TypeError: cat() got an unexpected keyword argument 'loveInterest'"
cat(name="James")
cat("James") 										# name is mandatory (and positionally sensitive)
# cat(action="sit","Bob")							# SyntaxError: positional argument follows keyword argument
													# NOTE: In a function call, keyword arguments must follow positional arguments.
# cat(action="sang")								# TypeError: cat() missing 1 required positional argument: 'name'
cat("Bob",action="sit")
cat("Tob",action="kick", color="rainbow")
cat("Rob",color="white",action="meow")				# NOTE: keyword arguments DO NOT care about position (amongst themselves)
cat("Rob","white","meow")							# params treated as positional w/o keywords
# ^ prints "The meow cat named Rob did a white"
# cat("Jay", action="think", action="think twice")	# NOTE: No argument may receive a value more than once.
