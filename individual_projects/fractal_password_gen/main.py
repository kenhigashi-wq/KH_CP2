#KH fractal function
from helper import *
from turtle import * #import turtle
#set up things to make them faster and cleaner
tracer(0)
speed(0)
hideturtle()
#ask for a depth
depth = int(input("Enter recursion depth (1-10):"))
depth = max(1, min(11, depth))
#ask for the tringle color
tri_color = input("Triangle Color: ") or "white"
#ask fr a background color
bg = input("Enter background color (e.g., red, blue, green): ") or "black"
saving = input("Do you want to save the image(y or no)? ")

if saving == "y":
    save()
if saving == "n":
    pass

#make a variable for a screen
screen = Screen()
#set up the screen for the back ground color
screen.bgcolor(bg)
#set up the color for the triangle color
pencolor(tri_color)
    
#making the things are starting normally
penup()
goto(-150, -100)
setheading(0) # face right to keep the things consistent
pendown()

#draw
sierpinski(300, depth)
update()
done()
