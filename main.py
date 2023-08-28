import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
<<<<<<< HEAD
=======
screen.title('Turtle Crossing Game')
>>>>>>> 744bab9 (Initial commit)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()


    #Detect collision with car
    for car in car_manager.cars:
        if player.distance(car.body) < 20:
            game_is_on = False
            scoreboard.game_over()


    #Detect the top wall
    if player.is_at_finish_line():
        scoreboard.incr_score()
        player.go_to_start()
        car_manager.incr_car_speed()



screen.exitonclick()










