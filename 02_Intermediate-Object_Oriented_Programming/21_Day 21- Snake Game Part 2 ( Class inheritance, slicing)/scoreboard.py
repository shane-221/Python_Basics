from turtle import Turtle

# Constants
ALIGNMENT= "center"
FONTS= ("Arial", 15, "normal")

class Scoreboard( Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.score=0
        self.track_score()

    def track_score(self):
        self.clear()
        self.write(f"Score:{self.score}", False,align=ALIGNMENT, font=FONTS)

    def increase_score(self):
        self.score+=1
        self.track_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over")

