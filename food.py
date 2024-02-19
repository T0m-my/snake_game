from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.new_position()

    def new_position(self):
        random_x_cor = randint(-280, 280)
        random_y_cor = randint(-280, 280)
        random_position = (random_x_cor, random_y_cor)
        self.goto(random_position)
