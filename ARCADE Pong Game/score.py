from turtle import Turtle
FONT = ("Arial",60,"bold")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.leftscore = 0
        self.rightscore = 0
        self.left_score()
        self.right_score()

    def left_score(self):
        self.penup()
        self.goto(x=-80,y=210)
        self.pendown()
        self.write(self.leftscore,font=FONT)
    def right_score(self):
        self.penup()
        self.goto(40,210)
        self.pendown()
        self.write(self.rightscore,font=FONT)
    def winner(self):
        self.pencolor("green")
        self.clear()
        self.goto(-260,0)
        self.write("GAME OVER!",font=FONT)
        self.goto(-100,-80)
        self.write(f"{self.leftscore} : {self.rightscore}",font=FONT)
