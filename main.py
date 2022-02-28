import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
turtle = Player()
text = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)
cars = []
counter = 0
speed = 5
lvl_speed = 6

game_is_on = True
turtle.turtle_body()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkeypress(turtle.turtle_move, "Up")
    if counter % lvl_speed == 0:
        car = CarManager(speed)
        car.car_position()
        car.car_body()
        cars.append(car)
        for i in cars:
            if i.xcor() < -300:
                cars.remove(i)
    for i in cars:
        i.car_move()
    if turtle.ycor() >= 280:
        turtle.clear()
        turtle.turtle_body()
        text.scoreboard()
        for i in cars:
            i.car_move_next_lvl()
        lvl_speed -= 2
        speed += 10
    for i in cars:
        if turtle.distance(i) <= 21 and i.xcor() != turtle.xcor():
            text.game_over()
            game_is_on = False
        elif turtle.distance(i) < 28 and i.xcor() == turtle.xcor():
            text.game_over()
            game_is_on = False

    counter += 1

screen.exitonclick()
