The main difference between a tuple and a list is that a tuple cannot change once you’ve created it. For example, if we try to replace the first value in the tuple  fibs  with the number 4 ( just as we replaced values in our  wizard_list), we get an error message: >>>  fibs[0] = 4 Traceback (most recent call last):   File "<pyshell>", line 1, in <module>     fibs[0] = 4 TypeError: 'tuple' object does not support item assignment

games= [“kickball”]
food=[“ice cream”]
fav=games+food

Python has a special module  called turtle  that we can use to learn how    computers draw pictures/vector graphics on a screen.
>>>  import  turtle

Creating  a  Canvas Now that we have imported the  turtle  module, we need to create a canvas—a blank space to draw on, like an artist’s canvas. To do so, we call the function  Pen  from  the  turtle  module,  which  automatically creates a canvas (we’ll learn more about what a function is later). Enter this into the Python shell: >>>  t = turtle.Pen()


forward  instruction  tells the turtle to move forward. To tell the turtle to advance 50 pixels, enter the following command: >>>  t.forward(50)

Now we’ll tell the turtle to turn left  90 degrees with the following  command: >>>  t.left(90)

The  t.left(90)  command points the arrow up (since it started by pointing to the right):


Now we’ll draw a square. Add the following code to the lines you’ve  already  entered:
>>>  t.forward(50)
>>>  t.left(90)
>>>  t.forward(50)
>>>  t.left(90)
>>>  t.forward(50)
>>>  t.left(90)

To erase the canvas,  enter  reset. This clears the canvas and puts the turtle back at its starting position.
>>>  t.reset()

You can also use  clear, which just clears the screen and leaves the turtle where it is. >>>  t.clear()

move it  backward. We can use  up  to lift the pen off the page (in other words, tell the turtle to stop drawing), and  down  to start drawing. These functions are written in the same way as the others we’ve used. Let’s try another drawing using some of these commands. This time, we’ll have the turtle draw two lines. Enter the following code:
>>>  t.reset()
>>>  t.backward(100)
>>>  t.up()
>>>  t.right(90)
>>>  t.forward(20)
>>>  t.left(90)
>>>  t.down()
>>>  t.forward(100)

Programming  Puzzles

#1:  A  Rectangle Create a new canvas using the  turtle  module’s  Pen  function and then draw a rectangle. #2: A  triangle Create another canvas, and this time, draw a triangle. Look back at  the diagram of the circle with the degrees (“Moving the Turtle” on  page  46)  to  remind  yourself which direction to turn the turtle using  degrees. #3: A Box Without Corners Write a program to draw the four lines shown here (the size isn’t important, just the shape):

whitespace = tab or a space


>>>  age = 12 u  >>>  if  age == 10: v         print("What do you call an unhappy cranberry?") print("A blueberry!")

elif  age == 11: print("What did the green grape say to the blue grape?")         print("Breathe! Breathe!") x  elif  age == 12: y         print("What did 0 say to 8?")         print("Hi guys!") elif  age == 13: print("Why wasn't 10 afraid of 7?")         print("Because rather than eating 9, 7 8 pi.") else: print("Huh?") What did 0 say to 8? Hi guys!

>>>  if  age == 10  or  age == 11  or  age == 12  or  age == 13: print('What is 13 + 49 + 84 + 155 + 97? A headache!') else: print('Huh?')

>>>  if  age >= 10  and  age <= 13: print('What is 13 + 49 + 84 + 155 + 97? A headache!') else: print('Huh?')

>>>  myval =  None >>>  print(myval) None

>>>  myval =  None >>>  if  myval ==  None: print("The variable myval doesn't have a value") The variable myval doesn't have a value

User input comes into Python as a string, which means that when you type the number 10 on your keyboard, Python saves the number 10 into a variable as a string, not a number.

>>>  age =  '10' >>>  converted_age =  int(age)

>>>  age = 10 >>>  converted_age =  str(age)

>>>  age =  '10.5' >>>  converted_age =  float(age) >>>  print(converted_age) 10.5

>>>  age =  '10.5' >>>  converted_age =  int(age) Traceback (most recent call last):     File "<pyshell#35>", line 1, in <module>     converted_age = int(age) ValueError: invalid literal for int() with base 10: '10.5'

You will also get a  ValueError  if you try to convert a string that doesn’t contain a number in digits

>>>  money = 2000
>>>  if  money > 1000:
    print("I'm rich!!")
else:
    print("I'm not rich!!")
        print("But I might be later...")

#2:  twinkies! Create an  if  statement that checks whether a number of Twinkies (in the variable  twinkies) is less than 100 or greater than 500. Your program should print the message “Too few or too many” if the condition  is  true.

#3: Just the Right  number Create an  if  statement that checks whether the amount of money contained in the variable  money  is between 100 and 500  or  between 1,000  and  5,000. #4: I Can  fight  those  ninjas Create an  if  statement that prints the string “That’s too many” if  the variable  ninjas  contains a number that’s less than 50, prints “It’ll be a struggle, but I can take ’em” if it’s less than 30, and prints “I can fight those ninjas!” if it’s less than 10. You might try  out your code with: >>>  ninjas = 5

#4: I Can  fight  those  ninjas Create an  if  statement that prints the string “That’s too many” if  the variable  ninjas  contains a number that’s less than 50, prints “It’ll be a struggle, but I can take ’em” if it’s less than 30, and prints “I can fight those ninjas!” if it’s less than 10. You might try  out your code with: >>>  ninjas = 5


The  range  function doesn’t actually create a list of numbers; it returns an  iterator, which is a type of Python object specially designed to work with loops. However, if we combine  range  with list, we get a list of numbers. >>>  print(list(range(10, 20))) [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

You don’t need to stick to using the  range  and  list  functions when  making  for  loops. You could also use a list you’ve already created, such as the shopping list from Chapter 3, as follows:
>>>  wizard_list = ['spider legs',  'toe of frog',  'snail tongue', 'bat wing',  'slug butter',  'bear burp']
>>>  for  i  in  wizard_list:
print(i)
spider legs toe of frog snail tongue bat wing slug butter bear burp

hugehairypants = ['huge',  'hairy',  'pants']
for  i  in  hugehairypants:
    print(i)                  #
    for  j  in  hugehairypants:    # These lines are the FIRST block.
        print(j)              #


>>> x = 45v
>>> y = 80w
while x < 50 and y < 100:
        x = x + 1
        y = y + 1
        print(x, y)

while  True:
    ‘’’some code’’’
    if  some_value ==  True:
        break

The condition for the  while  loop is just  True, which is always true, so the code in the block will always run (thus, the loop is eternal). Only if the variable  some_value  is true will Python break out of the loop.

#3: My five favorite IngredientsCreate a list containing five different sandwich ingredients, such as the following:>>> ingredients = ['snails', 'leeches', 'gorilla belly-button lint',                'caterpillar eyebrows', 'centipede toes']Now create a loop that prints out the list (including the numbers):1 snails2 leeches3 gorilla belly-button lint4 caterpillar eyebrows5 centipede toes

P107

Return statement for functions
def  savings(pocket_money, paper_route, spending): return  pocket_money + paper_route – spending

>>>  another_variable = 100 >>>  def  variable_test2():         first_variable = 10         second_variable = 20 v         return  first_variable * second_variable * another_variable In this code, even though the variables  first_variable  and second_variable  can’t be used outside the function, the variable another_variable  (which was created outside the function at  u) can  be used inside it at  v. Here’s the result of calling this function: >>>  print(variable_test2()) 20000

Modules:
Tkinter
PyGame
PIL (images)
Panda3D (3D graphics)
Time
Sys
>>>  import  sys
>>>  print(sys.stdin.readline())
If you then type some words and press enter, those words will be printed out in the shell.

>>>  def  silly_age_joke(): print('How old are you?')          age =  int(sys.stdin.readline()) if  age >= 10  and  age <= 13: print('What is 13 + 49 + 84 + 155 + 97? A headache!') else: print('Huh?') Did you recognize the function  int  at  u,  which converts a string to a number? We included that function because  readline() returns whatever someone enters as a string, but we want a number so that we can compare it with the numbers 10 and 13 at  v.

Class Child(parent):
>>>  class  Inanimate(Things): pass >>>  class  Animate(Things): pass

reginald = Giraffes()

class  ThisIsMySillyClass:
    def  this_is_a_class_function():
        print('it’s a class function')
    def  this_is_also_a_class_function():
        print('also a class function')

class  Animals(Animate):
    def  breathe(self):
        pass
    def  move(self):
        pass
    def  eat_food(self):
        pass

why use classes and objects at all, when you could just write normal functions called breathe,  move,  eat_food, and so on?

reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()

Because we’re using objects and classes, we can tell Python exactly which giraffe we’re talking about when we want to run the move  function.

__init__  function
notice that there are two underscore characters on each side, for a total of four

This is a special type of function in Python classes and must have this name

The  init  function is a way to set the properties for an object when the object is first created, and Python will automatically call this function when we create a new object. Here’s how to use  it:
>>>  class  Giraffes:
def  __init__(self, spots):
self.giraffe_spots = spots

Just like the other functions we have defined in the class, the  init  function also needs to have  self  as the first parameter.

>>>  ozwald = Giraffes(100) >>>  gertrude = Giraffes(150) >>>  print(ozwald.giraffe_spots) 100 >>>  print(gertrude.giraffe_spots) 150

P110

Python’s  built-in functions  don’t need to be imported first

The  abs  function returns the  absolute  value  of a number, which is the value of a number without its sign.
>>>  print(abs(10))
10
>>>  print(abs(-10))
10

>>>  steps = -3
>>>  if  abs(steps) > 0:
    print('Character is moving')
If we hadn’t used  abs, the  if  statement might look like this:
>>>  steps = -3
>>>  if  steps < 0  or  steps > 0:
    print('Character is moving')

When using  bool  for numbers, 0 returns  False, while any other number returns  True.

When you use  bool  for other values, like strings, it returns  False if there’s no value for the string (in other words, the keyword  None or an empty string). Otherwise, it will return  True, as shown here:
>>>  print(bool(None)) False
>>>  print(bool('a')) True
>>>  print(bool(' ')) True
