import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


#initialize screen and create game window prior to additional global variables for rendering purposes.
SCREEN = Screen()


#create game window
SCREEN.setup(width=600, height=600)
SCREEN.tracer(0)


#initialize additional global variables
CAR_MANAGER = CarManager()
PLAY = True
PLAYER = Player()
SCOREBOARD = Scoreboard()


#connect keyboard stroke to turle movement
SCREEN.listen()
SCREEN.onkey(PLAYER.go_up, "Up")


#initiate game loop
try:
    while PLAY:
        time.sleep(0.1)
        SCREEN.update()

        #create and move the cars
        CAR_MANAGER.create_car()
        CAR_MANAGER.move_cars()

        #if turtle and a car(s) collide then end game
        for car in CAR_MANAGER.all_cars:
            if car.distance(PLAYER) < 20:
                PLAY = False
                SCOREBOARD.game_over()

        #if player crosses finish line then increase level and difficulty
        if PLAYER.is_at_finish_line():
            PLAYER.go_to_start()
            CAR_MANAGER.level_up()
            SCOREBOARD.increase_level()

except KeyboardInterrupt:
    print('\nSee you later.')

SCREEN.exitonclick()