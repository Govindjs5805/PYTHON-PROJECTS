from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x = 10
        self.y = 10
        self.sleeptime = 0.05

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x,new_y)
    def bounce(self):
        self.y *= -1
    def hit(self):
        self.x *= -1
