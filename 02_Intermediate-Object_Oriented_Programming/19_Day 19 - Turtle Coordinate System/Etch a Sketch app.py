from turtle import Turtle, Screen

tim= Turtle()
screen = Screen()

# Todo: Functionality of the movements
def move_forward():
    tim.forward(10)
def move_left():
    tim.left(10)
def move_right():
    tim.right( 10)
def move_backwards():
    tim.back(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
# Todo: Connect the functions to the keys
screen.listen()
                # Need to tell the key functions to listen to  the keys
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(clear, "c")

# Todo: Exit only when clicked
screen.exitonclick()
    