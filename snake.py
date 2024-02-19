from turtle import Turtle

SEGMENT_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
LEFT_DIRECTION = 180
RIGHT_DIRECTION = 0
UP_DIRECTION = 90
DOWN_DIRECTION = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def create_snake(self):
        for position in SEGMENT_POSITIONS:
            self.add_segment(position)

    def grow_snake(self):
        self.add_segment(self.segments[-1].position())

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x_cor = self.segments[segment_num - 1].xcor()
            new_y_cor = self.segments[segment_num - 1].ycor()
            new_position = (new_x_cor, new_y_cor)
            self.segments[segment_num].goto(new_position)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN_DIRECTION:
            self.snake_head.setheading(UP_DIRECTION)

    def down(self):
        if self.snake_head.heading() != UP_DIRECTION:
            self.snake_head.setheading(DOWN_DIRECTION)

    def left(self):
        if self.snake_head.heading() != RIGHT_DIRECTION:
            self.snake_head.setheading(LEFT_DIRECTION)

    def right(self):
        if self.snake_head.heading() != LEFT_DIRECTION:
            self.snake_head.setheading(RIGHT_DIRECTION)
