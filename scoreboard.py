from turtle import Turtle


SCORE_FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 50, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Level: {self.score}', False, align='center', font=SCORE_FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', True, align='center', font=GAME_OVER_FONT)

    def incr_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



