from turtle import Turtle


class Paddle:

    def __init__(self):
        self.board_list = []
    def create_board(self, side):
        # Todo: Create the paddle

        for i in range(0, 5):
            square = Turtle()
            square.penup()
            square.shape("square")
            square.color("white")
            square.goto(side)
            self.board_list.append(square)
            x_cor = side[0]

            y_cor = side[1] - 20
            side = (x_cor, y_cor)

    def up(self):
        if self.board_list[0].ycor()<290:        # making sure there are boundary conditions for the extent to go down.
            for square in self.board_list:
                new_y = square.ycor()+20
                square.goto(square.xcor(),new_y)

    def down(self):
        if self.board_list[-1].ycor()>-280:       # making sure there are boundary conditions for the extent to go down.
            for square in self.board_list:
                new_y = square.ycor()-20
                square.goto(square.xcor(),new_y)
