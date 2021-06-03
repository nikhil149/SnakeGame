from turtle import Screen
import time
from food import Food
from snake import Snake
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("MySnake Game")
screen.tracer(0)

my_snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.right, "Right")
screen.onkey(my_snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # Detect collision with food
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        score.increase_score()

    # Detect Collision with wall
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        score.reset_score()
        my_snake.reset_snake()

    for seg in my_snake.segment:
        if seg == my_snake.head:
            pass
        elif my_snake.head.distance(seg) < 10:
            score.reset_score()
            my_snake.reset_snake()



screen.exitonclick()
