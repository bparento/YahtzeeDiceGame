from player import Player
from display_dice import display_dice

class PlayYahtzee:
    def __init__(self):
        self.player = Player()
    
    def roll(self):
        self.start_new_turn()
        self.player.display_score_card()
        self.player.player_turn.roll()
        display_dice(self.player.player_turn.yahtzee_dice.get_values())
    
    def choose_category(self):
        category = input("Choose a scoring category: ")
        while category not in self.player.remaining_categories():
            print("Invalid category. Choose a valid category.")
            category = input("Choose a scoring category: ")
        
    def start_new_turn(self):
        self.player.player_turn = self.player.PlayerTurn()

    def turn(self):
        self.roll()
        self.choose_category()

    def play_game(self):
        while not self.player.is_full():
            self.turn()

        self.game_over()

    def generate_block_art(self):
        # ASCII art for game-over screen
        art = """
        Congratulations!
        ________  
        \       \ 
         \       \
          \_______\\
        """
        print(art)

    def game_over(self):
        self.player.display_final_score()
        self.generate_block_art()
        exit()


if __name__ == '__main__':
    game = PlayYahtzee()
    game.play_game()