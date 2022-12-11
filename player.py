from turtle import Turtle


#initialize global variables
FINISH_LINE_Y = 280
MOVE_DISTANCE = 10
STARTING_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)


    def go_up(self):
        '''Move turtle functionality.'''
        self.forward(MOVE_DISTANCE)


    def go_to_start(self):
        '''Move turtle to starting point.'''
        self.goto(STARTING_POSITION)


    def is_at_finish_line(self):
        '''Determine if turtle completes level.'''
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False