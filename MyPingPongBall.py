import turtle
import os
wn=turtle.Screen()
wn.title("My PingPong Ball")
wn.bgcolor("blue")
#wn.bgpic("background.png")
wn.setup(width=900, height=600)
#icon=turtle.image.load('icon.png')
#icon = "icon.png"
#turtle.display.set_icon(icon)
wn.tracer(0)

# Score
score_A=0
score_B=0

# Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-400,0)

# Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(400,0)

# PingPong Ball
ppball=turtle.Turtle()
ppball.speed(0)
ppball.shape("circle")
ppball.color("orange")
ppball.penup()
ppball.goto(0,0)
ppball.dx=0.3
ppball.dy=-0.3

# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0     Player B: 0", align="center",font=("Comic Sans MS",26,"normal"))
# Function
def Up_paddle_a():
   y=paddle_a.ycor()
   y+=20
   paddle_a.sety(y)

def Down_paddle_a():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def Up_paddle_b():
   y=paddle_b.ycor()
   y+=20
   paddle_b.sety(y)

def Down_paddle_b():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

# Specific Key Of Keyboard
wn.listen()
wn.onkeypress(Up_paddle_a,"w")
wn.onkeypress(Down_paddle_a,"s")
wn.onkeypress(Up_paddle_b,"Up")
wn.onkeypress(Down_paddle_b,"Down")

# Main Game Loop
while True:
    wn.update()
    # PingPong Ball Moving
    ppball.setx(ppball.xcor()+ppball.dx)
    ppball.sety(ppball.ycor()+ppball.dy)

    # Border Binding
    if ppball.ycor()>290:
        ppball.sety(290)
        ppball.dy *= -1

    if ppball.ycor() < -290:
            ppball.sety(-290)
            ppball.dy *= -1

    if ppball.xcor() > 440:
            ppball.goto(0,0)
            ppball.dx *= -1
            score_A += 1
            pen.clear()
            pen.write("Player A: {}     Player B: {}".format(score_A,score_B), align="center", font=("Comic Sans MS", 26, "normal"))

    if ppball.xcor() < -440:
            ppball.goto(0,0)
            ppball.dx *= -1
            score_B += 1
            pen.clear()
            pen.write("Player A: {}     Player B: {}".format(score_A, score_B), align="center", font=("Comic Sans MS", 26, "normal"))

    # Paddle and PingPong Ball collision
    if (ppball.xcor()>390 and ppball.xcor()<400) and (ppball.ycor()<paddle_b.ycor()+40 and ppball.ycor()>paddle_b.ycor()-40):
        ppball.setx(390)
        ppball.dx *= -1

    if (ppball.xcor()<-390 and ppball.xcor()>-400) and (ppball.ycor()<paddle_a.ycor()+40 and ppball.ycor()>paddle_a.ycor()-40):
        ppball.setx(-390)
        ppball.dx *= -1





