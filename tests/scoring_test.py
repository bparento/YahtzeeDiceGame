import unittest
from yahtzeedicegame.scoring import *

class TestScoring(unittest.TestCase):
    def setUp(self):
        self.scorer = Scoring()
    
    def test_init(self):
        scorer = Scoring()
        # Check if score_card is initialized as an empty dictionary
        self.assertEqual(scorer.score_card, {})
        # Check if all_categories are initialized correctly
        
        expected_categories = {
            'Ones': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 6,
            'ThreeOfAKind': 7, 'FourOfAKind': 8, 'FullHouse': 9,
            'SmallStraight': 10, 'LargeStraight': 11, 'Yahtzee': 12, 'Chance': 13
        }
        self.assertDictEqual(scorer.all_categories, expected_categories)

    def test_calculate_score_ones(self):
        score = self.scorer.calculate_score('Ones', [1, 1, 2, 3, 1])
        self.assertEqual(score, 3, "Expected score for Ones is incorrect.")

    def test_calculate_score_twos(self):
        score = self.scorer.calculate_score('Twos', [2, 2, 2, 1, 3])
        self.assertEqual(score, 6, "Expected score for Twos is incorrect.")

    def test_calculate_score_three_of_a_kind(self):
        score = self.scorer.calculate_score('ThreeOfAKind', [3, 3, 3, 4, 5])
        self.assertEqual(score, 9, "Expected score for Three of a Kind is incorrect.")

    def test_calculate_score_four_of_a_kind(self):
        score = self.scorer.calculate_score('FourOfAKind', [2, 2, 2, 2, 5])
        self.assertEqual(score, 8, "Expected score for Four of a Kind is incorrect.")

    def test_calculate_score_full_house(self):
        score = self.scorer.calculate_score('FullHouse', [1, 1, 2, 2, 1])
        self.assertEqual(score, 7, "Expected score for Full House is incorrect.")

    def test_calculate_score_invalid_category(self):
        score = self.scorer.calculate_score('InvalidCategory', [1, 2, 3, 4, 5])
        self.assertEqual(score, 0, "Expected score for an invalid category is not 0.")

    def test_calculate_score_small_straight(self):
        score = self.scorer.calculate_score('SmallStraight', [1, 2, 3, 4, 6])
        self.assertEqual(score, 25, "Expected score for Small Straight is incorrect.")

    def test_calculate_score_large_straight(self):
        score = self.scorer.calculate_score('LargeStraight', [2, 3, 4, 5, 6])
        self.assertEqual(score, 30, "Expected score for Large Straight is incorrect.")

    def test_calculate_score_yahtzee(self):
        score = self.scorer.calculate_score('Yahtzee', [3, 3, 3, 3, 3])
        self.assertEqual(score, 50, "Expected score for Yahtzee is incorrect.")

    def test_calculate_score_chance(self):
        score = self.scorer.calculate_score('Chance', [1, 2, 3, 4, 5])
        self.assertEqual(score, 15, "Expected score for Chance is incorrect.")

    def test_calculate_score_invalid_category(self):
        score = self.scorer.calculate_score('InvalidCategory', [1, 2, 3, 4, 5])
        self.assertEqual(score, 0, "Expected score for an invalid category is not 0.")

    def test_mark_score(self):
        self.scorer.mark_score('Ones', 3)
        score_card = self.scorer.get_score_card()
        self.assertEqual(score_card['Ones'], 3, "Marking score failed.")

    
    # Add more test cases for the remaining categories and edge cases...

if __name__ == '__main__':
    unittest.main()
