from turtle import Turtle, Screen

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
new_turtle=[]
bla=0

for _ in range (3):
    tim = Turtle("square")
    tim.color("white")
    new_turtle.append(tim)
for turtles in new_turtle:
    turtles.goto(x=bla, y=0)
    bla+=20




























screen.exitonclick()