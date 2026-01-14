from  turtle import Turtle
import random
import time

ANGLE =290


class Ball(Turtle):

    def __init__(self):                 # Todo: Changes everything into turtle class
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed =0.1
                                    # Todo: Turtle to move while accounting for the vertical boundaries
    def move(self):
        if self.ycor() >= 280:          # sTART WITH THE SPECIFIC CASES THEN MOVE DOEN TO THE GENERAL ONES
            angle= random.randint(280, 350)
            self.setheading(angle)      # Can also run another method. Where we increase or decrease by 10.
            self.forward(15)            ## But there is a lack of dynamism for the angle. Hence, I  used my
                                        ### own method.
        elif self.ycor()<=-280:
            angle= random.randint(0, 90)
            self.setheading(angle)
            self.forward(15)

        elif -280 < self.ycor() < 280:
            self.forward(15)


                                    # Todo: setting of the initial direction. Need to pull a random angle though
    def direction(self):
        self.setheading(ANGLE)


                                    # Todo: Detect collisions relative to the side of the paddle
                                    ## Need to define the angles of rebound separately. Relative to where the paddle is
    def detect_collision(self, paddle_list, main_length_angle, upper_width_angle, lower_width_angle):
        self.move_speed *= 0.9
        for item in paddle_list:
                    # Looping through each of the square from the paddle. Finding the leftmost coordinate. Then pushing
                    ## the ball back
            left_side = (item.xcor()-15, item.ycor())
            upper_side= (item.xcor(), item.ycor()+15)
            lower_side =(item.xcor(), item.ycor()-15)
                    # Left side of the paddle
            if self.distance(left_side)<10:
                angle = random.randint(*main_length_angle)
                self.setheading(angle)
                self.forward(30)
                break
                    # Upper side of the paddle
            elif self.distance(upper_side)<10:
                angle = random.randint(*upper_width_angle)
                self.setheading(angle)
                self.forward(30)
                break                   # Good idea to exit the loop given that only one point would be reached
                    # Lower side of the paddle
            elif self.distance(lower_side) < 10:
                angle = random.randint(*lower_width_angle)
                self.setheading(angle)
                self.forward(30)
                break

    def reset_position(self,bounce_right):
        time.sleep(0.2)
        self.move_speed = 0.1
        self.goto(0, 0)
        if bounce_right:
            self.setheading(random.randint(315,405))
        else:
            self.setheading(random.randint(135,225))
























