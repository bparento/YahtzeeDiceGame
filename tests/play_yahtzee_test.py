import unittest
from unittest.mock import patch
from io import StringIO
from yahtzeedicegame.play_yahtzee import *  # Replace 'play_yahtzee' with the actual module name

class TestPlayYahtzee(unittest.TestCase):
    def setUp(self):
        self.play_yahtzee = PlayYahtzee()

    def test_choose_category_valid(self):
        with patch('builtins.input', side_effect=['Ones']):
            chosen_category = self.play_yahtzee.choose_category()
        self.assertEqual(chosen_category, 'Ones', "Expected category 'Ones' not chosen.")

    def test_choose_category_invalid_then_valid(self):
        with patch('builtins.input', side_effect=['Invalid', 'Ones']):
            chosen_category = self.play_yahtzee.choose_category()
        self.assertEqual(chosen_category, 'Ones', "Expected category 'Ones' not chosen.")

if __name__ == '__main__':
    unittest.main()
