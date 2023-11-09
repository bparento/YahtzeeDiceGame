from typing import List

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