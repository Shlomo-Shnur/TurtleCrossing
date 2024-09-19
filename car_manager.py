from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_WIDTH = SCREEN_HEIGHT = 600
LEFT = 180


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        random_ycor = random.randint(-SCREEN_HEIGHT // 2 + 50, SCREEN_HEIGHT // 2 - 50)
        new_car.penup()
        new_car.goto(SCREEN_WIDTH // 2, random_ycor)
        new_car.setheading(LEFT)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_speed)
        self.clear_cars()

    def clear_cars(self):
        for car in self.cars:
            if car.xcor() < -SCREEN_WIDTH // 2 - 100:
                self.cars.remove(car)
                car.hideturtle()
                del car

    def speed_up_cars(self):
        self.move_speed += MOVE_INCREMENT
