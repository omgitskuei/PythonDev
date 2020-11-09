# -*- coding: utf-8 -*-
"""
Program name: Notes on break in Python.

Summary: Notes on syntax, usage, and example snippets of breaks
Created on: Sat Oct 24 11:37:09 2020
@author: omgitskuei (Github)
"""

# say the break was inside the loop condition, so true, would kick program out of loop, as if the loop condition was false
for num in [31, 23, 12, 21]:
    if num%2==0:
        print("Data contains even")
        break
    else:
        print("num=", num)


# Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement. This is exemplified by the following loop, which searches for prime numbers:
for n in range(2, 10):			# n is 2 up to 9
	print("n =", n)
	for x in range(2, n):		# x is 2 up to n
		print("x =", x)
		print("n % x =", n % x)
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			print('> > > break')
			break				# ends looping-if early if not-prime already found
	else:						# when (for x) loop used up all iterable, AND break didn't trigger
		# loop fell through without finding a factor (n % x == 0 never triggered)
		print(n, 'is a prime number')
		print()

# When used with a loop, the else clause has more in common with the else clause of a try statement than it does with that of if statements: a try statement’s else clause runs when no exception occurs, and a loop’s else clause runs when no break occurs.
