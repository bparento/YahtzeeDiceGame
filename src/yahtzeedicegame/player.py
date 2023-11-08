from typing import List, Dict
from scoring import Scoring
from dice import YahtzeeDice
from display_dice import display_dice

class Player(Scoring):
    def __init__(self,score=0):
        self.name = input()
        self.score = score

    class PlayerTurn:
        def __init__(self,rolls_left = 3):
            self.yahtzee_dice = YahtzeeDice()
            self.rolls_left = rolls_left
            self.held_dice = []

        def roll(self):
            if self.rolls_left > 0:
                # Simulate rolling the dice and updating their values
                # You should implement your dice rolling logic here
                self.yahtzee_dice.dice = [1, 2, 3, 4, 5]  # Example values, replace with your logic
                self.rolls_left -= 1

        def hold(self):
            pass

        def get_state(self):
            pass

# test=Player()
# print(test.name)
# print(test.score)
