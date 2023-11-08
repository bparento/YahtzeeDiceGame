#Reqs:
    #Must use random lib
    #Dataclasses library for creating data types
    #typing library for type annotation

#Should include two classes:
    #Dice(single die with customizable number of sides)
    #YahtzeeDice (A child of Dice and represents a set of dice)

import random
from dataclasses import dataclass, field
from typing import List

class Die:
    def __init__(self, sides=6, current_value=None):
        self.sides = sides
        self.current_value = current_value

    def roll(self):
        self.current_value = random.randint(1,self.sides)
        return self.current_value


class Yahzee:
    def __init__(self,num_dice = 5):
        self.num_dice = num_dice

    def __post_init__(self,dice_set):
        self.dice_set = dice_set
    
    def roll_all(self,dice_set):
        return # Rolls all the dice in dice_set and returns a list of the rolled values.
    
    def get_values(self, dice_set):
        return #Returns a list containing the current values of all dice in dice_set.

class YahtzeeDice(Die):
    pass

