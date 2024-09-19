import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = SCREEN_HEIGHT = 600


def game():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)

    terry = Player()
    car_manager = CarManager()
    score = Scoreboard()

    screen.listen()
    screen.onkey(terry.move, "Up")

    counter = 0
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.move_cars()
        if counter % 6 == 0:
            car_manager.create_car()
        for car in car_manager.cars:
            if terry.distance(car) < 20:
                game_is_on = False
                score.game_over()
        counter += 1
        if terry.check_finish():
            terry.refresh()
            car_manager.speed_up_cars()
            score.increase_level()

    screen.exitonclick()


if __name__ == "__main__":
    game()
