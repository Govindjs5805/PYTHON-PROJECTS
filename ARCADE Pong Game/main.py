from turtle import Turtle,Screen
from score import Score
import time
from ball import Ball
from line import Line
from block import Block
screen = Screen()
screen.title("PONG GAME")
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)
score_board = Score()
line = Line()
over=False
left_block = Block((-380,0))
right_block = Block((370,0))
ball = Ball()

screen.listen()
screen.onkey(fun=right_block.up,key="Up")
screen.onkey(fun=right_block.down,key="Down")
screen.onkey(fun=left_block.up,key="w")
screen.onkey(fun=left_block.down,key="s")
while over==False:
    time.sleep(ball.sleeptime)
    screen.update()
    score_board.left_score()
    score_board.right_score()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -275:
        ball.bounce()
    if ball.distance(right_block) < 50 and ball.xcor()>340:
        ball.hit()
    elif ball.xcor() > 420:
        ball.goto(0,0)
        ball.hit()
        score_board.leftscore+=1
        time.sleep(0.5)
        score_board.clear()
    if ball.distance(left_block) <50 and ball.xcor() <-350:
        ball.hit()
    elif ball.xcor() < -400:
        ball.goto(0,0)
        ball.hit()
        score_board.rightscore += 1
        time.sleep(0.5)
        score_board.clear()
    if score_board.leftscore ==5 or score_board.rightscore==5:
        score_board.winner()
        line.winner()
        over=True



screen.exitonclick()
