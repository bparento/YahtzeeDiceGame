import random
from dataclasses import dataclass, field

@dataclass
class Dice:
    sides: int = 6
    current_value: int = field(default=None, init=False)

    def roll(self):
        self.current_value = random.randint(1, self.sides)

class YahzeeDice(Dice):
    def __init__(self, num_dice=5):
        super().__init__()  # Call the __init__ method of the parent class
        self.num_dice = num_dice
        self.dice_set = [Dice() for _ in range(self.num_dice)]

    def roll_all(self):
        [dice.roll() for dice in self.dice_set]

    def get_values(self):
        return [dice.current_value for dice in self.dice_set]

test = YahzeeDice()
test.roll_all()  # Roll the dice before getting values
print(test.get_values())
