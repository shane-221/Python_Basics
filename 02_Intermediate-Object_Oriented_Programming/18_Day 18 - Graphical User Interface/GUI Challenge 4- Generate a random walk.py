from turtle import Turtle, Screen
import random
import turtle

# Colour scheme to be moved from the standard 0 to 1 to o to 255. NEED TO BE FROM THE TURTLE Class itself.
turtle.colormode(255)
timmy_the_turtle = Turtle()
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed(7)

# Todo 1: Turtle functions
def random_direction():
    direction =[0,90,180, 270]
    final_direction = random.choice(direction)
    return final_direction


def random_colour():
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    z = random.randint(0, 255)
    colour_scheme = (x, y, z)
    return colour_scheme

# Todo 2: Application of functions.
for i in range(0,100):
    timmy_the_turtle.pencolor(random_colour())
    timmy_the_turtle.forward(50)
    timmy_the_turtle.right(random_direction())


# Todo 3:  Exit on click function
my_screen = Screen()
my_screen.setup (width=150, height=150, startx=0, starty=0)
my_screen.exitonclick()