from turtle import Screen
from player import Player_Turtle
import time
from car_manager import Cars
from scoreboard import Scoreboard


# Todo: creating the screen function
screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

# Todo: Addition of the Plater Turtle
player= Player_Turtle()

# Todo: Creation of the Scoreboard
scoreboard = Scoreboard()

# Todo: Ability of the Player turtle to move
screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")

# Todo: Movement of the obstacles.
cars= Cars()
cars.car_manager()


# Todo: Screen update function
game_on= True

while game_on:
    time.sleep(0.1)
    screen.update()

    cars.move_one_car()
    cars.loop_the_cars()
    # Todo: What happens when the Turtle touches the cars--> exit loop

    for i in cars.all_car:
        for x in i:
            if player.distance(x)<20:
                game_on=False
                scoreboard.game_over()
    # Todo: what happens if the turtle clears the game.
    if player.ycor()>=280:
        player.start_position()
        cars.speed_up()
        scoreboard.increase_score()


# Todo: Exit on click function
screen.exitonclick()