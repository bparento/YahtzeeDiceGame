import random
from dataclasses import dataclass, field
from typing import List

@dataclass
class Dice:
    """
    Represents a single dice.
    """
    sides: int = 6
    current_value: int = field(default=None, init=False)

    def roll(self):
        """
        Rolls the dice and assigns a random value between 1 and the number of sides.
        """
        self.current_value = random.randint(1, self.sides)

class YahzeeDice(Dice):
    """
    Represents a set of dice for Yahtzee.
    """
    def __init__(self, num_dice=5):
        """
        Initializes a set of Yahtzee dice with a specified number of dice.
        """
        super().__init__()  # Call the __init__ method of the parent class
        self.num_dice = num_dice
        self.dice_set = [Dice() for _ in range(self.num_dice)]

    def roll_all(self):
        """
        Rolls all the dice in the set.
        """
        [dice.roll() for dice in self.dice_set]

    def get_values(self) -> List[int]:
        """
        Retrieves the current values of all the dice in the set.
        Returns:
            List[int]: A list of the current values of the dice.
        """
        return [dice.current_value for dice in self.dice_set]


