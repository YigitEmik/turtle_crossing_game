from turtle import Turtle
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.level = 1
        self.color("black")
        self.goto(-280,250)
        self.write(f"Level: {self.level}",False, "left", FONT)
    
    def new_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}",False, "left", FONT)
        
    def game_over(self):
        self.clear()
        self.goto(-70,0)
        self.write(f"Game Over!\nLevel: {self.level}",False, "left", FONT)
        
        
        
        
