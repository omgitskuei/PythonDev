# Fibonacci series [the sum of two elements defines the next]:
a, b = 0, 1		# multiple assignment
while a < 10:

    print("a",a)

    # NOTE: expressions on the right are ALL evaluated BEFORE any assignments on the left take place
    # right-hand side expressions are evaluated from the left to the right
    a, b = b, a+b

    # tempB = b    # same as above
    # b = a + b
    # a = tempB

    # tempA = a    # same as above
    # a = b
    # b = tempA + b

    print("a",a,"b",b)