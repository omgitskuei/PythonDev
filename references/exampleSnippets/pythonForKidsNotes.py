
from turtle import *
import turtle
import time
P110


create a small program to print every other word in the following string,
starting with the first word(this):
"this if is you not are a reading very this good then way you to have hide done a it message wrong"

Create a Python program to copy a file.
(Hint: You’ll need to open the file that you want to copy,
 read it in , and then create a new file—the copy.)
Check that your program works by printing the contents of the new file on the screen.







Traceback(most recent call last):   File "<pyshell#1>", line 1, in <module > sys.exit()
This won’t work if you’re not using the modified version of IDLE that we set up in Chapter 1.

Reading with the stdin Object
The  stdin  object(short for standard  input) in the  sys  module  prompts a user to enter information to be read into the shell and used by the program. As you learned in Chapter 7, this object has a  readline function, which is used to read a line of text typed on the keyboard until  the  user  presses enter. It works like the  input  function that we used in the random number guessing game earlier in this chapter. For example, enter the following: >> > import sys >> >  v = sys.stdin.readline() He who laughs last thinks slowest

Python will store the string  He who laughs last thinks slowest in the variable  v. To confirm this, print the contents of  v: >> > print(v) He who laughs last thinks slowest

One of the differences between  input and the  readline  function is that with readline, you can specify the number of characters to read as a parameter(however, at the moment this works only in the console, not when you’re running in the shell). For example: >> >  v = sys.stdin.readline(13) He who laughs last thinks slowest >> > print(v) He who laughs

Writing with the stdout  object Unlike  stdin, the  stdout  object (short for  standard  output) can be used to write messages to the shell (or console), rather than reading them in . In some ways, it’s the same as  print, but  stdout  is a file object, so it has the same functions we used in Chapter 9, such as write. Here’s an example: >> >  import  sys >> >  sys.stdout.write("What does a fish say when it swims into a wall? Dam.") What does a fish say when it swims into a wall? Dam.52

Notice that when  write  finishes, it returns a count of the number of characters it has written. You can see  52  printed into the shell at the end of the message.

Which Version of Python Am I Using?

For example, you might put the version of Python into an About window of your program,  like  this: >> > import sys >> > print(sys.version) 3.1.2 (r312: 79149, Mar 21 2013, 00: 41: 52)[MSC v.1500 32 bit(Intel)]

Doing  time with the time module Python’s  time  module contains functions for displaying the time, though not necessarily as you might expect. Try this: >> > import time >> > print(time.time()) 1300139149.34

The number returned by the call to time() is actually the number of seconds since January 1, 1970, at 00: 00: 00 AM

to find out how long parts of your program take to run, you can record the time at the beginning and end

>> > def lots_of_numbers(max):
    for x in range(0,  max):
        print(x)

>> > def lots_of_numbers(max):
    t1 = time.time() for x in range(0,  max):
        print(x)
    t2 = time.time()
    print('it took %s seconds' % (t2 - t1))

Calling the program again, we get the following result(which will vary depending on the speed of your system): >> >  lots_of_numbers(1000) 0 1 2 3 . . . 997 998 999 it took 50.159196853637695 seconds

Converting a Date with asctime The function  asctime  takes a date as a tuple and converts it into something more readable. (Remember that a tuple is like a list with items that you can’t change.) As you saw in Chapter 7, calling asctime  without any parameters will display the current date and time in a readable form. >> > import time >> > print(time.asctime()) Mon Mar 11 22: 03: 41 2013

To call  asctime with a parameter, we first create a tuple with values for the date and time.

>> >  t = (2007, 5, 27, 10, 30, 48, 6, 0, 0)

The values in the sequence are year, month, day, hours, minutes, seconds, day of the week(0 is Monday, 1 is Tuesday, and so on), day of the year(we put 0 as a placeholder), and whether or not it is daylight saving time(0 if it isn’t
                                                                                                                                                                                                                           1 if it is ).

Unlike  asctime, the function  localtime  returns  the  current  date and time as an object


print(time.localtime())
time.struct_time(tm_year=2020, tm_mon=2, tm_mday=23, tm_hour=22,
                 tm_min=18, tm_sec=39, tm_wday=0, tm_yday=73, tm_isdst=0)

To print the current year and month, you can use their index positions

t = time.localtime()
year = t[0]
month = t[1]
print(year)
# 2020
print(month)
# 2

The function  sleep is quite useful  when you want to delay or slow down your program.

>> > for x in range(1, 61): print(x)

This code will rapidly print all numbers from 1 to 60. However, we can tell Python to sleep for a second between each print statement, like this:

>> > for x in range(1, 61): print(x)         time.sleep(1)

pickle  module is used to convert Python objects into something that can be  written into a file and then easily read back out.

For example, here’s how we might add a save feature to a game:

>> > import pickle v
>> >  game_data = {'player-position':  'N23 E45', 'pockets': ['keys',  'pocket knife',  'polished stone'], 'backpack': ['rope',  'hammer',  'apple'], 'money': 158.50}
>> >  save_file = open('save.dat',  'wb')
>> >  pickle.dump(game_data, save_file)
>> >  save_file.close()

If you were to open the  save.dat  file, you would see that it doesn’t look like a text file
it looks like a jumbled mixture of normal text and special characters.

>> >  load_file = open('save.dat',  'rb')
>> >  loaded_game_data = pickle.load(load_file)
>> >  load_file.close()

To prove that our saved data has been loaded correctly, print the  variable: >> > print(loaded_game_data) {'money': 158.5, 'backpack': ['rope', 'hammer', 'apple'], 'player-position': 'N23 E45', 'pockets': ['keys', 'pocket knife', 'polished stone']}

>> > import copy
>> > class Car: pass
>> >  car1 = Car()
>> >  car1.wheels = 4
>> >  car2 = car1
>> >  car2.wheels = 3
>> > print(car1.wheels)
>> >  car3 = copy.copy(car1)
>> >  car3.wheels = 6
>> > print(car1.wheels)
What is printed

tkinter can be used to create full applications, like a simple word processor, as well as for simple drawing.

>> > from tkinter import *
>> >  tk = Tk()
>> >  btn = Button(tk, text="click me")
>> >  btn.pack()

Using from module - name import * allows us to use the contents of a module without using its name.
In contrast, when using import turtle in previous examples, we needed to include the module name to access its
contents:
t = turtle.Pen()

When we use import *, we don’t need to call  turtle.Pen, as we did in Chapters 4 and 11. This isn’t so useful with the  turtle  module, but it is when you are using modules with a lot of classes and functions, because it reduces the amount you need to type.

t = Pen()

The  tk  object creates a basic window  to which we can then add other things, such as buttons, input boxes, or a canvas to draw on.
This is the main class provided by the  tkinter  module—without creating an object of the  Tk class, you won’t be able to do any graphics or animations.

Although we’ve added this button to the window, it won’t be displayed until you enter the line  btn.pack(), which tells the button to appear

>> > def hello():
    print('hello there')

Then we modify our example to use this new function:
>> > from tkinter import *
>> >  tk = Tk()
>> >  btn = Button(tk, text="click me", command=hello)
>> >  btn.pack()

We’ve added the parameter  command, which tells Python to use the  hello  function when the button is clicked.

Now when you click the button, you will see “hello there” written to the shell. This will appear each time the button is clicked.

Using  named  Parameters

Sometimes functions have a lot of parameters, and we may not always need to provide a value for every parameter. Named parameters are a way we can provide values for only the parameters that we need to give values.

>> > def person(width, height):
    print('I am %s feet wide, %s feet high' % (width, height))

>> >  person(4, 3) I am 4 feet wide, 3 feet high
