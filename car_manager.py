from turtle import Turtle
from car_maker import Car
import random

MOVE_INCREMENT = 10
STARTING_POS = 310


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = MOVE_INCREMENT



    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Car()
            self.cars.append(new_car)



    def move_car(self):
        for car in self.cars:
            car.create_car()
            car.move_forward(self.car_speed)



    def incr_car_speed(self):
        self.car_speed += 5