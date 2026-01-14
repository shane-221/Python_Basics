from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
open("my_file.txt")

# Todo: Initial prep of the code environment
screen= Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Stops the automatic movement


# Todo : Building of the snake body
snake = Snake()
food = Food()
score= Scoreboard()


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
    # Todo: Detect whether the food and the snake collide.
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Todo: Detecting the corner of the game and end the game when the snake hits the wall.
    if snake.head.xcor()> 280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset()
        snake.reset()
    # Todo: Detect collision with its own tail.
        # Done by checking if head collides with any aspect of the tail. Then trigger end of game sequence.
        # Could also do it using the position of each of the modules in the list. But this would be a longer process.
    for i in snake.number_of_snakes[1:]:
        if  snake.head.distance(i)<10:
            score.reset()
            snake.reset()
















# Todo: Exit screen.
screen.exitonclick()