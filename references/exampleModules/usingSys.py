"""
Using the Sys module.

The sys module contains functions that control the Python shell.

Here, we’ll look at how to use exit function, stdin and stdout objects,
and version variable.

Created on Sat Aug 29 10:01:06 2020.

@author: omgitskuei
"""
# -*- coding: utf-8 -*-


import sys

"""
[exit] function is a way of stopping the Python shell or console.
"""
sys.exit()


"""
[stdin] object (standard input) in sys module prompts user.
This object has a stdin.readline() function used to read a line of text.


It is similar to [input()] built-in function, but not the same:
    1) [input()] has an optional prompt parameter that will be displayed if
    the interpreter is running interactively. Eg. input("What is 1+1?")
    This leads to some overhead, even if the prompt is empty (the default).
    Conversely, if you do want a prompt, it may be faster than doing a
    [print()] before each readline call.
    2) [input()] strips off any newline from the end of the input.
    If you're going to strip that anyway, it's faster to let input do it for
    you, rather than doing sys.stdin.readline().strip().
    3) [input()] will raise an EOFError when you call it if there is no more
    input (stdin has been closed on the other end).
    sys.stdin.readline on the other hand will return an empty string at EOF
    , which you need to know to check for.
https://stackoverflow.com/questions/22623528/sys-stdin-readline-and-input-which-one-is-faster-when-reading-lines-of-inpu
    4) One of the differences between input and the readline function
    is that with readline, you can specify the number of characters to
    read as a parameter.
    5) Also
"""
userInput = sys.stdin.readline()
print(f"You entered {userInput}")
# [userInput] is stored as String
userInput2 = input("What's for dinner?")
print(f"You entered {userInput2}")
# Similar to above

v = sys.stdin.readline(13)
# Enter "He who laughs last thinks slowest"
print(v)
# He who laughs


"""
[sys.stdout] object can write messages to shell/console.
"""
sys.stdout.write("What does a fish say when it swims into a wall? Dam.")
# What does a fish say when it swims into a wall? Dam.


"""
[sys.version] object print python version information
"""
print(sys.version)
# 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)]


def silly_age_joke():
    """
    Print joke if user input is between 10 and 13.

    Parameters
    ----------
        age: int
            A whole number to determine which print to use.

    Returns
    -------
        None
    """
    age = int(input("How old are you?"))
    # converts string to int
    if age >= 10 and age <= 13:
        print('What is 13 + 49 + 84 + 155 + 97? A headache!')
    else:
        print('Huh?')


# run function
silly_age_joke()
