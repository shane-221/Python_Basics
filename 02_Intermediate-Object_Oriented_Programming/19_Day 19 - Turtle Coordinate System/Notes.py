from turtle import Turtle, Screen

tim= Turtle()
screen = Screen()

# Todo 1: To get the computer to listen to a jey and then make a move. Need to first enable the Listen method.
## todo need to continue through the screen instance.
def move_forward():
    tim.forward(10)

screen. listen()
screen.onkey(move_forward, "space")
                            ## No need to add the parenthesis there and then. The parenthesis make it run there and then
screen.exitonclick()