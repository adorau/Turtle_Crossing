from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.font = FONT
        self.lvl = 1
        self.scoreboard()

    def game_over(self):
        self.hideturtle()
        self.clear()
        self.write("Game Over", move=False, align='center', font=self.font)

    def scoreboard(self):
        self.hideturtle()
        self.clear()
        self.penup()
        self.goto(-100,250)
        self.write(f"Level: {self.lvl}", move=True, align='left', font=("Courier", 20, "normal"))
        self.lvl += 1
