# -*- coding: utf-8 -*-

Python’s  built-in functions  don’t need to be imported first

The  abs  function returns the  absolute  value  of a number, which is the value of a number without its sign.
>>>  print(abs(10))
10
print(abs(-10))
10

>>>  steps = -3
>>>  if  abs(steps) > 0:
    print('Character is moving')
If we hadn’t used  abs, the  if  statement might look like this:
>>>  steps = -3
>>>  if  steps < 0  or  steps > 0:
    print('Character is moving')

When using  bool  for numbers, 0 returns  False, while any other number returns  True.


The  bool  function will also return  False  for lists, tuples, and maps that
do not contain any values, or  True  when  they  do:

my_silly_list = []
print(bool(my_silly_list))
# False
my_silly_list = ['s',  'i',  'l',  'l',  'y']
print(bool(my_silly_list))
# True

>>>  year =  input('Year of birth: ')
Year of birth:
>>>  if  not  bool(year.rstrip()):
    print('You need to enter a value for your year of birth')
You need to enter a value for your year of birth

sys.stdin.readline()
Same as input()

rstrip  function (which removes any spaces and enter  characters from the end of the string

dir  function  (short  for  directory)

to display the functions that are available for a list value, enter this:
>>>  dir(['a',  'short',  'list'])

dir  function works on pretty much anything, including strings, numbers, functions, modules, objects, and classes.

sometimes the information it returns may not be very useful. For example, if you call  dir  on the number 1, it displays a number of special functions (those that start and end with underscores) used by Python itself, which isn’t really useful (you can usually ignore most of them): >>>  dir(1)

>>>  popcorn =  'I love popcorn!' >>>  dir(popcorn)

At this point, you could use  help  to get a short description of any function in the list. Here’s an example of running  help  against the  upper  function: >>>  help(popcorn.upper) Help on built-in function upper: upper(...) S.upper() -> str Return a copy of S converted to uppercase.

arrow (->) on the next line means that this function returns a string  (str

eval  function  (short  for  evaluate) takes a string as a parameter and runs it as though it were a Python expression.
>>>  your_calculation =  input('Enter a calculation: ') Enter a calculation:  12*52 >>>  eval(your_calculation) 624


Expressions that are split over more than one line (such as  if statements) generally won’t evaluate, as in this example: >>>  eval('''if True:         print("this won't work at all")''')
SyntaxError

The  exec  function is like  eval, except that
1) you can use it to run more complicated programs
2) exec doesn’t return a value whereas eval will return

>>>  my_small_program =  '''print('ham') print('sandwich')''' >>>  exec(my_small_program) ham sandwich In the

You could use  exec  to run mini programs that your Python program reads in from files—really, programs inside programs!

But try to convert a string containing a floating-point number into an integer, and you get an error message.
int('123.456')

Len function counts white spaces in string
len('this is a test string')

When used with a list or a tuple,  len  returns the number of items in that list or tuple:

When used with a list or a tuple,  len  returns the number of items in that list or tuple:

he max and min  functions The  max  function returns the largest item in a list, tuple, or string. For example, here’s how to use it with a list of numbers: >>>  numbers = [5, 4, 10, 30, 22] >>>  print(max(numbers)) 30

A string with the characters separated by commas or spaces will also work: >>>  strings =  's,t,r,i,n,g,S,T,R,I,N,G' >>>  print(max(strings))

lowercase letters come after uppercase letters, so  t  is more than  T.

>>>  my_list_of_numbers =  list(range(0, 500, 50)) >>>  print(my_list_of_numbers) [0, 50, 100, 150, 200, 250, 300, 350, 400, 450] >>>  print(sum(my_list_of_numbers)) 2250

Opening a File in Python Python’s  built-in  open  function opens a file in the Python shell and displays its contents. How you tell the function which file to open depends on your operating system.
Windows
>>>  test_file =  open('c:\\Users\\<your username>\\test.txt')
>>>  text = test_file.read()
>>>  print(text)
Apple
>>>  test_file =  open('/Users/sarahwinters/test.txt')
Ubuntu
>>>  test_file =  open('/home/jacob/test.txt')

>>>  test_file =  open('c:\\myfile.txt',  'w') The  parameter  'w'  tells Python that we want to write to the file object, rather than read from it.

>>>  test_file =  open('c:\\myfile.txt',  'w') >>>  test_file.write('What is green and loud? A froghorn!') >>>  test_file.close()

>>>  test_file =  open('myfile.txt') >>>  print(test_file.read()) What is green and loud? A froghorn!

>>>  a =  abs(10) +  abs(-10)
>>>  print(a)
>>>  b =  abs(-10) + -10
>>>  print(b)
