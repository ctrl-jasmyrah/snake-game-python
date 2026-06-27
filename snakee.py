from turtle import Turtle
# import time

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
RIGHT=0
MOVE_DISTANCE=20
LEFT=180
class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:


            self.add_segments(position)
    def add_segments(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.speed("slowest")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def snake_move(self):


        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg_num - 1].xcor()
            y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cor, y_cor)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading()!=DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)

        self.segments.clear()
        self.create_snake()















# screen=Screen():
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.tracer(0)
# screen.title("My Snake Game")




# game_is_on=True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)







# screen.exitonclick()
