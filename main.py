from turtle import Screen
from score_board import Scoreboard
from paddle import Paddle
from ball import Ball
import time

my_screen = Screen()
my_screen.title("Paddle Game")
my_screen.setup(1200, 600)
my_screen.bgcolor("black")
my_screen.tracer(0)

ball = Ball()
l_paddle = Paddle((-560, 0))
r_paddle = Paddle((560, 0))
score_board = Scoreboard()


my_screen.listen()
my_screen.onkey(l_paddle.go_up, "w")
my_screen.onkey(l_paddle.go_down, "s")
my_screen.onkey(r_paddle.go_up, "o")
my_screen.onkey(r_paddle.go_down, "l")

game_is_on = True
while game_is_on:
	time.sleep(ball.move_speed)
	ball.move_of_ball()
	my_screen.update()

	# collision with wall
	if ball.ycor() > 290 or ball.ycor() < -290:
		ball.bounce_y()

	# collision with paddle
	if ball.distance(r_paddle) < 50 and ball.xcor() > 530 or ball.distance(l_paddle) < 50 and ball.xcor() < -530:
		print("contact")
		ball.bounce_x()

	# right paddle miss the ball
	if ball.xcor() > 600:
		ball.reset_position()
		score_board.l_point()

	if ball.xcor() < -600:
		ball.reset_position()
		score_board.r_point()


my_screen.exitonclick()
