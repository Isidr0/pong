from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, paddle_pos):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        # turtle size start as 20x20. i guess turtlesize multiplies original turtle size.
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(paddle_pos)
        self.color("white")

    def move_paddle_up(self):
        new_y = self.ycor() + 20
        self.setposition(self.xcor(), new_y)

    def move_paddle_down(self):
        new_y = self.ycor() - 20
        self.setposition(self.xcor(), new_y)
