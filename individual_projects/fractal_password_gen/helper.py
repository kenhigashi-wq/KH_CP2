from turtle import *

#function for the simple triangle. lets gooooooooooooooooooooooooo
def triangle(size):
    for _ in range(3):
        forward(size)
        left(120)

#function for actually doing the drawing thing.
#if the depth is 1, draw a simple triangle, if not make 3 smaller triangles
def sierpinski(size, lvl):#also make the recursion stuff.
    if lvl == 1:
        triangle(size)
        return

    #bottom left
    sierpinski(size/2, lvl - 1)

    #bottom right triangle
    penup()
    forward(size/2)
    pendown()
    sierpinski(size/2, lvl - 1)
    penup()
    backward(size/2)
    pendown()

    #The topest triangle
    penup()
    left(60)
    forward(size / 2)
    right(60)
    pendown()
    sierpinski(size / 2, lvl - 1)

    
    #reutrn the turtle to the original spot
    left(60)
    backward(size/2)
    right(60)

def save():
    canvas = getscreen().getcanvas()
    canvas.postscript(file="triangle.png")