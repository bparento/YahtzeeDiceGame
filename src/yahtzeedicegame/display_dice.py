from typing import List

def display_dice(values: List[int], held_indicies: List[int]=[]):
    """
    Display the ASCII art representation of dice faces based on their values.

    Args:
    values (List[int]): List of integers representing dice face values (1 to 6).
    held_indices (List[int], optional): List of indices of dice to be displayed as held. Defaults to an empty list.
    """    
    # ANSI escape code for green text
    green_text = "\033[92m"
    # ANSI escape code to reset to default color
    reset_color = "\033[0m"

    dice_faces = {
    1: [
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘"
    ],
    2: [
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘"
    ],
    3: [
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘"
    ],
    4: [
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘"
    ],
    5: [
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘"
    ],
    6: [
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘"
    ]
}
    for i, value in enumerate(values):
        die = dice_faces[value] # Retrieve the ASCII art for the current dice value
        if i in held_indicies:
            # Display held dice in a different color using ANSI escape codes
            die = [f"\033[92m{line}\033[0m" for line in die]
                # Print each line of the ASCII art for the current dice
        # Print each line of the ASCII art for the current dice
        for line in die:
            print(line)
    