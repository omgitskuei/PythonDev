#dict(mapping|iterable|**kwarg)
dict(one="1"|)
#defined a function called p that takes a string and prints it out.
def p(pstr):
    print(pstr)
p("Hi")

def sum_nums(n1, n2):
    print(n1)
    print(n2)
print(n1+n2)
    return n1+n2

sum_nums(5,8)

a=sum_nums(3, 2)
p(a)

def bmi(kg, m):
    return "{0:0.2f}".format(kg/(m**2))
print(bmi(68, 1.7))

#you COULD just return the numbers without formatting them but that's not ideal.
def bm3(kg, m):
    return kg/(m**2)
p(bm3(68, 1.7))

#notice how you need the return, otherwise calling it with variables and printing gives you nothing
def bm3(kg, m):
    kg/(m**2)
p(bm3(68, 1.7))

#i = 0, 1, 2, runs 3 times total, 3 is exclusive
for i in range(3):
    p("a")

#function definition
def changeme(myvar):
    print("in function, before changes:", myvar)
    myvar=50
    print(id(myvar))
    print("in function, after changes:", myvar)
    return myvar
#this myvar (20) is immutable and is a global variable, is a separate var from the myvar in the "def changeme(myvar)" line
myvar=20
print(id(myvar))
#see how the ID for myvar outside the changeme function is different from the ID inside the function

changeme(myvar)
print("outside function:", myvar, "\n")

#you'd have to do myvar=changeme(myvar) to make sure the value over-rides the original global variable, if thats what you want.
#I'll make another global variable to 'receive' the returned results
myvar2=changeme(myvar)
print("outside function2:", myvar2)

#list, set, dict are mutable, same ID so changes to it via functions WILL STICK, unlike above
def changeme(myvar):
    print("in function, before changes:", myvar)
    myvar[2]=50
    print("in function, after changes:", myvar)
    return myvar
#this myvar is immutable, and is a separate variable from the myvar in the "def changeme(myvar)" line
myvar=[10, 20, 30, 60]
changeme(myvar)
#at this point, myvar has been changed by changeme, and this sticks even outside the function
print("outside function:", myvar, "\n")
myvar2=changeme(myvar)
print("outside function2:", myvar2)

{'foo'}

set('foo')

set('foo')

x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
x


#Alternately, a set can be defined with curly braces ({}):

x = {<obj>, <obj>, ..., <obj>}

#Observe the difference between these two set definitions:
{'foo'}
{'foo'}

set('foo')
{'o', 'f'}

#A set can be empty. However, recall that Python,
#... interprets empty curly braces ({}) as an empty dictionary,
#... so the only way to define an empty set is with the set() function:
x = set()
type(x)
<class 'set'>
x
set()

x = {}
type(x)
<class 'dict'>

An empty set is falsy in Boolean context:
x = set()
bool(x)
False


#Read/Writing files
#Open/Create new file
fo = open('myfile.txt', "w")
print('File Name:', fo.name)
#Open file, similar to w, but x will make error message if no file found, will not create new)
#fo = open('myfile.txt', "x")

#Write file
fo.write('Python is a great language')

#Read file
fo = open("myfile.txt", "r")
str = fo.read(10)
print("read string:", str)

#Close file
fo.close

fo = open('myfile.txt', "r+")
while True:
    line=fo.readline() #reads one line at a time
    if not line:
        break
    print(line, end='')  #there's an automatic enter at the end of print. end='' removes the auto-enter
fo.close

fo = open('myfile.txt', "r+")
while True:
    line=fo.readlines() #reads multiple lines at once
    if not line:
        break
    print(line, end='')  #there's an automatic enter at the end of print. end='' removes the auto-enter
fo.close

fo = open('myfile.txt', "r+")
line=fo.readlines() #reads multiple lines at once
print(line, end='')  #there's an automatic enter at the end of print. end='' removes the auto-enter
fo.close

fo = open('myfile.txt', "r+")
line=fo.readlines() #reads multiple lines at once
print(line, end='')  #there's an automatic enter at the end of print. end='' removes the auto-enter
fo.close

fo = open('myfile.txt', "r+")
line=fo.readline() #reads one line at once
print(line, end='')  #there's an automatic enter at the end of print. end='' removes the auto-enter
fo.close

try:
    fp = open('myfile.txt', 'r')
    data = fp.read()
    print('Content:')
    print(data)
except:
    print('Error:File IO error')
finally:
    fp.close

with open("myfile.txt", "r") as fp:
    data=fp.read()
    print('Content:')
    print(data)
fp.close()

import urllib.request
x = urllib.request.urlopen('https://kai.one/colab_quiz_18.txt');
print(x.read().decode('utf-8'));
