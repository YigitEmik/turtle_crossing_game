from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#Cars
#  a-Randomly Generated on y-axis
#  b-Moves from right to left
#  c-Speeds up on each level

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.x = 10 #First car's X cor
        
    def create_car(self):
        global random_y
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 260)
        self.x += 30
        new_car.goto(self.x, random_y)
        self.all_cars.append(new_car)
            
    def new_level(self):
        self.car_speed += MOVE_INCREMENT
    
    def move_cars(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.car_speed
            car.setx(new_x)
            
    def delete_cars(self):
        for car in self.all_cars:
            if car.xcor() < -400:
                self.all_cars.remove(car)
                