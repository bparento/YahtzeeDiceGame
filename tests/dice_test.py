import unittest
from unittest.mock import patch
from yahtzeedicegame.dice import * # Replace 'your_dice_module' with the module name where your code resides

class TestYahzeeDice(unittest.TestCase):
    def test_roll_all(self):
        # Mocking the random.randint function to control the output
        with patch('your_dice_module.random.randint', side_effect=[1, 2, 3, 4, 5]):
            yahzee = YahzeeDice()
            yahzee.roll_all()
            values = yahzee.get_values()
            expected_values = [1, 2, 3, 4, 5]
            self.assertEqual(values, expected_values, "Values after rolling all dice do not match expected values.")

    def test_get_values(self):
        yahzee = YahzeeDice()
        yahzee.dice_set = [Dice(current_value=1), Dice(current_value=2), Dice(current_value=3),
                           Dice(current_value=4), Dice(current_value=5)]
        values = yahzee.get_values()
        expected_values = [1, 2, 3, 4, 5]
        self.assertEqual(values, expected_values, "Retrieved values do not match expected values.")

if __name__ == '__main__':
    unittest.main()
