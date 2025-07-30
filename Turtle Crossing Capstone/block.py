from turtle import Turtle
import random
COLOURS = ["blue","green","yellow","red","orange","purple","violet","indigo"]
class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.penup()
        self.speed=5
        self.random_y=random.randint(-240,265)
        self.goto(x=440,y=self.random_y)
        self.color(random.choice(COLOURS))
        self.right(180)
    def move(self):
        self.forward(self.speed)
