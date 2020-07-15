The main difference between a tuple and a list is that a tuple cannot change once you’ve created it. For example, if we try to replace the first value in the tuple  fibs  with the number 4 ( just as we replaced values in our  wizard_list), we get an error message: >>>  fibs[0] = 4 Traceback (most recent call last):   File "<pyshell>", line 1, in <module>     fibs[0] = 4 TypeError: 'tuple' object does not support item assignment

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



reginald = Giraffes()

class  ThisIsMySillyClass:
    def  this_is_a_class_function():
        print('it’s a class function')
    def  this_is_also_a_class_function():
        print('also a class function')



 called breathe,  move,  eat_food, and so on?

reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()



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
