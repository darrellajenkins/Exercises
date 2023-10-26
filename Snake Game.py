# main.py

import turtle


from snake import Snake


from food import Food


from scoreboard import Scoreboard


import time


win = turtle.Screen()
win.setup(600, 600)
win.bgcolor("black")
win.title("Get On The Snake!")
win.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

win.listen()

win.onkey(snake.up, "Up")
win.onkey(snake.down, "Down")
win.onkey(snake.left, "Left")
win.onkey(snake.right, "Right")

gameon = True

while gameon:
    win.update()
    time.sleep(0.2)  # I changed this from 0.1 to 0.2 to slow the snake down a little bit
    snake.move()

    #  Detects a collision with food
    if snake.head.distance(food) < 25:
        food.refresh()
        snake.extend()
        scoreboard.keep_score()

    #  Detects a collision with a wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        gameon = False
        scoreboard.gameover()

    #  Detects a collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            gameon = False
            scoreboard.gameover()

win.exitonclick()

# scoreboard.py

import turtle


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.speed(0)
        self.penup()
        self.goto(0, 270)
        self.color("purple")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score:  {self.score}  High Score:  {self.highscore}", align="center", font=('Bauhaus 93', 18, 'normal'))

    def gameover(self):
        self.goto(0, 0)
        self.color("red")
        self.write(arg="GAME OVER", align="center", font=('Bauhaus 93', 24, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.update_scoreboard()

    def keep_score(self):
        self.score += 1
        self.update_scoreboard()

# food.py

import turtle


import random


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

# snake.py

import turtle


START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START:
            self.addseg(position)

    def addseg(self, position):
        sly = turtle.Turtle("square")
        sly.color("white")
        sly.shapesize(stretch_wid=0.45, stretch_len=0.85)  # added this to make it look more like a snake
        sly.penup()
        sly.goto(position)
        self.segments.append(sly)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.addseg(self.segments[-1].position())

    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[segnum - 1].xcor()
            newy = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            


