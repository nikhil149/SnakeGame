from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align="center", font=("Arial", 24, "normal"))
    #
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    # def set_high_score(self):
    #     self.clear()
    #     self.write(f"High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0

        self.update_score()



