"""
Using the Turtle module.

It can draw simple shapes.

NOTE: To add an outline to the star, change the color to black and
redraw the star without filling.

Created on Sat Aug 29 10:01:06 2020.

@author: omgitskuei
"""
# -*- coding: utf-8 -*-

import turtle
import time

t = turtle.Pen()
t.reset()


"""
turtle.Pen().reset() clears the canvas.
"""


def drawSquare(size, filled):
    """
    Draws a square.

    Parameters
    ----------
    size: int. Try size = 25, 50, 75, 100, 125.
    filled: boolean.

    Returns
    -------
    None.

    """
    if filled is True:
        # set fill color to purple
        t.color(0.5, 0.5, 1)
        t.begin_fill()
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    if filled is True:
        t.end_fill()


def drawStar1():
    """
    Draw a star.

    Returns
    -------
    None.

    """
    for x in range(1, 9):
        t.forward(100)
        t.left(225)


def drawStar2():
    """
    Draw a star.

    Returns
    -------
    None.

    """
    for x in range(1, 38):
        t.forward(100)
        t.left(175)


def drawStar3():
    """
    Draw a 19-point star.

    Returns
    -------
    None.

    """
    for x in range(1, 20):
        t.forward(100)
        t.left(95)


def drawStar4():
    """
    Draw a 9-point star.

    Returns
    -------
    None.

    """
    for x in range(1, 19):
        t.forward(100)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)


def drawAnyRegularPolygon(size, points):
    """
    Draw a equilateral and equal angles polygon.

    Parameters
    ----------
    size : int
        The size of the star.
    points : int
        The number of points the shape has.

    Returns
    -------
    None.

    """
    for x in range(1, points+1):
        t.forward(size)
        t.left(360/points)


def drawAnyStar(size, points):
    """
    Draw a star with equal angles and equilateral sides.

    Parameters
    ----------
    size : int
        The size of the star.
    points : int
        The number of points the star has.

    Returns
    -------
    None.

    """
    if points % 2 == 0:
        boop = (180-((points-2)*180)/points)
        for x in range(1, points+1):
            t.forward(size/2)
            t.left(-boop)
            t.forward(size/2)
            t.left(180-(180-2*boop))
    else:
        strokes = points + 1
        for x in range(1, strokes):
            t.forward(size)
            t.right(180-(180/points))


"""
Coloring things

turtle.Pen().color(red, green, blue) specifies what color to fill with.
red, green, blue range between 0 to 1 (1 for 100%).

NOTE: .color(0, 0, 0) is BLACK.

turtle.Pen().begin_fill() and turtle.Pen().end_fill() fills in a color
"""


"""
Moving the turtle

Move the turtle without drawing lines by using t.up() to lift
the pen and use t.down() to set it back down again.
"""


def drawCar():
    """
    Draw a car.

    Returns
    -------
    None.

    """
    # Draw a car (chassis)
    t.color(1, 0, 0)
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.end_fill()

    # Draw a wheel
    t.color(0, 0, 0)
    t.up()
    t.forward(10)
    t.down()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Draw second wheel
    t.setheading(0)
    t.up()
    t.forward(90)
    t.right(90)
    t.forward(10)
    t.setheading(0)
    t.begin_fill()
    t.down()
    t.circle(10)
    t.end_fill()


# drawCar()

# Draw square with fill
# drawSquare(75, True)

# Draw pentagon
# drawAnyRegularPolygon(100, 5)
# drawAnyRegularPolygon(75, 8)

# Draw triangle
# drawAnyRegularPolygon(50, 3)

# Draw square
# drawAnyRegularPolygon(25, 4)

# Draw a star

drawAnyStar(100, 3)
time.sleep(1)
t.reset()
drawAnyStar(100, 4)
time.sleep(1)
t.reset()
drawAnyStar(100, 5)
time.sleep(1)
t.reset()
drawAnyStar(100, 6)
time.sleep(1)
t.reset()
drawAnyStar(100, 7)
time.sleep(1)
t.reset()
drawAnyStar(100, 8)
time.sleep(1)
t.reset()
drawAnyStar(100, 9)
time.sleep(1)
t.reset()
drawAnyStar(100, 10)

# Add turtle.done() to prevent Python Turtle Graphics window from crashing
# after drawing.
turtle.done()
