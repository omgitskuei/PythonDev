import turtle
# Python module turtle is used to demonstrate how computers draw pictures/vector graphics on a screen.
>>>  import  turtle

# We need to create a canvas — a blank space to draw on by calling the function Pen from the turtle module
>>>  t = turtle.Pen()

# NOTE: tutle pointer always starts pointing right
# Move the turtle forward, advancing by 50 pixels:
>>>  t.forward(50)

# Turn the turtle 90 degrees left:
# The command points the arrow up (since it started pointing right):
>>>  t.left(90)

""" Draw a square """
>>>  t = turtle.Pen()
>>>  t.forward(50)
>>>  t.left(90)
>>>  t.forward(50)
>>>  t.left(90)
>>>  t.forward(50)
>>>  t.left(90)
>>>  t.forward(50)
>>>  t.left(90)

""" Draw a triangle """
import turtle
t = turtle.Pen()
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)

# To erase/clear the canvas,  enter  reset.
# This also puts the turtle back at its starting position.
>>>  t.reset()
# clear() is similar to reset; erases the canvas, however, leaves the turtle where it is
>>>  t.clear()

# We can use  up  to lift the pen off the page (in other words, tell the turtle to stop drawing), and  down  to start drawing.
>>>  t.up()

""" Draw two lines """
>>>  t.backward(100)
>>>  t.up()
>>>  t.right(90)
>>>  t.forward(20)
>>>  t.left(90)
>>>  t.down()
>>>  t.forward(100)
