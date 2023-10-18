# SnakePong
# By Adam Liewehr

import turtle
import time
import random

delay = 0.1

wn = turtle.Screen()
wn.title("SnakePong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = 5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake_a head_a
head_a = turtle.Turtle()
head_a.speed(0)
head_a.shape("square")
head_a.color("white")
head_a.penup()
head_a.goto(200, 0)
head_a.direction = "stop"
segments_a = []

# Snake_b head_b
head_b = turtle.Turtle()
head_b.speed(0)
head_b.shape("square")
head_b.color("orange")
head_b.penup()
head_b.goto(-200, 0)
head_b.direction = "stop"
segments_b = []

def go_up_a():
    if head_a.direction != "down":
        head_a.direction = "up"

def go_down_a():
    if head_a.direction != "up":
        head_a.direction = "down"

def go_left_a():
    if head_a.direction != "right":
        head_a.direction = "left"

def go_right_a():
    if head_a.direction != "left":
        head_a.direction = "right"

def go_up_b():
    if head_b.direction != "down":
        head_b.direction = "up"

def go_down_b():
    if head_b.direction != "up":
        head_b.direction = "down"

def go_left_b():
    if head_b.direction != "right":
        head_b.direction = "left"

def go_right_b():
    if head_b.direction != "left":
        head_b.direction = "right"

def move_a():
    if head_a.direction == "up":
        y = head_a.ycor()
        head_a.sety(y + 20)

    if head_a.direction == "down":
        y = head_a.ycor()
        head_a.sety(y - 20)

    if head_a.direction == "left":
        x = head_a.xcor()
        head_a.setx(x - 20)

    if head_a.direction == "right":
        x = head_a.xcor()
        head_a.setx(x + 20)

def move_b():
    if head_b.direction == "up":
        y = head_b.ycor()
        head_b.sety(y + 20)

    if head_b.direction == "down":
        y = head_b.ycor()
        head_b.sety(y - 20)

    if head_b.direction == "left":
        x = head_b.xcor()
        head_b.setx(x - 20)

    if head_b.direction == "right":
        x = head_b.xcor()
        head_b.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up_a, "Up")
wn.onkeypress(go_down_a, "Down")
wn.onkeypress(go_left_a, "Left")
wn.onkeypress(go_right_a, "Right")

wn.onkeypress(go_up_b, "w")
wn.onkeypress(go_down_b, "s")
wn.onkeypress(go_left_b, "a")
wn.onkeypress(go_right_b, "d")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

# Check for a collision with the food
    if head_a.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments_a.append(new_segment)

    if head_b.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments_b.append(new_segment)

# Move the end segments_a first in reverse order
    for index in range(len(segments_a) - 1, 0, -1):
        x = segments_a[index - 1].xcor()
        y = segments_a[index - 1].ycor()
        segments_a[index].goto(x, y)

    for index in range(len(segments_b) - 1, 0, -1):
        x = segments_b[index - 1].xcor()
        y = segments_b[index - 1].ycor()
        segments_b[index].goto(x, y)

    # Move segment 0 to where the head_a is
    if len(segments_a) > 0:
        x = head_a.xcor()
        y = head_a.ycor()
        segments_a[0].goto(x, y)

    move_a()

    if len(segments_b) > 0:
        x = head_b.xcor()
        y = head_b.ycor()
        segments_b[0].goto(x, y)

    move_b()

    # Check for collision between the ball and the snake segments and head
    for segment in segments_a:
        if segment.distance(ball) < 20:
            ball.dx *= -1
    if head_a.distance(ball) < 20:
        ball.dx *= -1

    for segment in segments_b:
        if segment.distance(ball) < 20:
            ball.dx *= -1
    if head_b.distance(ball) < 20:
        ball.dx *= -1

    # Check for head_a collision with the body segments_a
    for segment in segments_a:
        if segment.distance(head_a) < 20:
            head_a.goto(200, 0)
            head_a.direction = "stop"

            # Hide the segments_a
            for segment in segments_a:
                segment.goto(1000, 1000)

            # Clear the segments_a list
            segments_a.clear()

    for segment in segments_b:
        if segment.distance(head_b) < 20:
            head_b.goto(-200, 0)
            head_b.direction = "stop"

            # Hide the segments_b
            for segment in segments_b:
                segment.goto(1000, 1000)

            # Clear the segments_b list
            segments_b.clear()

    # check if snake goes off-screen, if so reset position
    if head_a.xcor() >= 400 or head_a.ycor() >= 300 or head_a.xcor() <= -400 or head_a.ycor() <= -300:
        head_a.goto(200, 0)
        head_a.direction = "stop"

        # Hide the segments_a
        for segment in segments_a:
            segment.goto(1000, 1000)

        # Clear the segments_a list
        segments_a.clear()

    if head_b.xcor() >= 400 or head_b.ycor() >= 300 or head_b.xcor() <= -400 or head_b.ycor() <= -300:
        head_b.goto(-200, 0)
        head_b.direction = "stop"

        # Hide the segments_b
        for segment in segments_b:
            segment.goto(1000, 1000)

        # Clear the segments_b list
        segments_b.clear()

    time.sleep(delay)