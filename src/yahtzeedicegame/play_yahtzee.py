from player import Player
from display_dice import display_dice

class PlayYahtzee:
    def __init__(self):
        self.player = Player()
    
    def roll(self):
        self.player.player_turn.roll()
        self.dice_values = self.player.player_turn.yahtzee_dice.get_values()
        self.held_value = self.player.player_turn.held_dice

    def choose_category(self):
        category = input("Choose a scoring category: ")
        while category not in self.player.remaining_categories():
            print("Invalid category. Choose a valid category.")
            category = input("Choose a scoring category: ")
        
    def start_new_turn(self):
        self.player.player_turn = self.player.PlayerTurn()

    def turn(self):
        while self.player.player_turn.rolls_left > 0:
            print(f"Rolls left: {self.player.player_turn.rolls_left}")
            action = input("Enter action (r: Roll, h: Hold, c: Choose Category): ").lower()
            if action == 'r':
                self.roll()
                state = self.player.player_turn.get_state()
                display_dice(state['dice_values'], self.held_value)
            elif action == 'h':
                self.player.player_turn.hold(self.held_value)

            elif action == 'c':
                self.choose_category()
                self.player.display_score_card()
                break
            else:
                print("Invalid action. Please enter 'r' to roll, 'h' to hold, or 'c' to choose category.")

        self.start_new_turn()

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
    print("Lets Begin")
    game = PlayYahtzee()
    game.play_game()