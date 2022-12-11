from turtle import Turtle


#initialize global variable
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-295, 260)
        self.update_scoreboard()


    def update_scoreboard(self):
        '''Update scoreboard functionality.'''
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def increase_level(self):
        '''Increase level functionality.'''
        self.level += 1
        self.update_scoreboard()


    def game_over(self):
        '''Display "GAME OVER" when game ends.'''
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)