# -*- coding: utf-8 -*-

"""
paddleball.py Minigame Paddle Ball.

Code based off of "Python For Kids" by Jason R. Briggs, No Starch Press

Created on Fri Oct  9 22:55:08 2020
@author: Github omgitskuei
"""

from tkinter import *
import random
import time

tk = Tk()
tk.title("Paddle Ball")
# make the window a fixed size.
# 0, 0 means "window cannot be changed either horizontally or vertically"
tk.resizable(0, 0)
# place the window containing our canvas in front of all other windows
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
