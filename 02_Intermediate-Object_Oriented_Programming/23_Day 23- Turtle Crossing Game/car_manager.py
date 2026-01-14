from turtle import Turtle
import random


# Todo: Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
XCOR= 320


class Cars(Turtle):
        # Todo: Import all the classes from the modules and Variables that are used.
    def __init__(self):
        super().__init__()
        self.penup()
        self.one_car = []
        self.all_car = []
        self.level = 3          # Not placed any limits on the speed of the game. But can do it if I want to.




        # Todo: creating one car with 2 squares and placing them into a list along a random Y
    def create_one_car(self,x_cor, y_cor):
        one_car=[]
        for i in range(0,2):
            i= Turtle()
            i.shape("square")
            i.penup()
            i.goto(x_cor, y_cor)
            one_car.append(i)
            x_cor = i.xcor()+20
            y_cor =i.ycor()
        self.hideturtle()
        self.all_car.append(one_car)

        random_colour= random.choice(COLORS)
        one_car[0].color(random_colour)
        one_car[1].color(random_colour)


        # Todo: moving each of the turtles within the list  by 5 units forward
    def move_one_car(self):
        for i in self.all_car:
            self.penup()
            for part in i:
                x_cor =part.xcor()
                y_cor =part.ycor()
                part.goto(x_cor-self.level, y_cor)

        # Todo: Creating multiple squares that do the same functionality with a time lag
    def car_manager(self):
        for i in range(0, 30):
            any_random_y = random.randint(-260, 260)
            any_random_x = random.randint(320, 1000)
            self.create_one_car(any_random_x,any_random_y)

        # Todo: Looping the cars so it appears again at a random place
    def loop_the_cars(self):
        for i in self.all_car:
            # Todo: need to recycle the old car to a random location
            if i[1].xcor()<-400:
                any_random_y = random.randint(-260, 280)
                any_random_x = random.randint(320, 1000)
                i[0].goto(any_random_x, any_random_y)

                i[1].goto(any_random_x + 20, any_random_y)
    def speed_up(self):
        self.level+=1












