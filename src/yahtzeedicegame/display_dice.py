#Requirements
    #Include, typing library for type annotation

from typing import List, Dict


def display_dice(values: List[int], held_indicies: List[int]=[]):
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
        die = dice_faces[value]
        if i in held_indicies:
            # Display held dice in a different color using ANSI escape codes
            die = [f"\033[92m{line}\033[0m" for line in die]
        for line in die:
            print(line)

# #Validation of working Display
# dice_values = [3, 3, 6, 2, 5]
# held_dice_indices = [0, 2]
# display_dice(dice_values, held_dice_indices)