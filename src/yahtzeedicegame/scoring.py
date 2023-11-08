#Yahtzee Scoring
from collections import Counter

class Scoring:
    def __init__(self, score_card, all_categories):
        self.score_card = score_card #A dictionary to store the scores for each category.
        self.all_categories = all_categories #A set containing all possible scoring categories.

    def calculate_score(self): #Given a category and dice values, calculates the score for that category.
        return 

    def mark_score(self): #Records a score for a given category in score_card.
        pass

    def get_score_card(self): # Returns the current score_card.
        return self.score_card

    def is_category_used(self): #Checks if a category has already been used.
        pass

    def remaining_categories(self): #Returns a list of remaining categories.
        pass

    def num_remaining_categories(self): #Returns a list of remaining categories.
        pass

    def num_used_categories(self): #Returns the number of remaining categories.
        pass

    def is_full(self): #Returns the number of used categories.
        pass

    def display_score_card(self): #Displays the scorecard in a user-friendly format in the terminal.
        pass


