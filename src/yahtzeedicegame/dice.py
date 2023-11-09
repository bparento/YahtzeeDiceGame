import random
from dataclasses import dataclass, field
from typing import List

class Dice:
    def __init__(self, sides=6, current_value=None):
        self.sides = sides
        self.current_value = current_value

    def roll(self):
        self.current_value = random.randint(1,self.sides)
        return self.current_value

class YahzeeDice(Dice):
    def __init__(self, num_dice=5):
        Dice.__init__(self, sides=6, current_value=None)
        self.num_dice = num_dice
        self.dice_set = [Dice() for _ in range(self.num_dice)]
    
    def roll_all(self):
        return [dice.roll() for dice in self.dice_set] # Rolls all the dice in dice_set and returns a list of the rolled values.
    
    def get_values(self):
        return [dice.current_value for dice in self.dice_set] #Returns a list containing the current values of all dice in dice_set.

