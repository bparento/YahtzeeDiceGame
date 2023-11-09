from player import Player
from display_dice import display_dice

class PlayYahtzee:
    def __init__(self, player):
        self.player = player
    
    def roll(self):
        self.start_new_turn()
        self.player.display_score_card()
        self.player.roll_dice()
        display_dice(self.player.dice)
    
    def choose_category(self):
        category = input("Choose a scoring category: ")
        while category not in self.player.available_categories():
            print("Invalid category. Choose a valid category.")
            category = input("Choose a scoring category: ")

    def start_new_turn(self):
        return self.player.PlayerTurn()

    def turn(self):
        pass

    def play_game(self):
        pass

    def generate_block_art(self):
        pass

    def game_over(self):
        pass


if __name__ == '__main__':
    game = PlayYahtzee()
    game.play_game()