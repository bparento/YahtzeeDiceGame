#Yahtzee Scoring
from collections import Counter

class Scoring:
    """
    Class responsible for managing the scoring in a Yahtzee game.
    """
    def __init__(self):
        """
        Initializes the scoring system.
        """
        self.score_card = {} #A dictionary to store the scores for each category.
        self.all_categories = {
            'Ones': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 6,
            'ThreeOfAKind': 7, 'FourOfAKind': 8, 'FullHouse': 9,
            'SmallStraight': 10, 'LargeStraight': 11, 'Yahtzee': 12, 'Chance': 13
        }

    def calculate_score(self, category, dice_values): #Given a category and dice values, calculates the score for that category.
        """
        Given a category and dice values, calculates the score for that category.

        Args:
        category (str): The category to score.
        dice_values (List[int]): Values of the dice.

        Returns:
        int: The calculated score for the given category.
        """
        count_values = Counter(dice_values)
        sorted_values = sorted(dice_values)

        if category in {'Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes'}:
            number =  int(self.all_categories[str(category)])
            if number >= 1 and number <= 6:
                return count_values[number] * number
            else:
                return 0  # In case of invalid numbers
        
        elif category in {'ThreeOfAKind', 'FourOfAKind'}:
            target_count = 3 if category == 'ThreeOfAKind' else 4
            for value, count in count_values.items():
                if count >= target_count:
                    return target_count * value
            return 0
        
        elif category == 'FullHouse':
            if (len(count_values) == 2 and list(count_values.values()) in [[2, 3], [3, 2]]) or (len(count_values) == 1 and list(count_values.values())[0] == 5):
                return sum(sorted_values)
            return 0
        
        elif category == 'SmallStraight':
            if any(sorted_values[i + 1] - sorted_values[i] != 1 for i in range(len(sorted_values) - 1)) or len(set(sorted_values)) < 4:
                return 0
            return 25
        
        elif category == 'LargeStraight':
            if any(sorted_values[i + 1] - sorted_values[i] != 1 for i in range(len(sorted_values) - 1)) or len(set(sorted_values)) < 5:
                return 0
            return 30
        
        elif category == 'Yahtzee':
            if count_values.most_common(1)[0][1] == 5:
                return 50
            return 0
        
        elif category == 'Chance':
            return sum(dice_values)
        
        else:
            return 0

    def mark_score(self, category, score): #Records a score for a given category in score_card.
        """
        Records a score for a given category in score_card.

        Args:
        category (str): The category to mark the score.
        score (int): The score to be recorded for the category.
        """
        self.score_card[category] = score

    def get_score_card(self): # Returns the current score_card.
        """
        Returns the current score_card.

        Returns:
        dict: The current score card with category and scores.
        """    
        return self.score_card

    def is_category_used(self, category): #Checks if a category has already been used.
        """
        Checks if a category has already been used.

        Args:
        category (str): The category to check.

        Returns:
        bool: True if the category has been used, False otherwise.
        """
        return category in self.score_card

    def remaining_categories(self):
        """
        Retrieves the remaining categories to be scored.

        Returns:
        List[str]: List of categories that haven't been scored yet.
        """
        return sorted(list(set(self.all_categories.keys()) - (self.score_card.keys())))

    def num_remaining_categories(self):
        """
        Retrieves the number of remaining categories to be scored.

        Returns:
        List[str]: List of num_categories that haven't been scored yet.
        """
        return len(self.remaining_categories())

    def num_used_categories(self):
        """
        Retrieves the number of used categories to be scored.

        Returns:
        List[str]: List of number of unused categories that haven't been scored yet.
        """
        return len(self.score_card)

    def is_full(self):
        """
        Checks if the scoring is full.

        Returns:
        True/False: if num_used_categories() == len(self.all_categories)
        """
        return self.num_used_categories() == len(self.all_categories)

    def display_score_card(self):
        """
        Displays score

        Returns: 
        The values of the score card
        """
        print("Score Card:")
        for category, score in self.score_card.items():
            print(f"{category}: {score}")
