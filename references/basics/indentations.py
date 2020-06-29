# Python Indentation
# Indentation refers to the spaces at the beginning of a code line.

# Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

# Python uses indentation to indicate a block of code.

# Example
if 5 > 2:
  print("Five is greater than two!")

# Python will give you an error if you skip the indentation

# NOTE: 4 spaces per indent level, using space instead of tab is Preferrable
# Only use tab if to remain consistent
if True:
    print("True")
else:
    print("False")
# Indents always follow : colon.
# the Indents must be aligned:
if True:
	print("True")
		print("True")    #this would cause IndentationError
else:
   print("False")
