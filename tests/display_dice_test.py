import unittest
from io import StringIO
from unittest.mock import patch
from yahtzeedicegame.display_dice import *  # Replace 'your_dice_module' with the actual module name

class TestDisplayDice(unittest.TestCase):
    def setUp(self):
        self.test_output = StringIO()

    def test_display_dice(self):
        values = [1, 2, 3, 4, 5]
        held_indices = [1, 3]
        expected_output = [
            "┌───────┐",
            "│       │",
            "│   ●   │",
            "│       │",
            "└───────┘",
            "┌───────┐",
            "\033[92m│ ●     │\033[0m",
            "\033[92m│       │\033[0m",
            "└───────┘",
            "┌───────┐",
            "│ ●     │",
            "│   ●   │",
            "│     ● │",
            "└───────┘",
            "┌───────┐",
            "\033[92m│ ●   ● │\033[0m",
            "│       │",
            "\033[92m│ ●   ● │\033[0m",
            "└───────┘",
            "┌───────┐",
            "│ ●   ● │",
            "│   ●   │",
            "│ ●   ● │",
            "└───────┘"
        ]
        
        with patch('sys.stdout', new=self.test_output):
            display_dice(values, held_indices)

        output = self.test_output.getvalue().splitlines()
        # Compare each line of the output with the expected output
        for line, expected_line in zip(output, expected_output):
            self.assertEqual(line, expected_line)

if __name__ == '__main__':
    unittest.main()
