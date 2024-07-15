from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=640)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.write_score()
scoreboard.draw_line()


screen.listen()
screen.onkey(fun=snake.up,key='Up')
screen.onkey(fun=snake.down,key='Down')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.left, key='Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # detect collision

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -310:
        scoreboard.reset()
        snake.reset()
        
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    
    

screen.exitonclick()