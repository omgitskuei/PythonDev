# -*- coding: utf-8 -*-
"""
in & not in operators
Determines whether a value is or isn’t in a list

Created on Thu May 27 17:13:20 2021
@author: omgitskuei
"""

'howdy' in ['hello', 'hi', 'howdy', 'heyas']
#True

greetings = ['hello', 'hi', 'howdy', 'heyas']
'cat' in greetings
#False

'howdy' not in greetings
#False

'cat' not in greetings
#True


"""
The following program lets the user type in a pet name
and then checks to see whether the name is in a list of pets
Source: Automate the boring stuff with Python, P.87
"""
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')


