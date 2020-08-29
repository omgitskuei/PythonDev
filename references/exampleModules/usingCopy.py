"""
Using the Copy module.

The copy module contains functions for creating copies of objects.

Module Copy can also copy a list of objects.

NOTE: Using copy.copy(), Changes to the original list WILL affect the copied
list.
NOTE: Using copy.copy(), New objects added to the original list WILL NOT affect
the copied list.

Using copy.deepcopy(), you can copy a new list, AND copy items inside the
original list.

Created on Sat Aug 29 10:01:06 2020.

@author: omgitskuei
"""

# -*- coding: utf-8 -*-

import copy


class Animal:
    """
    Suppose we have an Animal class with a constructor _init_.

    An example object.

    Parameters
    ----------
        species: string
        number_of_legs: int
        color: string

    Returns
    -------
        Animal object
    """

    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color


"""
Copying an object
"""
# Create a new object
harryTheHippo = Animal("hippo", 4, "pink")
# Create a copy
johnTheHippo = copy.copy(harryTheHippo)
print(f"Harry the Hippo's color =  {harryTheHippo.color}")
# pink
print(f"John the Hippo's color = {johnTheHippo.color}")
# pink


"""
Copying a list of objects
"""
# Create a new list of animals
harry = Animal('hippogriff', 6, 'pink')
carrie = Animal('chimera', 4, 'green polka dots')
newList = [harry, carrie]
# Copy list of animals
copiedList = copy.copy(newList)
print(f"First Animal in list's specie = {copiedList[0].species}")
# hippogriff
print(f"Second Animal in list's specie = {copiedList[1].species}")
# chimera


"""
NOTE: copy.copy() - The function makes a 'shallow' copy.

1) Changing objects in to the original list WILL affect the copied objects
    in the copied list.
    The copied list is created containing the same objects as the original
    list - the copied list is created without its own new objects.

2) Adding new objects to original list WILL NOT add new objects to the copied
    list.
"""
# Change first animal in new list
newList[0].species = 'ghoul'
print(f"newList[0]'s species = {newList[0].species} {id(newList[0])}")
# ghoul
print(f"copiedList[0]'s species = {copiedList[0].species} {id(copiedList[0])}")
# ghoul
# NOTE: IDs are the same

# Add a new object to the first list
sally = Animal('dog', 4, 'blue')
newList.append(sally)
print(len(newList))
# 4
print(len(copiedList))
# 3

"""
Deepcopy a list
We get a new list complete with copies of all of its objects.
As a result, changes to one of our original Animal objects won’t affect the
objects in the new list.

"""
# DeepCopy a list (items are separate objects)
newNewList = copy.deepcopy(newList)
# Change an item in original
newList[0].species = 'dragon'
print(newList[0].species)
# dragon
print(newNewList[0].species)
# ghoul
# the copied list doesn’t change
