from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()

screen.tracer(0)
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.bgcolor('black')

# xcor = 0
# for _ in range(3):
#     new_turtle = Turtle('square')
#     new_turtle.color('white')
#     new_turtle.setx(xcor)
#     xcor -= 20

snake = Snake()
snake_food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # make snake move
    snake.move()

    # grow snake length
    if snake.snake_head.distance(snake_food) < 15:
        snake.grow_snake()
        snake_food.new_position()
        scoreboard.increment_score()

    # collision into wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 270 or snake.snake_head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        snake.reset_snake()
        snake_food.new_position()
        scoreboard.reset_()

    # collision into snake body

    # for segment in snake.segments:
    #     if segment == snake.snake_head:
    #         pass
    #     elif snake.snake_head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    #
    # or
    #
    # segments = snake.segments[1:]
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            snake.reset_snake()
            snake_food.new_position()
            scoreboard.reset_()

screen.exitonclick()
