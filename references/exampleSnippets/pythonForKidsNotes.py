tkinter can be used to create full applications, like a simple word processor,
as well as for simple drawing.

>> > from tkinter import *
>> >  tk = Tk()
>> >  btn = Button(tk, text="click me")
>> >  btn.pack()


The  tk  object creates a basic window  to which we can then add other things,
such as buttons, input boxes, or a canvas to draw on.
This is the main class provided by the  tkinter  module—without creating an
object of the  Tk class, you won’t be able to do any graphics or animations.

Although we’ve added this button to the window, it won’t be displayed until
you enter the line  btn.pack(), which tells the button to appear

>> > def hello():
    print('hello there')

Then we modify our example to use this new function:
>> > from tkinter import *
>> >  tk = Tk()
>> >  btn = Button(tk, text="click me", command=hello)
>> >  btn.pack()

We’ve added the parameter  command, which tells Python to use the  hello
function when the button is clicked.

Now when you click the button, you will see “hello there” written to the
shell. This will appear each time the button is clicked.

Using  named  Parameters

Sometimes functions have a lot of parameters, and we may not always need
to provide a value for every parameter. Named parameters are a way we can
provide values for only the parameters that we need to give values.

>> > def person(width, height):
    print('I am %s feet wide, %s feet high' % (width, height))

>> >  person(4, 3) I am 4 feet wide, 3 feet high
