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


# sys.stdin.readline()
# The above snippet stores user input after pressing enter, stored as String.


def silly_age_joke():
    """
    Illustrating a public function with.

    sad
    """
    print('How old are you?')
    age = int(sys.stdin.readline())
    # converts string to int
    if age >= 10 and age <= 13:
        print('What is 13 + 49 + 84 + 155 + 97? A headache!')
    else:
        print('Huh?')


silly_age_joke()
