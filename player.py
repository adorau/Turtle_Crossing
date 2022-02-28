from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

    def turtle_body(self):
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.setposition(STARTING_POSITION)

    def start_position(self):
        self.setposition(STARTING_POSITION)

    def turtle_move(self):
        self.fd(MOVE_DISTANCE)
