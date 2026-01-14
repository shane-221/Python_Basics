from turtle import Screen
from snake import Snake
import time
# Todo: Initial prep of the code environment
screen= Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Stops the automatic movement


# Todo : Building of the snake body
snake = Snake()

# Todo : Application of the Keystroke
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Todo: Getting the snake to move
game_is_on=True
while game_is_on:
    screen.update()        # Updating the movement of the snake with a timeout to see.
    time.sleep(0.1)

    snake.move()















# Todo: Exit screen.
screen.exitonclick()