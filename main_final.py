from turtle import Screen
from snakee import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")
X_CRASH1= 280
X_CRASH2= -280
Y_CRASH1= 280
Y_CRASH2= -280

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on=True
score=0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    if snake.segments[0].distance(food)< 20:
        food.refresh()
        scoreboard.score_increase()
        snake.extend()
    if snake.segments[0].xcor()>290 or snake.segments[0].xcor()<-290:

        scoreboard.reset()
        snake.reset()
    if snake.segments[0].ycor()>290 or snake.segments[0].ycor()<-290:

        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:

        if snake.segments[0].distance(segment)<10:

            scoreboard.reset()
            snake.reset()

screen.exitonclick()