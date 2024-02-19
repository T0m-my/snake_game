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
        self.high_score = self.retrieve_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.current_score} High score: {self.high_score}', False, align=ALIGNMENT, font=FONT)

    def reset_(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            # self.update_scoreboard()
            self.save_high_score()
        self.current_score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.current_score += 1
        self.update_scoreboard()

    def retrieve_high_score(self):
        with open('data.txt', mode='r') as current_high_score:
            return int(current_high_score.read())

    def save_high_score(self):
        with open('data.txt', mode='w') as current_high_score:
            current_high_score.write(f'{self.high_score}')
