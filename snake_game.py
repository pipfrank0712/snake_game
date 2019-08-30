#1. practicing class
#2. play with time/ introducing delay
#3. reccurring defination to build snake body 

import turtle
import time
import random
import math

delay = 0.1

# setup screen
wn = turtle.Screen()  # capitalize S
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width = 600, height = 600)
wn.tracer(0)    #turns of screen update

class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.speed(0)
		# self.shape("square")
		self.color("white")
		self.penup()
		self.hideturtle()
		self.goto(0,260)
		self.score = 0
		self.high_score = 0
		self.write("Score: 0 High Score: 0", align = "center", font =("Courier", 24, "normal"))
	def update_score_food(self):
		self.clear()
		self.score += 10
		self.write("Score: %s High Score: 0" %self.score, align = "center", font =("Courier", 24, "normal"))
	def update_score_highest(self):
		self.clear()
		if self.score > self.high_score:
			self.high_score = self.score
		self.write("Score: %s High Score: %s" %(self.score, self.high_score), align = "center", font =("Courier", 24, "normal"))			

# create snake head
class Head(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.speed(0)
		self.shape("square")
		self.color("black")
		self.penup()
		self.goto(0,0)
		self.direction = "stop"
	def move(self):
		if self.direction == "up":
			self.sety(self.ycor() + 20)
		if self.direction == "down":
			self.sety(self.ycor() - 20)
		if self.direction == "right":
			self.setx(self.xcor() + 20)
		if self.direction == "left":
			self.setx(self.xcor() - 20)
		if self.xcor() > 300 or self.xcor() < -300 or self.ycor() > 300 or self.ycor() < -300:
			time.sleep(1)
			self.goto(0,0)
			global delay   ##########make the delay changing global
			delay = 0.1
			self.direction = "stop"
			for segment in segments:
				segment.clear_segment()
			segments.clear()
			pen.update_score_highest()    ## introduced an instance in this class, should be in class or put outside (in main loop)?

	def turn_up(self):
		if self.direction != "down":
			self.direction = "up"
		else:
			return
	def turn_down(self):
		if self.direction != "up":
			self.direction = "down"
		else:
			return
	def turn_right(self):
		if self.direction != "left":
			self.direction = "right"
		else:
			return
	def turn_left(self):
		if self.direction != "right":
			self.direction = "left"
		else:
			return
	def is_collision(self, object):
		a = self.xcor() - object.xcor()
		b = self.ycor() - object.ycor()
		if math.sqrt(a**2 + b**2) < 20:
			return True
		else:
			return False


# create snake food
class Food(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.speed(0)
		self.shape("circle")
		self.color("red")
		self.penup()
		self.goto(random.randint(-280,280), random.randint(-280,280))

class Segment(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("grey")
		self.penup()
		self.speed(0)
	def clear_segment(self):
		self.goto(1000,1000)

# create instances
head = Head()
food = Food()
segments = []
pen = Pen()

#bonding keyboard
turtle.listen()
turtle.onkey(head.turn_up, "Up")
turtle.onkey(head.turn_down, "Down")
turtle.onkey(head.turn_left, "Left")
turtle.onkey(head.turn_right, "Right")
#main game loop
while True:
	wn.update()

	if head.is_collision(food):
		food.goto(random.randint(-280,280), random.randint(-280,280))
		pen.update_score_food()
		segment = Segment()
		segments.append(segment)

		delay -= 0.005  # speed up head speed while become longer	

		# move the last one into previous one's position
	for i in range(len(segments)-1, 0, -1):
		x = segments[i - 1].xcor()
		y = segments[i - 1].ycor()
		segments[i].goto(x,y)	
		# move the segement 0 to where head is
	if len(segments) > 0:
		segments[0].goto(head.xcor(), head.ycor())		

	head.move()   ## move after set segment 0 to avoid overlap // before collision check for avoid alway reporting collision to segment 0


	for segment in segments:
		if head.is_collision(segment):
			for segment in segments:
				segment.clear_segment()
			segments.clear()
			time.sleep(1)
			head.goto(0,0)
			pen.update_score_highest()
			delay = 0.1    # reset delay



	time.sleep(delay)





wn.mainloop()
