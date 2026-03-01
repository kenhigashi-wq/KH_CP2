#KH fractal function
from turtle import * #import turtle
#set up things to make them faster and cleaner
tracer(0)
speed(0)
hideturtle()
#ask for a depth
depth = int(input("Enter recursion depth (1-5):"))
depth = max(1, min(5, depth))
#ask for the tringle color
tri_color = input("Triangle Color: ") or "white"
#ask fr a background color
bg = input("Enter background color (e.g., red, blue, green): ") or "black"


#make a variable for a screen
screen = Screen()
#set up the screen for the back ground color
screen.bgcolor(bg)
#set up the color for the triangle color
pencolor(tri_color)

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
    
#making the things are starting normally
penup()
goto(-150, -100)
setheading(0) # face right to keep the things consistent
pendown()

#draw
sierpinski(300, depth)
update()
done()
