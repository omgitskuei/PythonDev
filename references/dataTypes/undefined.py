# If a variable is not “defined” (assigned a value), trying to use it will give you an error:
# >>> n  # try to access an undefined variable
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NOTE: NameError: name 'n' is not defined


# NOTE: In interactive mode, the last printed expression is assigned to the variable [_].
# This means that when you are using Python as a desk calculator,
# it is somewhat easier to continue calculations, for example:

>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _ # this _ means 12.5625
113.0625
>>> round(_, 2)
113.06
# This variable should be treated as read-only by the user. Don’t explicitly assign a value to it
