from typing import List, Dict
from scoring import Scoring
from dice import YahzeeDice
from display_dice import display_dice

class Player(Scoring):
    def __init__(self):
        super().__init__()  # Initialize the Scoring class
        self.name = input("Please Enter your name: ")
        self.score = 0

    class PlayerTurn:
        def __init__(self):
            self.yahtzee_dice = YahzeeDice()
            self.rolls_left = 3
            self.held_dice = []
            # self.yahtzee_dice.roll_all()
            # display_dice(self.yahtzee_dice.get_values())

        def roll(self):
            for index, dice in enumerate(self.yahtzee_dice.dice_set):
                if index not in self.held_dice:
                    dice.roll()
            self.rolls_left -= 1

        def hold(self, indices: List[int]):
            self.held_dice.extend(indices)

        def get_state(self):
            return {
                'dice_values': self.yahtzee_dice.get_values(),
                'rolls_left': self.rolls_left,
                'held_dice': self.held_dice
            }

