from turtle import Turtle
FONT = ("Arial",100,"bold")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level=1
        self.goto(-390,260)
        self.pendown()
        self.hideturtle()
        self.pencolor("black")
        self.write(f"LEVEL : {self.level}",font=("Arial",20,"bold"))
    def levelup(self):
        self.penup()
        self.clear()
        self.goto(-390,260)
        self.pendown()
        self.pencolor("black")
        self.write(f"LEVEL : {self.level}",font=("Arial",20,"bold"))
    def win(self):
        self.penup()
        self.goto(-320,0)
        self.pendown()
        self.pencolor("red")
        self.write("YOU WIN!",font=FONT)
    def lose(self):
        self.penup()
        self.pencolor("red")
        self.goto(x=-120,y=0)
        self.pendown()
        self.write("GAME OVER !",font=("Arial",30,"bold"))
