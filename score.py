from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()

        self.hideturtle()
        self.update_scoreboard_right()

    def score_l(self):
        self.score_left += 1
        self.update_scoreboard_right()

    def score_r(self):
        self.score_right += 1
        self.update_scoreboard_right()

    def update_scoreboard_right(self):
        self.clear()
        self.goto(-150, 350)
        self.write(f"Score {self.score_left}", align="left", font=("Arial", 24, "normal"))
        self.goto(150, 350)
        self.write(f"Score {self.score_right}", align="left", font=("Arial", 24, "normal"))
