# TODO: Preparatory stuff
from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


# Todo: Creation of the screen
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Todo: Creation of the Ball

ball=  Ball()

# Todo: Creation of the scoreboard
scoreboard= Scoreboard()

# Todo: Creating two boards from the Paddle class
R_PADDLE=(310,50)
L_PADDLE=(-310,50)

r_board= Paddle()
r_board.create_board(side = R_PADDLE)
l_board= Paddle()
l_board.create_board(side=L_PADDLE)

# Todo: Being able to move the paddle
            # For right paddle
screen.listen()
screen.onkey(r_board.up, "Up")
screen.onkey(r_board.down, "Down")

            # For left Paddle
screen.listen()
screen.onkey(l_board.up, "w")
screen.onkey(l_board.down, "s")

# Todo : Need to update from the changes since the tracer is off.
game_is_on = True
ball.direction()
while game_is_on:

    screen.update()
    time.sleep(ball.move_speed)
    if -400<ball.xcor()<400:
        ball.move()
        ball.detect_collision(
                            paddle_list = r_board.board_list,
                            main_length_angle=(135, 225),
                            upper_width_angle=(120, 160),
                            lower_width_angle=(200, 240)
                            )
        ball.detect_collision(
                            paddle_list=l_board.board_list,
                            main_length_angle=(315,360),
                            upper_width_angle=(30,60),
                            lower_width_angle=(300,330)
                            )
    elif ball.xcor()>400 :
        ball.reset_position(bounce_right=False)
        scoreboard.l_point()

    elif ball.xcor()<-400:
        ball.reset_position(bounce_right=True)
        scoreboard.r_point()





# Todo: Exit on click function
screen.exitonclick()