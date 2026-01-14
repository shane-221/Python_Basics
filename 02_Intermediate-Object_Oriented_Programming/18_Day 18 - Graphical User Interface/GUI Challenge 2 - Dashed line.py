from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

# Todo 1: Turtle challenges
    # Todo 2.B: Draw a dashed line
for i in range(1,10):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)

# Exit on click function
my_screen = Screen()
my_screen.exitonclick()