import unittest
from unittest.mock import patch
from yahtzeedicegame.player import *

class TestPlayerTurn(unittest.TestCase):
    def setUp(self):
        self.player_turn = Player().PlayerTurn()

    def test_roll(self):
        initial_values = self.player_turn.get_state()['dice_values']
        with patch.object(self.player_turn.yahtzee_dice, 'roll_all'):
            self.player_turn.roll()
        new_values = self.player_turn.get_state()['dice_values']
        # Check if the dice values change after rolling
        self.assertNotEqual(initial_values, new_values, "Dice values did not change after rolling.")

    def test_hold(self):
        initial_held_dice = self.player_turn.get_state()['held_dice']
        # Hold dice at index 0 and 2
        self.player_turn.hold([0, 2])
        new_held_dice = self.player_turn.get_state()['held_dice']
        # Check if the held dice indices are updated
        self.assertListEqual(new_held_dice, [0, 2], "Held dice indices were not updated correctly.")

if __name__ == '__main__':
    unittest.main()
