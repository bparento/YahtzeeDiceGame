#Yahtzee Scoring
from collections import Counter

class Scoring:
    def __init__(self):
        self.score_card = {} #A dictionary to store the scores for each category.
        self.all_categories = {
            'Ones': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 6,
            'ThreeOfAKind': 7, 'FourOfAKind': 8, 'FullHouse': 9,
            'SmallStraight': 10, 'LargeStraight': 11, 'Yahtzee': 12, 'Chance': 13
        }

    def calculate_score(self, category, dice_values): #Given a category and dice values, calculates the score for that category.
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
        self.score_card[category] = score

    def get_score_card(self): # Returns the current score_card.
        return self.score_card

    def is_category_used(self, category): #Checks if a category has already been used.
        return category in self.score_card

    def remaining_categories(self):
        return sorted(list(set(self.all_categories.keys()) - (self.score_card.keys())))

    def num_remaining_categories(self):
        return len(self.remaining_categories())

    def num_used_categories(self):
        return len(self.score_card)

    def is_full(self):
        return self.num_used_categories() == len(self.all_categories)

    def display_score_card(self):
        print("Score Card:")
        for category, score in self.score_card.items():
            print(f"{category}: {score}")
