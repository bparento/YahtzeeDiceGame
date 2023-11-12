from player import Player
from display_dice import display_dice

class PlayYahtzee:
    """
    Represents the main game logic for playing Yahtzee.
    """
    def __init__(self):
        self.player = Player() # Creates an instance of the Player class
        self.start_new_turn() # Starts a new turn for the player
        self.s = 0

    def roll(self):
        """
        Rolls the dice and handles the game state.
        """
        self.current_turn.roll() # Rolls the dice for the current turn
        state = self.current_turn.get_state() # Retrieves the current state of the game
        self.dice_values = state['dice_values'] # Obtains the current dice values
        self.held_value = state['held_dice']  # Obtains the held dice values

    def choose_category(self):
        """
        Allows the player to choose a scoring category.
        """
        while True:
            remaining = self.player.remaining_categories() # Retrieves remaining scoring categories
            green_remaining = [f"\033[32m{category}\033[0m" for category in remaining] # Formats remaining categories
            print("The remaining categories are:", ", ".join(green_remaining)) ## Displays remaining categories
            category = input("Choose a scoring category: ")# Asks the player to choose a category

            if category in self.player.remaining_categories():
                return category # Returns the chosen category if valid
            else:
                print("Invalid category. Choose a valid category.") # Notifies the player about an invalid choice
    
    def start_new_turn(self):
        """
        Starts a new turn for the player.
        """
        self.current_turn = self.player.PlayerTurn()  # Starts a new turn for the player using the PlayerTurn class

    def turn(self):
        """
        Manages a player's turn in the game.
        """
        while self.current_turn.rolls_left >= 0:
            if self.current_turn.rolls_left == 3:
                action = input("Press r to roll: ").lower()  # Asks for input to roll the dice

                if action == 'r':
                    self.roll()  # Rolls the dice if 'r' is pressed
                    state = self.current_turn.get_state()  # Retrieves the current state
                    display_dice(state['dice_values'])  # Displays the dice values
                else:
                    print(f"Invalid action {self.player.name}. Please enter 'r' to roll.")
                    # Notifies the player about an invalid action
            
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
        """
        Manages the entire game, taking turns until the game is over.
        """
        while not self.player.is_full():  # Plays the game until all categories are filled
            self.turn()  # Manages a player's turn
        self.game_over()  # Ends the game when all categories are filled

    def generate_block_art(self):
        """
        Generates ASCII art for the game-over screen.
        """
        art = """
        Congratulations!
        ________  
        \       \ 
         \       \
          \_______\\
        """
        print(art)  # Prints the ASCII art for the game-over screen

    def game_over(self):
        """
        Handles the game-over process and displays the final score.
        """
        self.generate_block_art()  # Shows the game-over ASCII art
        totalScore = sum(list(self.player.score_card.keys()))  # Calculates the total score
        print(f"Your final score is: {totalScore}" + ", congrats!")  # Displays the final score
        exit()  # Exits the game

if __name__ == '__main__':
    print("Let's Begin")
    game = PlayYahtzee()  # Starts a new game of Yahtzee
    game.play_game()  # Initiates the game by taking turns until it's over