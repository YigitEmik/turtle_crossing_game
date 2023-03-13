import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Game Scene
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#Turtles(Cars, Player, Scoreboard)
cars = CarManager()
turtle = Player()
score = Scoreboard()

#Key press
screen.onkeypress(turtle.move, "Up")

#Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    
    #Collision
    for car in cars.all_cars:
        if turtle.distance(car) < 25:
            game_is_on = False
    cars.delete_cars()
    
    #New Level
    if turtle.ycor() >= 300:
        cars.new_level()
        turtle.new_level()
        score.new_level()
#Game Over
if game_is_on == False:
    time.sleep(0.1)
    screen.update()
    score.game_over()
screen.exitonclick()

        
    
    
