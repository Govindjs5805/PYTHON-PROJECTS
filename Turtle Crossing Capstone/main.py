from turtle import Turtle,Screen
from block import Block
from score import Score
import time
screen = Screen()
screen.bgcolor("white")
screen.setup(width=800,height=600)
screen.tracer(0)
ammalu = Turtle()
ammalu.penup()
ammalu.goto(0,-280)
ammalu.shape("turtle")
ammalu.shapesize(stretch_wid=1.2,stretch_len=1.2)
ammalu.left(90)
segments = []
def reset():
    ammalu.goto(0,-280)
def run():
    ammalu.forward(10)
j=6
k=6
score = Score()
ammalu.color("black")
screen.listen()
screen.onkeypress(fun=run,key="space")
game_is_on = True
while game_is_on == True:
    screen.update()
    time.sleep(0.1)
    if j%k==0:
        blocks = Block()
    segments.append(blocks)
    j+=1
    for i in segments:
        if ammalu.distance(i) < 20:
            score.lose()
            game_is_on=False
    for i in segments:
        i.move()
    if ammalu.ycor() > 300:
        score.level+=1
        score.levelup()
        blocks.speed+=5
        reset()


    if k==3:
        screen.clear()
        score.win()
        game_is_on=False




screen.exitonclick()
