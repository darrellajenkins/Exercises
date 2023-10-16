# Main.py

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
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.keep_score()

    #  Detects a collision with a wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameon = False
        scoreboard.gameover()

    #  Detects a collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            gameon = False
            scoreboard.gameover()

    #  ALTERNATIVE CODE FOR detecting a collision with tail:
    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment) < 10:
    #         gameon = False
    #         scoreboard.gameover()

win.exitonclick()

#
