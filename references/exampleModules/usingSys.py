# -*- coding: utf-8 -*-

import sys

# sys.stdin.readline()
# The above snippet stores user input after pressing enter, stored as String.

def silly_age_joke():
    print('How old are you?')
    age =  int(sys.stdin.readline())    # converts string to int
    if  age >= 10  and  age <= 13:
        print('What is 13 + 49 + 84 + 155 + 97? A headache!')
    else:
        print('Huh?')

silly_age_joke()