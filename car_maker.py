from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.body = Turtle('square')
        self.top = Turtle('circle')
        self.front = Turtle('circle')
        self.back = Turtle('circle')
        self.window_1 = Turtle('square')
        self.window_2 = Turtle('square')
        self.wheel_1 = Turtle('circle')
        self.wheel_2 = Turtle('circle')
        self.wheel_1_inside = Turtle('circle')
        self.wheel_2_inside = Turtle('circle')
        self.starting_pos()
        self.body_x = self.body.xcor()
        self.body_y = self.body.ycor()
        self.car_color = random.choice(COLORS)
        self.create_car()

    def starting_pos(self):
        self.body.penup()
        self.top.penup()
        self.front.penup()
        self.back.penup()
        self.window_1.penup()
        self.window_2.penup()
        self.wheel_1_inside.penup()
        self.wheel_2_inside.penup()
        self.wheel_1.penup()
        self.wheel_2.penup()
        self.body.goto(280, random.randint(-250, 250))
        self.hideturtle()


    def create_car(self):
        self.body.shapesize(.9, 1.5)
        self.top.shapesize(1)
        self.back.shapesize(0.8)
        self.body.color(self.car_color)
        self.top.color(self.car_color)
        self.top.color(self.car_color)
        self.front.color(self.car_color)
        self.back.color(self.car_color)
        self.wheel_1.color(self.car_color)
        self.wheel_2.color(self.car_color)



        self.window_1.shapesize(.2, .4)
        self.window_1.color('white')

        self.window_2.shapesize(.2, .3)
        self.window_2.color('white')

        self.wheel_1.shapesize(.5)
        self.wheel_1_inside.shapesize(.4)
        self.wheel_1.color('white')

        self.wheel_2.shapesize(.5)
        self.wheel_2_inside.shapesize(.4)
        self.wheel_2.color('white')

        self.body.penup()
        self.top.penup()
        self.front.penup()
        self.back.penup()
        self.window_1.penup()
        self.window_2.penup()
        self.wheel_1_inside.penup()
        self.wheel_2_inside.penup()
        self.wheel_1.penup()
        self.wheel_2.penup()


        #Go-To
        self.body.goto(self.body_x, self.body_y)
        self.front.goto(self.body_x - 15, self.body_y)
        self.back.goto(self.body_x + 10, self.body_y)
        self.top.goto(self.body_x, self.body_y + 5)
        self.window_1.goto(self.body_x - 5, self.body_y + .7)
        self.window_2.goto(self.window_1.xcor() + 10, self.window_1.ycor())
        self.wheel_1.goto(self.body_x - 10, self.body_y - 10)
        self.wheel_1_inside.goto(self.wheel_1.xcor(), self.wheel_1.ycor())
        self.wheel_2.goto(self.body_x + 8, self.body_y - 10)
        self.wheel_2_inside.goto(self.wheel_2.xcor(), self.wheel_2.ycor())


    def move_forward(self, incr):
        self.body_x -= incr
        self.hideturtle()


