from turtle import Turtle, Screen
from snakee import Snake
from food import Food
# tim=Turtle()
# foods=Food()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores=0
        with open("data.txt") as data:
            self.highscore=int(data.read())

        self.penup()
        self.hideturtle()
        self.color("aquamarine")
        self.goto(0,270)
        self.write(f"Score: {self.scores} High score: {self.highscore}", align="center", font=("Courier",15, "bold"))
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.scores} High score: {self.highscore}", align="center", font=("Courier",15, "bold"))

    def score_increase(self):
        self.scores+=1
        self.clear()
        self.write(f"Score: {self.scores} High score: {self.highscore}", align="center", font=("Courier", 15, "bold"))
    def reset(self):
        if self.scores>self.highscore:
            self.highscore=self.scores
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.scores=0
        self.update_scoreboard()







    # def game_over(self):
    #     self.penup()
    #     self.goto(0,0)
    #     self.pencolor("yellow")
    #     self.hideturtle()
    #     self.write("GAME OVER", align="center", font=("Courier", 25, "bold") )




# print(score)
# screen=Screen()
# screen.exitonclick()



# tim.penup()
#         tim.color("aquamarine")
#         tim.goto(0,280)