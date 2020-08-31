"""
Using the Tkinter module.

The Tkinter module (“Tk interface”) is the standard Python interface to the
Tk GUI toolkit.
Tk itself is not part of Python; it is maintained at ActiveState.

Running python -m Tkinter from the command line should open a window
demonstrating a simple Tk interface, letting you know that Tkinter is
properly installed on your system, and also showing what version of Tcl/Tk
is installed, so you can read the Tcl/Tk documentation specific to that
version.

Note Tkinter has been renamed to tkinter in Python 3. The 2to3 tool will
automatically adapt imports when converting your sources to Python 3.

Created on Sat Aug 29 10:01:06 2020.

@author: omgitskuei
"""
# -*- coding: utf-8 -*-

# from tkinter import *
import tkinter


"""
Test to see if tkinter is installed properly

This should make a window with two buttons.
"""
tkinter._test()




"""
Tk class is meant to be instantiated only once in an application

The  tk  object creates a basic window  to which we can then add other things,
such as buttons, input boxes, or a canvas to draw on.
"""
tk = Tk()
"""
parameter command tells Python to use function hello when button is clicked.
You will see “hello there” written to the shell with each click.
"""
btn = Button(tk, text="click me", command=hello)

def hello():
    """
    Prints a string

    Parameters
    ----------
        None.

    Returns
    -------
        None.
    """
    print('hello there')

# Tells the button to appear
btn.pack()
tk.mainloop()




# Make a button
from tkinter import *
from tkinter import ttk
root = Tk()
ttk.Button(root, text="Hello World").grid()
root.mainloop()


"""
https://tkdocs.com/tutorial/firstexample.html
"""
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()


"""
When it’s time to really draw
something, we need a different component: a canvas object, which is
an object of the class Canvas (provided by the tkinter module).
"""
from tkinter import *
tk = Tk()
tk.title("Example with canvas")
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_rectangle(10, 10, 300, 50)
tk.mainloop()


"""
prompt user for color
"""
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
colorchooser.askcolor()
tk.mainloop()


"""
drawing arcs
"""
canvas.create_arc(10, 10, 200, 100, extent=180, style=ARC)


"""
display text
"""
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_text(150, 100, text='There once was a man from Toulouse,')
canvas.create_text(130, 120, text='Who rode around on a moose.', fill='red')
canvas.create_text(150, 150, text='He said, "It\'s my curse,',
font=('Times', 15))
canvas.create_text(200, 200, text='But it could be worse,',
font=('Helvetica', 20))
canvas.create_text(220, 250, text='My cousin rides round',
font=('Courier', 22))
canvas.create_text(220, 300, text='on a goose."', font=('Courier', 30))
tk.mainloop()


"""
display image (GIF)

With tkinter, you can ONLY LOAD GIF images.
You can display other types of images, such as PNG (.png) and JPG (.jpg),
but you’ll need to use a different module, such as the
Python Imaging Library (http://www.pythonware.com/products/pil/).

FYI, make sure the image file is actually present
"""
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
my_image = PhotoImage(file='c:\\test.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)
tk.mainloop()


"""
Basic animations
"""
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=200)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(0, 60):
    canvas.move(1, 5, 0)
    tk.update()
    time.sleep(0.05)
tk.mainloop()
