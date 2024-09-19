from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(-280, 250)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.home()
        self.write(f"Game Over.", align="center", font=FONT)
