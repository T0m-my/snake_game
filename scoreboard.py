from turtle import Turtle

FONT = ('courier', 20, 'normal')
ALIGNMENT = 'center'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.current_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.current_score}', False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.clear()
        self.current_score += 1
        self.update_scoreboard()
