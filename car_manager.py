from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self,current_speed):
        super().__init__()
        self.speed_lvl = current_speed
        self.y = random.randint(-250, 300)

    def car_body(self):
        self.penup()
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(COLORS))

    def car_move(self):
        self.backward(self.speed_lvl)

    def car_position(self):
        self.penup()
        self.goto(300,self.y)

    def car_move_next_lvl(self):
        self.speed_lvl += MOVE_INCREMENT
