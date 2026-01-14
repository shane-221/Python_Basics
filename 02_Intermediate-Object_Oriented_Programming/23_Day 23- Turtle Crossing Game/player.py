from turtle import Turtle

# Todo: All constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player_Turtle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")

    def start_position(self):
        self.goto(STARTING_POSITION)
    def up(self):
        self.forward(MOVE_DISTANCE)

    def right (self):
        self.setheading(0)
        self.forward(10)
        self.setheading(90)

    def left (self):
        self.setheading(180)
        self.forward(10)
        self.setheading(90)


