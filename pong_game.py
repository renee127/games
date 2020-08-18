"""
   Version of classic pong game with simple program (no OOP).
"""
import os
import turtle

# TODO: offer user choices, play computer
# 2 player, how difficult, how fast
#  decrease the paddle as lose - how to work with 2 player
# add sounds

# Create interface window
win = turtle.Screen()
win.title('Version of Pong')
win.bgcolor('grey')
win.setup(width = 800, height = 600)

# Use tracer to stop window from automatically updating
win.tracer(0)

# Initialize scoring variables
score_a = 0
score_b = 0

# First_paddle : left paddle
first_paddle = turtle.Turtle()
# Set speed & shape of paddle
first_paddle.speed(0)
first_paddle.shape('square')
# Resized paddle from 20,20 to 100, 10
first_paddle.shapesize(stretch_wid = 5, stretch_len = 0.5)
first_paddle.color('white')
first_paddle.penup() # So it doesn't draw trailing line
first_paddle.goto(-355, 0) # start location

# Second_paddle : right paddle
second_paddle = turtle.Turtle()
# Set speed & shape of paddle
second_paddle.speed(0)
second_paddle.shape('square')
# Resized paddle from 20,20 to 100, 10
second_paddle.shapesize(stretch_wid = 5, stretch_len = 0.5)
second_paddle.color('white')
second_paddle.penup() # So it doesn't draw trailing line
second_paddle.goto(355, 0) # start location

# Ball
ball = turtle.Turtle()
# Set speed & shape of paddle
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup() # So it doesn't draw trailing line
ball.goto(0, 0) # start location
ball.dx = 4 # dx meaning change in x
ball.dy = 4 # dy meaning change in y

# Pen to show scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup() # avoids the line
pen.hideturtle() # don't need to see it, just text
pen.goto(0,260)
pen.write('Player A: 0   Player B: 0', align='center', font=('Courier', 20))

# Functions to move objects
# Used small steps of 5 pixels for smoother AI
def first_paddle_up():
    y = first_paddle.ycor() 
    y += 5
    first_paddle.sety(y)

def first_paddle_down():
    y = first_paddle.ycor() 
    y -= 5
    first_paddle.sety(y)

def second_paddle_up():
    y = second_paddle.ycor() 
    y += 15
    second_paddle.sety(y)

def second_paddle_down():
    y = second_paddle.ycor() 
    y -= 15
    second_paddle.sety(y)

# Keyboard binding : arrows Up, Down
# Chose y/u vs w/s because of continuous movement
win.listen()
win.onkeypress(first_paddle_down, 'y')
win.onkeypress(first_paddle_up, 'u')
win.onkeypress(second_paddle_down, 'Down')
win.onkeypress(second_paddle_up, 'Up')

# Game loop 
while True:
    # Updates every time
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking consider size of ball (20 X 20)
    # adjusted some #s to inc illusion of bouncing
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # should reverse direction of ball
        os.system('afplay tom.wav&') # & to stop delay

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1 # should reverse direction of ball
        os.system('afplay tom.wav&') # & to stop delay

    if ball.xcor() > 380:
        ball.setx(380)
        ball.dx *= -1 # should reverse direction of ball
        score_a += 1 # score_A gets a point
        pen.clear() # must clear screen, otherwise it will write over itself
        pen.write('Player A: {}   Player B: {}'.format(score_a, score_b), \
            align='center', font=('Courier', 20))
        os.system('afplay tom.wav&') # & to stop delay

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1 # should reverse direction of ball
        score_b += 1 # score_B gets a point
        pen.clear() # must clear screen, otherwise it will write over itself
        pen.write('Player A: {}   Player B: {}'.format(score_a, score_b), \
            align='center', font=('Courier', 20))
        os.system('afplay tom.wav&') # & to stop delay

    # Paddle and ball collisions
    if (ball.xcor() < -340 and ball.xcor() > -350) and \
        (ball.ycor() < first_paddle.ycor() + 50) and \
        (ball.ycor() > first_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1                  
        os.system('afplay hat.wav&') # & to stop delay

    if (ball.xcor() > 340 and ball.xcor() < 350) and \
        (ball.ycor() < second_paddle.ycor() + 50) and \
        (ball.ycor() > second_paddle.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system('afplay hat.wav&') # & to stop delay

    # Reset if ball trapped between paddle and wall
    if (ball.xcor() < -355 and ball.xcor() > -400) and \
        (ball.ycor() < first_paddle.ycor() + 50) and \
        (ball.ycor() > first_paddle.ycor() - 50):
        #ball.goto(0,0)
        ball.dx *= -1
        os.system('afplay hat.wav&') # & to stop delay
    if (ball.xcor() > 355 and ball.xcor() < 400) and \
        (ball.ycor() < second_paddle.ycor() + 50) and \
        (ball.ycor() > second_paddle.ycor() - 50):
        #ball.goto(0,0)
        ball.dx *= -1
        os.system('afplay hat.wav&') # & to stop delay

    # Keep paddles in screen area via wraparound
    if first_paddle.ycor() > 300:
        first_paddle.sety(-300)
    if first_paddle.ycor() < -300:
        first_paddle.sety(300)    

    if second_paddle.ycor() > 300:
        second_paddle.sety(-300)
    if second_paddle.ycor() < -300:
        second_paddle.sety(300)

    # AI Player
    if first_paddle.ycor() < ball.ycor(): # and abs(first_paddle.ycor() - ball.ycor()) > 5: 
        first_paddle_up()
    elif first_paddle.ycor() > ball.ycor(): # and abs(first_paddle.ycor() - ball.ycor()) > 5: 
        first_paddle_down() 
    

