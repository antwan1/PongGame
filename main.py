from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import  time
from score import Scoreboard
# Screen Options
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, startx=600)
screen.listen()
screen.tracer(0)
# Paddle


paddle_left = Paddle((350, 0))
paddle_right = Paddle((-350, 0))

# paddle keys

pong_ball = Ball()
score = Scoreboard()

screen.onkey(paddle_left.go_up, "Up")
screen.onkey(paddle_left.go_down, "Down")

screen.onkey(paddle_right.go_up, "w")
screen.onkey(paddle_right.go_down, "s")
game_is_on = True
while game_is_on:
    time.sleep(0.1)

    screen.update()

    pong_ball.move_ball()

    if pong_ball.ycor() > 350 or pong_ball.ycor() < -350:
        pong_ball.bounce_back_neg()

    if pong_ball.distance(paddle_left) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(paddle_right) < 50 and \
            pong_ball.xcor() -320:
        pong_ball.bounce_back_pos()

    if pong_ball.xcor() > 380:
        pong_ball.reset_position
        score.score_l()
    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        score.score_right



screen.exitonclick()
