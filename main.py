from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create screen.
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
# print(ball.xcor().distance(0.0, 280.0))
scoreboard = Scoreboard()

screen.onkeypress(l_paddle.move_paddle_up, 'w')
screen.onkeypress(l_paddle.move_paddle_down, 's')
screen.onkeypress(r_paddle.move_paddle_up, 'i')
screen.onkeypress(r_paddle.move_paddle_down, 'k')

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # Detect if ball leaves screen on right side
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()


screen.exitonclick()