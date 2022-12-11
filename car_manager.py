import random
from turtle import Turtle


#initialize global variables
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
STARTING_MOVE_DISTANCE = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        '''Create car functionality.'''
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)


    def move_cars(self):
        '''Move car across screen.'''
        for car in self.all_cars:
            car.backward(self.car_speed)


    def level_up(self):
        '''Increase speed of cars if level is completed.'''
        self.car_speed += MOVE_INCREMENT