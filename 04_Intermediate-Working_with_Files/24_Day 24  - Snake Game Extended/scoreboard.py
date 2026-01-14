from turtle import Turtle

#Todo:  Constants
ALIGNMENT= "center"
FONTS= ("Arial", 15, "normal")

# Todo: Pulling the high score from the total games.
with open("data.txt", mode="r") as high_score:
    content = int(high_score.read())

class Scoreboard( Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.score=0
        self.high_score = content
        self.track_score()

    def track_score(self):
        self.clear()
        self.write(f"Score:{self.score}   High Score :{self.highscore}", False,align=ALIGNMENT, font=FONTS)

    def increase_score(self):
        self.score+=1
        self.track_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over")



    def reset(self ):
        if self.score > self.high_score:
            self.high_score = self.score
        # Saving the high score within the text file.
        with open("data.txt", mode = "w") as file:
            file.write(str(self.high_score))
        self.score = 0              # Ordering of the code matters
        self.track_score()



