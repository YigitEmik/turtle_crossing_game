from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

#Player
# a-Moves Up
# b-Next level if player touches top of the game screen

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def new_level(self):
        self.goto(STARTING_POSITION)
        
