from turtle import Turtle
class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(3)
        self.goto(0,295)
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.right(90)
        self.draw()
    def draw(self):
        for i in range(20):
            self.forward(20)
            self.penup()
            self.forward(15)
            self.pendown()
    def winner(self):
        self.clear()
