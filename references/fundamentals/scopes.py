# function definition
def changeme(myvar):
    print("in function, before changes:", myvar)
    myvar = 50
    print(id(myvar))
    print("in function, after changes:", myvar)
    return myvar


# this myvar (20) is immutable and is a global variable, is a separate var from the myvar in the "def changeme(myvar)" line
myvar = 20
print(id(myvar))
# see how the ID for myvar outside the changeme function is different from the ID inside the function

changeme(myvar)
print("outside function:", myvar, "\n")

# you'd have to do myvar=changeme(myvar) to make sure the value over-rides the original global variable, if thats what you want.
# I'll make another global variable to 'receive' the returned results
myvar2 = changeme(myvar)
print("outside function2:", myvar2)

# list, set, dict are mutable, same ID so changes to it via functions WILL STICK, unlike above


def changeme(myvar):
    print("in function, before changes:", myvar)
    myvar[2] = 50
    print("in function, after changes:", myvar)
    return myvar


# this myvar is immutable, and is a separate variable from the myvar in the "def changeme(myvar)" line
myvar = [10, 20, 30, 60]
changeme(myvar)
# at this point, myvar has been changed by changeme, and this sticks even outside the function
print("outside function:", myvar, "\n")
myvar2 = changeme(myvar)
print("outside function2:", myvar2)
