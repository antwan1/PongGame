from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.shapesize(stretch_wid=1)
        self.y_move = 10
        self.x_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_back_neg(self):
        self.y_move *= -1

    def bounce_back_pos(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_back_pos()

    # def bounce_back_pos(self):
    #     pos_y = self.ycor() + 0.12
    #     self.goto(self.xcor(), pos_y)
    #
    # def bounce_back_left(self):
    #     right_bounce = self.xcor() - 0.12
    #     self.goto(self.xcor(), right_bounce)
    #
    # def bounce_back_right(self):
    #     left = self.xcor() + 0.12
    #     self.goto(self.xcor(), left)
