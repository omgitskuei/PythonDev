# -*- coding: utf-8 -*-
"""
The Collatz Sequence.

Write a function named collatz() that has one parameter named number.
If number is even, collatz() should print (number/2) and return this value.
If number is odd, collatz() should print and return (3*number+1).

Then write a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1.

(Amazingly enough, this sequence actually works for any integer—sooner
or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t
sure why.

Your program is exploring what’s called the Collatz sequence,
sometimes called “the simplest impossible math problem.”)

Remember to convert the return value from input() to an integer with
the int() function; otherwise, it will be a string value.

Hint: An integer number is even if number % 2 == 0, and it’s odd if
number % 2 == 1.

The output of this program could look something like this:
Enter number:
3
10
5
16
8
4
2
1

Source: Automating the Boring Stuff with Python by Al Sweigart, p.77 (chpt.3)
Date:
"""

# ****************************************************************************
# *                                 Functions                                *
# ****************************************************************************


def collatz(number):
    """
    Calculate the next number in the collatz sequence.

    Parameters
    ----------
    number : int
        Current number in the sequence.

    Returns
    -------
    int/float
        Next number in the sequence.
    """
    if(number % 2 == 0):
        return int(number/2)
    else:
        return int(3*number+1)


# ****************************************************************************
# *                                  Main                                    *
# ****************************************************************************
validInput = False

# number = 3
# validInput = True

# Get user input for the initial number in the sequence
for i in range(0, 3, 1):
    try:
        number = int(input('Enter number:'))
        validInput = True
        break
    except ValueError:
        print('Wow, invalid input!')

if(validInput):
    # Prints the initial number
    print(number)

    # Calculate the sequence until it ends at 1
    while(number != 1):
        number = collatz(number=number)
        print(number)
