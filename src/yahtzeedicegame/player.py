from typing import List, Dict
from scoring import Scoring
from dice import YahzeeDice

class Player(Scoring):
    """
    Represents a player in the Yahtzee game.
    Inherits attributes and methods from Scoring class.
    """
    def __init__(self):
        """
        Initializes a player, inheriting scoring features.
        """    
        super().__init__()  # Initialize the Scoring class
        self.name = input("Please Enter your name: ")
        self.score = 0 # Initializes the player's score

    class PlayerTurn:
        def __init__(self):
            """
            Initializes a player's turn with the necessary attributes.
            """
            self.yahtzee_dice = YahzeeDice() # Initializes a set of Yahtzee dice
            self.rolls_left = 3 # Sets the number of available rolls in a turn to 3
            self.held_dice = [] # Initializes the list to hold indices of held dice
            # self.yahtzee_dice.roll_all()
            # display_dice(self.yahtzee_dice.get_values())

        def roll(self):
            """
            Rolls the dice for a player's turn.
            """
            for index, dice in enumerate(self.yahtzee_dice.dice_set):
                if index not in self.held_dice:
                    dice.roll() # Rolls the dice if it's not held
            self.rolls_left -= 1 # Reduces the available rolls after rolling

        def hold(self, indices: List[int]):
            """
            Holds the specified dice in a turn.
            
            Args:
            indices (List[int]): Indices of dice to be held.
            """
            self.held_dice.extend(indices) # Adds specified dice indices to the held_dice list

        def get_state(self):
            """
            Retrieves the current state of a player's turn.

            Returns:
            Dict: A dictionary containing dice values, remaining rolls, and held dice indices.
            """
            return {
                'dice_values': self.yahtzee_dice.get_values(),  # Current dice values
                'rolls_left': self.rolls_left, # Remaining rolls in a turn
                'held_dice': self.held_dice # Indices of held dice
            }