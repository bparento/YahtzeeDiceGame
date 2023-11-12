from player import Player
from display_dice import display_dice

class PlayYahtzee:
    def __init__(self):
        self.player = Player()
        self.start_new_turn()
        self.s = 0

    def roll(self):
        self.current_turn.roll()
        state = self.current_turn.get_state()
        self.dice_values = state['dice_values']
        self.held_value = state['held_dice']

    def choose_category(self):
        while True:
            remaining = self.player.remaining_categories()
            green_remaining = [f"\033[32m{category}\033[0m" for category in remaining]
            print("The remaining categories are:", ", ".join(green_remaining))
            category = input("Choose a scoring category: ")

            if category in self.player.remaining_categories():
                return category
            else:
                print("Invalid category. Choose a valid category.")
    
    def start_new_turn(self):
        self.current_turn = self.player.PlayerTurn()

    def turn(self):
        while self.current_turn.rolls_left >= 0:
            if self.current_turn.rolls_left == 3:
                action = input("Press r to roll: ").lower()
                if action == 'r':
                    self.roll()
                    state = self.current_turn.get_state()
                    display_dice(state['dice_values'])
                else:
                    print(f"Invalid action {self.player.name}. Please enter 'r' to roll.")
            
            if self.current_turn.rolls_left == 0:
                print("Below is your working hand: ")
                display_dice(state['dice_values'],held_indicies=[0,1,2,3,4])
                state = self.current_turn.get_state()
                category = self.choose_category()
                score = self.player.calculate_score(category, state['dice_values'])
                self.player.mark_score(category, score)
                self.player.display_score_card()
                break

            else:
                print(f"\nRolls left: {self.current_turn.rolls_left}")
                action = input("Enter action (r: Roll, h: Hold, c: Choose Category): ").lower()

                if action == 'r':
                    self.roll()
                    state = self.current_turn.get_state()
                    display_dice(state['dice_values'], state['held_dice'])

                elif action == 'h':
                    indices_str = input("Enter indices (space-separated & between 1-5) to hold: ")
                    indices = [(int(idx)-1) for idx in indices_str.split()]
                    self.current_turn.hold(indices)
                    state = self.current_turn.get_state()
                    display_dice(state['dice_values'], state['held_dice'])

                elif action == 'c':
                    print("Below is your working hand: ")
        
                    display_dice(state['dice_values'],held_indicies=[0,1,2,3,4])
                    category = self.choose_category()
                    score = self.player.calculate_score(category, state['dice_values'])
                    self.player.mark_score(category, score)
                    self.player.display_score_card()
                    break
                else:
                    print("Invalid action. Please enter 'r' to roll, 'h' to hold, or 'c' to choose category.")
                
        self.current_turn = self.player.PlayerTurn()

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
        self.generate_block_art()
        totalScore = sum(list(self.player.score_card.keys()))
        print(f"Your final score is: {totalScore}" + ", congrats!")
        exit()

if __name__ == '__main__':
    print("Let's Begin")
    game = PlayYahtzee()
    game.play_game()
