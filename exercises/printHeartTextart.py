# -*- coding: utf-8 -*-
"""
Print Heart Textart.

Write a function that takes a list of lists of type str (list[list[str]])
and print out textart with it.

For example:
Say each item of the inner lists is a one-character string, like this:
grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

From grid, the function should print the image:
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

Hint:
----
You will need to use a loop in a loop in order to print grid[0][0],
then grid[1][0], then grid[2][0], and so on, up to grid[8][0].
This will finish the first row, so then print a newline.
Then your program should print grid[0][1], then grid[1][1], then grid[2][1],
and so on. The last thing your program will print is grid[8][5].
Also, remember to pass the end keyword argument to print() if you
don’t want a newline printed automatically after each print() call.

- P.103, Automating the boring stuff with Python Ed.2 (2015) by Al Sweigart
"""

# Notice that the grid of data given has the heart in the WRONG ORIENTATION
grid = [
    ['.', '.', '.', '.', '.', 'R'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'L']
]

def printTextart(theGrid):
    """
    Print grid (a list of lists) as textart (without spaces and [] brackets).

    Convert each list into a string. Append newline.
    Repeat for each list.

    Parameters
    ----------
        aList (list[list]): A list containing items of type list[str]

    Returns
    -------
        NONE
    """
    totalRows = len(theGrid)
    totalCols = len(theGrid[0])
    # 9
    # print(totalRows)
    # 6
    # print(totalCols)

    '''Prints list of lists'''
    print("---Prints list of lists---")
    for rowNum in range(0, totalRows, 1):
        aString = ""
        for colNum in range(0, totalCols, 1):
            aString = aString + theGrid[rowNum][colNum]
        print(aString)
    print()

    '''Prints heart (rotate picture clockwise 90 degrees)'''
    print("---Prints heart (rotate picture clockwise 90 degrees)---")
    # range function syntax: range(start, end, step)
    for colNum in range(0, totalCols, 1):
        aString = ""
        for rowNum in range(totalRows-1, -1, -1):
            aString = aString + theGrid[rowNum][colNum]
        print(aString)
    print()

    '''Prints heart (rotate picture clockwise, and flipped)'''
    print("---Prints heart (rotate picture clockwise, and flipped)---")
    for colNum in range(0, totalCols, 1):
        aString = ""
        for rowNum in range(0, totalRows, 1):
            aString = aString + theGrid[rowNum][colNum]
        print(aString)
    print()

    '''Prints heart (rotate picture anti-clockwise 90 degrees)'''
    print("---Prints heart (rotate picture anti-clockwise 90 degrees)---")
    # range function syntax: range(start, end, step)
    for colNum in range(totalCols-1, -1, -1):
        aString = ""
        for rowNum in range(0, totalRows, 1):
            aString = aString + theGrid[rowNum][colNum]
        print(aString)
    print()

    '''Prints heart (rotate picture anti-clockwise, and flipped)'''
    print("---Prints heart (rotate picture anti-clockwise, and flipped)---")
    # range function syntax: range(start, end, step)
    for colNum in range(totalCols-1, -1, -1):
        aString = ""
        for rowNum in range(totalRows-1, -1, -1):
            aString = aString + theGrid[rowNum][colNum]
        print(aString)
    print()
printTextart(grid)