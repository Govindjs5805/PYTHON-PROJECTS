from turtle import Turtle

class Block(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.color("white")
        self.penup()
        self.left(90)
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.goto(pos)
    def up(self):
        if self.ycor() <= 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(),new_y)

    def down(self):
        if self.ycor() >= -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
