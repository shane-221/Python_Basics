import turtle

import colorgram
import turtle as t
from turtle import Screen
import random

# Todo: Prep stuff
turtle.colormode(255)
timmy=t.Turtle()
timmy.penup()  # Lift the pen to avoid drawing a line
timmy.goto(-400, -200)  # Move to the new starting position
timmy.pendown()

# Todo:  Extract 10 colours from the image into a list. Can get the list and comment out the code as well( For learning
## purposes- just leave it.  

rgb_colours=[]
colours = colorgram.extract('image.jpg', 10)

for i in colours:
    rgb_colours.append((i.rgb.r, i.rgb.g, i.rgb.b))

# Todo : Use the colours to create the Painting.
    # Todo : Creating the dots(10 x10 and 50 paces apart, 20 in circumference)
def circle_rows():
    # Todo: need to choose a randon colour
    colour= random.choice(rgb_colours)
    timmy.pencolor(colour)
    timmy.dot(20)
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()

    # Todo: need the original conditions for the dot to start
y=-200
x=-400
n=0
    # Todo: Creating the loop for 10 rows on different levels
while n<10:
    for i in range(0,10):
        circle_rows()
        timmy.penup()
    n+=1
    y += 50
    timmy.goto(x, y)


# Todo: Exit on click screen
my_screen = Screen()
my_screen.setup (width=150, height=150, startx=0, starty=-50)
my_screen.exitonclick()






