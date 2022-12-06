# example of best practice function header
def hello1(name: str) -> None:
    print('hello ' + name)


# functions can have simple headers with no indications of type of args and of return
# what is the type for name? the reader has to read the code to know type of name is str
def hello2(name):
    print('hello ' + name)


hello1('sir')
hello2('Joe')
try:
    hello2(1)
except TypeError:
    print('TypeError: can only concatenate str (not "int") to str')  # this will be printed
hello1(name='Bob')


def add2(num1: int, num2: int) -> int:
    return num1 + num2


print(add2(1, 3))
print(add2(1.234, 3.5))  # despite add2 specifying that it takes 2 ints, passing float works
# though at least the IDE will point out that int was expected, not float, as warnings

# what if you want to specify which number is num1 and num2?
print(add2(num2=3, num1=1))  # same as above, verbose but explicit (easier to read, honestly)
