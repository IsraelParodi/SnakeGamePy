from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.set_score()

    def set_score(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.clear()

        with open("scores.txt") as file:
            self.high_score = int(file.read())

        self.write(
            f"Score: {self.score}       High Score: {self.high_score}",
            True,
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.set_score()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.color("white")
        self.write("Game Over", True, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scores.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.set_score()
