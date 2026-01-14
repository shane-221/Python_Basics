import random
import turtle
from turtle import Turtle, Screen

colours = ["red", "orange", "yellow", "green", "blue"]
names = ["red", "orange", "yellow", "green", "blue" ]

# Todo:  Set up of the screen
screen= Screen()
screen.setup(500, 400)
    # Input from the screen function
user_choice = screen.textinput(title= "Make your bet", prompt="Which turtle will win the game?")

# Todo:  Building of the turtle. In essence, create instances with unique states.
y=-180
x=-230
list_of_turtles=[]
for i in range(0, 5):
    names[i]=Turtle()# Choosing the name of the turtle
    names[i].shape("turtle")
    names[i].penup()
    names[i].color(colours[i])  # Choosing the colour of the turtle
    names[i].goto(x=x, y=y)
    y+=80
    list_of_turtles.append(names[i])
print(type(list_of_turtles[1]))


# Todo : Adjusting the pace of the game to get a winner
if user_choice:
    is_race_on = True


while is_race_on:
    for turtles in list_of_turtles:
            # Moving at different speeds
        random_speed = random.randint(0, 10)
        turtles.forward(random_speed)
            # Checking the colour
        if turtles.xcor()>230:
            is_race_on = False
            winning_colour= turtles.pencolor()
            if winning_colour==user_choice:
                print(f"You've won. The winning colour is {winning_colour} ")
            else:
                print(f"You've lost. The winning colour is {winning_colour} ")







screen.exitonclick()