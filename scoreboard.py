from turtle import Turtle
from food import Food
from snake import Snake

class Scoreboard(Turtle):
    
    def __init__(self):
        super(). __init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        
    def draw_line(self):
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-280,290)
        self.pendown()
        self.forward(560)
        
    def write_score(self):
        self.color('white')
        self.penup()
        self.goto(0,290)
        self.write(f"Score: {self.score} High Score: {self.high_score}",False,align='center', font=('Courier', 20, 'normal'))
        self.hideturtle()
        self.draw_line()
        
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()
        
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over",align='center', font=('Courier', 20, 'normal'))
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.clear()
        self.write_score()
            
            
        