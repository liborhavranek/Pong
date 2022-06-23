from turtle import Turtle

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.l_score = 0
		self.r_score = 0
		self.penup()
		self.color("white")
		self.hideturtle()
		self.update_score()

	def update_score(self):
		self.clear()
		self.goto(-300, 200)
		self.write(f" {self.l_score}", align='left', font=('Arial', 50, 'normal'))
		self.goto(300, 200)
		self.write(f" {self.r_score}", align='left', font=('Arial', 50, 'normal'))


	def l_point(self):
		self.l_score += 1
		self.update_score()

	def r_point(self):
		self.r_score += 1
		self.update_score()



